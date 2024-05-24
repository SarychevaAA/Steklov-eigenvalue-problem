import numpy as np
from PyQt5.QtCore import QObject, pyqtSignal
from matplotlib import pyplot as plt
from PyQt5 import QtWidgets
import constants
import eigenvalue_problem_solver


class Model(QObject):
    amount_changed = pyqtSignal(int)
    even_odd_changed = pyqtSignal(str)
    enable_reset_changed = pyqtSignal(bool)
    open_draw_window_changed = pyqtSignal()
    add_new_draw_widget_changed = pyqtSignal(object, object)
    minimize_window_with_draw_area_settings_changed = pyqtSignal()
    set_current_size_for_window_with_draw_area_settings_changed = pyqtSignal(int)
    generate_eigenvalue_graphics_changed = pyqtSignal(object)
    block_setting_window_changed = pyqtSignal(int)
    start_program_changed = pyqtSignal(int)
    @property
    def count_function(self):
        return self._count_function

    @count_function.setter
    def count_function(self, value):
        self._count_function = value

    @property
    def count_nodes(self):
        return self._count_nodes

    @count_nodes.setter
    def count_nodes(self, value):
        self._count_nodes = value

    @property
    def step(self):
        return self._step

    @step.setter
    def step(self, value):
        self._step = value

    @property
    def current_type_draw_area(self):
        return self._current_type_draw_area

    @current_type_draw_area.setter
    def current_type_draw_area(self, value):
        self._current_type_draw_area = value

    def open_draw_window(self):
        self.open_draw_window_changed.emit()

    def minimize_window_with_draw_area_settings(self):
        self.minimize_window_with_draw_area_settings_changed.emit()

    def set_current_size_for_window_with_draw_area_settings(self):
        self.set_current_size_for_window_with_draw_area_settings_changed.emit(self.current_type_draw_area)

    def change_method_for_draw_area(self):
        print("change_method_for_draw_area")
        self.points = list(zip(self.grid_x, self.grid_y))
        self.create_draw_area()
        if constants.SETTING_WINDOW_TYPE[self._current_type_draw_area] == "CURVES":
            pass
        if constants.SETTING_WINDOW_TYPE[self._current_type_draw_area] == "SQUARE":
            self._square_figure.create_square_figure(self.ax1, self.points, self.step, self.area_width, self.area_height, self._current_type_draw_area)
        if constants.SETTING_WINDOW_TYPE[self._current_type_draw_area] == "FILE":
            self._file_figure.create_file_figure(self.ax1, self.step, self.area_width, self.area_height, self._current_type_draw_area)



    def create_draw_area(self):
        print("create_draw_area")
        plt.close(self.fig1)
        self.fig1, self.ax1 = plt.subplots()
        self.ax1.invert_yaxis()
        if self._count_function % 2 == 0:
            start_point = -self._step * (self._count_nodes / 2) + self._step * 0.5
            finish_point = self._step * (self._count_nodes / 2) - self._step * 0.5
        else:
            start_point = -self._step * (self._count_nodes - 1) / 2
            finish_point = self._step * (self._count_nodes - 1) / 2
        self.grid_x = np.tile(np.linspace(start_point, finish_point, self._count_nodes),
                              self._count_nodes)
        self.grid_y = np.repeat(
            np.linspace(start_point, finish_point, self._count_nodes), self._count_nodes)
        self.area_width = self._step * self._count_nodes
        self.area_height = self._step * self._count_nodes
        print("WIDTH, HEIGHT", self.area_width, self.area_height)
        print(self.ax1, self.fig1)
        self.add_new_draw_widget_changed.emit(self.fig1, self.ax1)

    def find_eigenvalue(self, width=0, height=0):
        print(self._current_type_draw_area)
        if constants.SETTING_WINDOW_TYPE[self._current_type_draw_area] == "SQUARE":
            inner_points = self._square_figure.inner_points
            self.block_setting_window_changed.emit(self._current_type_draw_area)
        if self._count_function % 2 == 0:
            start_point = -self._step * (self._count_nodes + 2) / 2 + self._step * 0.5
            finish_point = self._step * (self._count_nodes + 2) / 2 - self._step * 0.5
        else:
            start_point = -self._step * (self._count_nodes + 1) / 2
            finish_point = self._step * (self._count_nodes + 1) / 2
        alg = eigenvalue_problem_solver.AlgorithmSteklov2D(self._count_function, self._count_nodes + 2, start_point,
                                                           finish_point,
                                                           self._count_nodes + 2, start_point, finish_point,
                                                           start_area=inner_points)
        self.final_fig_array = alg.alg_process()
        self.generate_eigenvalue_graphics_changed.emit(self.final_fig_array)

    def start_new_program(self):
        self.start_program_changed.emit(self._current_type_draw_area)

    def __init__(self, square_figure, file_figure):
        super().__init__()

        self.final_fig_array = None
        self.points_area = None
        self.line = None
        self.final_ax = None
        self.inner_points = None
        self.area_height = None
        self.area_width = None
        self.grid_y = None
        self.grid_x = None
        self._count_nodes = 0
        self._step = 0
        self.fig1 = None
        self.ax1 = None
        self.selector = None
        self.width = None
        self.height = None
        self.sc = None
        self.final_fig = None
        self._count_function = 0
        self._count_nodes = 0
        self._current_type_draw_area = 0
        self._square_figure = square_figure
        self._file_figure = file_figure

