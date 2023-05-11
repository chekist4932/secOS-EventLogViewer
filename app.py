from PyQt6.QtWidgets import QApplication
from screens.MainWindow import MainWindow
from screens.EventLogView import EventLogWindow

import sys

if __name__ == "__main__":
    app = QApplication(sys.argv)

    # window = MainWindow()
    window = EventLogWindow()
    window.show()

    sys.exit(app.exec())
