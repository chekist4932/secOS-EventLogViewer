from PyQt6.QtWidgets import QMainWindow, QTreeView
from src.model import event_log_table_model

_minimum_window_width = 300


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")
        self.__table_view = QTreeView()
        self.__table_view.setModel(event_log_table_model)
        self.setFixedSize(700, 600)
        self.setMinimumWidth(_minimum_window_width)
        self.setCentralWidget(self.__table_view)

    def __show_event_log_window(self):
        print("check")
