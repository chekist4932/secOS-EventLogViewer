from PyQt6.QtWidgets import QApplication, QMainWindow, QTreeView, QPushButton
from screens.MainWindow import MainWindow
from screens.EventLogView import EventLogWindow
from widgets.LogHeadersWidget import LogHeadersWidget

import sys





if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    # window = EventLogWindow()
    # window = EventLogListWidget()
    window.show()

    sys.exit(app.exec())
