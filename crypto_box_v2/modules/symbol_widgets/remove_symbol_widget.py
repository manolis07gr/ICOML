from PySide import QtGui, QtCore


class RemoveSymbol(QtGui.QPushButton):
    def __init__(self, mainWidget):
        QtGui.QPushButton.__init__(self, 'Rem Symbol')
        self.setFocusPolicy(QtCore.Qt.NoFocus)
        self.mainWidget = mainWidget

        self.setStatusTip('Select symbol from list and click here to remove it.')

        self.clicked.connect(self.removeSymbol)

    def removeSymbol(self):
        for thisSymbol in self.mainWidget.symbolList:
            if thisSymbol.name == self.mainWidget.listSymbols.currentItem().text():
                self.mainWidget.listSymbols.takeItem(self.mainWidget.listSymbols.currentRow())
                indexSymbol = self.mainWidget.symbolList.index(thisSymbol)
                del self.mainWidget.symbolList[indexSymbol]
                break
