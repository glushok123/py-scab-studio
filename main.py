# -*- coding: utf-8 -*-
import os
import shutil
import sys
from PyQt5 import uic, QtCore, QtGui
from PyQt5.QtGui import QTextCursor, QIcon, QImage
from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap
from threading import Thread
from PyQt5.QtCore import QThread, QTimer, Qt
# from Worker import Worker
# from ThreadRemoveBorder import ThreadForFunc
# from multiprocessing.pool import ThreadPool
from concurrent import futures
import time


###---PLUGIN DIALOG CLASS---###
class testDialog(QDialog):

    def __init__(self):
        QDialog.__init__(self)
        self.setGeometry(200, 200, 500, 350)
        layout = QVBoxLayout()
        self.lbl_1 = QLabel('Info: ', self)
        self.info = QLineEdit(self)
        self.lbl_2 = QLabel('Progress: ', self)
        self.prog = QProgressBar(self)
        self.btns = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel, self)
        for c in self.children():
            layout.addWidget(c)
        self.setLayout(layout)


# pyinstaller --onefile  .\main.py
class MainApp(QMainWindow, Thread):
    def __init__(self):
        super().__init__()
        # QThread.__init__(self)
        self.textEdit_8 = None
        self.textEdit_9 = None
        self.action = None
        self.listWidget = None
        self.listWidget_2 = None
        self.checkBox_4 = None
        self.checkBox_5 = None
        self.checkBox_6 = None
        self.checkBox_7 = None
        self.checkBox_8 = None
        self.label_8 = None
        self.label_8 = None
        self.label_8 = None
        self.checkBox_6 = None
        self.textEdit = None
        self.label = None
        self.progressBar = None
        self.label = None
        self.progressBar = None
        self.checkBox_2 = None
        self.checkBox_3 = None
        self.checkBox = None
        self.textEdit_3 = None
        self.textEdit_5 = None
        self.textEdit_6 = None
        self.textEdit_2 = None
        self.textEdit_4 = None
        self.pushButton_2 = None
        self.pushButton = None
        uic.loadUi('mainui.ui', self)
        self.dpi = ''
        self.countFile = 0
        self.dirInit = ''
        self.width_img = 0
        self.height_img = 0
        self.dirInit = ''
        self.isRemoveBorder = ''
        self.isSplit = ''
        self.isAddBorder = ''
        self.isShowStart = True
        self.isShowEnd = True
        self.isAddBorderForAll = True
        self.isAddBorderForAll = True
        self.isAddBlackBorder = False
        self.isPxIdentically = False
        self.fileurl = ''
        self.width_px = 100
        self.count_cpu = 4
        self.kf_w = 0.6
        self.kf_h = 0.8
        self.pxStartList = 300
        self.pxMediumVal = 100
        self.border_px = 100
        self.arrayErrorFile = []
        self.directoryName = ''
        self.postfix = '(до разделения на страницы)'
        self.procent = 0
        self.countFile = 0
        self.thread = None
        self.worker = None
        self.gif = None
        self.dlg = testDialog()
        self.initUI()

    from module.test import test
    from module.splitImage import initSplitImage, parseImage
    from module.removeBorder import initRemoveBorder, removeBorder
    from module.removePostBorder import initRemovePostBorder, removePostBorder
    from module.addBorder import initAddBorder, addBorder
    from module.rename import rename
    from module.addListWidget import showStartImage, showEndImage

    def initUI(self):
        self.pushButton.clicked.connect(self.startTread)
        self.pushButton_2.clicked.connect(self.getUrl)
        self.action.triggered.connect(self.getUrl)
        self.listWidget.itemClicked.connect(self.Clicked)
        self.listWidget_2.itemClicked.connect(self.Clicked)

    def statusLoaded(self, procent):
        self.progressBar.setValue(procent)

    def startTread(self):
        self.statusLoaded(0)
        path = '832.gif'
        self.gif = QtGui.QMovie(path)
        self.label_8.setMovie(self.gif)
        self.gif.start()

        t1 = Thread(target=self.start)
        t1.start()
        # t1.join()
        # self.gif.stop()

    def start(self):
        self.dpi = int(self.textEdit_4.toPlainText())
        self.kf_w = float(self.textEdit_8.toPlainText())
        self.kf_h = float(self.textEdit_9.toPlainText())
        self.width_px = int(self.textEdit_2.toPlainText())
        self.border_px = int(self.textEdit_3.toPlainText())
        self.pxStartList = int(self.textEdit_5.toPlainText())
        self.pxMediumVal = int(self.textEdit_6.toPlainText())
        self.count_cpu = int(self.textEdit_7.toPlainText())
        self.isRemoveBorder = self.checkBox.isChecked()  # удалять черную рамку
        self.isSplit = self.checkBox_3.isChecked()  # Делить изображение по полам
        self.isAddBorder = self.checkBox_2.isChecked()  # Добавлять черную рамку
        self.isAddBorderForAll = self.checkBox_4.isChecked()  # Добавлять черную рамку c 4 сторон
        self.isPxIdentically = self.checkBox_5.isChecked()  # Подстраивать разрешение
        self.isShowStart = self.checkBox_6.isChecked()  # Показывать изначальные сканы
        self.isShowEnd = self.checkBox_7.isChecked()  # Показывать получившмеся сканы
        self.isAddBlackBorder = self.checkBox_8.isChecked()  # Добавлять черную рамку

        array = self.fileurl.split("/")
        self.directoryName = array[-1]

        dir = os.path.abspath(os.curdir)
        dir = dir.replace('\\', '/')
        self.dirInit = dir + '/' + self.directoryName + self.postfix

        dirName = self.fileurl
        listOfFiles = list()
        for (dirpath, dirnames, filenames) in os.walk(dirName):
            listOfFiles += [os.path.join(dirpath, file) for file in filenames]

        for image in listOfFiles:
            url = image.replace('\\', '/')
            url = url.replace(str(self.fileurl), '')
            imageUrl = self.fileurl + url

        if self.isRemoveBorder:
            cursor = QTextCursor(self.textEdit.document())
            cursor.setPosition(0)
            self.textEdit.setTextCursor(cursor)
            self.textEdit.insertHtml(" <b>__СТАРТ УДАЛЕНИЯ РАМКИ__</b> <br>")

            t1 = Thread(target=self.initRemoveBorder, daemon=True)
            t1.start()
            t1.join()

            cursor.setPosition(0)
            self.textEdit.setTextCursor(cursor)
            self.textEdit.insertHtml(" <b>__КОНЕЦ УДАЛЕНИЯ РАМКИ__</b> <br>")
            # self.initRemoveBorder()
            self.fileurl = self.dirInit

        if self.isSplit:
            cursor = QTextCursor(self.textEdit.document())
            cursor.setPosition(0)
            self.textEdit.setTextCursor(cursor)
            self.textEdit.insertHtml(" <b>__СТАРТ РАЗДЕЛЕНИЕ ПО СТРАНИЦАМ__</b> <br>")

            t1 = Thread(target=self.initSplitImage, daemon=True)
            t1.start()
            t1.join()

            cursor.setPosition(0)
            self.textEdit.setTextCursor(cursor)
            self.textEdit.insertHtml(" <b>__КОНЕЦ РАЗДЕЛЕНИЕ ПО СТРАНИЦАМ__</b> <br>")
            # self.initSplitImage()
            dir = os.path.abspath(os.curdir)
            dir = dir.replace('\\', '/')
            self.fileurl = dir + '/' + self.directoryName

        if self.isRemoveBorder and self.isAddBlackBorder:
            cursor = QTextCursor(self.textEdit.document())
            cursor.setPosition(0)
            self.textEdit.setTextCursor(cursor)
            self.textEdit.insertHtml(" <b>__СТАРТ УДАЛЕНИЯ РАМКИ ДОП__</b> <br>")

            t1 = Thread(target=self.initRemovePostBorder, daemon=True)
            t1.start()
            t1.join()

            self.textEdit.setTextCursor(cursor)
            self.textEdit.insertHtml(" <b>__КОНЕЦ УДАЛЕНИЯ РАМКИ ДОП__</b> <br>")
            # self.initRemovePostBorder()

        if self.isAddBlackBorder:
            cursor = QTextCursor(self.textEdit.document())
            cursor.setPosition(0)
            self.textEdit.setTextCursor(cursor)
            self.textEdit.insertHtml(" <b>__СТАРТ ДОБАВЛЕНИЯ РАМКИ__</b> <br>")

            t1 = Thread(target=self.initAddBorder, daemon=True)
            t1.start()
            t1.join()

            self.textEdit.setTextCursor(cursor)
            self.textEdit.insertHtml(" <b>__КОНЕЦ ДОБАВЛЕНИЯ РАМКИ__</b> <br>")
            # self.initAddBorder()
            self.fileurl = self.dirInit

        if self.isRemoveBorder and self.isSplit:
            dir = os.path.abspath(os.curdir)
            dir = dir.replace('\\', '/')
            shutil.rmtree(dir + '/' + self.directoryName + self.postfix)
            self.fileurl = dir + '/' + self.directoryName
            self.rename()

        if self.isShowEnd:
            t2 = Thread(target=self.showEndImage, daemon=True)
            t2.start()

        cursor = QTextCursor(self.textEdit.document())
        cursor.setPosition(0)
        self.textEdit.setTextCursor(cursor)
        self.textEdit.insertHtml("<b> __КОНЕЦ ОБРАБОТКИ__ </b><br>")
        print("__ КОНЕЦ ОБРАБОТКИ __")
        self.label_8.setText("__ КОНЕЦ ОБРАБОТКИ __")
        # path = 'road-sign-roadtrip.gif'
        # gif = QtGui.QMovie(path)
        # self.label_8.setMovie(self.gif)
        # gif.start()
        # self.gif.stop()
        # msg = QMessageBox()
        # msg.setIcon(QMessageBox.Information)
        # msg.setText("Файлы обработаны")
        # msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        # msg.exec_()

    def Clicked(self, item):
        image = QImage(item.text())
        pixmap = QPixmap.fromImage(image)
        pixmap = pixmap.scaled(int(self.label_8.width() * 0.9), int(self.label_8.height() * 0.9),
                               QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation)
        self.label_8.setPixmap(pixmap)

    def getUrl(self):
        directory = QFileDialog.getExistingDirectory(self,
                                                     'Выберите папку со сканами которые необходимо разделить на страницы')
        if directory:
            directory = directory.replace('\\', '/')
            self.fileurl = directory
            _, _, files = next(os.walk(self.fileurl))
            self.countFile = len(files)

            self.label.setText(str(self.countFile))
            dir = os.path.abspath(os.curdir)
            dir = dir.replace('\\', '/')
            self.dirInit = dir + '/' + self.directoryName + self.postfix

            if self.checkBox_6.isChecked():
                print('isChecked')
                t1 = Thread(target=self.showStartImage, daemon=True)
                t1.start()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainApp()
    ex.show()
    sys.exit(app.exec_())
