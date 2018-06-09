from PyQt5 import QtWidgets, QtCore


class ListSymbols(QtWidgets.QListWidget):
    def __init__(self, mainWidget):
        QtWidgets.QListWidget.__init__(self, mainWidget)
        self.setFocusPolicy(QtCore.Qt.NoFocus)
        self.setAlternatingRowColors(True)

        self.mainWidget = mainWidget

        self.setStatusTip('List of symbols; add/remove symbols using the buttons below.')

        self.row = int(self.currentRow())
        self.itemClicked.connect(self.selectItem)


    def populateList(self):
        self.clear()
        for iSymbol in self.mainWidget.symbolList:
            self.addItem(iSymbol.name)

    def selectItem(self):
        if self.currentRow() == self.row:
            self.currentItem().setSelected(False)
        self.row = int(self.currentRow())
