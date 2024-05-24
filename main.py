import sys

import numpy as np
from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets
import matplotlib
from matplotlib import pyplot as plt
from matplotlib.path import Path

matplotlib.use('Qt5Agg')
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg, NavigationToolbar2QT as NavigationToolbar
from views.ui_main_view import Ui_MainWindow
from Custom_Widgets.Widgets import *
import eigenvalue_problem_solver
import app_rc

class MplCanvas(FigureCanvasQTAgg):

    def __init__(self, fig, ax):
        self.fig = fig
        self.ax = ax
        super(MplCanvas, self).__init__(self.fig)


class DrawFigure:
    def __init__(self, ax, pts, x, y):
        self.inner_points = None
        self.ax = ax
        self.pts = pts
        self.xs = []
        self.ys = []
        self.x = x
        self.y = y
        self.line, = ax.plot(self.xs, self.ys)
        self.init_area_lim(np.min(x), np.max(x), np.min(y), np.max(y))
        self.line.set_linewidth(4)
        self.is_draw = False

    def init_area_lim(self, x_min, x_max, y_min, y_max):
        self.ax.set_xlim(x_min, x_max)
        self.ax.set_ylim(y_min, y_max)
    def finish_draw(self, event):
        if event.button == 1:
            self.xs.append(self.xs[0])
            self.ys.append(self.ys[0])
            self.line.set_data(self.xs, self.ys)
            self.line.figure.canvas.draw()
            self.is_draw = True
            path = Path(list(zip(self.xs, self.ys)))
            self.ind = np.nonzero(path.contains_points(self.pts))[0]
            self.inner_points = np.array(self.pts)[self.ind]
            self.ax.scatter(self.inner_points[:][0], self.inner_points[:][1])
            self.line.figure.canvas.draw_idle()

    def draw_mouse(self, event):
        if event.button == 1:
            if self.is_draw == True:
                self.xs = []
                self.ys = []
                self.is_draw = False
            self.xs.append(event.xdata)
            self.ys.append(event.ydata)
            self.line.set_data(self.xs, self.ys)
            self.line.figure.canvas.draw()

    def connect_to_mouse(self, figure):
        figure.fig.canvas.mpl_connect('motion_notify_event', self.draw_mouse)
        figure.fig.canvas.mpl_connect('button_release_event', self.finish_draw)


class SquareFigure:
    def __init__(self, ax, pts, x, y, width, height, step):
        self.step = step
        self.points_area = None
        self.line_2 = None
        self.inner_points = None
        self.ax = ax
        self.pts = pts
        self.xs = []
        self.ys = []
        self.x = 0
        self.y = 0
        self.line, = ax.plot(self.xs, self.ys)
        self.line.set_linewidth(4)
        self.is_draw = False
        self.width = width
        self.height = height
        self.init_area_lim(self.width, self.height)
        self.draw_figure(0, 0)

    def init_area_lim(self, width, height):
        self.ax.set_xlim(-width/2-width*0.1, width/2+width*0.1)
        self.ax.set_ylim(-height/2-height*0.1, height/2+height*0.1)

    def draw_figure(self, width, height):
        print("DRA", width, height)
        x = - width / 2
        y = - height / 2
        print(x, y)
        rectangle = plt.Rectangle((x, y), width, height)
        path = Path(rectangle.get_verts())
        self.ind = np.nonzero(path.contains_points(self.pts, radius=self.step*0.1))[0]
        self.inner_points = np.array(self.pts)[self.ind]
        print("KINS", self.line)
        if self.line is not None:
            self.line.remove()
        if self.points_area is not None:
            self.points_area.remove()
        self.line, = self.ax.plot(rectangle.get_verts()[:, 0], rectangle.get_verts()[:, 1], color="blue")
        self.line.figure.canvas.draw_idle()
        self.init_area_lim(self.width, self.height)
        print("INI", self.pts, self.inner_points)
        if len(self.inner_points) > 0:
            self.points_area = self.ax.scatter(self.inner_points[:, 0], self.inner_points[:, 1], color="purple")
        self.ax.figure.canvas.draw_idle()



