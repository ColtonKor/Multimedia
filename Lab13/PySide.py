import sys
from PySide6.QtWidgets import (QApplication, QWidget, QLabel, QVBoxLayout, QPushButton, QComboBox, QHBoxLayout, QLineEdit)
from PySide6.QtCore import Slot  
from PySide6.QtCore import Qt
from __feature__ import snake_case, true_property

my_app = QApplication([])

# The dictionary from the previous lab
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


#Lab 13
class Task12(QWidget):
    def __init__(self):
        super().__init__()
        self.palette = Qt.blue
        
        # I decided to put both the background and the nested in the same Window because the background was only one line.
        h_layout = QHBoxLayout()
        b1 = QLineEdit("What's your favorite song?")
        b2 = QPushButton("Confirm Song")
        #I made a different version of the nested layout by switching around the layouts and adding different objects in the window
        h_layout.add_widget(b1)
        h_layout.add_widget(b2)

        v_layout = QVBoxLayout()
        b4 = QComboBox()

        b4.add_items(color_list)

        b5 = QPushButton("Confirm Color")


        v_layout.add_widget(b4)
        v_layout.add_widget(b5)

        main_layout = QVBoxLayout()

        main_layout.add_layout(h_layout)
        main_layout.add_layout(v_layout)
        self.set_layout(main_layout)


class Task3(QWidget):
    def __init__(self):
        super().__init__()
        h_layout = QHBoxLayout()
        self.b4 = QComboBox()

        
        self.b4.add_items(color_list)

        b5 = QPushButton("Confirm Color!")

        h_layout.add_widget(self.b4)
        h_layout.add_widget(b5)
        # I followed the same format I did for the last lab on showing the rgb and hex from the color.
        # I instead ignored those values and just focused on the names.
        main_layout = QVBoxLayout()

        main_layout.add_layout(h_layout)
        self.set_layout(main_layout)
        b5.clicked.connect(self.on_click)

    @Slot()
    def on_click(self):
        i = self.b4.current_index
        self.new_win = NewTask3(color_list[i]) # I passed the color name into the new window
        self.new_win.show()

class NewTask3(QWidget):
  def __init__(self, Color):
    super().__init__()
    self.palette = getattr(Qt, Color) # I was looking up how to get the color from the variable to be Qt and I found this which works.

a = Task12()
b = Task3()
a.show()
b.show()
sys.exit(my_app.exec())