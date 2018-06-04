from PySide import QtGui


class GetSymbol(QtGui.QLineEdit):
    def __init__(self, mainWidget):
        QtGui.QLineEdit.__init__(self)
        self.mainWidget = mainWidget

        self.setStatusTip('Enter symbol here and press enter to add it in the list.')

        self.returnPressed.connect(self.mainWidget.addSymbol.getSymbol)
