import sys
from PyQt5.QtWidgets import *
from part_admin_UI import AdminWindow
class AWindow(QWidget, AdminWindow):
    def __init__(self, name):
        super(QWidget, self).__init__()
        self.setupUi(self, name)
app = QApplication(sys.argv)
w = AWindow("LRY")
w.show()
app.exec()
