from PyQt5.QtWidgets import *
from part_user_UI import UserWindow
class UWindow(QWidget, UserWindow):
    def __init__(self, name):
        super(QWidget, self).__init__()
        self.setupUi(self, name)
