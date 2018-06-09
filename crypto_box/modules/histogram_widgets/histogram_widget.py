from PyQt5 import QtWidgets, QtCore


class HistogramWidget(QtWidgets.QPushButton):
    def __init__(self, mainWidget):
        QtWidgets.QPushButton.__init__(self, 'Correlation && Histograms')
        self.setFocusPolicy(QtCore.Qt.NoFocus)
        self.mainWidget = mainWidget

        self.clicked.connect(self.showWidget)

    def showWidget(self):
        self.mainWidget.showHistogramWidgets()
