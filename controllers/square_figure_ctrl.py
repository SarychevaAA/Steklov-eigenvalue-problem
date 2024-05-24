from PyQt5.QtCore import QObject, pyqtSlot


class SquareFigureController(QObject):
    def __init__(self, square_figure):
        super().__init__()

        self._square_figure = square_figure

    @pyqtSlot(float)
    def change_width(self, width):
        self._square_figure.width = width

    @pyqtSlot(float)
    def change_height(self, height):
        self._square_figure.height = height



