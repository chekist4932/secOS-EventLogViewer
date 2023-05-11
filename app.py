from PyQt6.QtWidgets import QApplication
from windows.MainWindow import MainWindow
import sys

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
