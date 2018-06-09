from PyQt5 import QtWidgets, QtCore


class SetClosePrice(QtWidgets.QCheckBox):
    def __init__(self, mainWidget):
        QtWidgets.QCheckBox.__init__(self, 'Close')
        self.mainWidget = mainWidget

        self.setStatusTip('Check the box to show the close prices.')

        self.setCheckState(QtCore.Qt.Checked)

        self.stateChanged.connect(self.getClosePrice)

    def getClosePrice(self):
        if self.isChecked():
            self.mainWidget.timeseriesGraph.plotClose = True
            self.mainWidget.setOpenClosePrice.setCheckState(QtCore.Qt.Unchecked)
            self.mainWidget.setHighLowPrice.setCheckState(QtCore.Qt.Unchecked)
        else:
            self.mainWidget.timeseriesGraph.plotClose = False
        self.mainWidget.updatePlots()


class SetOpenClosePrice(QtWidgets.QCheckBox):
    def __init__(self, mainWidget):
        QtWidgets.QCheckBox.__init__(self, 'Op/Cl')
        self.mainWidget = mainWidget

        self.setStatusTip('Check the box to show the open and close prices.')

        self.stateChanged.connect(self.getOpenClosePrice)

    def getOpenClosePrice(self):
        if self.isChecked():
            self.mainWidget.timeseriesGraph.plotOpenClose = True
            self.mainWidget.setClosePrice.setCheckState(QtCore.Qt.Unchecked)
            self.mainWidget.setHighLowPrice.setCheckState(QtCore.Qt.Unchecked)
        else:
            self.mainWidget.timeseriesGraph.plotOpenClose = False
        self.mainWidget.updatePlots()

class SetHighLowPrice(QtWidgets.QCheckBox):
    def __init__(self, mainWidget):
        QtWidgets.QCheckBox.__init__(self, 'Hi/Lo')
        self.mainWidget = mainWidget

        self.setStatusTip('Check the box to show the high and low prices.')

        self.stateChanged.connect(self.getHighLowPrice)

    def getHighLowPrice(self):
        if self.isChecked():
            self.mainWidget.timeseriesGraph.plotHighLow = True
        else:
            self.mainWidget.timeseriesGraph.plotHighLow = False
        self.mainWidget.updatePlots()

class SetPercReturn(QtWidgets.QCheckBox):
    def __init__(self, mainWidget):
        QtWidgets.QCheckBox.__init__(self, 'Ret %')
        self.mainWidget = mainWidget

        self.setStatusTip('Check the box to show the returns in %.')

        self.setCheckState(QtCore.Qt.Checked)

        self.stateChanged.connect(self.getPercReturn)

    def getPercReturn(self):
        if self.isChecked():
            self.mainWidget.timeseriesGraph.plotRPerc = True
            self.mainWidget.histogramGraph.plotRPerc = True
            self.mainWidget.setBPReturn.setCheckState(QtCore.Qt.Unchecked)
        else:
            self.mainWidget.timeseriesGraph.plotRPerc = False
            self.mainWidget.histogramGraph.plotRPerc = False
            self.mainWidget.setBPReturn.setCheckState(QtCore.Qt.Checked)
        self.mainWidget.updatePlots()


class SetBPReturn(QtWidgets.QCheckBox):
    def __init__(self, mainWidget):
        QtWidgets.QCheckBox.__init__(self, 'Ret bp')
        self.mainWidget = mainWidget

        self.setStatusTip('Check the box to show the returns in basis points')

        self.stateChanged.connect(self.getBPReturn)

    def getBPReturn(self):
        if self.isChecked():
            self.mainWidget.timeseriesGraph.plotRPerc = False
            self.mainWidget.histogramGraph.plotRPerc = False
            self.mainWidget.setPercReturn.setCheckState(QtCore.Qt.Unchecked)
        else:
            self.mainWidget.timeseriesGraph.plotRPerc = True
            self.mainWidget.histogramGraph.plotRPerc = True
            self.mainWidget.setPercReturn.setCheckState(QtCore.Qt.Checked)
        self.mainWidget.updatePlots()


