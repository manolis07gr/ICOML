from PyQt5 import QtWidgets, QtCore

import file_parameters as fp
import symbol_list_class as slc


class ButtonReadFile(QtWidgets.QPushButton):
    def __init__(self, mainWidget):
        QtWidgets.QPushButton.__init__(self, 'Load symbols')
        self.setFocusPolicy(QtCore.Qt.NoFocus)
        self.mainWidget = mainWidget

        self.mainWidget.symbolList = []

        self.setStatusTip('Load symbol list from file.')

        self.clicked.connect(self.getData)

    def getData(self):
        if len(self.mainWidget.symbolList) == 0:
            self.mainWidget.symbolList = slc.SymbolList(fp.fileSymbolList).symbolList
        else:
            tmpSymbolList = slc.SymbolList(fp.fileSymbolList).symbolList
            for thisSymbol in tmpSymbolList:
                isInList = False
                for existingSymbol in self.mainWidget.symbolList:
                    if thisSymbol.name == existingSymbol.name:
                        isInList = True
                if isInList is False:
                    self.mainWidget.symbolList.append(thisSymbol)
        self.mainWidget.listSymbols.populateList()
