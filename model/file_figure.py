import numpy as np
from PyQt5.QtCore import QObject, pyqtSignal
from PyQt5.uic.properties import QtGui
from matplotlib import pyplot as plt
from PyQt5.QtWidgets import QFileDialog, QMainWindow, QTextEdit, QAction
from matplotlib.path import Path
import pandas

class FileFigure(QObject):
    update_size_figure_settings_changed = pyqtSignal(int, object)
    set_settings_value_limits_changed = pyqtSignal(int, object)
    write_error_changed = pyqtSignal(str)

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self._width = value
        self.draw_figure()

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value
        self.draw_figure()

    @property
    def inner_points(self):
        return self._inner_points

    def read_data(self, file_data):
        self.write_error_changed.emit("Количество узлов в файле неправильное.")
        if  len(file_data) == self.count_point and len(file_data[0]) == self.count_point:
            for j in range(len(file_data)):
                for i in range(len(file_data[0])):
                    self.line.figure.canvas.draw_idle()
                    self.init_area_lim(self.area_width, self.area_height)
                    if len(self._inner_points) > 0:
                        self.points_area = self.ax.scatter(self._inner_points[:, 0], self._inner_points[:, 1],
                                                           color="purple")
                    self.ax.figure.canvas.draw_idle()

    def init_area_lim(self, width, height):
        self.ax.set_xlim(-width / 2 - width * 0.1, width / 2 + width * 0.1)
        self.ax.set_ylim(-height / 2 - height * 0.1, height / 2 + height * 0.1)

    def create_file_figure(self, ax, step, area_width, area_height, type):
        self.step = step
        self.ax = ax
        self.ax = ax
        self.area_width = area_width
        self.area_height = area_height
        self.type = type
        self.line, = ax.plot(self.xs, self.ys)
        self.line.set_linewidth(4)
        self.init_area_lim(self.area_width, self.area_height)
        self._width = self.area_width
        self._height = self.area_height
        self.count_point = int(self.area_width/self.step)

    def start_program(self):
        self.area_width = 0
        self.area_height = 0
        self.index_inner_points = None
        self.step = 0
        if self.line is not None:
            self.line.remove()
        self._inner_points = None
        self.pts = None
        self.xs = []
        self.ys = []
        self.line = None
        self.is_draw = False
        self._width = 1
        self._height = 1
        self.type = None

    def __init__(self):
        super().__init__()
        self.count_point = None
        self.area_width = 0
        self.area_height = 0
        self.index_inner_points = None
        self.step = 0
        self.points_area = None
        self.line_2 = None
        self._inner_points = None
        self.ax = None
        self.pts = None
        self.xs = []
        self.ys = []
        self.line = None
        self.is_draw = False
        self._width = 1
        self._height = 1
        self.type = None
