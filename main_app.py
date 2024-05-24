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
from model.model import Model
from controllers.main_ctrl import MainController
from views.main_view import MainWindow
from model.square_figure import SquareFigure
from controllers.square_figure_ctrl import SquareFigureController
from model.file_figure import FileFigure
from controllers.file_figure_ctrl import FileFigureController


class App(QApplication):
    def __init__(self, sys_argv):
        super(App, self).__init__(sys_argv)
        self.square_figure = SquareFigure()
        self.file_figure = FileFigure()
        self.model = Model(self.square_figure, self.file_figure)

        self.main_controller = MainController(self.model, self.square_figure, self.file_figure)
        self.square_controller = SquareFigureController(self.square_figure)
        self.file_controller = FileFigureController(self.file_figure)
        self.main_view = MainWindow(self.model, self.main_controller, self.square_figure, self.square_controller, self.file_figure, self.file_controller)
        self.main_view.show()


if __name__ == '__main__':
    app = App(sys.argv)
    sys.exit(app.exec_())