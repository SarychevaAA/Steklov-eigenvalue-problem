import sys

import numpy as np
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets
import matplotlib
from PyQt5.QtCore import QSize
from matplotlib import pyplot as plt
from matplotlib.path import Path
from PyQt5.QtCore import Qt

import constants
from views.canvas import GraphicCanvas

matplotlib.use('Qt5Agg')
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg, NavigationToolbar2QT as NavigationToolbar
from views.ui_main_view import Ui_MainWindow
from Custom_Widgets.Widgets import *


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, model, main_controller, square_figure, square_figure_controller, file_figure, file_figure_controller,*args, **kwargs):
        super().__init__(*args, **kwargs)
        self.menu_page_2 = None
        self.count_tab = 0
        self.final_toolbar = None
        self.compact = None
        self._model = model
        self._main_controller = main_controller
        self._square_figure = square_figure
        self._square_figure_controller = square_figure_controller
        self._file_figure = file_figure
        self._file_figure_controller = file_figure_controller
        self.sc_disc = None
        self.sc = None
        self.count_nodes = 0
        self.step = 0
        self.fig1 = None
        self.ax1 = None
        self.setupUi(self)
        loadJsonStyle(self, self, jsonFiles={'resources/style.json'})
        self.setMinimumSize(850, 700)
        self.draw_eigenvalue = False
        # self.add_connect_to_generate()

        self.pushButton.clicked.connect(lambda: self._main_controller.open_draw_widget(self.lineEdit.text(), self.spinBox_2.text(), self.lineEdit_2.text()))
        self.comboBox.currentIndexChanged.connect(lambda: self._main_controller.change_type_window_for_settings_draw_area(self.comboBox.currentIndex()))

        self._model.open_draw_window_changed.connect(self.on_open_draw_window)
        self._model.add_new_draw_widget_changed.connect(self.on_add_new_draw_widget)
        self._model.minimize_window_with_draw_area_settings_changed.connect(self.on_minimize_window_with_draw_area_settings)
        self._model.set_current_size_for_window_with_draw_area_settings_changed.connect(self.on_set_current_size_for_window_with_draw_area_settings)
        self._model.generate_eigenvalue_graphics_changed.connect(self.on_generate_eigenvalue_graphics)
        self._model.block_setting_window_changed.connect(self.on_block_setting_window)
        self._model.start_program_changed.connect(self.on_start_program)

        self._file_figure.write_error_changed.connect(self.on_write_error)
        self.pushButton_3.clicked.connect(lambda: self._file_figure_controller.read_file())

        self._square_figure.update_size_figure_settings_changed.connect(self.on_update_size_figure_settings)
        self._square_figure.set_settings_value_limits_changed.connect(self.on_set_settings_value_limits)
        self.add_connect_for_square_figure_settings()

        self.pushButton_2.clicked.connect(lambda: self._main_controller.create_graphics())
        self.pushButton_4.clicked.connect(lambda: self._main_controller.start_program())

        self.current_ind_discr = self.stackedWidget.currentIndex()



    def add_connect_for_square_figure_settings(self):
        self.doubleSpinBox_2.valueChanged.connect(lambda: self._square_figure_controller.change_width(self.doubleSpinBox_2.value()))
        self.doubleSpinBox_3.valueChanged.connect(lambda: self._square_figure_controller.change_height(self.doubleSpinBox_3.value()))
    @pyqtSlot()
    def on_open_draw_window(self):
        self.stackedWidget_2.setCurrentWidget(self.menu_page_2)
        self.stackedWidget.setCurrentWidget(self.page_2)
        self.comboBox.setCurrentIndex(0)

    @pyqtSlot(object, object)
    def on_add_new_draw_widget(self, figure, ax):
        self.stackedWidget_2.removeWidget(self.menu_page_2)
        self.menu_page_2 = QWidget()
        self.menu_page_2.setObjectName(u"menu_page_2")
        self.menu_page_2.setEnabled(True)
        self.menu_page_2.setMaximumSize(QSize(16777215, 16777215))
        self.stackedWidget_2.addWidget(self.menu_page_2)
        self.stackedWidget_2.setCurrentWidget(self.menu_page_2)
        self.compact = QtWidgets.QVBoxLayout(self.menu_page_2)
        sc_disc = GraphicCanvas(figure, ax)
        toolbar = NavigationToolbar(sc_disc, self)
        self.compact.addWidget(toolbar)
        self.compact.addWidget(sc_disc)

    @pyqtSlot()
    def on_minimize_window_with_draw_area_settings(self):
        self.none_page.setMaximumSize(0, 0)
        self.stackedWidget_3.setCurrentWidget(self.none_page)
        self.stackedWidget_3.setMaximumSize(0, 0)

    @pyqtSlot(int)
    def on_set_current_size_for_window_with_draw_area_settings(self, index):
        setting_window = [
            self.page_file,
            self.page_circle,
            self.page_square,
            self.none_page,
            self.none_page
        ]
        current_window = setting_window[index]
        w = current_window.size().width()
        h = current_window.size().height()
        self.stackedWidget_3.setCurrentWidget(setting_window[index])
        self.stackedWidget_3.setMaximumSize(w, h)

    @pyqtSlot(int, object)
    def on_update_size_figure_settings(self, type, data):
        if constants.SETTING_WINDOW_TYPE[type] == "SQUARE":
            self.doubleSpinBox_2.setFocus()
            width = float(data['width'])
            height = float(data['height'])
            self.doubleSpinBox_2.setValue(width)
            self.doubleSpinBox_3.setValue(height)
            if self.doubleSpinBox_2.value() != width or self.doubleSpinBox_3.value() != height:
                self.doubleSpinBox_2.setValue(width)
                self.doubleSpinBox_3.setValue(height)

    @pyqtSlot(int, object)
    def on_set_settings_value_limits(self, type, data):
        if constants.SETTING_WINDOW_TYPE[type] == "SQUARE":
            self.doubleSpinBox_2.setSingleStep(data.get("step"))
            self.doubleSpinBox_3.setSingleStep(data.get("step"))
            self.doubleSpinBox_2.setMinimum(data.get("step"))
            self.doubleSpinBox_3.setMinimum(data.get("step"))
            self.doubleSpinBox_2.setMaximum(data.get("width"))
            self.doubleSpinBox_3.setMaximum(data.get("height"))

    @pyqtSlot(object)
    def on_generate_eigenvalue_graphics(self, fig_array):
        self.stackedWidget_2.setCurrentWidget(self.menu_page_1)
        self.count_tab = len(fig_array)
        for i in range(len(fig_array)):
            main_tab = QWidget()
            main_tab.setObjectName(f"main_tab_{i}")
            main_tab.setMaximumSize(QSize(16777214, 16777214))
            self.tabWidget.addTab(main_tab, f"{1+4*i}-{4+4*i}")
            self.compact = QtWidgets.QVBoxLayout(main_tab)
            sc = GraphicCanvas(fig_array[i][0], fig_array[i][1])
            sc.fig.tight_layout()
            sc.fig.subplots_adjust(left=0, right=0.9, top=0.9, bottom=0.1)
            final_toolbar = NavigationToolbar(sc, self)
            self.compact.addWidget(final_toolbar)
            self.compact.addWidget(sc)

    @pyqtSlot(int)
    def on_block_setting_window(self, type):
        self.comboBox.setEnabled(False)
        self.comboBox.setProperty("class", "block_combo_box")
        self.frame_11.setStyleSheet("""
        #frame_11{
            background-color: rgba(90, 106, 122, 0.2);
            }
        """)
        self.pushButton_2.setEnabled(False)
        self.frame_24.setStyleSheet("""
        #frame_24{
            background-color: rgba(90, 106, 122, 0.2);
            }
        """)
        self.stackedWidget_3.setStyleSheet("""
        #stackedWidget_3, #page_square, #page_file, #page_circle, #none_page, #frame26{
            background-color: rgba(90, 106, 122, 0.10);
            }
        """)
        if constants.SETTING_WINDOW_TYPE[type] == "SQUARE":
            self.doubleSpinBox_2.setEnabled(False)
            self.doubleSpinBox_3.setEnabled(False)

    @pyqtSlot(int)
    def on_start_program(self, type):
        for i in range(self.count_tab):
            self.tabWidget.removeTab(i)
        self.on_set_current_size_for_window_with_draw_area_settings(0)
        self.stackedWidget.setCurrentIndex(0)
        self.stackedWidget_3.setCurrentIndex(0)
        self.stackedWidget_2.setCurrentWidget(self.menu_page_3)
        self.tabWidget.setCurrentIndex(0)
        self.comboBox.setEnabled(True)
        self.doubleSpinBox_2.setEnabled(True)
        self.doubleSpinBox_3.setEnabled(True)
        self.pushButton_2.setEnabled(True)
        self.frame_11.setStyleSheet("""
        #frame_11{
            background-color: rgb(90, 106, 122);
            }
        """)

        self.frame_24.setStyleSheet("""
        #frame_24{
            background-color: rgb(90, 106, 122);
            }
        """)
        self.stackedWidget_3.setStyleSheet("""
        #stackedWidget_3, #page_square, #page_file, #page_circle, #none_page, #frame26{
            background-color: rgb(90, 106, 122);
            }
        """)

    @pyqtSlot(str)
    def on_write_error(self, text):
        self.error_text = QLabel()
        self.error_text.setText(QCoreApplication.translate("MainWindow", text))
        self.error_text.setObjectName(u"error_text")
        self.error_text.setMaximumSize(QSize(180, 16777215))
        self.horizontalLayout_25 = QVBoxLayout(self.frame_22)
        self.horizontalLayout_25.setSpacing(9)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.horizontalLayout_25.addWidget(self.error_text)
