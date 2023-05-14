from PyQt6.QtWidgets import QMainWindow, QHBoxLayout, QWidget
from PyQt6.QtCore import Qt
from widgets.LogHeadersWidget import LogHeadersWidget
from widgets.LogViewWidget import LogViewWidget

_minimum_window_width = 300


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("EventLogViewer")
        self._box = QHBoxLayout()

        self._event_headers_widget = LogHeadersWidget()
        self._event_logs_widget = LogViewWidget()

        self._box.addWidget(self._event_headers_widget, 0, Qt.AlignmentFlag.AlignLeft)
        self._box.addWidget(self._event_logs_widget, 1)
        self.setLayout(self._box)

        self.setMinimumWidth(_minimum_window_width)
        wdg = QWidget()
        wdg.setLayout(self._box)

        self.setCentralWidget(wdg)


