import sys
#import time
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtWidgets import QWidget, QGraphicsDropShadowEffect, QProgressBar
from PyQt5.QtCore import QThread, QTimer, Qt

class ThreadForFunc(QThread):
    def __init__(self, file):
        QThread.__init__(self)
        self.file = file
        self.run()

    def run(self):
        print('Start run')
        print(self.file)
        self.test_func()

    def test_func(self):
        print('Работает!')
        self.num = 0
        while True:
            print(f'{self.num}')
            self.msleep(1000)
            self.num += 1