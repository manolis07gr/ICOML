from PyQt5 import QtWidgets, QtCore

import symbol_list_class as slc


class AddSymbol(QtWidgets.QPushButton):
    def __init__(self, mainWidget):
        QtWidgets.QPushButton.__init__(self, 'Add Symbol')
        self.setFocusPolicy(QtCore.Qt.NoFocus)
        self.mainWidget = mainWidget

        self.setStatusTip('Enter symbol above and click here to add it in the list.')

        self.clicked.connect(self.getSymbol)

    def getSymbol(self, tmpStr = ''):
        if tmpStr == '':
            tmpStr = self.mainWidget.getSymbol.text().upper()
        if tmpStr != '':
            symbolExists = False
            for thisSymbol in self.mainWidget.symbolList:
                if tmpStr == thisSymbol.name:
                    symbolExists = True
            for thisMarket in self.mainWidget.marketList:
                if tmpStr == thisMarket.name:
                    symbolExists = True
            if symbolExists is False:
                symbol = slc.SymbolList('', addSymbol = True, symbol = tmpStr).symbolList
                if len(symbol) != 0:
                    self.mainWidget.symbolList.append(symbol[0])
                    self.mainWidget.listSymbols.addItem(symbol[0].name)
        self.mainWidget.getSymbol.clear()
