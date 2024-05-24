import matplotlib

matplotlib.use('Qt5Agg')
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg, NavigationToolbar2QT as NavigationToolbar


class GraphicCanvas(FigureCanvasQTAgg):
    def __init__(self, fig, ax):
        self.fig = fig
        self.ax = ax
        super(GraphicCanvas, self).__init__(self.fig)
