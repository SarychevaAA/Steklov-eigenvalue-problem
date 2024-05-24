import numpy as np
import pandas
from PyQt5 import QtWidgets
from PyQt5.QtCore import QObject, pyqtSlot
from PyQt5.QtWidgets import QFileDialog
from PyQt5.uic.properties import QtGui


class FileFigureController(QObject):
    def __init__(self, file_figure):
        super().__init__()

        self._file_figure = file_figure

    @pyqtSlot()
    def read_file(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(None, "Выберите файл", "", "txt (*.txt)", options=options)
        data = pandas.read_csv(fileName, sep=" ", header=None)
        self._file_figure.read_data(np.matrix(data))



