import sys
from PyQt5.QtWidgets import *
from main_UI import MainWindow
class MyWindow(QWidget, MainWindow):
    def __init__(self):
        super(QWidget, self).__init__()
        self.setupUi(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MyWindow()
    w.show()
    app.exec()
