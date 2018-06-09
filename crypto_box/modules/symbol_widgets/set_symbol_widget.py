from PyQt5 import QtWidgets, QtCore
import numpy as np

import style_parameters as sp
from misc_parameters import pc


class SetSymbol(QtWidgets.QPushButton):
    def __init__(self, mainWidget, idColor):
        QtWidgets.QPushButton.__init__(self, 'Set symbol')
        self.setFocusPolicy(QtCore.Qt.NoFocus)
        self.mainWidget = mainWidget
        self.idColor = idColor

        self.activeSymbol = None

        self.setStatusTip('Set symbol to plot and calculate returns.')

        self.clicked.connect(self.selectSymbol)

    def selectSymbol(self):
        self.setDown(True)
        self.activeSymbolList = []
        try:
            self.widgetList.close()
        except:
            pass
        self.widgetList = QtWidgets.QListWidget(self.mainWidget)
        widgetList = self.widgetList
        widgetList.setAlternatingRowColors(True)

        widgetList.addItem('--- None ---')
        self.activeSymbolList.append(None)
        for thisSymbol in self.mainWidget.symbolList:
            widgetList.addItem(thisSymbol.name + ' (' + thisSymbol.description + ')')
            self.activeSymbolList.append(thisSymbol)
        activesymbolNameList = []
        for thisActiveSymbol in self.activeSymbolList:
            if thisActiveSymbol is not None:
                activesymbolNameList.append(thisActiveSymbol.name)
        for thisMarket in self.mainWidget.marketList:
            if thisMarket.name not in activesymbolNameList:
                widgetList.addItem(thisMarket.name + ' (' + thisMarket.description + ')')
                self.activeSymbolList.append(thisMarket)

        widgetList.setGeometry(QtWidgets.QWidget.geometry(self))
        widgetList.setMinimumWidth(QtWidgets.QWidget.size(self).width())
        widgetList.setMinimumHeight(400)
        widgetList.move(QtWidgets.QWidget.pos(self).x(), QtWidgets.QWidget.pos(self).y() - 400)
        widgetList.setFocusPolicy(QtCore.Qt.NoFocus)
        if len(self.mainWidget.symbolList) != 0:
            widgetList.show()
        else:
            self.setDown(False)

        widgetList.itemClicked.connect(self.getSymbol)

    def getSymbol(self):
        self.widgetList.close()
        self.setDown(False)
        iSymbol = self.widgetList.currentRow()
        string = self.widgetList.currentItem().text()
        tmpString = string.split('&')
        string = '&&'.join(tmpString)
        if string != '--- None ---':
            self.setText(' ' + string)
            self.setStyleSheet('SetSymbol {color: ' + sp.colorLine[self.idColor] + '; text-align: left; font-weight: bold;}')
            self.activeSymbol = self.activeSymbolList[iSymbol]
#            for i in range(0, 5):
#                self.mainWidget.statSymbol[5*self.idColor+i].setStyleSheet('QLabel {color: ' + sp.colorLine[self.idColor] + ';}')
        else:
            self.setText('Set symbol')
            self.setStyleSheet('SetSymbol {text-align: center;}')
            self.activeSymbol = None
            for i in range(0, 5):
                self.mainWidget.statSymbol[5*self.idColor+i].setText('')

        self.mainWidget.updatePlots()
