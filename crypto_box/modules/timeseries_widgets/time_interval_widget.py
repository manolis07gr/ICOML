from PySide import QtGui, QtCore

import misc_parameters as mp


class SetTimeInterval(QtGui.QPushButton):
    def __init__(self, mainWidget):
        QtGui.QPushButton.__init__(self, 'Time range')
        self.setStatusTip('Change the time window of the timeseries graph.')

        self.setFocusPolicy(QtCore.Qt.NoFocus)
        self.mainWidget = mainWidget

        self.clicked.connect(self.setTimeWindow)

    def setTimeWindow(self):
        self.setDown(True)
        try:
            self.widgetList.close()
        except:
            pass

        self.widgetList = QtGui.QListWidget(self.mainWidget)
        widgetList = self.widgetList
        widgetList.setAlternatingRowColors(True)

        widgetList.addItem(mp.strOneMonth)
        widgetList.addItem(mp.strThreeMonths)
        widgetList.addItem(mp.strSixMonths)
        widgetList.addItem(mp.strOneYear)
        widgetList.addItem(mp.strThreeYears)
        widgetList.addItem(mp.strTenYears)

        widgetList.setGeometry(QtGui.QWidget.geometry(self))
        widgetList.setMinimumWidth(QtGui.QWidget.size(self).width())
        widgetList.setMinimumHeight(120)
        widgetList.move(QtGui.QWidget.pos(self).x(), QtGui.QWidget.pos(self).y() - 120)
        widgetList.setFocusPolicy(QtCore.Qt.NoFocus)
        widgetList.show()

        widgetList.itemClicked.connect(self.getTInterval)

    def getTInterval(self):
        self.setText(self.widgetList.currentItem().text())
        self.widgetList.close()
        self.setDown(False)

        dTimeInterval = []
        dTimeInterval.append(mp.oneMonth)
        dTimeInterval.append(mp.threeMonths)
        dTimeInterval.append(mp.sixMonths)
        dTimeInterval.append(mp.oneYear)
        dTimeInterval.append(mp.threeYears)
        dTimeInterval.append(mp.tenYears)

        iInterval = self.widgetList.currentRow()
        self.mainWidget.timeseriesGraph.dTimeInterval = dTimeInterval[iInterval]
        self.mainWidget.histogramGraph.dTimeInterval = dTimeInterval[iInterval]
        self.mainWidget.updatePlots()
