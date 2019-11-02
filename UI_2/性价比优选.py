# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '性价比优选.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import (QApplication, QMainWindow, QPushButton)
import requests
import optparse
import json

class xjb(QMainWindow):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(929, 405)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(60, 60, 151, 51))
        self.pushButton.setStyleSheet("\n"
"border-style:none;\n"
"padding:11px;\n"
"border-radius:3px;\n"
"background:transparent;")
        self.pushButton.setText("")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(260, 50, 151, 61))
        self.pushButton_2.setStyleSheet("\n"
"border-style:none;\n"
"padding:11px;\n"
"border-radius:3px;\n"
"background:transparent;")
        self.pushButton_2.setText("")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(450, 50, 161, 71))
        self.pushButton_3.setStyleSheet("\n"
"border-style:none;\n"
"padding:11px;\n"
"border-radius:3px;\n"
"background:transparent;")
        self.pushButton_3.setText("")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(Form)
        self.pushButton_4.setGeometry(QtCore.QRect(660, 50, 171, 71))
        self.pushButton_4.setStyleSheet("\n"
"border-style:none;\n"
"padding:11px;\n"
"border-radius:3px;\n"
"background:transparent;")
        self.pushButton_4.setText("")
        self.pushButton_4.setObjectName("pushButton_4")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(10, -60, 911, 551))
        self.label.setStyleSheet("image: url(:/955/photo/27a0ce800e118b09d51f4c0e7bc7cdbd.jpg);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(450, 50, 221, 101))
        self.label_4.setStyleSheet("image: url(:/955/photo/资源 4xxhdpi.png);")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(650, 50, 221, 101))
        self.label_5.setStyleSheet("image: url(:/955/photo/资源 5xxhdpi.png);")
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(250, 50, 221, 101))
        self.label_6.setStyleSheet("image: url(:/955/photo/资源 3xxhdpi.png);")
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(50, 50, 181, 81))
        self.label_7.setStyleSheet("image: url(:/955/photo/资源 1xxhdpi.png);")
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(40, 180, 840, 150))
        self.label_2.setStyleSheet("image: url(:/955/photo/1.png);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_2.setVisible(False)
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(40, 180, 840, 150))
        self.label_3.setStyleSheet("image: url(:/955/photo/2.png);")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.label_3.setVisible(False)
        self.label_8 = QtWidgets.QLabel(Form)
        self.label_8.setGeometry(QtCore.QRect(40, 180, 840, 150))
        self.label_8.setStyleSheet("image: url(:/955/photo/3.png);")
        self.label_8.setText("")
        self.label_8.setObjectName("label_8")
        self.label_8.setVisible(False)
        self.label_9 = QtWidgets.QLabel(Form)
        self.label_9.setGeometry(QtCore.QRect(40, 180, 840, 150))
        self.label_9.setStyleSheet("image: url(:/955/photo/4.png);")
        self.label_9.setText("")
        self.label_9.setObjectName("label_9")
        self.label_9.setVisible(False)
        self.label.raise_()
        self.label_4.raise_()
        self.label_5.raise_()
        self.label_6.raise_()
        self.label_7.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.label_8.raise_()
        self.label_9.raise_()
        self.pushButton_2.raise_()
        self.pushButton_3.raise_()
        self.pushButton_4.raise_()
        self.pushButton.raise_()

        self.retranslateUi(Form)
        self.pushButton.clicked.connect(self.play1)
        self.pushButton_2.clicked.connect(self.play2)
        self.pushButton_3.clicked.connect(self.play3)
        self.pushButton_4.clicked.connect(self.play4)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))

    def play1(self):
        self.label_2.setVisible(True)
        self.label_3.setVisible(False)
        self.label_8.setVisible(False)
        self.label_9.setVisible(False)

    def play2(self):
        self.label_3.setVisible(True)
        self.label_2.setVisible(False)
        self.label_8.setVisible(False)
        self.label_9.setVisible(False)

    def play3(self):
        self.label_8.setVisible(True)
        self.label_3.setVisible(False)
        self.label_2.setVisible(False)
        self.label_9.setVisible(False)

    def play4(self):
        self.label_9.setVisible(True)
        self.label_2.setVisible(False)
        self.label_8.setVisible(False)
        self.label_3.setVisible(False)

    import photo
    if __name__ == "__main__":
        import sys
        from PyQt5.QtGui import QIcon

        app = QtWidgets.QApplication(sys.argv)
        widget = QtWidgets.QWidget()
        ui = Ui_Form()
        ui.setupUi(widget)
        widget.setWindowIcon(QIcon('web.png'))  # 增加icon图标，如果没有图片可以没有这句
        widget.show()
        sys.exit(app.exec_())