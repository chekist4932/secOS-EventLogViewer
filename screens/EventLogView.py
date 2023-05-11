from PyQt6.QtWidgets import QMainWindow, QTableView, QTreeView
from PyQt6.QtGui import QStandardItem

from PyQt6.QtCore import Qt

from src.model import main_tree_model, count_headers, max_header_len
from src.log_getter import get_event_logs
from src.schemas import LogSchema

_minimum_window_width = 300
_event_logs = get_event_logs()


class EventLogWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        self._tree_view = QTreeView()
        self._tree_view.setSortingEnabled(True)
        self._tree_view.setModel(main_tree_model)
        for event_log in _event_logs:
            sc = LogSchema(**event_log).dict()
            item = [QStandardItem(item_log) for item_log in sc.values()]
            for col_count, row in enumerate(item):
                row.setEditable(False)
                align_flag = Qt.AlignmentFlag.AlignLeft
                col_width = max_header_len * 9
                row.setTextAlignment(align_flag)
                self._tree_view.setColumnWidth(col_count, col_width)
            main_tree_model.appendRow(item)

        self.setFixedSize(700, 600)
        self.setMinimumWidth(_minimum_window_width)

        self.setCentralWidget(self._tree_view)
