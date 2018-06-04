from PySide import QtGui, QtCore

import misc_functions as mf


class ProgressBar(QtGui.QProgressBar):
    def __init__(self, length):
        QtGui.QProgressBar.__init__(self)
        self.setWindowTitle('Downloading data...')
        self.setRange(0, length)
        self.setGeometry(0, 0, 500, 30)
        mf.centerWindow(self)
        self.iProgress = -1
        self.setValue(self.iProgress)
        self.show()
        QtGui.QApplication.processEvents()

    def updateValue(self, string):
        self.iProgress += 1
        self.setValue(self.iProgress)
        self.setWindowTitle('Downloading data and calculating returns for ' + string + '...')
        QtGui.QApplication.processEvents()

    def closeEvent(self, event):
        event.ignore()
