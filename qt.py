from PyQt5 import QtWidgets, uic
from PyQt5.QtCore import QDir, Qt, QUrl
from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtWidgets import (QApplication, QFileDialog, QHBoxLayout, QLabel,
        QPushButton, QSizePolicy, QSlider, QStyle, QVBoxLayout, QWidget,QMessageBox)
from PyQt5.QtWidgets import QMainWindow,QWidget, QPushButton, QAction
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import QIcon
import sys
from PyQt5 import QtWidgets
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QImage



class AppFile(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'PyQt5 file dialogs - pythonspot.com'
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 480
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        
        self.openFileNameDialog()
        #self.openFileNamesDialog()
        self.saveFileDialog()
        
        self.show()
    
    def openFileNameDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self,"Select File For Encrypt & Decryption", "","MP4 Files (*.mp4)", options=options)
        if fileName:
            print(fileName)
            dlg.lineEdit.setText(fileName)
       
    def saveFileDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getSaveFileName(self,"File Seve Name","","MP4 Files (*.mp4)", options=options)
        if fileName:
            print(fileName)
            dlg.lineEdit_3.setText(fileName+".mp4")


def encrypt():                                      #เข้ารหัส
    fo = open(dlg.lineEdit.text(), "rb")
    fileOpen = fo.read()
    fo.close()
    fileOpen = bytearray(fileOpen)
    key = int(dlg.lineEdit_2.text())

    for index,value in enumerate(fileOpen):
        fileOpen[index] = value^key
    fo = open(dlg.lineEdit_3.text(),"wb")
    fo.write(fileOpen)
    fo.close()
    controller.show_en()

def decryption():                                      #ถอดรหัส
    fo = open(dlg.lineEdit.text(), "rb")
    fileOpen = fo.read()
    fo.close()
    fileOpen = bytearray(fileOpen)
    key = int(dlg.lineEdit_2.text())

    for index,value in enumerate(fileOpen):
        fileOpen[index] = value^key
    fo = open(dlg.lineEdit_3.text(),"wb")
    fo.write(fileOpen)
    fo.close()
    controller.show_de()


class En(QtWidgets.QWidget):

    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setWindowTitle('Encrypt Complete')
        self.resize(200, 100)
        self.setStyleSheet("background-image: url(a.jpg)\n""")

        layout = QtWidgets.QGridLayout()
        

        font = QtGui.QFont()
        font.setFamily("Rockwell Nova")
        font.setPointSize(23)


        self.label1 = QtWidgets.QLabel('Encryption Complete')
        self.label1.setFont(font)
        layout.addWidget(self.label1)
        self.setLayout(layout)

class De(QtWidgets.QWidget):

    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setWindowTitle('Decryption Complete')
        self.resize(200, 100)
        self.setStyleSheet("background-image: url(a.jpg)\n""")

        layout = QtWidgets.QGridLayout()
        

        font = QtGui.QFont()
        font.setFamily("Rockwell Nova")
        font.setPointSize(23)


        self.label1 = QtWidgets.QLabel('Decryption Complete')
        self.label1.setFont(font)
        layout.addWidget(self.label1)
        self.setLayout(layout)

class About(QtWidgets.QWidget):

    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setWindowTitle('About')
        self.resize(500, 300)
        self.setStyleSheet("background-image: url(a.jpg)\n""")

        layout = QtWidgets.QGridLayout()
        

        font = QtGui.QFont()
        font.setFamily("Segoe Script")
        font.setPointSize(18)


        self.label1 = QtWidgets.QLabel('\t\t         About\n\n   Mr.Phanuwat Kawila             Mr.Anucha Leurach\n   61523206025-6                  61523206008-2\n   Computer Engineering           Computer Engineering\n\nRajamangala University of Technology Lanna Chiang Mai')
        self.label1.setFont(font)
        layout.addWidget(self.label1)

        #self.button = QtWidgets.QPushButton('Login')
        #self.button.clicked.connect(self.login)
        #layout.addWidget(self.button)
        self.setLayout(layout)




class Help(QtWidgets.QWidget):

    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setWindowTitle('MP4 Cryptography Help')
        self.resize(500, 300)
        
        
        self.setStyleSheet("background-image: url(a.jpg)\n""")

        layout = QtWidgets.QGridLayout()
        

        font = QtGui.QFont()
        font.setFamily("Segoe Script")
        font.setPointSize(18)


        self.label1 = QtWidgets.QLabel('\t       MP4 Cryptography Help\n\n1> Click button Browse for Select File Cryptography\n2> Select Location and Flinename for Save\n3> Enter Key For Cryptography (0-225)\n4> Click Encryption or Decryption')
        self.label1.setFont(font)
        layout.addWidget(self.label1)

        #self.button = QtWidgets.QPushButton('Login')
        #self.button.clicked.connect(self.login)
        #layout.addWidget(self.button)
        self.setLayout(layout)


class Controller:

    def __init__(self):
        pass

    def show_help(self):
        self.login = Help()
        self.login.show()

    def show_about(self):
        self.window = About()
        self.window.show()

    def show_en(self):
        self.window = En()
        self.window.show()

    def show_de(self):
        self.window = De()
        self.window.show()

    #en



if __name__ == '__main__':
    controller = Controller()
    app = QtWidgets.QApplication([])
    dlg = uic.loadUi("cy.ui")        
    dlg.show()
    dlg.pushButton.clicked.connect(AppFile)
    dlg.pushButton_2.clicked.connect(encrypt)
    dlg.pushButton_3.clicked.connect(decryption)
    dlg.pushButton_4.clicked.connect(controller.show_about)
    dlg.pushButton_5.clicked.connect(controller.show_help)
    app.exec_()