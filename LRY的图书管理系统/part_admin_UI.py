from pymysql import *
from PyQt5 import QtCore, QtGui, QtWidgets
class AdminWindow(object):
    def setupUi(self, Form, name):
        self.name = name
        Form.setObjectName("Form")
        Form.resize(1181, 301)
        self.tabWidget = QtWidgets.QTabWidget(Form)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 1181, 301))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.tabWidget.setFont(font)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setAccessibleName("")
        self.tab.setObjectName("tab")
        self.lineEdit = QtWidgets.QLineEdit(self.tab)
        self.lineEdit.setGeometry(QtCore.QRect(130, 20, 291, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_3.setGeometry(QtCore.QRect(130, 120, 291, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_4.setGeometry(QtCore.QRect(130, 170, 291, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        self.lineEdit_4.setFont(font)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_2.setGeometry(QtCore.QRect(130, 70, 291, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(20, 20, 101, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(40, 70, 91, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.tab)
        self.label_3.setGeometry(QtCore.QRect(40, 170, 91, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.tab)
        self.label_4.setGeometry(QtCore.QRect(40, 120, 91, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.textBrowser = QtWidgets.QTextBrowser(self.tab)
        self.textBrowser.setGeometry(QtCore.QRect(460, 10, 711, 251))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.textBrowser.setFont(font)
        self.textBrowser.setObjectName("textBrowser")
        self.pushButton = QtWidgets.QPushButton(self.tab)
        self.pushButton.setGeometry(QtCore.QRect(310, 220, 75, 28))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(11)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.label_10 = QtWidgets.QLabel(self.tab)
        self.label_10.setGeometry(QtCore.QRect(40, 220, 91, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.spinBox = QtWidgets.QSpinBox(self.tab)
        self.spinBox.setGeometry(QtCore.QRect(130, 220, 131, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        self.spinBox.setFont(font)
        self.spinBox.setMinimum(1)
        self.spinBox.setMaximum(100)
        self.spinBox.setObjectName("spinBox")
        self.tabWidget.addTab(self.tab, "")
        self.tab_6 = QtWidgets.QWidget()
        self.tab_6.setObjectName("tab_6")
        self.label_8 = QtWidgets.QLabel(self.tab_6)
        self.label_8.setGeometry(QtCore.QRect(20, 20, 151, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.lineEdit_8 = QtWidgets.QLineEdit(self.tab_6)
        self.lineEdit_8.setGeometry(QtCore.QRect(170, 20, 251, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        self.lineEdit_8.setFont(font)
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.textBrowser_6 = QtWidgets.QTextBrowser(self.tab_6)
        self.textBrowser_6.setGeometry(QtCore.QRect(460, 10, 711, 251))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.textBrowser_6.setFont(font)
        self.textBrowser_6.setObjectName("textBrowser_6")
        self.label_9 = QtWidgets.QLabel(self.tab_6)
        self.label_9.setGeometry(QtCore.QRect(60, 70, 101, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.lineEdit_9 = QtWidgets.QLineEdit(self.tab_6)
        self.lineEdit_9.setGeometry(QtCore.QRect(170, 70, 251, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        self.lineEdit_9.setFont(font)
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.pushButton_6 = QtWidgets.QPushButton(self.tab_6)
        self.pushButton_6.setGeometry(QtCore.QRect(190, 220, 75, 28))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(11)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setObjectName("pushButton_6")
        self.tabWidget.addTab(self.tab_6, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.label_7 = QtWidgets.QLabel(self.tab_4)
        self.label_7.setGeometry(QtCore.QRect(20, 20, 151, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.lineEdit_7 = QtWidgets.QLineEdit(self.tab_4)
        self.lineEdit_7.setGeometry(QtCore.QRect(170, 20, 251, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        self.lineEdit_7.setFont(font)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.textBrowser_4 = QtWidgets.QTextBrowser(self.tab_4)
        self.textBrowser_4.setGeometry(QtCore.QRect(460, 10, 711, 251))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.textBrowser_4.setFont(font)
        self.textBrowser_4.setObjectName("textBrowser_4")
        self.pushButton_4 = QtWidgets.QPushButton(self.tab_4)
        self.pushButton_4.setGeometry(QtCore.QRect(190, 220, 75, 28))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(11)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")
        self.label_11 = QtWidgets.QLabel(self.tab_4)
        self.label_11.setGeometry(QtCore.QRect(80, 70, 91, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.spinBox_2 = QtWidgets.QSpinBox(self.tab_4)
        self.spinBox_2.setGeometry(QtCore.QRect(170, 70, 131, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        self.spinBox_2.setFont(font)
        self.spinBox_2.setMinimum(1)
        self.spinBox_2.setMaximum(100)
        self.spinBox_2.setObjectName("spinBox_2")
        self.tabWidget.addTab(self.tab_4, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.label_5 = QtWidgets.QLabel(self.tab_2)
        self.label_5.setGeometry(QtCore.QRect(50, 20, 81, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_5.setGeometry(QtCore.QRect(10, 50, 171, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.lineEdit_5.setFont(font)
        self.lineEdit_5.setText("")
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.tab_2)
        self.textBrowser_2.setGeometry(QtCore.QRect(190, 10, 981, 251))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.textBrowser_2.setFont(font)
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.pushButton_2 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_2.setGeometry(QtCore.QRect(50, 220, 75, 28))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(11)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.label_6 = QtWidgets.QLabel(self.tab_3)
        self.label_6.setGeometry(QtCore.QRect(40, 20, 101, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit_6.setGeometry(QtCore.QRect(10, 50, 171, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.lineEdit_6.setFont(font)
        self.lineEdit_6.setText("")
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.pushButton_3 = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_3.setGeometry(QtCore.QRect(50, 220, 75, 28))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(11)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.textBrowser_3 = QtWidgets.QTextBrowser(self.tab_3)
        self.textBrowser_3.setGeometry(QtCore.QRect(190, 10, 981, 251))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.textBrowser_3.setFont(font)
        self.textBrowser_3.setObjectName("textBrowser_3")
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.pushButton_5 = QtWidgets.QPushButton(self.tab_5)
        self.pushButton_5.setGeometry(QtCore.QRect(50, 220, 75, 28))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(11)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setObjectName("pushButton_5")
        self.textBrowser_5 = QtWidgets.QTextBrowser(self.tab_5)
        self.textBrowser_5.setGeometry(QtCore.QRect(190, 10, 981, 251))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.textBrowser_5.setFont(font)
        self.textBrowser_5.setObjectName("textBrowser_5")
        self.tabWidget.addTab(self.tab_5, "")

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "管理员 %s 您好!" % (self.name)))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Form", "图书录入"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_6), _translate("Form", "图书归还"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("Form", "图书删除"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Form", "图书查询"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("Form", "借出人信息查询"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("Form", "归还提醒"))
        self.tabWidget.setWhatsThis(_translate("Form", "<html><head/><body><p><br/></p></body></html>"))
        self.label.setText(_translate("Form", "书籍条形码:"))
        self.label_2.setText(_translate("Form", "书籍名称:"))
        self.label_3.setText(_translate("Form", "书籍作者:"))
        self.label_4.setText(_translate("Form", "书籍类型:"))
        self.label_5.setText(_translate("Form", "书籍信息:"))
        self.label_6.setText(_translate("Form", "借书人信息:"))
        self.label_7.setText(_translate("Form", "书籍条形码/名称:"))
        self.label_8.setText(_translate("Form", "书籍条形码/名称:"))
        self.label_9.setText(_translate("Form", "借书人信息:"))
        self.label_10.setText(_translate("Form", "书籍数量:"))
        self.label_11.setText(_translate("Form", "书籍数量:"))
        self.textBrowser_2.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'微软雅黑\',\'微软雅黑\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'微软雅黑\';\">注: 书籍信息可以是条形码、书籍名、书籍类型、书籍作者</span></p></body></html>"))
        self.textBrowser_3.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'微软雅黑\',\'微软雅黑\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'微软雅黑\';\">注: 借书人信息可以是借书人姓名、手机号</span></p></body></html>"))
        self.textBrowser_4.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'微软雅黑\',\'微软雅黑\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'微软雅黑\';\">注: 删除书籍时只会删除图书馆里有的书籍, 不能删除有被借出的书籍, 若删除该书的数量超出了图书管有的该书的数量, 则只会清空图书馆里有的该书</span></p></body></html>"))
        self.textBrowser_5.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'微软雅黑\',\'微软雅黑\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'微软雅黑\';\">注: 超时一天, 罚款一毛  超时1年判定书籍丢失,可降低借书人的社会信誉值, 若最终归还书籍并缴纳罚款可归还借书人的社会信誉值</span></p></body></html>"))
        self.textBrowser_6.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'微软雅黑\',\'微软雅黑\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'微软雅黑\';\">注: 借书人信息可以是借书人姓名、手机号</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'微软雅黑\';\">超时一天, 罚款一毛  超时1年判定书籍丢失,可降低借书人的社会信誉值, 若最终归还书籍并缴纳罚款可归还借书人的社会信誉值</span></p></body></html>"))
        self.pushButton.setText(_translate("Form", "录入"))
        self.pushButton_2.setText(_translate("Form", "查询"))
        self.pushButton_3.setText(_translate("Form", "查询"))
        self.pushButton_4.setText(_translate("Form", "删除"))
        self.pushButton_5.setText(_translate("Form", "开始检查"))
        self.pushButton_6.setText(_translate("Form", "确认"))
        self.pushButton.clicked.connect(self.part)
        self.pushButton_2.clicked.connect(self.part2)
        self.pushButton_3.clicked.connect(self.part3)
        self.pushButton_4.clicked.connect(self.part4)
        self.pushButton_5.clicked.connect(self.part5)
        self.pushButton_6.clicked.connect(self.part6)
    
    def part(self):
        bookid = self.lineEdit.text()
        bookname = self.lineEdit_2.text()
        bookclass = self.lineEdit_3.text()
        bookwriter = self.lineEdit_4.text()
        booknum = self.spinBox.value()
        if len(bookid) == 0 or len(bookname) == 0 or len(bookclass) == 0 or len(bookwriter) == 0:
            self.textBrowser.setText("书籍信息未填写, 请继续输入!")
            self.textBrowser.repaint()
        else:
            con = connect(host = 'localhost', 
                          user = 'root', 
                          passwd='1qaz!QAZ', 
                          port= 3306, 
                          db='library', 
                          charset='utf8')
            cur = con.cursor()
            sql = "select * from book_have where id = '%s'" % (bookid)
            cur.execute(sql)
            values = cur.fetchall()
            if values == ():
                sql = "insert into book_have values('%s', '%s', '%s', '%s', %d, %d, %d)" % (bookid, bookname, bookclass, bookwriter, booknum, booknum, 0)
                cur.execute(sql)
                con.commit()
                cur.close()
                con.close()
                self.textBrowser.setText("是新书籍 录入成功!")
                self.textBrowser.repaint()
            elif values[0][1] != bookname:
                cur.close()
                con.close()
                self.textBrowser.setText("是已有书籍 录入失败! 请检查书籍条形码是否与书籍名相匹配")
                self.textBrowser.repaint()
            elif values[0][2] != bookclass:
                cur.close()
                con.close()
                self.textBrowser.setText("是已有书籍 录入失败! 请检查书籍是否与书籍类型相匹配")
                self.textBrowser.repaint()
            elif values[0][3] != bookwriter:
                cur.close()
                con.close()
                self.textBrowser.setText("是已有书籍 录入失败! 请检查书籍是否与书籍作者相匹配")
                self.textBrowser.repaint()
            else:
                sql = "update book_have set num = %d, bookget = %d where id = '%s';" % (values[0][4]+booknum, values[0][5]+booknum, values[0][0])
                cur.execute(sql)
                con.commit()
                cur.close()
                con.close()
                self.textBrowser.setText("是已有书籍 录入成功!")
                self.textBrowser.repaint()

    def part2(self):
        books = self.lineEdit_5.text()
        if len(books) == 0:
            self.textBrowser_2.setText("书籍信息未填写, 请继续输入!")
            self.textBrowser_2.repaint()
        else:
            con = connect(host = 'localhost', 
                          user = 'root', 
                          passwd='1qaz!QAZ', 
                          port= 3306, 
                          db='library', 
                          charset='utf8')
            cur = con.cursor()
            sql = "select * from book_have where id = '%s'" % (books)
            cur.execute(sql)
            values_id = cur.fetchall()
            sql = "select * from book_have where name = '%s'" % (books)
            cur.execute(sql)
            values_name = cur.fetchall()
            sql = "select * from book_have where class = '%s'" % (books)
            cur.execute(sql)
            values_class = cur.fetchall()
            sql = "select * from book_have where writer = '%s'" % (books)
            cur.execute(sql)
            values_writer = cur.fetchall()
            cur.close()
            con.close()
            key = True
            text = ""
            if values_id != ():
                text += "根据书籍条形码查询:\n"
                for x in values_id:
                    text += "书籍条形码: %s, 书籍名称: %s, 书籍类型: %s, 作者: %s, 书籍数量: %d, 馆内书籍数量: %d, 被借出书籍数量: %d\n" % (x[0], x[1], x[2], x[3], x[4], x[5], x[6])
                key = False
            if values_name != () and key == True:
                if text != "":
                    text += "--------------------我是分割线--------------------\n"
                text += "根据书籍名称查询:\n"
                for x in values_name:
                    text += "书籍条形码: %s, 书籍名称: %s, 书籍类型: %s, 作者: %s, 书籍数量: %d, 馆内书籍数量: %d, 被借出书籍数量: %d\n" % (x[0], x[1], x[2], x[3], x[4], x[5], x[6])
                key = False
            if values_class != ():
                if text != "":
                    text += "--------------------我是分割线--------------------\n"
                text += "根据书籍类型码查询:\n"
                for x in values_class:
                    text += "书籍条形码: %s, 书籍名称: %s, 书籍类型: %s, 作者: %s, 书籍数量: %d, 馆内书籍数量: %d, 被借出书籍数量: %d\n" % (x[0], x[1], x[2], x[3], x[4], x[5], x[6])
                key = False
            if values_writer != ():
                if text != "":
                    text += "--------------------我是分割线--------------------\n"
                text += "根据书籍作者查询:\n"
                for x in values_writer:
                    text += "书籍条形码: %s, 书籍名称: %s, 书籍类型: %s, 作者: %s, 书籍数量: %d, 馆内书籍数量: %d, 被借出书籍数量: %d\n" % (x[0], x[1], x[2], x[3], x[4], x[5], x[6])
                key = False
            if key:
                self.textBrowser_2.setText("未查询到匹配项!")
                self.textBrowser_2.repaint()
            else:
                self.textBrowser_2.setText(text)
                self.textBrowser_2.repaint()

    def part3(self):
        None  # TODO

    def part4(self):
        books = self.lineEdit_7.text()
        booknum = self.spinBox_2.value()
        if len(books) == 0:
            self.textBrowser_4.setText("书籍信息未填写, 请继续输入!")
            self.textBrowser_4.repaint()
        else:
            con = connect(host = 'localhost', 
                          user = 'root', 
                          passwd='1qaz!QAZ', 
                          port= 3306, 
                          db='library', 
                          charset='utf8')
            cur = con.cursor()
            sql = "select * from book_have where id = '%s'" % (books)
            cur.execute(sql)
            values_id = cur.fetchall()
            sql = "select * from book_have where name = '%s'" % (books)
            cur.execute(sql)
            values_name = cur.fetchall()
            key = True
            if values_id != ():
                if values_id[0][5] - booknum > 0:
                    sql = "update book_have set num = %d, bookget = %d where id = '%s';" % (values_id[0][4]-booknum, values_id[0][5]-booknum, values_id[0][0])
                    cur.execute(sql)
                    con.commit()
                    cur.close()
                    con.close()
                    if values_id[0][6] != 0:
                        self.textBrowser_4.setText("删除成功! 图书馆内还有该书 %d 本, 还有 %d 本被借走" % (values_id[0][5]-booknum, values_id[0][6]))
                        self.textBrowser_4.repaint()
                    else:
                        self.textBrowser_4.setText("删除成功! 图书馆内还有该书 %d 本, 没有该书被借走" % (values_id[0][5]-booknum))
                        self.textBrowser_4.repaint()
                    key = False
                elif values_id[0][6] != 0 and values_id[0][5] - booknum <= 0:
                    sql = "update book_have set num = %d, bookget = %d where id = '%s';" % (values_id[0][4]-values_id[0][5], 0, values_id[0][0])
                    cur.execute(sql)
                    con.commit()
                    cur.close()
                    con.close()
                    self.textBrowser_4.setText("删除成功! 图书馆内已没有该书, 但还有 %d 本被借走" % (values_id[0][6]))
                    self.textBrowser_4.repaint()
                    key = False
                else:
                    sql = "delete from book_have where id = '%s';" % (values_id[0][0])
                    cur.execute(sql)
                    con.commit()
                    cur.close()
                    con.close()
                    self.textBrowser_4.setText("删除成功! 图书馆内已没有该书所有记录")
                    self.textBrowser_4.repaint()
                    key = False
            if values_name != ():
                if values_name[0][5] - booknum > 0:
                    sql = "update book_have set num = %d, bookget = %d where name = '%s';" % (values_name[0][4]-booknum, values_name[0][5]-booknum, values_name[0][1])
                    cur.execute(sql)
                    con.commit()
                    cur.close()
                    con.close()
                    if values_name[0][6] != 0:
                        self.textBrowser_4.setText("删除成功! 图书馆内还有该书 %d 本, 还有 %d 本被借走" % (values_name[0][5]-booknum, values_name[0][6]))
                        self.textBrowser_4.repaint()
                    else:
                        self.textBrowser_4.setText("删除成功! 图书馆内还有该书 %d 本, 没有该书被借走" % (values_name[0][5]-booknum))
                        self.textBrowser_4.repaint()
                    key = False
                elif values_name[0][6] != 0 and values_name[0][5] - booknum <= 0:
                    sql = "update book_have set num = %d, bookget = %d where name = '%s';" % (values_name[0][4]-values_name[0][5], 0, values_name[0][1])
                    cur.execute(sql)
                    con.commit()
                    cur.close()
                    con.close()
                    self.textBrowser_4.setText("删除成功! 图书馆内已没有该书, 但还有 %d 本被借走" % (values_name[0][6]))
                    self.textBrowser_4.repaint()
                    key = False
                else:
                    sql = "delete from book_have where name = '%s';" % (values_name[0][1])
                    cur.execute(sql)
                    con.commit()
                    cur.close()
                    con.close()
                    self.textBrowser_4.setText("删除成功! 图书馆内已没有该书所有记录")
                    self.textBrowser_4.repaint()
                    key = False
            if key:
                cur.close()
                con.close()
                self.textBrowser_4.setText("删除失败! 图书馆内没有该书所有记录")
                self.textBrowser_4.repaint()

    def part5(self):
        None  # TODO

    def part6(self):
        None  # TODO
