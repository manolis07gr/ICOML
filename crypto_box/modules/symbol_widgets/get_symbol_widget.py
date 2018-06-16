from PyQt5 import QtWidgets


class GetSymbol(QtWidgets.QLineEdit):
    def __init__(self, mainWidget):
        QtWidgets.QLineEdit.__init__(self)
        self.mainWidget = mainWidget

        self.setStatusTip('Enter symbol here and press Enter to add it in the list.')

        self.returnPressed.connect(self.mainWidget.addSymbol.getSymbol)
