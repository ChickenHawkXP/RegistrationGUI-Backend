# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\jayma\OneDrive\Documents\GitHub\SQLPythonDB - Backend\BackendUI.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QAction, QTableWidget,QTableWidgetItem,QVBoxLayout,QInputDialog,QLineEdit
import mysql.connector
from emailer import email
import json

table = 'information'
with open("config.json","r") as json_read:
    data = json.load(json_read)
try:
    database = mysql.connector.connect(host = data['host'],
                                        user = data['user'],
                                        password = data['password'],
                                        database = data['database'],
                                        auth_plugin = data['auth_plugin'])
except:
    print('Could not make connection with database!')
cursor = database.cursor(buffered=True)
class Ui_MainWindow(QWidget,object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 410)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(770, 290, 201, 61))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(520, 290, 211, 61))
        self.pushButton_2.setObjectName("pushButton_2")
        self.refresh = QtWidgets.QPushButton(self.centralwidget)
        self.refresh.setGeometry(QtCore.QRect(510,10,75,23))
        self.refresh.setObjectName('refresh')
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 10, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 110, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 200, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(16)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(350, 10, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(16)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(200, 10, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(16)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(200, 110, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(16)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(200, 200, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(16)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(16)
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(350, 110, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(16)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(16)
        self.name = QtWidgets.QLineEdit(self.centralwidget)
        self.name.setGeometry(QtCore.QRect(20, 60, 113, 20))
        self.name.setObjectName("name")
        self.lastname = QtWidgets.QLineEdit(self.centralwidget)
        self.lastname.setGeometry(QtCore.QRect(20, 160, 113, 20))
        self.lastname.setObjectName("lastname")
        self.email = QtWidgets.QLineEdit(self.centralwidget)
        self.email.setGeometry(QtCore.QRect(20, 250, 113, 20))
        self.email.setObjectName("email")
        self.dob = QtWidgets.QLineEdit(self.centralwidget)
        self.dob.setGeometry(QtCore.QRect(350, 60, 113, 20))
        self.dob.setObjectName("dob")
        self.major = QtWidgets.QLineEdit(self.centralwidget)
        self.major.setGeometry(QtCore.QRect(200, 250, 113, 20))
        self.major.setObjectName("major")
        self.sex = QtWidgets.QLineEdit(self.centralwidget)
        self.sex.setGeometry(QtCore.QRect(200, 160, 113, 20))
        self.sex.setObjectName("sex")
        self.address = QtWidgets.QLineEdit(self.centralwidget)
        self.address.setGeometry(QtCore.QRect(200, 60, 113, 20))
        self.address.setObjectName("address")
        self.phone = QtWidgets.QLineEdit(self.centralwidget)
        self.phone.setGeometry(QtCore.QRect(350, 160, 113, 20))
        self.phone.setObjectName("phone")
        self.searchbutton = QtWidgets.QPushButton(self.centralwidget)
        self.searchbutton.setGeometry(QtCore.QRect(30, 300, 421, 71))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(16)
        self.searchbutton.setFont(font)
        self.searchbutton.setObjectName("searchbutton")
        self.lists = QtWidgets.QTableWidget(self.centralwidget)
        self.lists.setGeometry(QtCore.QRect(510, 40, 461, 221))
        self.lists.setObjectName("QTableWidget")
        self.lists.setColumnCount(8)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 851, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.searchbutton.clicked.connect(self.search)
        self.pushButton.clicked.connect(self.send_all)
        self.pushButton_2.clicked.connect(self.email_selected)
        self.refresh.clicked.connect(self.refreshDB)
        self.lists.cellDoubleClicked.connect(self.change_cell)
        '''
        self.name.textChanged.connect(self.search)
        self.lastname.textChanged.connect(self.search)
        self.email.textChanged.connect(self.search)
        self.dob.textChanged.connect(self.search)
        self.major.textChanged.connect(self.search)
        self.sex.textChanged.connect(self.search)
        self.address.textChanged.connect(self.search)
        self.height.textChanged.connect(self.search)
        self.phone.textChanged.connect(self.search)
        self.pets.textChanged.connect(self.search)
        '''

    def headers(self):
        self.lists.setItem(0,0,QTableWidgetItem("Name"))
        self.lists.setItem(0,1,QTableWidgetItem("Last Name"))
        self.lists.setItem(0,2,QTableWidgetItem("Date of Birth"))
        self.lists.setItem(0,3,QTableWidgetItem("Email"))
        self.lists.setItem(0,4,QTableWidgetItem("Address"))
        self.lists.setItem(0,5,QTableWidgetItem("Phone"))
        self.lists.setItem(0,6,QTableWidgetItem("Sex"))
        self.lists.setItem(0,7,QTableWidgetItem("Major"))

    def initRows(self):
        rowcount = 1
        cursor.execute("SELECT * FROM %s" %table)
        for i in cursor:
            rowcount+=1
        self.lists.setRowCount(rowcount)
    
    def initDB(self):
        row = 0
        self.initRows()
        self.headers()
        cols = self.lists.columnCount()
        cursor.execute("SELECT * FROM %s" %table)
        rowcount = self.lists.rowCount()
        print(rowcount)
        for i in cursor:
            row += 1
            col = 0
            try:
                for x in range(cols):
                    self.lists.setItem(row,col,QTableWidgetItem(i[x]))
                    #print(i[x])
                    col +=1
            except:
                pass
        return rowcount

    def get_db_rows(self):
        database.commit()
        cursor.execute('SELECT * FROM %s' %table)
        rows = 0
        for i in cursor:
            rows += 1
        print(rows)
        return rows

    def refreshDB(self):
        row = 0
        self.lists.clear()
        self.headers()
        dbrow = self.get_db_rows()
        print(dbrow)
        rows = self.lists.rowCount()-1
        cols = self.lists.columnCount()
        cursor.execute('SELECT * FROM %s'%table)
        dif = abs(dbrow - rows)
        if dbrow > rows:
            self.lists.insertRow(rows)
        self.initDB()

    def search(self):
        self.lists.clear()
        cols = self.lists.columnCount()
        totalrows = self.get_db_rows
        name = self.name.text()
        lname = self.lastname.text()
        email = self.email.text()
        dob = self.dob.text()
        major = self.major.text()
        sex = self.sex.text()
        address = self.address.text()
        phone = self.phone.text()

        if name == "" or name == "'":
            name = '%%%%'
        if lname == "" or lname == "'":
            lname = '%%%%'
        if email == "" or email == "'":
            email = '%%%%'
        if dob == "" or dob == "'":
            dob = '%%%%'
        if major == "" or major == "'":
            major = '%%%%'
        if sex == "" or sex == "'":
            sex = '%%%%'
        if address == "" or address == "'":
            address = '%%%%'
        if phone == "" or phone == "'":
            phone = '%%%%'
        cursor.execute("""SELECT * FROM %s
                        WHERE `FNAME` LIKE '%s%%'
                        AND `LNAME` LIKE '%s%%'
                        AND `DOB` LIKE '%s%%'
                        AND `EMAIL` LIKE '%s%%'
                        AND `ADDRESS` LIKE '%s%%'
                        AND `PHONE` LIKE '%s%%'
                        AND `SEX` LIKE '%s%%'
                        AND `MAJOR` LIKE '%s%%'
                        """ %(table,name,lname,dob,email,address,phone,sex,major))
        row = 0
        self.headers()
        try:
            for i in cursor:
                row += 1
                col = 0
                for x in range(cols):
                    self.lists.setItem(row,col,QTableWidgetItem(i[x]))
                    col +=1
        except:
            pass

    def send_all(self):
        #cursor.execute('SELECT `EMAIL` FROM %s' %table)
        #email.send(cursor)
        print("\nPlease wait while the emails get sent...\n")
        mail_list = self.get_emails()
        email.send(mail_list)
     
    def update_db(self):
        row = self.lists.currentRow()
        totalcols = self.lists.columnCount()
        fname = self.lists.item(row,0).text()
        lname = self.lists.item(row,1).text()
        dob = self.lists.item(row,2).text()
        email = self.lists.item(row,3).text()
        address = self.lists.item(row,4).text()
        phone = self.lists.item(row,5).text()
        sex = self.lists.item(row,6).text()
        major = self.lists.item(row,7).text()
        cursor.execute("""UPDATE `%s`
                          SET 
                          `FNAME` = '%s',
                          `LNAME` = '%s',
                          `DOB` = '%s',
                          `EMAIL` = '%s',
                          `ADDRESS` = '%s',
                          `PHONE` = '%s',
                          `SEX` = '%s',
                          `MAJOR` = '%s'
                          WHERE
                          `EMAIL` = '%s'""" %(table,fname,lname,dob,email,address,phone,sex,major,email))
        database.commit()
    def change_cell(self):
        row = self.lists.currentRow()
        col = self.lists.currentColumn()
        text, okPressed = QInputDialog.getText(self,'Change cell','What would you like to change this too?: ',QLineEdit.Normal,"")
        if text != '' and okPressed:
            self.lists.setItem(row,col,QTableWidgetItem(text))
        self.update_db()
    def email_selected(self):
        emails = list()
        emails.clear()
        try:
            value = self.lists.currentRow()
            get_email = self.lists.item(value,3).text()
        except:
            print('No row with data has been selected!')
            return
        emails.append(get_email)
        email.send(emails)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Email All"))
        self.pushButton_2.setText(_translate("MainWindow", "Email Selected"))
        self.label.setText(_translate("MainWindow", "First Name"))
        self.label_2.setText(_translate("MainWindow", "Last Name"))
        self.label_3.setText(_translate("MainWindow", "Email"))
        self.label_4.setText(_translate("MainWindow", "D.O.B"))
        self.label_5.setText(_translate("MainWindow", "Address"))
        self.label_6.setText(_translate("MainWindow", "Sex"))
        self.label_7.setText(_translate("MainWindow", "Major"))
        self.label_9.setText(_translate("MainWindow", "Phone"))
        self.searchbutton.setText(_translate("MainWindow", "Search"))
        self.refresh.setText(_translate("MainWindow", "Refresh DB"))

    def get_emails(self):
        emails = list()
        emails.clear()
        cols = self.lists.rowCount()
        row = 1
        try:
            for i in range(cols):
                value = self.lists.item(row,3).text()
                emails.append(value)
                row += 1
        except:
            pass
        return emails
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.initRows()
    ui.initDB()
    ui.get_emails()
    MainWindow.show()
    
    sys.exit(app.exec_())
