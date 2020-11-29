# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'welcome.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import os
import time
import platform
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *


# YOUR APPLICATION


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1090, 700)

        ## REMOVE TITLE BAR
        MainWindow.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        MainWindow.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        
        MainWindow.setIconSize(QtCore.QSize(40, 30))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 1350, 800))
        self.tabWidget.setStyleSheet("QTabWidget{\n"
"    image: url(:/newPrefix/row/Untitlkjl1.jpg);\n"
"\n"
"        font-size: 21px;\n"
"        color: rgb(255, 255, 255);\n"
"        background-color: rgb(255, 107, 39);\n"
"        border: 8px solid rgb(255, 107, 39);\n"
"        transition: ease-in-out;\n"
"        border-radius:20px;  \n"
"\n"
"}")
        self.tabWidget.setTabBarAutoHide(False)
        self.tabWidget.setObjectName("tabWidget")
        self.Build = QtWidgets.QWidget()
        self.Build.setAutoFillBackground(False)
        self.Build.setStyleSheet("")
        self.Build.setObjectName("Build")
        self.frame = QtWidgets.QFrame(self.Build)
        self.frame.setGeometry(QtCore.QRect(-10, -10, 1350, 771))
        self.frame.setStyleSheet("background:url(back3.jpg)")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.lineEdit = QtWidgets.QLineEdit(self.frame)
        self.lineEdit.setGeometry(QtCore.QRect(100, 325, 301, 41))
        self.lineEdit.setMinimumWidth(450)
        self.lineEdit.setStyleSheet("\n"
"\n"
"          background: transparent;\n"
"\n"
"\n"
"          font-size:25px;\n"
"")
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(100, 93, 211, 41))
        self.label_3.setStyleSheet("QLabel{\n"
"    background-image: url(https://raw.githubusercontent.com/Aryia-Behroziuan/images/main/ads.jpg);\n"
"   font-size: 45px;\n"
"    color: rgb(0, 0, 255);\n"
"}\n"
"")
        self.label_3.setObjectName("label_3")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(100, 130, 331, 51))
        self.label.setStyleSheet("QLabel{\n"
"    background-image: url(https://raw.githubusercontent.com/Aryia-Behroziuan/images/main/ads.jpg);\n"
"    font-size: 35px;\n"
"}")
        self.label.setObjectName("label")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(100, 200, 311, 61))
        self.label_4.setStyleSheet("QLabel{\n"
"    background-image: url(https://raw.githubusercontent.com/Aryia-Behroziuan/images/main/ads.jpg);\n"
"    font-size: 20px;\n"
"}")
        self.label_4.setObjectName("label_4")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(100, 287, 271, 41))
        self.label_2.setStyleSheet("QLabel{\n"
"    background-image: url(https://raw.githubusercontent.com/Aryia-Behroziuan/images/main/ads.jpg);\n"
"    font-size: 20px;\n"
"}")
        self.label_2.setObjectName("label_2")
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(100, 365, 271, 31))
        self.label_5.setStyleSheet("QLabel{\n"
"    background-image: url(https://raw.githubusercontent.com/Aryia-Behroziuan/images/main/ads.jpg);\n"
"    font-size: 20px;\n"
"}")
        self.label_5.setObjectName("label_5")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_3.setGeometry(QtCore.QRect(100, 250, 301, 41))
        self.lineEdit_3.setMinimumWidth(450)
        self.lineEdit_3.setStyleSheet("\n"
"\n"
"          background: transparent;\n"
"\n"
"\n"
"          font-size:25px;\n"
"")
        self.lineEdit_3.setInputMask("")
        self.lineEdit_3.setText("")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(100, 520, 301, 51))
        self.pushButton.setStyleSheet("border: none;\n"
"outline: none;\n"
"height: 40px;\n"
"background: rgb(76, 70, 255);\n"
"color: rgb(255, 255, 255);\n"
"font-size: 18px;\n"
"border: 10px solid rgb(76, 70, 255);\n"
"border-radius: 10px;\n"
"QPushButton{\n"
"            border: none;\n"
"          outline: none;\n"
"          height: 40px;\n"
"          background: rgb(255, 92, 42);\n"
"          color: rgb(255, 255, 255);\n"
"          font-size: 18px;\n"
"          border: 10px solid rgb(255, 92, 42);\n"
"          border-radius: 10px;\n"
"}")


        self.pushButton_11 = QtWidgets.QPushButton(self.frame)
        self.pushButton_11.setGeometry(QtCore.QRect(100, 570, 301, 51))
        self.pushButton_11.setText('Exit')
        self.pushButton_11.setMinimumWidth(70)
        self.pushButton_11.setStyleSheet("border: none;\n"
"outline: none;\n"
"height: 40px;\n"
"background: #ffffff;\n"
"color: #000000;\n"
"font-size: 18px;\n"
"border: 10px solid #ffffff;\n"
"border-radius: 10px;\n"
"QPushButton{\n"
"            border: none;\n"
"          outline: none;\n"
"          height: 40px;\n"
"          background: rgb(255, 92, 42);\n"
"          color: rgb(255, 255, 255);\n"
"          font-size: 18px;\n"
"          border: 10px solid rgb(255, 92, 42);\n"
"          border-radius: 10px;\n"
"}")
        self.pushButton.setDefault(False)
        self.pushButton.setFlat(False)
        self.pushButton.setObjectName("pushButton")
        self.textEdit = QtWidgets.QTextEdit(self.frame)
        self.textEdit.setGeometry(QtCore.QRect(100, 395, 301, 111))
        self.textEdit.setMinimumWidth(450)
        self.textEdit.setStyleSheet("overflow: auto;\n"
"\n"
"          background: transparent;\n"
"\n"
"\n"
"          font-size:25px;\n"
"")
        self.textEdit.setObjectName("textEdit")
        self.tabWidget.addTab(self.Build, "")
        self.open = QtWidgets.QWidget()
        self.open.setMinimumSize(QtCore.QSize(0, 713))
        self.open.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.open.setObjectName("open")
        self.frame_2 = QtWidgets.QFrame(self.open)
        self.frame_2.setGeometry(QtCore.QRect(0, 0, 1381, 791))
        self.frame_2.setStyleSheet("background-image: url(back54.jpg);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label_6 = QtWidgets.QLabel(self.frame_2)
        self.label_6.setGeometry(QtCore.QRect(750, 195, 221, 41))
        self.label_6.setStyleSheet("QLabel{\n"
"    background-image: url(https://raw.githubusercontent.com/Aryia-Behroziuan/images/main/ads.jpg);\n"
"    font-size: 35px;\n"
"    color:rgb(255, 255, 255);\n"
"}")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.frame_2)
        self.label_7.setGeometry(QtCore.QRect(650, 220, 511, 91))
        self.label_7.setStyleSheet("QLabel{\n"
"    background-image: url(ads.jpg);\n"
"    font-size: 20px;\n"
"    color: rgb(216, 216, 216);\n"
"}")
        self.label_7.setObjectName("label_7")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_4.setGeometry(QtCore.QRect(650, 300, 471, 41))
        self.lineEdit_4.setMinimumWidth(1)
        self.lineEdit_4.setStyleSheet("font-size: 24px;\n"
"color: rgb(255, 255, 255);\n"
"background: transparent;")
        self.lineEdit_4.setText("")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_2.setGeometry(QtCore.QRect(800, 350, 161, 51))
        self.pushButton_2.setStyleSheet("        border: none;\n"
"          background-color: rgb(255, 255, 255);\n"
"          outline: none;\n"
"          height: 40px;\n"
"color: rgb(0, 0, 0);\n"
"\n"
"          font-size: 18px;\n"
"          border: 10px solid rgb(255, 255, 255);\n"
"          border-radius: 10px;")
        self.pushButton_2.setObjectName("pushButton_2")
        self.tabWidget.addTab(self.open, "")
        self.about = QtWidgets.QWidget()
        self.about.setObjectName("about")
        self.frame_5 = QtWidgets.QFrame(self.about)
        self.frame_5.setGeometry(QtCore.QRect(-10, 0, 1401, 861))
        self.frame_5.setStyleSheet("background-image: url(abot.jpg);")
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.label_15 = QtWidgets.QLabel(self.frame_5)
        self.label_15.setGeometry(QtCore.QRect(40, 30, 1421, 631))
        self.label_15.setStyleSheet("QLabel{\n"
"    background-image: url(https://raw.githubusercontent.com/Aryia-Behroziuan/images/main/ads.jpg);\n"
"    font-size: 30px;\n"
"    color: rgb(255, 255, 255);\n"
"}")
        self.label_15.setObjectName("label_15")
        self.tabWidget.addTab(self.about, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        
        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.pushButton.clicked.connect(self.get_data)
        self.pushButton_11.clicked.connect(self.exit)
        self.pushButton_2.clicked.connect(self.pushButton_2.deleteLater)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def exit(self):
        MainWindow.close()
        self.main.close()
        self.close()

    def get_data(self):
        print(self.lineEdit_3.text())
        #Programm
        #Input Data For Programm
        url = self.lineEdit_3.text()
        NameProject = self.lineEdit.text()
        Document =  str(self.textEdit.textCursor())

        #Create Project
        Createfile = str(url+NameProject)
        os.mkdir(str(Createfile))

        #Create index File
        Createindex = str(url+NameProject+'\index.html')
        index = open(str(Createindex), "a")
        index.write("<html>")
        index.write("\n    <head><title>CodeDoxs</title></head>")
        index.write("\n    <body>\n    <h1>Welcome To The CodeDoxs 1.0.0</h1>\n    <a href='http://aryia-behroziuan.github.io/codedoxs/'>CodeDoxs-Web</a>\n    <br/><a href='http://aryia-behroziuan.github.io/web/'>Web-Aryia Behroziuan</a>\n</body>")
        index.write("\n</html>")

        Createurls = str(url+NameProject+'\_URL_.html')
        mainurls = open(str(Createurls), "a")
        mainurls.write("Document URL Web Print URLS WebPage: Locslhost")

        #Create Document Project
        Createindex = str(url+NameProject+'\Document.txt')
        maindocument = open(str(Createindex), "a")
        maindocument.write("Document Project Dats Set")
        maindocument.write("\n")
        maindocument.write("\n")
        maindocument.write("DataSet={")
        maindocument.write("\n      Name:"+NameProject+',')
        maindocument.write("\n      URL:"+url+' Localhost'+',')
        maindocument.write("\n      Document:"+Document+',')

       
        maindocument.write("\n      Languages:"+'HTML ,'+'Css ,'+'JS ,'+'Scss '+',')

        namesys = str(platform.node())
        sys = str(platform.platform())
        v_python = str(platform.python_build())
        compayler = str(platform.python_compiler())
        platform1 = str(platform.release())
        system = str(platform.system())
        datasys = str(platform.uname())

        maindocument.write("\n      Creator:"+namesys+',')
        maindocument.write("\n      Version:"+v_python+',')
        maindocument.write("\n      Compiler:"+compayler+',')
        maindocument.write("\n      Platform:"+platform1+',')
        maindocument.write("\n      System:"+system+platform1+',')
        maindocument.write("\n      Data System:"+datasys+',')
        maindocument.write("\n}")
        maindocument.write("\n")
        maindocument.write("CodeDoxs Version={")
        maindocument.write("\n      Version:"+'1.0.0'+',')
        maindocument.write("\n      Framwork:"+'CodeDoxs'+',')
        maindocument.write("\n      Programmer CodeDoxs:"+'Aryia-Behroziaun'+',')
        maindocument.write("\n      CodeDoxs-Web:"+'http://aryia-behroziaun.github.io/codedoxs/'+',')
        maindocument.write("\n      Aryia-Behroziuan-Web:"+'aryia-behroziaun.github.io/web/'+',')
        maindocument.write("\n}")


        #Create Config
        Createconfig = str(url+NameProject+'\Confin')
        os.mkdir(str(Createconfig))
        #Create Pages
        CreatePages = str(url+NameProject+'\Pages')
        os.mkdir(str(CreatePages))

        Pages1 = str(url+NameProject+'\Pages\index.html')
        Pages2 = open(str(Pages1), "a")

        Pages3 = str(url+NameProject+'\Pages\Home.html')
        Pages4 = open(str(Pages3), "a")

        Pages5 = str(url+NameProject+'\Pages\Login.html')
        Pages6 = open(str(Pages5), "a")


        Pages7 = str(url+NameProject+'\Pages\SignUp.html')
        Pages8 = open(str(Pages7), "a")

        Pages9 = str(url+NameProject+'\Pages\SignOut.html')
        Pages10 = open(str(Pages9), "a")


        Pages11 = str(url+NameProject+'\Pages\Content.html')
        Pages12 = open(str(Pages11), "a")


        Pages13 = str(url+NameProject+'\Pages\ContentOne.html')
        Pages14 = open(str(Pages13), "a")

        Pages15 = str(url+NameProject+'\Pages\__Config.html')
        Pages16 = open(str(Pages15), "a")

        Pages17 = str(url+NameProject+'\Pages\__CodeDoxs_SETING__.txt')
        Pages18 = open(str(Pages17), "a")

        Pages19 = str(url+NameProject+'\Pages\__SETING__.html')
        Pages20 = open(str(Pages19), "a")

        Pages21 = str(url+NameProject+'\Pages\__SETING_ALL__.html')
        Pages22 = open(str(Pages21), "a")

        Pages23 = str(url+NameProject+'\Pages\__SHOP__.html')
        Pages24 = open(str(Pages21), "a")

        Pages25 = str(url+NameProject+'\Pages\__ANALIZE__.html')
        Pages26 = open(str(Pages25), "a")



        #Create css
        Createcss = str(url+NameProject+'\css')
        os.mkdir(str(Createcss))
        #Create Config-image
        Createimage = str(url+NameProject+'\images')
        os.mkdir(str(Createimage))
        #Create JS
        CreateJS = str(url+NameProject+'\JS')
        os.mkdir(str(CreateJS))
        #Create Scss
        Createscss = str(url+NameProject+'\Scss')
        os.mkdir(str(Createscss))
        #Create Vendor
        CreateVendor = str(url+NameProject+'\VenDor')
        os.mkdir(str(CreateVendor))


        #Create Content For CSS
        Createcss1 = str(url+NameProject+'\css'+'\_main.css')
        Createcss2 = open(str(Createcss1), "a")

        Createcss3 = str(url+NameProject+'\css'+'\_Config.css')
        Createcss4 = open(str(Createcss3), "a")

        Createcss5 = str(url+NameProject+'\css'+'\Home.css')
        Createcss6 = open(str(Createcss5), "a")

        Createcss7 = str(url+NameProject+'\css'+'\Login.css')
        Createcss8 = open(str(Createcss7), "a")

        Createcss9 = str(url+NameProject+'\css'+'\SignUp.css')
        Createcss10 = open(str(Createcss9), "a")

        Createcss11 = str(url+NameProject+'\css'+'\SignOut.css')
        Createcss12 = open(str(Createcss11), "a")

        Createcss13 = str(url+NameProject+'\css'+'\Content.css')
        Createcss14 = open(str(Createcss13), "a")

        Createcss15 = str(url+NameProject+'\css'+'\ContentOne.css')
        Createcss16 = open(str(Createcss15), "a")

        Createcss17 = str(url+NameProject+'\css'+'\mainBranch.css')
        Createcss18 = open(str(Createcss17), "a")

        Createcss19 = str(url+NameProject+'\css'+'\__CodeDoxs_SETING__.txt')
        Createcss20 = open(str(Createcss19), "a")
        
        Createcss21 = str(url+NameProject+'\css'+'\__SETING__.css')
        Createcss22 = open(str(Createcss21), "a")

        Createcss23 = str(url+NameProject+'\css'+'\__SETING_ALL_.css')
        Createcss24 = open(str(Createcss23), "a") 

        Createcss25 = str(url+NameProject+'\css'+'\__SHOP__.css')
        Createcss26 = open(str(Createcss25), "a") 

        Createcss27 = str(url+NameProject+'\css'+'\__ANALIZE__.css')
        Createcss28 = open(str(Createcss27), "a")

        #Create Content For JS
        Createjs30 = str(url+NameProject+'\JS'+'\_main2.js')
        Createjs31 = open(str(Createjs30), "a")

        Createjs4 = str(url+NameProject+'\JS'+'\_Config2.js')
        Createjs5 = open(str(Createjs4), "a")

        Createjs6 = str(url+NameProject+'\JS'+'\Home2.js')
        Createjs7 = open(str(Createjs6), "a")

        Createjs8 = str(url+NameProject+'\JS'+'\Login2.js')
        Createjs9 = open(str(Createjs8), "a")

        Createjs10 = str(url+NameProject+'\JS'+'\SignUp2.js')
        Createjs11 = open(str(Createjs10), "a")

        Createjs12 = str(url+NameProject+'\JS'+'\SignOut2.js')
        Createjs13 = open(str(Createjs12), "a")

        Createjs14 = str(url+NameProject+'\JS'+'\Content2.js')
        Createjs15 = open(str(Createjs14), "a")

        Createjs16 = str(url+NameProject+'\JS'+'\ContentOne2.js')
        Createjs17 = open(str(Createjs16), "a")

        Createjs18 = str(url+NameProject+'\JS'+'\index2.js')
        Createjs19 = open(str(Createjs18), "a")

        Createjs20 = str(url+NameProject+'\JS'+'\All_Config2.js')
        Createjs21 = open(str(Createjs20), "a")

        #Create Content For Scss
        Createscss1 = str(url+NameProject+'\Scss'+'\_base2.scss')
        Createscss2 = open(str(Createscss1), "a")

        Createscss3 = str(url+NameProject+'\Scss'+'\_components2.scss')
        Createscss4 = open(str(Createscss3), "a")

        Createscss5 = str(url+NameProject+'\Scss'+'\_layouts2.scss')
        Createscss6 = open(str(Createscss5), "a")

        Createscss7 = str(url+NameProject+'\Scss'+'\main2.scss')
        Createscss8 = open(str(Createscss7), "a")


     #Create Content For CSS
        Createcss1 = str(url+NameProject+'\css'+'\_main2.css')
        Createcss2 = open(str(Createcss1), "a")

        Createcss3 = str(url+NameProject+'\css'+'\_Config2.css')
        Createcss4 = open(str(Createcss3), "a")

        Createcss5 = str(url+NameProject+'\css'+'\Home2.css')
        Createcss6 = open(str(Createcss5), "a")

        Createcss7 = str(url+NameProject+'\css'+'\Login2.css')
        Createcss8 = open(str(Createcss7), "a")

        Createcss9 = str(url+NameProject+'\css'+'\SignUp2.css')
        Createcss10 = open(str(Createcss9), "a")

        Createcss11 = str(url+NameProject+'\css'+'\SignOut2.css')
        Createcss12 = open(str(Createcss11), "a")

        Createcss13 = str(url+NameProject+'\css'+'\Content2.css')
        Createcss14 = open(str(Createcss13), "a")

        Createcss15 = str(url+NameProject+'\css'+'\ContentOne2.css')
        Createcss16 = open(str(Createcss15), "a")

        Createcss17 = str(url+NameProject+'\css'+'\mainBranch2.css')
        Createcss18 = open(str(Createcss17), "a")

        Createcss19 = str(url+NameProject+'\css'+'\__CodeDoxs_SETING__2.txt')
        Createcss20 = open(str(Createcss19), "a")
        
        Createcss21 = str(url+NameProject+'\css'+'\__SETING__2.css')
        Createcss22 = open(str(Createcss21), "a")

        Createcss23 = str(url+NameProject+'\css'+'\__SETING_ALL_2.css')
        Createcss24 = open(str(Createcss23), "a") 

        Createcss25 = str(url+NameProject+'\css'+'\__SHOP__2.css')
        Createcss26 = open(str(Createcss25), "a") 

        Createcss27 = str(url+NameProject+'\css'+'\__ANALIZE__2.css')
        Createcss28 = open(str(Createcss27), "a")


        #Create Content For Scss
        Createscss1 = str(url+NameProject+'\Scss'+'\_base2.scss')
        Createscss2 = open(str(Createscss1), "a")

        Createscss3 = str(url+NameProject+'\Scss'+'\_components2.scss')
        Createscss4 = open(str(Createscss3), "a")

        Createscss5 = str(url+NameProject+'\Scss'+'\_layouts2.scss')
        Createscss6 = open(str(Createscss5), "a")

        Createscss7 = str(url+NameProject+'\Scss'+'\main2.scss')
        Createscss8 = open(str(Createscss7), "a")
        

        self.time.sleep(2)
        self.MainWindow.close()


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Build.setWhatsThis(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "CodeDoxs."))
        self.label.setText(_translate("MainWindow", "Build your projects"))
        self.label_4.setText(_translate("MainWindow", "URL New Project"))
        self.label_2.setText(_translate("MainWindow", "Name Project"))
        self.label_5.setText(_translate("MainWindow", "Document"))
        self.pushButton.setText(_translate("MainWindow", "Build"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Build), _translate("MainWindow", "Build"))
        self.label_6.setText(_translate("MainWindow", "Welcome Back"))
        self.label_7.setText(_translate("MainWindow", "<html><head/><body><p>If you have already created aproject, you can develop it</p></body></html>"))
        self.pushButton_2.setText(_translate("MainWindow", "Development"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.open), _translate("MainWindow", "Open "))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.about), _translate("MainWindow", "About"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
