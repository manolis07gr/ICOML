from PyQt5 import QtWidgets


class SetMovAvg(QtWidgets.QCheckBox):
    def __init__(self, mainWidget):
        QtWidgets.QCheckBox.__init__(self, 'Mov Avg')
        self.mainWidget = mainWidget

        self.setStatusTip('Check the box to show 10day moving averages.')

        self.stateChanged.connect(self.getMovAvg)

    def getMovAvg(self):
        if self.isChecked():
            self.mainWidget.timeseriesGraph.plotMovAvg = True
        else:
            self.mainWidget.timeseriesGraph.plotMovAvg = False
        self.mainWidget.timeseriesGraph.plotPrices()


class SetMovStd(QtWidgets.QCheckBox):
    def __init__(self, mainWidget):
        QtWidgets.QCheckBox.__init__(self, 'Mov Std')
        self.mainWidget = mainWidget

        self.setStatusTip('Check the box to show the range of +/-1 10day moving standard deviation.')

        self.stateChanged.connect(self.getMovStd)

    def getMovStd(self):
        if self.isChecked():
            self.mainWidget.timeseriesGraph.plotMovStd = True
        else:
            self.mainWidget.timeseriesGraph.plotMovStd = False
        self.mainWidget.timeseriesGraph.plotPrices()
