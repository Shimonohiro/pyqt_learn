import sys
from PyQt6.QtWidgets import *
from PyQt6 import uic
from PyQt6.QtGui import QColor

class ColorSliderApp(QWidget):

    def __init__(self):
        super().__init__()
        self.ui = uic.loadUi('F:/pyqt_learn/mw.ui')
        self.ui.verticalSlider.valueChanged.connect(self.updateColor)
        self.ui.verticalSlider_2.valueChanged.connect(self.updateColor)
        self.ui.verticalSlider_3.valueChanged.connect(self.updateColor)
        self.updateColor()

    def updateColor(self):
        red = self.ui.verticalSlider.value()
        green = self.ui.verticalSlider_2.value()
        blue = self.ui.verticalSlider_3.value()
        color = QColor(red, green, blue)
        self.ui.label_4.setStyleSheet(f"background-color: {color.name()}")

if __name__ == '__main__':
    app = QApplication(sys.argv)

    w = ColorSliderApp()
    # 展示窗口
    w.ui.show()

    app.exec()
