from bcrypt import *
from pymysql import *
from random import *
from part_connect import *
from part_admin import *
from part_user import *
from PyQt5 import QtWidgets, QtCore, QtGui
class MainWindow(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(809, 197)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(60, 150, 75, 23))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(11)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(110, 20, 211, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(30, 20, 71, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(50, 60, 51, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(110, 60, 211, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(Form)
        self.lineEdit_3.setGeometry(QtCore.QRect(110, 100, 111, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(30, 100, 71, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(16)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(230, 100, 91, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(210, 150, 75, 23))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(11)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.textBrowser = QtWidgets.QTextBrowser(Form)
        self.textBrowser.setGeometry(QtCore.QRect(340, 10, 461, 181))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(11)
        self.textBrowser.setFont(font)
        self.textBrowser.setObjectName("textBrowser")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)


    def retranslateUi(self, Form):
        self.co = self.code()
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "LRY的图书管理系统 登录界面"))
        self.label.setText(_translate("Form", "用户名:"))
        self.label_2.setText(_translate("Form", "密码:"))
        self.label_3.setText(_translate("Form", "验证码:"))
        self.label_4.setText(_translate("Form", self.co))
        self.pushButton.setText(_translate("Form", "登录"))
        self.pushButton_2.setText(_translate("Form", "注册"))
        self.pushButton.clicked.connect(self.sign)
        self.pushButton_2.clicked.connect(self.login)
    
    def login(self):
        self.hide()
        self.new_window = LWindow()
        self.new_window.show()

    def sign(self):
        _translate = QtCore.QCoreApplication.translate
        name = self.lineEdit.text()
        password = self.lineEdit_2.text()
        verificationcode = self.lineEdit_3.text()
        if len(name) == 0 or len(password) == 0 or len(verificationcode) == 0:
            self.textBrowser.setText("登录信息未填写, 请继续输入!")
            self.textBrowser.repaint()
        elif verificationcode != self.co:
            self.textBrowser.setText("验证码输入错误, 请继续输入!")
            self.textBrowser.repaint()
            self.co = self.code()
            self.label_4.setText(_translate("Form", self.co))
        else:
            con = connect(host = 'localhost', 
                          user = 'root', 
                          passwd='1qaz!QAZ', 
                          port= 3306, 
                          db='library', 
                          charset='utf8')
            cur = con.cursor()
            sql = "select name, password, identity from user where name = '%s'" % (name)
            cur.execute(sql)
            values = cur.fetchall()
            cur.close()
            con.close()
            if values != ():
                if checkpw(password.encode(), values[0][1].encode()):
                    self.close()
                    if  values[0][2] == "admin":
                        self.hide()
                        self.new_window = AWindow(values[0][0])
                        self.new_window.show()
                    else:
                        self.hide()
                        self.new_window = UWindow(values[0][0])
                        self.new_window.show()
                else:
                    self.textBrowser.setText("账号或密码错误, 请重新输入!")
                    self.textBrowser.repaint()
                    self.co = self.code()
                    self.label_4.setText(_translate("Form", self.co))
            else:
                self.textBrowser.setText("账号或密码错误, 请重新输入!")
                self.textBrowser.repaint()
                self.co = self.code()
                self.label_4.setText(_translate("Form", self.co))

    def code(self):
        c = ''
        l = [['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'], ['1', '2', '3', '4', '5', '6', '7', '8', '9']]
        for x in range(6):
            if randint(0,1) == 0:
                c += l[0][randint(0, 51)]
            else:
                c += l[1][randint(0, 8)]
        return c
