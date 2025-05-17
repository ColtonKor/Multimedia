import PySide6.QtCore


#The Widget I picked is called QWizard. Wizards are designed to help the person through difficult challenges while using QTWidget.


# import sys
# from PySide6.QtWidgets import QApplication, QWidget, QLabel
# from PySide6.QtCore import Qt

# from __feature__ import snake_case, true_property

# my_qt_app = QApplication([])

# class ColorWindow(QWidget):
#     def __init__(self):
#         super().__init__()

#         self.window_title = 'Window'
#         self.palette = Qt.darkMagenta
#         label1 = QLabel('<h1>Colton Korhummel</h1>')
#         label1.set_parent(self)

# my_window = ColorWindow()
# my_window.show()

# sys.exit(my_qt_app.exec())


import sys
from PySide6.QtWidgets import (QApplication, QWidget, QLabel, QVBoxLayout, QPushButton, QComboBox, QHBoxLayout, QLineEdit)
from PySide6.QtCore import Slot  
from PySide6.QtCore import Qt
from __feature__ import snake_case, true_property

my_app = QApplication([])

# Lab 11
# class MyWindow(QWidget):
#   def __init__(self):
#       super().__init__()
#       self.show()

# class LayoutOne(QWidget):
#   def __init__(self):
#       super().__init__()
#       label1 = QLabel('Label 1')
#       label2 = QLabel('Label 2')
#       vbox = QVBoxLayout()
#       vbox.add_widget(label1)
#       vbox.add_widget(label2)
#       self.set_layout(vbox)
#       self.resize(800, 600)
#       self.show()

#Lab12
colors = {
    "red": {"rgb": (255, 0, 0), "hex": "#FF0000"},
    "green": {"rgb": (0, 255, 0), "hex": "#00FF00"},
    "blue": {"rgb": (0, 0, 255), "hex": "#0000FF"},
    "yellow": {"rgb": (255, 255, 0), "hex": "#FFFF00"},
    "cyan": {"rgb": (0, 255, 255), "hex": "#00FFFF"},
    "magenta": {"rgb": (255, 0, 255), "hex": "#FF00FF"},
    "black": {"rgb": (0, 0, 0), "hex": "#000000"},
    "white": {"rgb": (255, 255, 255), "hex": "#FFFFFF"}
}
color_list = list(colors.keys())

class ButtonOne(QWidget):
    def __init__(self):
        super().__init__()
        vbox = QVBoxLayout()

        self.my_combo_box = QComboBox()
        self.my_combo_box.add_items(color_list)
        self.my_label = QLabel("RGB:     Hex: ")

        vbox = QVBoxLayout()
        vbox.add_widget(self.my_combo_box)
        vbox.add_widget(self.my_label)

        my_btn1 = QPushButton('button 1')
        self.my_lbl = QLabel('Task 1 buttons')
        my_btn1.clicked.connect(self.on_click1)

        my_btn2 = QPushButton('button 2')
        my_btn2.clicked.connect(self.on_click2)

        self.my_combo_box.currentIndexChanged.connect(self.update_ui)

        vbox.add_widget(self.my_lbl)
        vbox.add_widget(my_btn1)
        vbox.add_widget(my_btn2)
        self.set_layout(vbox)
        self.resize(400, 400)
        self.show()

    @Slot()
    def update_ui(self):
        my_index = self.my_combo_box.current_index
        current = self.my_list[my_index]
        color = colors.get(current.lower())
        rgb = color['rgb']
        hex = color['hex']
        self.my_label.text = f'RGB: {rgb}    Hex: {hex}'


    @Slot()
    def on_click1(self):
        self.my_lbl.text = 'I just pressed the first button'

    @Slot()
    def on_click2(self):
        self.my_lbl.text = 'The second button has been clicked!'

my_window = ButtonOne()

sys.exit(my_app.exec())