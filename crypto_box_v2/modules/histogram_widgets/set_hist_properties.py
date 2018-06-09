from PySide import QtGui, QtCore

import misc_parameters as mp


class SetNBins(QtGui.QPushButton):
    def __init__(self, mainWidget):
        QtGui.QPushButton.__init__(self, '# of bins')
        self.setStatusTip('Set the number of bins for the histogram')

        self.setFocusPolicy(QtCore.Qt.NoFocus)
        self.mainWidget = mainWidget

        self.clicked.connect(self.setNBins)

    def setNBins(self):
        self.setDown(True)
        try:
            self.widgetList.close()
        except:
            pass

        self.widgetList = QtGui.QListWidget(self.mainWidget)
        widgetList = self.widgetList
        widgetList.setAlternatingRowColors(True)

        widgetList.addItem(mp.strTwenty)
        widgetList.addItem(mp.strThirty)
        widgetList.addItem(mp.strFifty)

        widgetList.setGeometry(QtGui.QWidget.geometry(self))
        widgetList.setMinimumWidth(QtGui.QWidget.size(self).width())
        widgetList.setMinimumHeight(60)
        widgetList.move(QtGui.QWidget.pos(self).x(), QtGui.QWidget.pos(self).y() - 60)
        widgetList.setFocusPolicy(QtCore.Qt.NoFocus)
        widgetList.show()

        widgetList.itemClicked.connect(self.getNBins)

    def getNBins(self):
        self.setText(self.widgetList.currentItem().text())
        self.widgetList.close()
        self.setDown(False)

        nBins = []
        nBins.append(mp.twenty)
        nBins.append(mp.thirty)
        nBins.append(mp.fifty)

        iBins = self.widgetList.currentRow()
        self.mainWidget.histogramGraph.nBins = nBins[iBins]
        self.mainWidget.histogramGraph.plotStatistics()


class SetLineHistogram(QtGui.QCheckBox):
    def __init__(self, mainWidget):
        QtGui.QCheckBox.__init__(self, 'Line hist')
        self.mainWidget = mainWidget

        self.setStatusTip('Plot a line on top of the histogram to highlight the distribution')

        self.stateChanged.connect(self.getLineHistogram)

    def getLineHistogram(self):
        if self.isChecked():
            self.mainWidget.histogramGraph.plotLine = True
        else:
            self.mainWidget.histogramGraph.plotLine = False
        self.mainWidget.histogramGraph.plotStatistics()


class SetLogHistogram(QtGui.QCheckBox):
    def __init__(self, mainWidget):
        QtGui.QCheckBox.__init__(self, 'Log hist')
        self.mainWidget = mainWidget

        self.setStatusTip('Show the vertical axis of the histogram in log scale')

        self.stateChanged.connect(self.getLogHistogram)

    def getLogHistogram(self):
        if self.isChecked():
            self.mainWidget.histogramGraph.plotLog = True
        else:
            self.mainWidget.histogramGraph.plotLog = False
        self.mainWidget.histogramGraph.plotStatistics()


class SetColorVaR(QtGui.QCheckBox):
    def __init__(self, mainWidget):
        QtGui.QCheckBox.__init__(self, 'color VaR')
        self.mainWidget = mainWidget

        self.setStatusTip('Color with light red the 5% historical VaR and with dark red the 1% historical VaR')

        self.stateChanged.connect(self.getColorVaR)

    def getColorVaR(self):
        if self.isChecked():
            self.mainWidget.histogramGraph.plotVaR = True
        else:
            self.mainWidget.histogramGraph.plotVaR = False
        self.mainWidget.histogramGraph.plotStatistics()
