from PyQt5 import QtWidgets, QtCore

import file_parameters as fp
import symbol_list_class as slc


class ButtonDefineMarket(QtWidgets.QPushButton):
    def __init__(self, mainWidget):
        QtWidgets.QPushButton.__init__(self, 'Set index')
        self.mainWidget = mainWidget
        self.setFocusPolicy(QtCore.Qt.NoFocus)

        self.mainWidget.marketList = []
        self.activeMarket = None

        self.setStatusTip('Set index symbol to define the market, e.g. for the calculation of beta.')

        self.clicked.connect(self.selectIndex)

    def selectIndex(self):
        self.setDown(True)
        firstCall = False
        if (len(self.mainWidget.marketList) == 0):
            self.mainWidget.marketList = slc.SymbolList(fp.fileMarket).symbolList
            firstCall = True
        try:
            self.widgetList.close()
        except:
            pass

        if firstCall is True:
            string = self.mainWidget.marketList[0].description
            tmpString = string.split('&')
            string = '&&'.join(tmpString)
            self.setText(string)
            self.activeMarket = self.mainWidget.marketList[0]
            self.setDown(False)
            firstCall = False

        self.widgetList = QtWidgets.QListWidget(self.mainWidget)
        widgetList = self.widgetList
        widgetList.setAlternatingRowColors(True)
        for iMarket in self.mainWidget.marketList:
            widgetList.addItem(iMarket.description)
        widgetList.setGeometry(QtWidgets.QWidget.geometry(self))
        widgetList.setMinimumHeight(150)
        widgetList.move(QtWidgets.QWidget.pos(self).x() - QtWidgets.QWidget.size(self).width(), QtWidgets.QWidget.pos(self).y())
        widgetList.setFocusPolicy(QtCore.Qt.NoFocus)
        widgetList.show()

        widgetList.itemClicked.connect(self.getMarket)

    def getMarket(self):
        iMarket = self.widgetList.currentRow()
        string = self.widgetList.currentItem().text()
        tmpString = string.split('&')
        string = '&&'.join(tmpString)
        self.setText(string)
        self.activeMarket = self.mainWidget.marketList[iMarket]
        self.widgetList.close()
        self.setDown(False)
        self.mainWidget.updatePlots()
