from PyQt6.QtWidgets import QTreeView, QVBoxLayout, QWidget, QMessageBox
from widgets.LogInfoDialog import LogInfo

from src.model import event_tree_model
from src.log_getter import get_event_logs

_minimum_widget_width = 300


class LogViewWidget(QWidget):
    def __init__(self):
        super().__init__()
        self._tree_view = QTreeView()
        self._tree_view.setMinimumWidth(_minimum_widget_width)
        self._tree_view.setSortingEnabled(True)
        self.vbox = QVBoxLayout()
        self.initUI()

    def initUI(self):
        self._tree_view.setModel(event_tree_model)
        self._tree_view.expandAll()
        self._tree_view.clicked.connect(self.some_action)

        self.vbox.addWidget(self._tree_view)
        self.setLayout(self.vbox)

    def some_action(self):
        log_number = self._tree_view.selectedIndexes()[0].data()
        log = get_event_logs.find_log(log_number)
        dialog = LogInfo(log=log, parent=self)
        dialog.exec()
