import time

from PyQt5.QtCore import QThread, QObject, pyqtSignal

from PyQt5.QtWidgets import (QAction, QMessageBox, QDialog, QVBoxLayout,
                            QLabel, QLineEdit, QProgressBar, QDialogButtonBox,
                            )

###---WORKER CLASS---###
class Worker(QObject):
    progressChanged = pyqtSignal()
    finished = pyqtSignal(object)
    cancelled = pyqtSignal()

    def __init__(self):  # define additional constructor parameters if required
        QObject.__init__(self)
        self.progress = 0
        self.isCancelled = False

    def process(self):
        for i in range(21):
            time.sleep(0.5)
            val = i * 5
            self.setProgress(val)
            if self.isCancelled:
                self.finished.emit(False)
                return

        self.finished.emit('Task finished')  # emit an object if required

    def setProgress(self, progressValue):
        self.progress = progressValue
        self.progressChanged.emit()

    def cancel(self):
        self.isCancelled = True
        self.cancelled.emit()