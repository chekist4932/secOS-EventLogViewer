from PyQt6.QtWidgets import QMainWindow, QTableView, QTreeView
from PyQt6.QtGui import QStandardItem

from PyQt6.QtCore import Qt

from src.model import event_tree_model, count_headers, max_header_len
from src.log_getter import get_event_logs
from src.schemas import LogSchema

_minimum_window_width = 300


class EventLogWindow(QMainWindow):
    def __init__(self):
        super().__init__()


        self._tree_view = QTreeView()
        self._tree_view.setSortingEnabled(True)
        self._tree_view.setModel(event_tree_model)
        # col_width = max_header_len * 9
        # self._tree_view.setColumnWidth(col_count, col_width)

        self.setFixedSize(700, 600)
        self.setMinimumWidth(_minimum_window_width)

        self.setCentralWidget(self._tree_view)
