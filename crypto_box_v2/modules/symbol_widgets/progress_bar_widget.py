from PyQt5 import QtWidgets, QtCore

import misc_functions as mf


class ProgressBar(QtWidgets.QProgressBar):
    def __init__(self, length):
        QtWidgets.QProgressBar.__init__(self)
        self.setWindowTitle('Downloading data...')
        self.setRange(0, length)
        self.setGeometry(0, 0, 500, 30)
        mf.centerWindow(self)
        self.iProgress = -1
        self.setValue(self.iProgress)
        self.show()
        QtWidgets.QApplication.processEvents()

    def updateValue(self, string):
        self.iProgress += 1
        self.setValue(self.iProgress)
        self.setWindowTitle('Downloading data and calculating returns for ' + string + '...')
        QtWidgets.QApplication.processEvents()

    def closeEvent(self, event):
        event.ignore()
