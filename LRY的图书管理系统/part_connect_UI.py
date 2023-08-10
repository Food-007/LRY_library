from bcrypt import *
from pymysql import *
from random import *
from part_user import *
from PyQt5 import QtCore, QtGui, QtWidgets
class LoginWindow(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(809, 271)
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
        self.label_2.setGeometry(QtCore.QRect(50, 100, 51, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(Form)
        self.lineEdit_3.setGeometry(QtCore.QRect(110, 100, 211, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_5 = QtWidgets.QLineEdit(Form)
        self.lineEdit_5.setGeometry(QtCore.QRect(110, 180, 111, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        self.lineEdit_5.setFont(font)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(30, 180, 71, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(16)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(230, 180, 91, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(130, 230, 75, 23))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(11)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.textBrowser = QtWidgets.QTextBrowser(Form)
        self.textBrowser.setGeometry(QtCore.QRect(340, 10, 461, 241))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(11)
        self.textBrowser.setFont(font)
        self.textBrowser.setObjectName("textBrowser")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(10, 140, 91, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(16)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.lineEdit_4 = QtWidgets.QLineEdit(Form)
        self.lineEdit_4.setGeometry(QtCore.QRect(110, 140, 211, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        self.lineEdit_4.setFont(font)
        self.lineEdit_4.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(30, 60, 71, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(16)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.lineEdit_2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(110, 60, 211, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit_2.setObjectName("lineEdit_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        self.co = self.code()
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "LRY的图书管理系统 注册界面"))
        self.label.setText(_translate("Form", "用户名:"))
        self.label_2.setText(_translate("Form", "密码:"))
        self.label_3.setText(_translate("Form", "验证码:"))
        self.label_4.setText(_translate("Form", self.co))
        self.pushButton.setText(_translate("Form", "注册"))
        self.textBrowser.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'微软雅黑\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">注:</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">1. 此次注册为LRY的图书管理系统的用户注册, 只会注册为普通用户.</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">2. 用于注册的用户名和密码无法更改, 请谨慎填写.</p></body></html>"))
        self.label_5.setText(_translate("Form", "确认密码:"))
        self.label_6.setText(_translate("Form", "手机号:"))
        self.pushButton.clicked.connect(self.login)
    
    def login(self):
        _translate = QtCore.QCoreApplication.translate
        name = self.lineEdit.text()
        phonenumber = self.lineEdit_2.text()
        password = self.lineEdit_3.text()
        password_twe = self.lineEdit_4.text()
        verificationcode = self.lineEdit_5.text()
        if len(name) == 0 or len(phonenumber) == 0 or len(password) == 0 or len(password_twe) == 0 or len(verificationcode) == 0:
            self.textBrowser.setText("注册信息未填写, 请继续输入!")
            self.textBrowser.repaint()
        elif verificationcode != self.co:
            self.textBrowser.setText("验证码输入错误, 请继续输入!")
            self.textBrowser.repaint()
            self.co = self.code()
            self.label_4.setText(_translate("Form", self.co))
        else:
            if password == password_twe and len(phonenumber) == 11:
                con = connect(host = 'localhost', 
                              user = 'root', 
                              passwd='1qaz!QAZ', 
                              port= 3306, 
                              db='library', 
                              charset='utf8')
                cur = con.cursor()
                sql = "select name, phonenumber, password from user where name = '%s'" % (name)
                cur.execute(sql)
                values = cur.fetchall()
                if values != ():
                    self.textBrowser.setText("用户名已被征用, 请重新输入!")
                    self.textBrowser.repaint()
                    self.co = self.code()
                    self.label_4.setText(_translate("Form", self.co))
                    cur.close() 
                    con.close()
                else:
                    sql = "select name, phonenumber, password from user where phonenumber = '%s'" % (phonenumber)
                    cur.execute(sql)
                    values = cur.fetchall()
                    if values != ():
                        self.textBrowser.setText("手机号已注册了一个账号, 请重新输入!")
                        self.textBrowser.repaint()
                        self.co = self.code()
                        self.label_4.setText(_translate("Form", self.co))
                        cur.close() 
                        con.close()
                    else:
                        salt = gensalt(rounds=10)
                        _password = hashpw(password.encode(), salt)
                        _password = _password.decode('utf-8')
                        sql = "insert into user values('%s', '%s', '%s', 'user')" % (name, _password, phonenumber)
                        cur.execute(sql)
                        con.commit()
                        cur.close() 
                        con.close()
                        self.hide()
                        self.new_window = UWindow(values[0][0])
                        self.new_window.show()
            elif len(phonenumber) != 11:
                self.textBrowser.setText("手机号输入错误, 请重新输入!")
                self.textBrowser.repaint()
            else:
                self.textBrowser.setText("两次输入的密码不相同, 请重新输入!")
                self.textBrowser.repaint()

    def code(self):
        c = ''
        l = [['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'], ['1', '2', '3', '4', '5', '6', '7', '8', '9']]
        for x in range(6):
            if randint(0,1) == 0:
                c += l[0][randint(0, 51)]
            else:
                c += l[1][randint(0, 8)]
        return c
