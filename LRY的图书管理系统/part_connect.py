from PyQt5.QtWidgets import *
from part_connect_UI import LoginWindow
class LWindow(QWidget, LoginWindow):
    def __init__(self):
        super(QWidget, self).__init__()
        self.setupUi(self)
