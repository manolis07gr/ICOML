from PySide import QtGui, QtCore

import misc_functions as mf
import symbol_classes as sc
import progress_bar_widget as pbw


class SymbolList(object):
    def __init__(self, nameFile, addSymbol = False, symbol = ''):

        self.symbolList = []

        symbolsAll = sc.SymbolListAll()
        if addSymbol == False:
            symbolsAsked = self.readSymbolsAsked(nameFile)
        else:
            symbolsAsked = []
            symbolsAsked.append(symbol)

        progressBar = pbw.ProgressBar(len(symbolsAsked))
        for thisSymbol in symbolsAsked:
            iSymbol = self.findIndex(thisSymbol, symbolsAll)
            if iSymbol != -1:
                nameSymbol = symbolsAll.name[iSymbol]
                progressBar.updateValue(nameSymbol)
                descriptionSymbol = symbolsAll.description[iSymbol]
                symbol = sc.Symbol(nameSymbol, descriptionSymbol)
                self.symbolList.append(symbol)

    def readSymbolsAsked(self, nameFile):
        symbolAskedList = []
        data = mf.openFile(nameFile)
        tmpLst = data.readline().rstrip()
        while tmpLst != '':
            symbolAskedList.append(str(tmpLst))
            tmpLst = data.readline().rstrip()
        data.close()
        return symbolAskedList

    def findIndex(self, symbol, symbolsAll):
        try:
            index = symbolsAll.name.index(symbol)
            return index
        except:
            mf.errorMessage('Error: Unable to find ' + symbol + ' in coinmarketcap ticker symbol list.')
            mf.errorMessage('Skipping ' + symbol + '.')
            return -1
