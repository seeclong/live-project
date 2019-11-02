from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import (QApplication, QMainWindow, QPushButton)
import sys
import requests
import optparse
import 首界面
import 潮流衣饰
import 桃子
import 最火商圈
import 最佳美食
import 性价比优选
from 首界面 import mainmeun
from 桃子 import taozi
from 潮流衣饰 import yifu
from 最火商圈 import shangquan
from 最佳美食 import food
from 性价比优选 import xjb


class Mywindow1(QtWidgets.QMainWindow):
    def __init__(self):
        super(Mywindow1, self).__init__()
        self.ui = mainmeun()  # 这句话是实例化类
        self.ui.setupUi(self)  # 这句话相当于设置控件

    def open(self):  # 被调用的类需要再编写一个open函数
        self.show()


class Mywindow2(QtWidgets.QMainWindow):
    def __init__(self):
        super(Mywindow2, self).__init__()
        self.ui = shangquan()
        self.ui.setupUi(self)

    def open(self):  # 被调用的类需要再编写一个open函数
        self.show()

class Mywindow3(QtWidgets.QMainWindow):
    def __init__(self):
        super(Mywindow3, self).__init__()
        self.ui = food()
        self.ui.setupUi(self)

    def open(self):  # 被调用的类需要再编写一个open函数
        self.show()


class Mywindow4(QtWidgets.QMainWindow):
    def __init__(self):
        super(Mywindow4, self).__init__()
        self.ui = xjb()
        self.ui.setupUi(self)

    def open(self):  # 被调用的类需要再编写一个open函数
        self.show()


class Mywindow5(QtWidgets.QMainWindow):
    def __init__(self):
        super(Mywindow5, self).__init__()
        self.ui = yifu()
        self.ui.setupUi(self)

    def open(self):  # 被调用的类需要再编写一个open函数
        self.show()


class Mywindow6(QtWidgets.QMainWindow):
    def __init__(self):
        super(Mywindow6, self).__init__()
        self.ui = taozi()
        self.ui.setupUi(self)

    def open(self):  # 被调用的类需要再编写一个open函数
        self.show()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    # 实例化各个类
    w1 = Mywindow1()
    w2 = Mywindow2()
    w3 = Mywindow3()
    w4 = Mywindow4()
    w5 = Mywindow5()
    w6 = Mywindow6()
    # 将主窗口进行展示调用
    w1.show()
    w1.ui.pushButton.clicked.connect(w2.open)
    w1.ui.pushButton_2.clicked.connect(w3.open)
    w1.ui.pushButton_3.clicked.connect(w4.open)
    w1.ui.pushButton_4.clicked.connect(w5.open)
    w2.ui.pushButton_hb.clicked.connect(w6.open)
    sys.exit(app.exec_())


