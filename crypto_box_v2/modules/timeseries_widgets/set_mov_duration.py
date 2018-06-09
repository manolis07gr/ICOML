from PySide import QtGui, QtCore

import misc_parameters as mp


class SetMovDuration(QtGui.QPushButton):
    def __init__(self, mainWidget):
        QtGui.QPushButton.__init__(self, 'Mov range')
        self.setStatusTip('Set the time interval for the moving average and standard deviation.')

        self.setFocusPolicy(QtCore.Qt.NoFocus)
        self.mainWidget = mainWidget

        self.clicked.connect(self.setMovInterval)

    def setMovInterval(self):
        self.setDown(True)
        try:
            self.widgetList.close()
        except:
            pass

        self.widgetList = QtGui.QListWidget(self.mainWidget)
        widgetList = self.widgetList
        widgetList.setAlternatingRowColors(True)

        widgetList.addItem(mp.strMTenDays)
        widgetList.addItem(mp.strMFourWeeks)
        widgetList.addItem(mp.strMThreeMonths)

        widgetList.setGeometry(QtGui.QWidget.geometry(self))
        widgetList.setMinimumWidth(QtGui.QWidget.size(self).width())
        widgetList.setMinimumHeight(60)
        widgetList.move(QtGui.QWidget.pos(self).x(), QtGui.QWidget.pos(self).y() - 60)
        widgetList.setFocusPolicy(QtCore.Qt.NoFocus)
        widgetList.show()

        widgetList.itemClicked.connect(self.getMovInterval)

    def getMovInterval(self):
        self.setText(self.widgetList.currentItem().text())
        self.widgetList.close()
        self.setDown(False)

        movInterval = []
        movInterval.append(mp.td)
        movInterval.append(mp.fw)
        movInterval.append(mp.tm)

        iInterval = self.widgetList.currentRow()
        self.mainWidget.timeseriesGraph.movInterval = movInterval[iInterval]
        self.mainWidget.timeseriesGraph.plotPrices()
