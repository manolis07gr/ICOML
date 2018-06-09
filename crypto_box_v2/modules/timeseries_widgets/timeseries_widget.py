from PyQt5 import QtWidgets, QtCore


class TimeseriesWidget(QtWidgets.QPushButton):
    def __init__(self, mainWidget):
        QtWidgets.QPushButton.__init__(self, 'TimeSeries')
        self.setFocusPolicy(QtCore.Qt.NoFocus)
        self.mainWidget = mainWidget
        self.setDown(True)

        self.clicked.connect(self.showWidget)

    def showWidget(self):
        self.mainWidget.showTimeseriesWidgets()
