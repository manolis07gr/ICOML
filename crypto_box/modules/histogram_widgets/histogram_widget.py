from PySide import QtGui, QtCore


class HistogramWidget(QtGui.QPushButton):
    def __init__(self, mainWidget):
        QtGui.QPushButton.__init__(self, 'Correlation && Histograms')
        self.setFocusPolicy(QtCore.Qt.NoFocus)
        self.mainWidget = mainWidget

        self.clicked.connect(self.showWidget)

    def showWidget(self):
        self.mainWidget.showHistogramWidgets()
