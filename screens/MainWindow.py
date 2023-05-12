from PyQt6.QtWidgets import QMainWindow, QTreeView, QTreeWidget
from src.model import event_log_table_model

_minimum_window_width = 300


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")
        self.__table_view = QTreeView()
        self.__table_view.setModel(event_log_table_model)
        self.__table_view.expandAll()
        self.__table_view.clicked.connect(self.some_action)
        self.setFixedSize(700, 600)
        self.setMinimumWidth(_minimum_window_width)
        self.setCentralWidget(self.__table_view)

    def some_action(self):
        for val in self.__table_view.selectedIndexes():
            print(val.data())
        print("check")
