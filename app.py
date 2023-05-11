from PyQt6.QtWidgets import QApplication
from PyQt6.QtWidgets import QMainWindow, QTableView

from src.model import model, count_headers, max_header_len

import sys

_minimum_window_width = 300


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        self._table_view = QTableView()
        self._table_view.setShowGrid(False)
        self._table_view.setSortingEnabled(True)

        self._table_view.setModel(model)
        for i in range(count_headers):
            self._table_view.setColumnWidth(i, max_header_len * 10)
        self.setFixedSize(800, 600)
        self.setMinimumWidth(_minimum_window_width)

        self.setCentralWidget(self._table_view)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    app.exec()
