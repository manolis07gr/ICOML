from PyQt5 import QtWidgets, QtCore
import misc_parameters as mp


class SetReturnInterval(QtWidgets.QPushButton):
    def __init__(self, mainWidget):
        QtWidgets.QPushButton.__init__(self, 'Ret range')
        self.setStatusTip('Change the return range of the timeseries graph.')

        self.setFocusPolicy(QtCore.Qt.NoFocus)
        self.mainWidget = mainWidget

        self.clicked.connect(self.setRInterval)

    def setRInterval(self):
        self.setDown(True)
        try:
            self.widgetList.close()
        except:
            pass

        self.widgetList = QtWidgets.QListWidget(self.mainWidget)
        widgetList = self.widgetList
        widgetList.setAlternatingRowColors(True)

        widgetList.addItem(mp.strFivePc)
        widgetList.addItem(mp.strTenPc)
        widgetList.addItem(mp.strTwentyFivePc)
        widgetList.addItem(mp.strFiftyPc)

        widgetList.setGeometry(QtWidgets.QWidget.geometry(self))
        widgetList.setMinimumWidth(QtWidgets.QWidget.size(self).width())
        widgetList.setMinimumHeight(80)
        widgetList.move(QtWidgets.QWidget.pos(self).x(), QtWidgets.QWidget.pos(self).y() - 80)
        widgetList.setFocusPolicy(QtCore.Qt.NoFocus)
        widgetList.show()

        widgetList.itemClicked.connect(self.getRInterval)

    def getRInterval(self):
        self.setText(self.widgetList.currentItem().text())
        self.widgetList.close()
        self.setDown(False)

        rInterval = []
        rInterval.append(mp.fivePc)
        rInterval.append(mp.tenPc)
        rInterval.append(mp.twentyFivePc)
        rInterval.append(mp.fiftyPc)

        iInterval = self.widgetList.currentRow()
        self.mainWidget.timeseriesGraph.rMax = rInterval[iInterval]
        self.mainWidget.histogramGraph.rMax = rInterval[iInterval]
        self.mainWidget.updatePlots()
