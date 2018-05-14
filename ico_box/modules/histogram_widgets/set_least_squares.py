from PySide import QtGui


class SetLeastSquaresLine(QtGui.QCheckBox):
    def __init__(self, mainWidget):
        QtGui.QCheckBox.__init__(self, 'Lst sqr')
        self.mainWidget = mainWidget

        self.setStatusTip('Perform linear regression and plot the line that is based on the least squares method')

        self.stateChanged.connect(self.getLeastSquaresLine)

    def getLeastSquaresLine(self):
        if self.isChecked():
            self.mainWidget.histogramGraph.plotLeastSquaresLine = True
        else:
            self.mainWidget.histogramGraph.plotLeastSquaresLine = False
        self.mainWidget.histogramGraph.plotStatistics()


class SetStdLine(QtGui.QCheckBox):
    def __init__(self, mainWidget):
        QtGui.QCheckBox.__init__(self, 'Lst sqr err')
        self.mainWidget = mainWidget

        self.setStatusTip('Show the standard deviation of the error')

        self.stateChanged.connect(self.getStdLine)

    def getStdLine(self):
        if self.isChecked():
            self.mainWidget.histogramGraph.plotStdLine = True
        else:
            self.mainWidget.histogramGraph.plotStdLine = False
        self.mainWidget.histogramGraph.plotStatistics()
