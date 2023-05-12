from PyQt6.QtWidgets import QTreeView
from PyQt6.QtWidgets import QWidget, QVBoxLayout

from src.model import event_headers_model
from src.model import event_log_changer

_fixed_widget_size = 150


class LogHeadersWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.__table_view = QTreeView()
        self._prev_header = ''
        self.__table_view.setFixedWidth(_fixed_widget_size)

        self.vbox = QVBoxLayout()
        self.initUI()

    def initUI(self):
        self.__table_view.setModel(event_headers_model)
        self.__table_view.expandAll()
        self.__table_view.clicked.connect(self.some_action)

        self.vbox.addWidget(self.__table_view)
        self.setLayout(self.vbox)

    def some_action(self):
        for val in self.__table_view.selectedIndexes():
            header = val.data()
            if header != self._prev_header:
                print(f"Header was changed '{header}' -> '{self._prev_header}'")
                self._prev_header = header
                event_log_changer(header)
