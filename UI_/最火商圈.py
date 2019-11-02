# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '最火商圈.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import (QApplication, QMainWindow, QPushButton)
import requests
import optparse
import json
class shangquan(QMainWindow):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(931, 401)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(10, -80, 911, 551))
        self.label.setStyleSheet("image: url(:/955/photo/27a0ce800e118b09d51f4c0e7bc7cdbd.jpg);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(750, 0, 211, 151))
        self.label_2.setStyleSheet("image: url(:/955/photo/4b03413f2dac09d281ca1492e7f92650.png);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.pushButton_hb = QtWidgets.QPushButton(Form)
        self.pushButton_hb.setGeometry(QtCore.QRect(790, 30, 131, 91))
        self.pushButton_hb.setStyleSheet("\n"
"border-style:none;\n"
"padding:11px;\n"
"border-radius:3px;\n"
"background:transparent;")
        self.pushButton_hb.setText("")
        self.pushButton_hb.setObjectName("pushButton_hb")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(-40, 50, 1011, 291))
        self.label_3.setStyleSheet("image: url(:/955/photo/QQ图片20191102112905.png);")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.label.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.pushButton_hb.raise_()

        self.retranslateUi(Form)
        self.pushButton_hb.clicked.connect(self.pushButton_hb.click)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
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
