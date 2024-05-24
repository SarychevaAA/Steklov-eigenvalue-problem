import numpy as np
from PyQt5.QtCore import QObject, pyqtSignal
from matplotlib import pyplot as plt
from PyQt5 import QtWidgets
from matplotlib.path import Path


class SquareFigure(QObject):
    update_size_figure_settings_changed = pyqtSignal(int, object)
    set_settings_value_limits_changed = pyqtSignal(int, object)

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

    def draw_figure(self):
        x = - self._width / 2
        y = - self._height / 2
        rectangle = plt.Rectangle((x, y), self._width, self._height)
        path = Path(rectangle.get_verts())
        self.index_inner_points = np.nonzero(path.contains_points(self.pts, radius=self.step * 0.1))[0]
        self._inner_points = np.array(self.pts)[self.index_inner_points]
        if self.line is not None:
            self.line.remove()
        if self.points_area is not None:
            self.points_area.remove()
        self.line, = self.ax.plot(rectangle.get_verts()[:, 0], rectangle.get_verts()[:, 1], color="blue")
        self.line.figure.canvas.draw_idle()
        self.init_area_lim(self.area_width, self.area_height)
        if len(self._inner_points) > 0:
            self.points_area = self.ax.scatter(self._inner_points[:, 0], self._inner_points[:, 1], color="purple")
        self.ax.figure.canvas.draw_idle()

    def init_area_lim(self, width, height):
        self.ax.set_xlim(-width / 2 - width * 0.1, width / 2 + width * 0.1)
        self.ax.set_ylim(-height / 2 - height * 0.1, height / 2 + height * 0.1)

    def create_square_figure(self, ax, pts, step, area_width, area_height, type):
        self.step = step
        self.ax = ax
        self.pts = pts
        self.ax = ax
        self.area_width = area_width
        self.area_height = area_height
        self.type = type
        self.line, = ax.plot(self.xs, self.ys)
        self.line.set_linewidth(4)
        self.init_area_lim(self.area_width, self.area_height)
        self.update_size_figure_settings_changed.emit(self.type, {"width": self.area_width, "height": self.area_height})
        self.draw_figure()
        self.set_settings_value_limits_changed.emit(self.type, {"width": self.area_width, "height": self.area_height,
                                                                "step": self.step})

    def remove_graphic(self):
        if self.line is not None:
            print("LINE", self.line)
            self.line.remove()
        if self.points_area is not None:
            self.points_area.remove()
        self.ax.figure.canvas.draw_idle()


    def __init__(self):
        super().__init__()
        self.area_width = 0
        self.area_height = 0
        self.index_inner_points = None
        self.step = 0
        self.points_area = None
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
