from PyQt6.QtWidgets import QVBoxLayout, QLabel, QDialog, QPushButton
from PyQt6.QtCore import Qt


class LogInfo(QDialog):
    def __init__(self, log: dict, parent=None):
        super(LogInfo, self).__init__(parent)
        self.setWindowTitle("Log Info")
        self.vertical_layout = QVBoxLayout(self)
        self.pushButton = QPushButton(self)
        self.pushButton.clicked.connect(self.btnClosed)
        self.pushButton.setText("Close Dialog")

        self.verticalLayout = QVBoxLayout(self)
        self.log = log
        for key, item in self.log.items():
            string_label = f"{key}: {item}"
            print(f"Label string: {string_label}")
            label = QLabel(string_label)
            label.setAlignment(Qt.AlignmentFlag.AlignLeft)
            label.setWordWrap(True)
            self.verticalLayout.addWidget(label)
        self.vertical_layout.addLayout(self.verticalLayout)
        self.vertical_layout.addWidget(self.pushButton)
        self.setLayout(self.vertical_layout)

    def btnClosed(self):
        self.close()
