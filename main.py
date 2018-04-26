#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import (QWidget, QToolTip, QPushButton, QApplication)
from PyQt5.QtGui import QFont
from board import Board

'''
Документация:
Это игра Lines, цель игры - набрать наибольшее количество очков, игра происходит на поле 9 х 9
'''

class Lines(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(100, 100, 300, 300)
        self.setWindowTitle('Lines')

        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Lines()
    sys.exit(app.exec_())
