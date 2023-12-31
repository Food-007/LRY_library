from pymysql import *
from time import *
from datetime import *
from PyQt5 import QtCore, QtGui, QtWidgets
class UserWindow(object):
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
        self.tab.setObjectName("tab")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(50, 20, 81, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.tab)
        self.lineEdit.setGeometry(QtCore.QRect(10, 50, 171, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.lineEdit.setFont(font)
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.textBrowser = QtWidgets.QTextBrowser(self.tab)
        self.textBrowser.setGeometry(QtCore.QRect(190, 10, 981, 251))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.textBrowser.setFont(font)
        self.textBrowser.setObjectName("textBrowser")
        self.pushButton = QtWidgets.QPushButton(self.tab)
        self.pushButton.setGeometry(QtCore.QRect(50, 220, 75, 28))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(11)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.pushButton_2 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_2.setGeometry(QtCore.QRect(50, 220, 75, 28))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(11)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.tab_2)
        self.textBrowser_2.setGeometry(QtCore.QRect(190, 10, 981, 251))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.textBrowser_2.setFont(font)
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.textBrowser_3 = QtWidgets.QTextBrowser(self.tab_3)
        self.textBrowser_3.setGeometry(QtCore.QRect(460, 10, 711, 251))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.textBrowser_3.setFont(font)
        self.textBrowser_3.setObjectName("textBrowser_3")
        self.label_2 = QtWidgets.QLabel(self.tab_3)
        self.label_2.setGeometry(QtCore.QRect(20, 20, 101, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit_2.setGeometry(QtCore.QRect(130, 20, 301, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setText("")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_3.setGeometry(QtCore.QRect(190, 220, 75, 28))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(11)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.textBrowser_4 = QtWidgets.QTextBrowser(self.tab_4)
        self.textBrowser_4.setGeometry(QtCore.QRect(460, 10, 711, 251))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.textBrowser_4.setFont(font)
        self.textBrowser_4.setObjectName("textBrowser_4")
        self.label_3 = QtWidgets.QLabel(self.tab_4)
        self.label_3.setGeometry(QtCore.QRect(20, 20, 151, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.tab_4)
        self.lineEdit_3.setGeometry(QtCore.QRect(130, 20, 301, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setText("")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.tab_4)
        self.pushButton_4.setGeometry(QtCore.QRect(190, 220, 75, 28))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(11)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")
        self.tabWidget.addTab(self.tab_4, "")

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "用户 %s 您好!" % (self.name)))
        self.tabWidget.setWhatsThis(_translate("Form", "<html><head/><body><p><br/></p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Form", "图书查询"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Form", "个人借书情况查询"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("Form", "图书借阅"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("Form", "图书归还"))
        self.textBrowser.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'微软雅黑\',\'微软雅黑\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'微软雅黑\';\">注: 书籍信息可以是条形码、书籍名、书籍类型、书籍作者</span></p></body></html>"))
        self.textBrowser_2.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'微软雅黑\',\'微软雅黑\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.textBrowser_3.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'微软雅黑\',\'微软雅黑\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'微软雅黑\';\">注: 一个人最多可借阅12本书籍, 不能借阅多本一样的书籍, 可以去图书管理员处续借  超时一天, 罚款一毛  超时1年判定书籍丢失,可降低借书人的社会信誉值, 若最终归还书籍并缴纳罚款可归还借书人的社会信誉值</span></p></body></html>"))
        self.textBrowser_4.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'微软雅黑\',\'微软雅黑\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'微软雅黑\';\">注: 超时一天, 罚款一毛  超时1年判定书籍丢失,可降低借书人的社会信誉值, 若最终归还书籍并缴纳罚款可归还借书人的社会信誉值</span></p></body></html>"))
        self.label.setText(_translate("Form", "书籍信息:"))
        self.label_2.setText(_translate("Form", "书籍条形码:"))
        self.label_3.setText(_translate("Form", "书籍条形码:"))
        self.pushButton.setText(_translate("Form", "查询"))
        self.pushButton_2.setText(_translate("Form", "查询"))
        self.pushButton_3.setText(_translate("Form", "确认"))
        self.pushButton_4.setText(_translate("Form", "确认"))
        self.pushButton.clicked.connect(self.part)
        self.pushButton_2.clicked.connect(self.part2)
        self.pushButton_3.clicked.connect(self.part3)
        self.pushButton_4.clicked.connect(self.part4)
    
    def part(self):
        books = self.lineEdit.text()
        if len(books) == 0:
            self.textBrowser.setText("")
            self.textBrowser.repaint()
            sleep(0.1)
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
                    text += "书籍条形码: %s, 书籍名称: %s, 书籍类型: %s, 作者: %s, 馆内书籍数量: %d\n" % (x[0], x[1], x[2], x[3], x[5])
                    key = False
            if values_name != () and key == True:
                if text != "":
                    text += "--------------------我是分割线--------------------\n"
                text += "根据书籍名称查询:\n"
                for x in values_name:
                    text += "书籍条形码: %s, 书籍名称: %s, 书籍类型: %s, 作者: %s, 馆内书籍数量: %d\n" % (x[0], x[1], x[2], x[3], x[5])
                key = False
            if values_class != ():
                if text != "":
                    text += "--------------------我是分割线--------------------\n"
                text += "根据书籍类型码查询:\n"
                for x in values_class:
                    text += "书籍条形码: %s, 书籍名称: %s, 书籍类型: %s, 作者: %s, 馆内书籍数量: %d\n" % (x[0], x[1], x[2], x[3], x[5])
                key = False
            if values_writer != ():
                if text != "":
                    text += "--------------------我是分割线--------------------\n"
                text += "根据书籍作者查询:\n"
                for x in values_writer:
                    text += "书籍条形码: %s, 书籍名称: %s, 书籍类型: %s, 作者: %s, 馆内书籍数量: %d\n" % (x[0], x[1], x[2], x[3], x[5])
                key = False
            if key:
                self.textBrowser.setText("")
                self.textBrowser.repaint()
                sleep(0.1)
                self.textBrowser.setText("未查询到匹配项!")
                self.textBrowser.repaint()
            else:
                self.textBrowser.setText("")
                self.textBrowser.repaint()
                sleep(0.1)
                self.textBrowser.setText(text)
                self.textBrowser.repaint()
    
    def part2(self):
        con = connect(host = 'localhost', 
                      user = 'root', 
                      passwd='1qaz!QAZ', 
                      port= 3306, 
                      db='library', 
                      charset='utf8')
        cur = con.cursor()
        sql = "select book_id, booklose_id from book_history where people_name = '%s';" % (self.name)
        cur.execute(sql)
        values_name = cur.fetchall()
        overover = True
        l = 0
        text = ""
        if values_name != ():
            for x in values_name:
                over = True
                l += 1
                sql = "select id, name, class, writer from book_have where id = '%s';" % (x[0])
                cur.execute(sql)
                books = cur.fetchall()
                sql = "select datediff(finish_borrow, now()) from library.book_history where people_name = '%s' and book_id = '%s';" % (self.name, books[0][0])
                cur.execute(sql)
                book_over = cur.fetchall()
                if book_over[0][0] < 0:
                    over = False
                if over:
                    text += "书籍条形码: %s, 书籍名称: %s, 书籍类型: %s, 作者: %s, 借书编号: %d, 状态: 未超时, 剩余 %d天应归还\n"  % (books[0][0], books[0][1], books[0][2], books[0][3], x[1], book_over[0][0])
                else:
                    text += "书籍条形码: %s, 书籍名称: %s, 书籍类型: %s, 作者: %s, 借书编号: %d, 状态: 已超时, 应缴纳罚款 %.1f元\n"  % (books[0][0], books[0][1], books[0][2], books[0][3], x[1], abs(book_over[0][0]/10))
                    overover = False
            cur.close()
            con.close()
            if overover:
                text += "您已借书 %d本, 还能借书 %d本" % (l, 12-l)
            else:
                text += "您已借书 %d本, 您有逾期未归还书籍, 不能继续借书, 请尽快去图书管理员处归还书籍" % (l)
            self.textBrowser_2.setText(" ")
            self.textBrowser_2.repaint()
            sleep(0.1)
            self.textBrowser_2.setText(text)
            self.textBrowser_2.repaint()
        else:
            self.textBrowser_2.setText("")
            self.textBrowser_2.repaint()
            sleep(0.1)
            self.textBrowser_2.setText("您目前没有借阅书籍!")
            self.textBrowser_2.repaint()
    
    def part3(self):
        books = self.lineEdit_2.text()
        if len(books) == 0:
            self.textBrowser_3.setText("")
            self.textBrowser_3.repaint()
            sleep(0.1)
            self.textBrowser_3.setText("书籍信息未填写, 请继续输入!")
            self.textBrowser_3.repaint()
        else:
            con = connect(host = 'localhost', 
                          user = 'root', 
                          passwd='1qaz!QAZ', 
                          port= 3306, 
                          db='library', 
                          charset='utf8')
            cur = con.cursor()
            sql = "select * from book_history where people_name = '%s'" % (self.name)
            cur.execute(sql)
            values_people = cur.fetchall()
            num = 0
            i = 0
            same = False
            for x in values_people:
                num += 1
                sql = "select datediff(finish_borrow, now()) from book_history where people_name = '%s';" % (self.name)
                cur.execute(sql)
                values_borrow = cur.fetchall()
                if values_borrow[0][0] < 0:
                    i += 1
            for x in values_people:
                if x[1] == books:
                    same = True
            if i >= 1:
                self.textBrowser_3.setText("")
                self.textBrowser_3.repaint()
                sleep(0.1)
                self.textBrowser_3.setText("您有 %d 本超时书籍, 请先归还超时书籍再借阅!" % (i))
                self.textBrowser_3.repaint()
            elif same:
                self.textBrowser_3.setText("")
                self.textBrowser_3.repaint()
                sleep(0.1)
                self.textBrowser_3.setText("您已借阅过该书, 若要续借清到图书管理员处办理!")
                self.textBrowser_3.repaint()
            elif num <= 11:
                sql = "select * from book_have where id = '%s'" % (books)
                cur.execute(sql)
                values_id = cur.fetchall()
                if values_id != ():
                    if values_id[0][5] == 0:
                        self.textBrowser_3.setText("")
                        self.textBrowser_3.repaint()
                        sleep(0.1)
                        self.textBrowser_3.setText("抱歉, 该书籍已被借光!")
                        self.textBrowser_3.repaint()
                    else:
                        sql = "select max(booklose_id) from book_history where book_id = '%s'" % (books)
                        cur.execute(sql)
                        values_lose_id = cur.fetchall()
                        if values_lose_id != ((None,),):
                            sql = "insert into book_history values('%s', '%s', '%s', now(), date_add(now(), interval 90 day), %d)" % (self.name, values_id[0][0], values_id[0][1], values_lose_id[0][0]+1)
                            cur.execute(sql)
                            con.commit()
                            sql = "select finish_borrow from book_history where booklose_id = %d and book_id = '%s'" % (values_lose_id[0][0] + 1, books)
                            cur.execute(sql)
                            values_finish_borrow = cur.fetchall()
                            v = values_lose_id[0][0] + 1
                        else:
                            sql = "insert into book_history values('%s', '%s', '%s', now(), date_add(now(), interval 90 day), %d)" % (self.name, values_id[0][0], values_id[0][1], 1)
                            cur.execute(sql)
                            con.commit()
                            sql = "select finish_borrow from book_history where booklose_id = %d and book_id = '%s'" % (1, books)
                            cur.execute(sql)
                            values_finish_borrow = cur.fetchall()
                            v = 1
                        sql = "update book_have set bookget = %d, booklose = %d where id = '%s';" % (values_id[0][5]-1, values_id[0][6]+1, books)
                        cur.execute(sql)
                        con.commit()
                        self.textBrowser_3.setText("")
                        self.textBrowser_3.repaint()
                        sleep(0.1)
                        values_finish_borrow = values_finish_borrow[0][0].strftime('%Y-%m-%d')
                        self.textBrowser_3.setText("借书成功! 该书籍应在 %s 之前归还, 书籍编码为: %d" % (values_finish_borrow, v))
                        self.textBrowser_3.repaint()
                else:
                    self.textBrowser_3.setText("")
                    self.textBrowser_3.repaint()
                    sleep(0.1)
                    self.textBrowser_3.setText("该书籍不存在, 或书籍信息填写错误, 请重新输入!")
                    self.textBrowser_3.repaint()
            else:
                self.textBrowser_3.setText("")
                self.textBrowser_3.repaint()
                sleep(0.1)
                self.textBrowser_3.setText("您的借阅书籍数量已达到上限, 请先归还部分书籍再借阅!")
                self.textBrowser_3.repaint()
            cur.close()
            con.close()

    def part4(self):
        books = self.lineEdit_3.text()
        if len(books) == 0:
            self.textBrowser_4.setText("")
            self.textBrowser_4.repaint()
            sleep(0.1)
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
            sql = "select book_id from book_history where people_name = '%s'" % (self.name)
            cur.execute(sql)
            values_have = cur.fetchall()
            have = []
            for x in values_have:
                have.append(x[0])
            sql = "select * from book_have where id = '%s'" % (books)
            cur.execute(sql)
            values_id = cur.fetchall()
            if books in have:
                sql = "select datediff(finish_borrow, now()) from book_history where people_name = '%s' and book_id = '%s';" % (self.name, books)
                cur.execute(sql)
                values_borrow = cur.fetchall()
                if values_borrow[0][0] >= 0:
                    sql = "delete from book_history where people_name = '%s' and book_id = '%s'" % (self.name, books)
                    cur.execute(sql)
                    con.commit()
                    sql = "update book_have set bookget = %d, booklose = %d where id = '%s';" % (values_id[0][5]+1, values_id[0][6]-1, books)
                    cur.execute(sql)
                    con.commit()
                    self.textBrowser_4.setText("")
                    self.textBrowser_4.repaint()
                    sleep(0.1)
                    self.textBrowser_4.setText("还书成功!")
                    self.textBrowser_4.repaint()
                else:
                    self.textBrowser_4.setText("")
                    self.textBrowser_4.repaint()
                    sleep(0.1)
                    self.textBrowser_4.setText("还书失败, 该书已超时, 请到图书管理员处归还并缴纳罚款")
                    self.textBrowser_4.repaint()
            else:
                self.textBrowser_4.setText("")
                self.textBrowser_4.repaint()
                sleep(0.1)
                self.textBrowser_4.setText("该书籍您未借阅, 或书籍信息填写错误, 请重新输入!")
                self.textBrowser_4.repaint()
            cur.close()
            con.close()
