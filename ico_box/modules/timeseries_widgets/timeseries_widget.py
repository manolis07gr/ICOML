from PySide import QtGui, QtCore


class TimeseriesWidget(QtGui.QPushButton):
    def __init__(self, mainWidget):
        QtGui.QPushButton.__init__(self, 'TimeSeries')
        self.setFocusPolicy(QtCore.Qt.NoFocus)
        self.mainWidget = mainWidget
        self.setDown(True)

        self.clicked.connect(self.showWidget)

    def showWidget(self):
        self.mainWidget.showTimeseriesWidgets()
