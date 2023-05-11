from PyQt6.QtWidgets import QMainWindow, QTableView

from src.model import model

_minimum_window_width = 300


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.n_times_clicked = 0

        self.setWindowTitle("My App")

        self._table_view = QTableView()
        self._table_view.setShowGrid(False)
        self._table_view.setSortingEnabled(True)

        self._table_view.setModel(model)

        self.setFixedSize(600, 600)
        self.setMinimumWidth(_minimum_window_width)

        self.setCentralWidget(self._table_view)
