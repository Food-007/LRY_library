from PyQt5 import QtCore, QtGui, QtWidgets
class YNWindow(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(451, 451)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(0, 0, 451, 391))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(".\\photo.png"))
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(60, 410, 75, 28))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(11)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(320, 410, 75, 28))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(11)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "缴纳付款"))
        self.pushButton.setText(_translate("Form", "已付款"))
        self.pushButton_2.setText(_translate("Form", "未付款"))
        self.pushButton.clicked.connect(self.yes)
        self.pushButton_2.clicked.connect(self.no)

    def yes(self):
        f = open(".\\key")
        self.hide()

    def no(self):
        self.hide()
