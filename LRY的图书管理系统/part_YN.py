from PyQt5.QtWidgets import *
from part_YN_UI import YNWindow
class YN(QWidget, YNWindow):
    def __init__(self):
        super(QWidget, self).__init__()
        self.setupUi(self)