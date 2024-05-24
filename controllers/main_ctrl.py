from PyQt5.QtCore import QObject, pyqtSlot


class MainController(QObject):
    def __init__(self, model, square_figure, file_figure):
        super().__init__()

        self._model = model
        self._square_figure = square_figure
        self._file_figure = file_figure


    @pyqtSlot(str, str, str)
    def open_draw_widget(self, count_nodes, count_function, step):
        print(count_nodes, count_function)
        self._model._count_nodes = int(count_nodes)
        self._model.count_function = int(count_function)
        self._model._step = float(step)
        self._model.create_draw_area()
        self._model.open_draw_window()

    @pyqtSlot(int)
    def change_type_window_for_settings_draw_area(self, ind):
        print("change_type_window_for_settings_draw_area", ind)
        self._model.current_type_draw_area = ind

        if self._model.current_type_draw_area == 3 or self._model.current_type_draw_area == 4:
            self._model.minimize_window_with_draw_area_settings()
        else:
            self._model.set_current_size_for_window_with_draw_area_settings()

        self._model.change_method_for_draw_area()

    @pyqtSlot()
    def create_graphics(self):
        self._model.find_eigenvalue()

    @pyqtSlot()
    def start_program(self):
        self._model.start_new_program()