class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.sc_disc = None
        self.count_nodes = 0
        self.step = 0
        self.fig1 = None
        self.ax1 = None
        self.selector = None
        self.setupUi(self)
        loadJsonStyle(self, self, jsonFiles={'resources/style.json'})
        self.setMinimumSize(850, 600)
        self.add_connect_to_generate()
        self.width = self.doubleSpinBox_2.value()
        self.height = self.doubleSpinBox_3.value()
        # self.start_area_x = -self.step * (self.count_nodes / 2) - self.step
        # self.finist_area_x = -self.step * (self.count_nodes / 2) - self.step
        # self.start_area_y = -self.step * (self.count_nodes / 2) - self.step
        # self.finist_area_y = (self.step * self.count_nodes / 2) + self.step
        self.add_connect_to_stackedWidgets()
        self.add_connect_to_gr()
        self.sc = None
        self.change_connect_parameters()
        self.current_ind_discr = self.stackedWidget.currentIndex()

        self.staked()

    def staked(self):
        for index in range(self.stackedWidget.count()):
            policy = QtWidgets.QSizePolicy.Ignored
            if index == self.stackedWidget.currentIndex():
                policy = QtWidgets.QSizePolicy.Expanding
            self.stackedWidget.widget(index).setSizePolicy(policy, policy)

    def add_connect_to_gr(self):
        self.pushButton_2.clicked.connect(lambda: self.generate_grafic())

    def add_connect_to_generate(self):
        self.pushButton.clicked.connect(lambda: self.open_draw())

    def create_draw_area(self):
        self.step = float(self.lineEdit_2.text())
        self.count_nodes = int(self.lineEdit.text())
        self.count_function = int(self.spinBox_2.text())
        self.fig1, self.ax1 = plt.subplots()
        self.ax1.invert_yaxis()
        self.fig2, self.ax2 = plt.subplots()
        if self.count_function % 2 == 0:
            start_point = -self.step * (self.count_nodes / 2) + self.step *0.5
            finish_point = self.step * (self.count_nodes / 2) - self.step *0.5
        else:
            start_point = -self.step * (self.count_nodes-1) / 2
            finish_point = self.step * (self.count_nodes-1) / 2
        self.grid_x = np.tile(np.linspace(start_point, finish_point, self.count_nodes),
                              self.count_nodes)
        self.grid_y = np.repeat(
            np.linspace(start_point, finish_point, self.count_nodes), self.count_nodes)
        self.companovka = QtWidgets.QVBoxLayout(self.menu_page_2)
        self.area_width = self.step * self.count_nodes
        self.area_height = self.step * self.count_nodes
        print(self.width, self.height)
        self.sc_disc = MplCanvas(self.fig1, self.ax1)
        toolbar = NavigationToolbar(self.sc_disc, self)
        self.companovka.addWidget(toolbar)
        self.companovka.addWidget(self.sc_disc)
    def draw_area(self):
        self.pts = list(zip(self.grid_x, self.grid_y))
        print(self.pts)
        if self.current_ind_discr == 4:
            print("MOUSE")
            self.selector = DrawFigure(self.sc_disc.ax, self.pts, self.grid_x, self.grid_y)
            self.selector.connect_to_mouse(self.sc_disc)
        if self.current_ind_discr == 2:
            print("SQUARE")
            self.selector = SquareFigure(self.sc_disc.ax, self.pts, self.grid_x, self.grid_y, self.area_width, self.area_height, self.step)

    def draw_rectangle(self, w, h):
        if self.current_ind_discr == 2:
            self.selector.draw_figure(w, h)

    def open_draw(self):
        count_nodes = int(self.lineEdit.text())
        count_function = int(self.spinBox_2.text())
        self.stackedWidget_2.setCurrentWidget(self.menu_page_2)
        self.create_draw_area()
        self.stackedWidget.setCurrentWidget(self.page_2)

    def generate_grafic(self):
        inner_points = self.selector.inner_points
        print("INNNER", inner_points)
        if self.count_function % 2 == 0:
            start_point = -self.step * (self.count_nodes+2) / 2 + self.step *0.5
            finish_point = self.step * (self.count_nodes+2)/ 2 - self.step *0.5
        else:
            start_point = -self.step * (self.count_nodes+1) / 2
            finish_point = self.step * (self.count_nodes+1) / 2
        alg = eigenvalue_problem_solver.AlgorithmSteklov2D(self.count_function, self.count_nodes+2, start_point, finish_point,
                                               self.count_nodes+2, start_point, finish_point, start_area=inner_points)
        self.figi, self.ax = alg.alg_process()
        self.stackedWidget_2.setCurrentWidget(self.menu_page_1)
        # if self.sc != None:
        #     self.sc.ax.clear()
        if self.sc == None:
            self.companovka = QtWidgets.QVBoxLayout(self.main_tab)
        if self.sc != None:
            self.companovka.removeWidget(self.toolbar)
            self.companovka.removeWidget(self.sc)
        self.sc = MplCanvas(self.figi, self.ax)
        self.sc.fig.set_size_inches(self.main_tab.width(), self.main_tab.height())
        self.toolbar = NavigationToolbar(self.sc, self)
        self.companovka.addWidget(self.toolbar)
        self.companovka.addWidget(self.sc)



    def add_connect_to_stackedWidgets(self):
        self.comboBox.currentIndexChanged.connect(lambda: self.changeStackedIndex(self.comboBox.currentIndex()))

    def changeStackedIndex(self, ind):
        elements1 = [
            self.page_file,
            self.page_circle,
            self.page_square,
        ]
        print(ind)
        if ind == 3 or ind == 4:
            self.none_page.setMaximumSize(0, 0)
            self.stackedWidget_3.setCurrentWidget(self.none_page)
            self.stackedWidget_3.setMaximumSize(0, 0)
        else:
            self.current_ind_discr = ind
            element = elements1[ind]
            w = element.size().width()
            h = element.size().height()
            self.stackedWidget_3.setCurrentWidget(elements1[ind])
            self.stackedWidget_3.setMaximumSize(w, h)
        if ind == 2:
            self.draw_area()

    def change_connect_parameters(self):
        self.doubleSpinBox_2.valueChanged.connect(lambda: self.change_width(self.doubleSpinBox_2.value()))
        self.doubleSpinBox_3.valueChanged.connect(lambda: self.change_height(self.doubleSpinBox_3.value()))

    def change_width(self, width):
        self.width = float(width)
        print("EEE", self.width, self.height)
        self.draw_rectangle(self.width, self.height)

    def change_height(self, height):
        self.height = float(height)
        print("EEE", self.width, self.height)
        self.draw_rectangle(self.width, self.height)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())