class SetNLogVol(QtWidgets.QCheckBox):
    def __init__(self, mainWidget):
        QtWidgets.QCheckBox.__init__(self, 'Volume')
        self.mainWidget = mainWidget

        self.setStatusTip('Check the box to show the volume in number of shares/contracts.')

        self.setCheckState(QtCore.Qt.Checked)

        self.stateChanged.connect(self.getNLogVol)

    def getNLogVol(self):
        if self.isChecked():
            self.mainWidget.timeseriesGraph.plotNLogVol = True
            self.mainWidget.setValueLogVol.setCheckState(QtCore.Qt.Unchecked)
        else:
            self.mainWidget.timeseriesGraph.plotNLogVol = False
            self.mainWidget.setValueLogVol.setCheckState(QtCore.Qt.Checked)
        self.mainWidget.updatePlots()


class SetValueLogVol(QtWidgets.QCheckBox):
    def __init__(self, mainWidget):
        QtWidgets.QCheckBox.__init__(self, 'Value')
        self.mainWidget = mainWidget

        self.setStatusTip('Check the box to show the value of the traded volume.')

        self.stateChanged.connect(self.getValueLogVol)

    def getValueLogVol(self):
        if self.isChecked():
            self.mainWidget.timeseriesGraph.plotNLogVol = False
            self.mainWidget.setNLogVol.setCheckState(QtCore.Qt.Unchecked)
        else:
            self.mainWidget.timeseriesGraph.plotNLogVol = True
            self.mainWidget.setNLogVol.setCheckState(QtCore.Qt.Checked)
        self.mainWidget.updatePlots()


class SetCounts(QtWidgets.QCheckBox):
    def __init__(self, mainWidget):
        QtWidgets.QCheckBox.__init__(self, 'Counts')
        self.mainWidget = mainWidget

        self.setCheckState(QtCore.Qt.Checked)
        self.setStatusTip('Check the box to show the counts in the histogram.')

        self.stateChanged.connect(self.getCounts)

    def getCounts(self):
        if self.isChecked():
            self.mainWidget.histogramGraph.plotCounts = True
            self.mainWidget.setFrequency.setCheckState(QtCore.Qt.Unchecked)
        else:
            self.mainWidget.histogramGraph.plotCounts = False
            self.mainWidget.setFrequency.setCheckState(QtCore.Qt.Checked)
        self.mainWidget.updatePlots()


class SetFrequency(QtWidgets.QCheckBox):
    def __init__(self, mainWidget):
        QtWidgets.QCheckBox.__init__(self, 'Freq/ncy')
        self.mainWidget = mainWidget

        self.setStatusTip('Check the box to show the frequency in the histogram.')

        self.stateChanged.connect(self.getFrequency)

    def getFrequency(self):
        if self.isChecked():
            self.mainWidget.histogramGraph.plotCounts = False
            self.mainWidget.setCounts.setCheckState(QtCore.Qt.Unchecked)
        else:
            self.mainWidget.histogramGraph.plotCounts = True
            self.mainWidget.setCounts.setCheckState(QtCore.Qt.Checked)
        self.mainWidget.updatePlots()


class Set1DolInvested(QtWidgets.QCheckBox):
    def __init__(self, mainWidget):
        QtWidgets.QCheckBox.__init__(self, 'invest $1')
        self.mainWidget = mainWidget

        self.setStatusTip('Divide the price with the value at the leftmost date, equivalent to a $1 investment.')

        self.stateChanged.connect(self.get1DolInvested)

    def get1DolInvested(self):
        if self.isChecked():
            self.mainWidget.timeseriesGraph.plot1dolInv = True
        else:
            self.mainWidget.timeseriesGraph.plot1dolInv = False
        self.mainWidget.timeseriesGraph.plotPrices()


class SetLogPrice(QtWidgets.QCheckBox):
    def __init__(self, mainWidget):
        QtWidgets.QCheckBox.__init__(self, 'log price')
        self.mainWidget = mainWidget

        self.setStatusTip('Show the vertical axis in log scale.')

        self.stateChanged.connect(self.getLogPrice)

    def getLogPrice(self):
        if self.isChecked():
            self.mainWidget.timeseriesGraph.plotLogPrice = True
        else:
            self.mainWidget.timeseriesGraph.plotLogPrice = False
        self.mainWidget.timeseriesGraph.plotPrices()
