import sys

from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import (
    QMainWindow, QApplication,
    QLabel, QCheckBox, QComboBox, QListWidget, QLineEdit,
    QLineEdit, QSpinBox, QDoubleSpinBox, QSlider, QVBoxLayout
)
from PyQt6.QtCore import Qt

class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        layout = QVBoxLayout(self)
        self.setWindowTitle("My App")

        widget = QLabel(self)
        widget.setPixmap(QPixmap('1.png'))
        widget.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter)

        self.setCentralWidget(widget)

        layout.addWidget(widget)
        self.setLayout(layout)

app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec()