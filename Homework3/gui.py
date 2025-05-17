# Name: Colton Korhummel
# Class: Multimedia CST 205
# Date: 3/10/2025
# Description: This file is used for making GUI that allows the users to search for images using a keyword and pick a filter they want on the picture.


from functions import my_search, filter
from image_info import image_info
import sys
from PySide6.QtWidgets import (QApplication, QWidget, QLineEdit, QLabel, QVBoxLayout, QPushButton, QComboBox)
from PySide6.QtCore import Slot  
from PySide6.QtGui import QPixmap
from __feature__ import snake_case, true_property



class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.my_list = ["None", "Sepia", "Negative", "Grayscale", "Thumbnail"]

        self.my_combo_box = QComboBox()
        self.my_combo_box.add_items(self.my_list)
        self.my_filter_label = QLabel("What Filter Would You Like?")
        self.my_search_label = QLabel("Enter a Keyword to Search for an Image:")
        self.my_le = QLineEdit("Keyword")
        self.my_btn = QPushButton("Submit")
        self.my_id_label = QLabel("Id")
        vbox = QVBoxLayout()
        vbox.add_widget(self.my_search_label)
        vbox.add_widget(self.my_le)
        vbox.add_widget(self.my_filter_label)
        vbox.add_widget(self.my_combo_box)
        vbox.add_widget(self.my_btn)
        vbox.add_widget(self.my_id_label)

        self.set_layout(vbox)
        self.my_btn.clicked.connect(self.on_submit)
        self.my_le.returnPressed.connect(self.on_submit)

    @Slot()
    def on_submit(self):
        image_tag = self.my_le.text
        index = self.my_combo_box.current_index
        filter_tag = self.my_list[index]
        id = my_search(image_tag)
        self.my_id_label.text = id
        filter(id, filter_tag)
        self.new_win = NewWindow()
        self.new_win.show()

        

class NewWindow(QWidget):
  def __init__(self):
    super().__init__()
    label = QLabel()
    my_pixmap = QPixmap("gui_image.jpg")
    label.pixmap = my_pixmap
    self.layout = QVBoxLayout()
    self.layout.add_widget(label)
    self.set_layout(self.layout)
        


my_app = QApplication([])
my_win = MyWindow()
my_win.show()
sys.exit(my_app.exec())