# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\jayma\OneDrive\Documents\GitHub\SQLPythonDB - Backend\BackendUI.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QAction, QTableWidget,QTableWidgetItem,QVBoxLayout
import mysql.connector
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
class Ui_MainWindow(object):
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
        self.lists.setRowCount(8)
        self.lists.setColumnCount(20)
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

    def initDB(self,db):
        self.headers()
        db.execute("SELECT * FROM %s" %table)
        row = 0
        for i in db:
            row += 1
            col = 0
            for x in range(10):
                self.lists.setItem(row,col,QTableWidgetItem(i[x]))
                #print(i[x])
                col +=1

    def search(self):
        self.lists.clear()
        name = self.name.text()
        lname = self.lastname.text()
        email = self.email.text()
        dob = self.dob.text()
        major = self.major.text()
        sex = self.sex.text()
        address = self.address.text()
        phone = self.phone.text()

        if name == "":
            name = '%%%%'
        if lname == "":
            lname = '%%%%'
        if email == "":
            email = '%%%%'
        if dob == "":
            dob = '%%%%'
        if major == "":
            major = '%%%%'
        if sex == "":
            sex = '%%%%'
        if address == "":
            address = '%%%%'
        if phone == "":
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
                for x in range(10):
                    self.lists.setItem(row,col,QTableWidgetItem(i[x]))
                    col +=1
        except:
            pass

    def send_all(self):
        from emailer import email
        print("\nPlease wait while the emails get sent...\n")

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

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.initDB(cursor)
    MainWindow.show()
    
    sys.exit(app.exec_())
