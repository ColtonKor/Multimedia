#The Widget I picked is called QWizard. Wizards are designed to help the person through difficult challenges while using QTWidget.


import sys
from PySide6.QtWidgets import QApplication, QWidget, QLabel
from PySide6.QtCore import Qt

from __feature__ import snake_case, true_property

my_qt_app = QApplication([])

class ColorWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.window_title = 'Window'
        self.palette = Qt.darkMagenta
        label1 = QLabel('<h1>Colton Korhummel</h1>')
        label1.set_parent(self)

my_window = ColorWindow()
my_window.show()

sys.exit(my_qt_app.exec())