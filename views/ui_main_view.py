# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_viewQRUSmu.ui'
##
## Created by: Qt User Interface Compiler version 5.15.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from Custom_Widgets.QCustomSlideMenu import QCustomSlideMenu


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1000, 545)
        MainWindow.setMinimumSize(QSize(0, 10))
        MainWindow.setMaximumSize(QSize(16777215, 16777215))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMinimumSize(QSize(0, 0))
        self.centralwidget.setMaximumSize(QSize(16777204, 16777211))
        self.centralwidget.setToolTipDuration(10)
        self.centralwidget.setStyleSheet(u"@font-face{\n"
"    font-family: Montserrat;\n"
"    src: url(':/fonts/fonts/Montserrat-Regular.ttf') format(\"truetype\");\n"
"}\n"
"\n"
"*{\n"
"    color: #fff;\n"
"    font-family: Montserrat;\n"
"    font-size: 14px;\n"
"    border: nine;\n"
"    background: none;\n"
"}\n"
"\n"
"#centralwidget{\n"
"    background-color: rgb(33, 43, 51);\n"
"}\n"
"\n"
"QTabBar::tab{\n"
"    padding: 6px;\n"
"    border-top-left-radius: 4px;\n"
"    border-top-right-radius: 4px;\n"
"}\n"
"\n"
"#left_menu_widget, #menu_page_1, #menu_page_2, #menu_page_3, #main_tab, #tabWidget, QTabBar::tab, #page_1, #page_2, #page_3, #frame_5, #frame_5_layout, #horizontalLayout_6{\n"
"    background-color: rgba(61, 80, 95, 100);\n"
"}\n"
"\n"
"#header_frame, #frame_3, #comboBox{\n"
"    background-color: rgb(61, 80, 95);\n"
"}\n"
"\n"
"#frame_8, #frame_9, #frame_10, #frame_11, #main_tab, #frame_12, #frame_24,  #page_square, #page_file, #page_circle, #stackedWidget_3, #frame_14{\n"
"    background-color: rgb(90, 106, 122);\n"
"    border-radiu"
                        "s: 8px;\n"
"}\n"
".standart{\n"
"    background-color: rgb(90, 106, 122);\n"
"    border-radius: 8px;\n"
"}\n"
".block{\n"
"    background-color: rgba(90, 106, 122, 0.2);\n"
"}\n"
"#stackedWidget_3{\n"
"    border-radius: 8px;\n"
"}\n"
"\n"
"QTabBar::tab:selected{\n"
"    background-color: rgb(90, 106, 122);\n"
"}\n"
"\n"
"#frame_5 QPushButton{\n"
"    padding: 10px;\n"
"    border-radius: 15px;\n"
"    background-color: rgba(33, 43, 51, 100);\n"
"    border: 3px solid rgb(120, 157, 186);\n"
"}\n"
"#page_file QPushButton{\n"
"    padding: 5px;\n"
"    border-radius: 15px;\n"
"    background-color: rgba(33, 43, 51, 100);\n"
"    border: 3px solid rgb(120, 157, 186);\n"
"}\n"
"\n"
"#frame_12 QPushButton{\n"
"    padding: 5px;\n"
"    border-radius: 15px;\n"
"    background-color: rgba(33, 43, 51, 100);\n"
"    border: 3px solid rgb(120, 157, 186);\n"
"}\n"
"#frame_24 QPushButton{\n"
"    padding: 5px;\n"
"    border-radius: 15px;\n"
"    background-color: rgba(33, 43, 51, 100);\n"
"    border: 3px solid rgb(120,"
                        " 157, 186);\n"
"}\n"
"#frame_14 QPushButton{\n"
"    padding: 5px;\n"
"    border-radius: 15px;\n"
"    background-color: rgba(33, 43, 51, 100);\n"
"    border: 3px solid rgb(120, 157, 186);\n"
"}\n"
"#comboBox, QTabBar::tab:!selected, QComboBox::drop-down, QComboBox::drop-arrow, QLineEdit, QSpinBox, QDoubleSpinBox, QCheckBox::indicator, QRadioButton::indicator:!checked{\n"
"    background-color: rgba(33, 43, 51, 100);\n"
"}\n"
"\n"
".standart_combo_box{\n"
"    background-color: rgba(33, 43, 51, 100);\n"
"}\n"
".block_combo_box{\n"
"    background-color: rgba(33, 43, 51, 0.2);\n"
"}\n"
"#frame_4 QPushButton{\n"
"    background-color: rgb(61, 80, 95);\n"
"    border-radius: 15px;\n"
"    border: 3px solid rgb(120, 157, 186);\n"
"}\n"
"\n"
"#frame_4 QPushButton:hover, #frame_5 QPushButton:hover{\n"
"    background-color: rgb(120, 157, 186);\n"
"}\n"
"\n"
"QSpinBox::down-button, QDoubleSpinBox::down-button{\n"
"    subcontrol-position: bottom right;\n"
"    height: 11px;\n"
"    width: 15px;\n"
"    image: url(:"
                        "/icons/icons/arrow_down.svg) cover;\n"
"    background-color: rgba(33, 43, 51, 100);\n"
"}\n"
"\n"
"QSpinBox::up-button, QDoubleSpinBox::up-button{\n"
"    subcontrol-position: top right;\n"
"    height: 11px;\n"
"    width: 15px;\n"
"    image: url(:/icons/icons/arrow_up.svg);\n"
"    background-color: rgba(33, 43, 51, 100);\n"
"}\n"
"\n"
"QRadioButton::indicator{\n"
"    background-color: rgba(33, 43, 51, 100);\n"
"    border-radius: 7px;\n"
"}\n"
"QRadioButton::indicator:checked{\n"
"    background-color: white;\n"
"    border: 4px solid rgba(33, 43, 51, 100);\n"
"}\n"
"QCheckBox::indicator {\n"
"    width: 14px;\n"
"    height: 14px;\n"
"}\n"
"QCheckBox::indicator:checked{\n"
"    image: url(:/icons/icons/done.svg);\n"
"}\n"
"QComboBox::drop-down {\n"
"    image: url(:/icons/icons/list_down.svg);\n"
"}")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(5)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_6 = QCustomSlideMenu(self.centralwidget)
        self.frame_6.setObjectName(u"frame_6")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_6.sizePolicy().hasHeightForWidth())
        self.frame_6.setSizePolicy(sizePolicy)
        self.frame_6.setMinimumSize(QSize(290, 0))
        self.frame_6.setMaximumSize(QSize(297, 16777215))
        self.verticalLayout_2 = QVBoxLayout(self.frame_6)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 9)
        self.stackedWidget = QStackedWidget(self.frame_6)
        self.stackedWidget.setObjectName(u"stackedWidget")
        sizePolicy.setHeightForWidth(self.stackedWidget.sizePolicy().hasHeightForWidth())
        self.stackedWidget.setSizePolicy(sizePolicy)
        self.stackedWidget.setMinimumSize(QSize(0, 535))
        self.stackedWidget.setMaximumSize(QSize(16777215, 16777215))
        self.stackedWidget.setLineWidth(0)
        self.page_1 = QWidget()
        self.page_1.setObjectName(u"page_1")
        sizePolicy.setHeightForWidth(self.page_1.sizePolicy().hasHeightForWidth())
        self.page_1.setSizePolicy(sizePolicy)
        self.page_1.setMaximumSize(QSize(16777215, 16777215))
        self.verticalLayout_5 = QVBoxLayout(self.page_1)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.frame_8 = QFrame(self.page_1)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setMinimumSize(QSize(4, 0))
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_8)
        self.verticalLayout_6.setSpacing(9)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_2 = QLabel(self.frame_8)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(16777215, 16777215))

        self.verticalLayout_6.addWidget(self.label_2)

        self.lineEdit_2 = QLineEdit(self.frame_8)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setMinimumSize(QSize(50, 22))
        self.lineEdit_2.setMaximumSize(QSize(100, 16777215))

        self.verticalLayout_6.addWidget(self.lineEdit_2)


        self.verticalLayout_5.addWidget(self.frame_8)

        self.frame_9 = QFrame(self.page_1)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_9)
        self.verticalLayout_7.setSpacing(8)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(8, 8, 8, 8)
        self.label_3 = QLabel(self.frame_9)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_7.addWidget(self.label_3)

        self.lineEdit = QLineEdit(self.frame_9)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMinimumSize(QSize(50, 22))
        self.lineEdit.setMaximumSize(QSize(100, 16777215))

        self.verticalLayout_7.addWidget(self.lineEdit)


        self.verticalLayout_5.addWidget(self.frame_9)

        self.frame_10 = QFrame(self.page_1)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setMinimumSize(QSize(0, 0))
        self.frame_10.setMaximumSize(QSize(16777215, 16777215))
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_15 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_15.setSpacing(12)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(8, 8, 8, 8)
        self.frame_17 = QFrame(self.frame_10)
        self.frame_17.setObjectName(u"frame_17")
        sizePolicy.setHeightForWidth(self.frame_17.sizePolicy().hasHeightForWidth())
        self.frame_17.setSizePolicy(sizePolicy)
        self.frame_17.setMinimumSize(QSize(0, 0))
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_17)
        self.verticalLayout_10.setSpacing(6)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.label_9 = QLabel(self.frame_17)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMaximumSize(QSize(16777215, 16777215))
        font = QFont()
        font.setFamily(u"Montserrat")
        self.label_9.setFont(font)

        self.verticalLayout_10.addWidget(self.label_9)

        self.spinBox_2 = QSpinBox(self.frame_17)
        self.spinBox_2.setObjectName(u"spinBox_2")
        self.spinBox_2.setMinimumSize(QSize(30, 22))
        self.spinBox_2.setMaximumSize(QSize(60, 51))
        self.spinBox_2.setMinimum(1)

        self.verticalLayout_10.addWidget(self.spinBox_2)


        self.horizontalLayout_15.addWidget(self.frame_17)


        self.verticalLayout_5.addWidget(self.frame_10, 0, Qt.AlignTop)

        self.frame_12 = QFrame(self.page_1)
        self.frame_12.setObjectName(u"frame_12")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_12.sizePolicy().hasHeightForWidth())
        self.frame_12.setSizePolicy(sizePolicy1)
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_12)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.pushButton = QPushButton(self.frame_12)
        self.pushButton.setObjectName(u"pushButton")
        sizePolicy2 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy2)
        self.pushButton.setMinimumSize(QSize(100, 20))
        self.pushButton.setIconSize(QSize(16, 16))

        self.horizontalLayout_13.addWidget(self.pushButton)


        self.verticalLayout_5.addWidget(self.frame_12, 0, Qt.AlignTop)

        self.frame_23 = QFrame(self.page_1)
        self.frame_23.setObjectName(u"frame_23")
        sizePolicy1.setHeightForWidth(self.frame_23.sizePolicy().hasHeightForWidth())
        self.frame_23.setSizePolicy(sizePolicy1)
        self.frame_23.setMaximumSize(QSize(16777215, 16777215))
        self.frame_23.setFrameShape(QFrame.StyledPanel)
        self.frame_23.setFrameShadow(QFrame.Raised)

        self.verticalLayout_5.addWidget(self.frame_23)

        self.stackedWidget.addWidget(self.page_1)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        sizePolicy.setHeightForWidth(self.page_2.sizePolicy().hasHeightForWidth())
        self.page_2.setSizePolicy(sizePolicy)
        self.page_2.setMinimumSize(QSize(0, 0))
        self.verticalLayout_15 = QVBoxLayout(self.page_2)
        self.verticalLayout_15.setSpacing(9)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.frame_11 = QFrame(self.page_2)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.frame_11)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.comboBox = QComboBox(self.frame_11)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setMaximumSize(QSize(16777215, 16777215))

        self.verticalLayout_16.addWidget(self.comboBox)


        self.verticalLayout_15.addWidget(self.frame_11, 0, Qt.AlignTop)

        self.stackedWidget_3 = QStackedWidget(self.page_2)
        self.stackedWidget_3.setObjectName(u"stackedWidget_3")
        sizePolicy3 = QSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.stackedWidget_3.sizePolicy().hasHeightForWidth())
        self.stackedWidget_3.setSizePolicy(sizePolicy3)
        self.stackedWidget_3.setMaximumSize(QSize(11111111, 81))
        self.page_file = QWidget()
        self.page_file.setObjectName(u"page_file")
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.MinimumExpanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.page_file.sizePolicy().hasHeightForWidth())
        self.page_file.setSizePolicy(sizePolicy4)
        self.page_file.setMaximumSize(QSize(16777215, 81))
        self.verticalLayout_17 = QVBoxLayout(self.page_file)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(-1, -1, -1, 9)
        self.frame_13 = QFrame(self.page_file)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.frame_13)
        self.verticalLayout_18.setSpacing(9)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_18.setContentsMargins(-1, 0, -1, 0)
        self.label_5 = QLabel(self.frame_13)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMaximumSize(QSize(16777215, 16777215))

        self.verticalLayout_18.addWidget(self.label_5)

        self.pushButton_3 = QPushButton(self.frame_13)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setMaximumSize(QSize(120, 35))
        self.pushButton_3.setIconSize(QSize(10, 16))

        self.verticalLayout_18.addWidget(self.pushButton_3)


        self.verticalLayout_17.addWidget(self.frame_13, 0, Qt.AlignTop)

        self.stackedWidget_3.addWidget(self.page_file)
        self.page_circle = QWidget()
        self.page_circle.setObjectName(u"page_circle")
        sizePolicy4.setHeightForWidth(self.page_circle.sizePolicy().hasHeightForWidth())
        self.page_circle.setSizePolicy(sizePolicy4)
        self.page_circle.setMaximumSize(QSize(16777215, 70))
        self.verticalLayout_20 = QVBoxLayout(self.page_circle)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.frame_25 = QFrame(self.page_circle)
        self.frame_25.setObjectName(u"frame_25")
        self.frame_25.setFrameShape(QFrame.StyledPanel)
        self.frame_25.setFrameShadow(QFrame.Raised)
        self.verticalLayout_19 = QVBoxLayout(self.frame_25)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(-1, 0, -1, -1)
        self.label_6 = QLabel(self.frame_25)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout_19.addWidget(self.label_6)

        self.doubleSpinBox = QDoubleSpinBox(self.frame_25)
        self.doubleSpinBox.setObjectName(u"doubleSpinBox")
        self.doubleSpinBox.setMaximumSize(QSize(90, 16777215))

        self.verticalLayout_19.addWidget(self.doubleSpinBox)


        self.verticalLayout_20.addWidget(self.frame_25, 0, Qt.AlignTop)

        self.stackedWidget_3.addWidget(self.page_circle)
        self.page_square = QWidget()
        self.page_square.setObjectName(u"page_square")
        sizePolicy4.setHeightForWidth(self.page_square.sizePolicy().hasHeightForWidth())
        self.page_square.setSizePolicy(sizePolicy4)
        self.page_square.setMaximumSize(QSize(16777215, 112))
        self.verticalLayout_21 = QVBoxLayout(self.page_square)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_21.setContentsMargins(-1, 9, -1, -1)
        self.frame_26 = QFrame(self.page_square)
        self.frame_26.setObjectName(u"frame_26")
        self.frame_26.setFrameShape(QFrame.StyledPanel)
        self.frame_26.setFrameShadow(QFrame.Raised)
        self.verticalLayout_22 = QVBoxLayout(self.frame_26)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.verticalLayout_22.setContentsMargins(-1, 0, -1, 0)
        self.label_8 = QLabel(self.frame_26)
        self.label_8.setObjectName(u"label_8")

        self.verticalLayout_22.addWidget(self.label_8)

        self.doubleSpinBox_2 = QDoubleSpinBox(self.frame_26)
        self.doubleSpinBox_2.setObjectName(u"doubleSpinBox_2")
        self.doubleSpinBox_2.setMaximumSize(QSize(90, 16777215))

        self.verticalLayout_22.addWidget(self.doubleSpinBox_2)

        self.label_10 = QLabel(self.frame_26)
        self.label_10.setObjectName(u"label_10")

        self.verticalLayout_22.addWidget(self.label_10, 0, Qt.AlignTop)

        self.doubleSpinBox_3 = QDoubleSpinBox(self.frame_26)
        self.doubleSpinBox_3.setObjectName(u"doubleSpinBox_3")
        self.doubleSpinBox_3.setMaximumSize(QSize(90, 16777215))

        self.verticalLayout_22.addWidget(self.doubleSpinBox_3)


        self.verticalLayout_21.addWidget(self.frame_26, 0, Qt.AlignTop)

        self.stackedWidget_3.addWidget(self.page_square)
        self.none_page = QWidget()
        self.none_page.setObjectName(u"none_page")
        sizePolicy5 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Ignored)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.none_page.sizePolicy().hasHeightForWidth())
        self.none_page.setSizePolicy(sizePolicy5)
        self.none_page.setMaximumSize(QSize(0, 0))
        self.stackedWidget_3.addWidget(self.none_page)

        self.verticalLayout_15.addWidget(self.stackedWidget_3)

        self.frame_24 = QFrame(self.page_2)
        self.frame_24.setObjectName(u"frame_24")
        sizePolicy1.setHeightForWidth(self.frame_24.sizePolicy().hasHeightForWidth())
        self.frame_24.setSizePolicy(sizePolicy1)
        self.frame_24.setMaximumSize(QSize(16777215, 16777215))
        self.frame_24.setFrameShape(QFrame.StyledPanel)
        self.frame_24.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frame_24)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.pushButton_2 = QPushButton(self.frame_24)
        self.pushButton_2.setObjectName(u"pushButton_2")
        sizePolicy6 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy6)
        self.pushButton_2.setMinimumSize(QSize(150, 30))

        self.verticalLayout_13.addWidget(self.pushButton_2)


        self.verticalLayout_15.addWidget(self.frame_24, 0, Qt.AlignTop)

        self.frame_14 = QFrame(self.page_2)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_14)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.pushButton_4 = QPushButton(self.frame_14)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setMinimumSize(QSize(150, 30))

        self.horizontalLayout_6.addWidget(self.pushButton_4)


        self.verticalLayout_15.addWidget(self.frame_14)

        self.frame_22 = QFrame(self.page_2)
        self.frame_22.setObjectName(u"frame_22")
        sizePolicy1.setHeightForWidth(self.frame_22.sizePolicy().hasHeightForWidth())
        self.frame_22.setSizePolicy(sizePolicy1)
        self.frame_22.setLayoutDirection(Qt.LeftToRight)
        self.frame_22.setFrameShape(QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QFrame.Raised)

        self.verticalLayout_15.addWidget(self.frame_22)

        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.stackedWidget.addWidget(self.page_3)

        self.verticalLayout_2.addWidget(self.stackedWidget)


        self.horizontalLayout.addWidget(self.frame_6)

        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setEnabled(True)
        self.frame.setMinimumSize(QSize(410, 545))
        self.frame.setMaximumSize(QSize(16777215, 16777215))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.header_frame = QFrame(self.frame)
        self.header_frame.setObjectName(u"header_frame")
        self.header_frame.setMinimumSize(QSize(0, 45))
        self.header_frame.setMaximumSize(QSize(16777215, 45))
        self.header_frame.setFrameShape(QFrame.StyledPanel)
        self.header_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.header_frame)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_5 = QFrame(self.header_frame)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_4.setSpacing(5)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(5, 3, 5, 3)
        self.pushButton_7 = QPushButton(self.frame_5)
        self.pushButton_7.setObjectName(u"pushButton_7")
        sizePolicy.setHeightForWidth(self.pushButton_7.sizePolicy().hasHeightForWidth())
        self.pushButton_7.setSizePolicy(sizePolicy)
        self.pushButton_7.setMinimumSize(QSize(30, 30))
        self.pushButton_7.setMaximumSize(QSize(30, 30))
        icon = QIcon()
        icon.addFile(u":/icons/icons/arrow_back.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_7.setIcon(icon)
        self.pushButton_7.setIconSize(QSize(15, 16))
        self.pushButton_7.setCheckable(False)

        self.horizontalLayout_4.addWidget(self.pushButton_7)

        self.label = QLabel(self.frame_5)
        self.label.setObjectName(u"label")

        self.horizontalLayout_4.addWidget(self.label)


        self.horizontalLayout_2.addWidget(self.frame_5)

        self.frame_3 = QFrame(self.header_frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(-1, 3, -1, 3)

        self.horizontalLayout_2.addWidget(self.frame_3)

        self.frame_4 = QFrame(self.header_frame)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_5.setSpacing(15)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 3, 5, 3)
        self.minimize_window_button = QPushButton(self.frame_4)
        self.minimize_window_button.setObjectName(u"minimize_window_button")
        self.minimize_window_button.setMinimumSize(QSize(30, 30))
        self.minimize_window_button.setMaximumSize(QSize(30, 30))
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/remove.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.minimize_window_button.setIcon(icon1)

        self.horizontalLayout_5.addWidget(self.minimize_window_button)

        self.restore_window_button = QPushButton(self.frame_4)
        self.restore_window_button.setObjectName(u"restore_window_button")
        self.restore_window_button.setMinimumSize(QSize(30, 30))
        self.restore_window_button.setMaximumSize(QSize(30, 30))
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/open.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.restore_window_button.setIcon(icon2)
        self.restore_window_button.setIconSize(QSize(13, 13))
        self.restore_window_button.setAutoRepeat(False)
        self.restore_window_button.setAutoExclusive(False)
        self.restore_window_button.setAutoRepeatInterval(300)

        self.horizontalLayout_5.addWidget(self.restore_window_button)

        self.close_window_button = QPushButton(self.frame_4)
        self.close_window_button.setObjectName(u"close_window_button")
        sizePolicy.setHeightForWidth(self.close_window_button.sizePolicy().hasHeightForWidth())
        self.close_window_button.setSizePolicy(sizePolicy)
        self.close_window_button.setMinimumSize(QSize(30, 30))
        self.close_window_button.setMaximumSize(QSize(30, 30))
        icon3 = QIcon()
        icon3.addFile(u":/icons/icons/close.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.close_window_button.setIcon(icon3)
        self.close_window_button.setIconSize(QSize(20, 20))

        self.horizontalLayout_5.addWidget(self.close_window_button)


        self.horizontalLayout_2.addWidget(self.frame_4, 0, Qt.AlignRight)


        self.verticalLayout.addWidget(self.header_frame)

        self.frame_7 = QFrame(self.frame)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_7)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 5, 5, 0)
        self.stackedWidget_2 = QStackedWidget(self.frame_7)
        self.stackedWidget_2.setObjectName(u"stackedWidget_2")
        self.menu_page_1 = QWidget()
        self.menu_page_1.setObjectName(u"menu_page_1")
        self.verticalLayout_4 = QVBoxLayout(self.menu_page_1)
        self.verticalLayout_4.setSpacing(3)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(6, 6, 6, 6)
        self.tabWidget = QTabWidget(self.menu_page_1)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setEnabled(True)
        self.tabWidget.setMaximumSize(QSize(16777214, 16777214))

        self.verticalLayout_4.addWidget(self.tabWidget)

        self.stackedWidget_2.addWidget(self.menu_page_1)
        self.menu_page_2 = QWidget()
        self.menu_page_2.setObjectName(u"menu_page_2")
        self.menu_page_2.setEnabled(True)
        self.menu_page_2.setMaximumSize(QSize(16777215, 16777215))
        self.stackedWidget_2.addWidget(self.menu_page_2)
        self.menu_page_3 = QWidget()
        self.menu_page_3.setObjectName(u"menu_page_3")
        self.stackedWidget_2.addWidget(self.menu_page_3)

        self.verticalLayout_3.addWidget(self.stackedWidget_2)


        self.verticalLayout.addWidget(self.frame_7)

        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(0, 10))
        self.frame_2.setMaximumSize(QSize(16777215, 10))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_14.setSpacing(0)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.size_grip = QFrame(self.frame_2)
        self.size_grip.setObjectName(u"size_grip")
        self.size_grip.setMinimumSize(QSize(10, 10))
        self.size_grip.setMaximumSize(QSize(10, 10))
        self.size_grip.setFrameShape(QFrame.StyledPanel)
        self.size_grip.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_14.addWidget(self.size_grip, 0, Qt.AlignRight)


        self.verticalLayout.addWidget(self.frame_2, 0, Qt.AlignRight)


        self.horizontalLayout.addWidget(self.frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)
        self.stackedWidget_3.setCurrentIndex(0)
        self.stackedWidget_2.setCurrentIndex(1)
        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0441\u0441\u0442\u043e\u044f\u043d\u0438\u0435 \u043c\u0435\u0436\u0434\u0443 \u0443\u0437\u043b\u0430\u043c\u0438", None))
        self.lineEdit_2.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u0443\u0437\u043b\u043e\u0432 \u0432 \u043f\u043b\u043e\u0441\u043a\u043e\u0441\u0442\u0438", None))
        self.lineEdit.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u0438\u0441\u043a\u043e\u043c\u044b\u0445 \u0421\u0424", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u0413\u0435\u043d\u0435\u0440\u0430\u0446\u0438\u044f", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0433\u0440\u0443\u0437\u043a\u0430 \u0438\u0437 \u0444\u0430\u0439\u043b\u0430", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0434\u0430\u043d\u0438\u0435 \u043e\u043a\u0440\u0443\u0436\u043d\u043e\u0441\u0442\u0438", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0434\u0430\u043d\u0438\u0435 \u043f\u0440\u044f\u043c\u043e\u0443\u0433\u043e\u043b\u044c\u043d\u043e\u0439 \u043e\u0431\u043b\u0430\u0441\u0442\u0438", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0434\u0430\u043d\u0438\u0435 \u0441 \u043f\u043e\u043c\u043e\u0449\u044c\u044e \u043f\u0440\u044f\u043c\u044b\u0445", None))
        self.comboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0434\u0430\u043d\u0438\u0435 \u0441 \u043f\u043e\u043c\u043e\u0449\u044c\u044e \u043a\u0440\u0438\u0432\u044b\u0445", None))

        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0433\u0440\u0443\u0437\u0438\u0442\u044c \u0444\u0430\u0439\u043b:", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0434\u0438\u0443\u0441:", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"\u0428\u0438\u0440\u0438\u043d\u0430:", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0441\u043e\u0442\u0430:", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0438\u0441\u043a\u0440\u0435\u0442\u0438\u0437\u0438\u0440\u043e\u0432\u0430\u0442\u044c \u043e\u0431\u043b\u0430\u0441\u0442\u044c", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0431\u0440\u043e\u0441\u0438\u0442\u044c", None))
        self.pushButton_7.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u041c\u0435\u043d\u044e", None))
        self.minimize_window_button.setText("")
        self.restore_window_button.setText("")
        self.close_window_button.setText("")

