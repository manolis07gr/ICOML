from PySide import QtGui, QtCore

import read_file_widget as rfw
import define_market_widget as dmw
import timeseries_graph_widget as tgw
import histogram_graph_widget as hgw
import timeseries_widget as tsw
import histogram_widget as hw
import list_symbols_widget as lsw
import set_symbol_widget as ssw
import add_symbol_widget as asw
import get_symbol_widget as gsw
import remove_symbol_widget as rsw
import time_interval_widget as tiw
import return_interval_widget as riw
import set_mov_avg as sma
import set_mov_duration as smd
import set_units as su
import set_least_squares as sls
import set_hist_properties as shp
from misc_parameters import idButton1, idButton2, idButton3, idButton4

class WidgetMain(QtGui.QWidget):
    
    def __init__(self):
        QtGui.QWidget.__init__(self)

        self.grid = QtGui.QGridLayout()

        # WorkSpaces
        self.timeseriesWidget = tsw.TimeseriesWidget(self)
        self.grid.addWidget(self.timeseriesWidget, 0, 0, 1, 6)
        self.histogramWidget = hw.HistogramWidget(self)
        self.grid.addWidget(self.histogramWidget, 0, 6, 1, 6)

        # Define market
        self.grid.addWidget(QtGui.QLabel("Index & Symbols:"), 0, 12, 1, 1)
        self.defineMarket = dmw.ButtonDefineMarket(self)
        self.grid.addWidget(self.defineMarket, 1, 12, 1, 1)

        # Symbols
        self.getData = rfw.ButtonReadFile(self)
        self.grid.addWidget(self.getData, 2, 12, 1, 1)
        self.listSymbols = lsw.ListSymbols(self)
        self.grid.addWidget(self.listSymbols, 3, 12, 5, 1)
        self.addSymbol = asw.AddSymbol(self)
        self.grid.addWidget(self.addSymbol, 9, 12, 1, 1)
        self.getSymbol = gsw.GetSymbol(self)
        self.grid.addWidget(self.getSymbol, 8, 12, 1, 1)
        self.removeSymbol = rsw.RemoveSymbol(self)
        self.grid.addWidget(self.removeSymbol, 10, 12, 1, 1)

        # Set symbol
        self.symbolWidget = []
        self.symbolWidget.append(ssw.SetSymbol(self, idButton1))
        self.grid.addWidget(self.symbolWidget[idButton1], 9, 0, 1, 3)
        self.symbolWidget.append(ssw.SetSymbol(self, idButton2))
        self.grid.addWidget(self.symbolWidget[idButton2], 9, 3, 1, 3)
        self.symbolWidget.append(ssw.SetSymbol(self, idButton3))
        self.grid.addWidget(self.symbolWidget[idButton3], 9, 6, 1, 3)
        self.symbolWidget.append(ssw.SetSymbol(self, idButton4))
        self.grid.addWidget(self.symbolWidget[idButton4], 9, 9, 1, 3)

        self.setTimeseriesWidgets()
        self.setHistogramWidgets()

        # Stretch params
        for nCol in range(0, 13):
            self.grid.setColumnStretch(nCol, 1)
        for nRow in range(0, 4):
            self.grid.setRowStretch(nRow, 1)
        for nRow in range(4, 10):
            self.grid.setRowStretch(nRow, 0)

        self.setLayout(self.grid)
     
        self.showTimeseriesWidgets()
        self.getData.getData()
        self.defineMarket.selectIndex()


    def setTimeseriesWidgets(self):
        self.listTimeseriesWidgets = []

        for thisWidget in self.symbolWidget:
            self.listTimeseriesWidgets.append(thisWidget)

        # Graph controls
        self.setTimeInterval = tiw.SetTimeInterval(self)
        self.listTimeseriesWidgets.append(self.setTimeInterval)
        self.grid.addWidget(self.setTimeInterval, 10, 0, 1, 1)
        self.setRInterval = riw.SetReturnInterval(self)
        self.listTimeseriesWidgets.append(self.setRInterval)
        self.grid.addWidget(self.setRInterval, 10, 1, 1, 1)

        self.set1DolInvested = su.Set1DolInvested(self)
        self.listTimeseriesWidgets.append(self.set1DolInvested)
        self.grid.addWidget(self.set1DolInvested, 10, 2, 1, 1)
        self.setMovDuration = smd.SetMovDuration(self)
        self.listTimeseriesWidgets.append(self.setMovDuration)
        self.grid.addWidget(self.setMovDuration, 10, 3, 1, 1)

        self.setMovAvg = sma.SetMovAvg(self)
        self.listTimeseriesWidgets.append(self.setMovAvg)
        self.grid.addWidget(self.setMovAvg, 10, 4, 1, 1)
        self.setMovStd = sma.SetMovStd(self)
        self.listTimeseriesWidgets.append(self.setMovStd)
        self.grid.addWidget(self.setMovStd, 10, 5, 1, 1)

        self.setClosePrice = su.SetClosePrice(self)
        self.listTimeseriesWidgets.append(self.setClosePrice)
        self.grid.addWidget(self.setClosePrice, 10, 6, 1, 1)
        self.setAdjustedPrice = su.SetAdjustedPrice(self)
        self.listTimeseriesWidgets.append(self.setAdjustedPrice)
        self.grid.addWidget(self.setAdjustedPrice, 10, 7, 1, 1)

        self.setPercReturn = su.SetPercReturn(self)
        self.listTimeseriesWidgets.append(self.setPercReturn)
        self.grid.addWidget(self.setPercReturn, 10, 8, 1, 1)
        self.setBPReturn = su.SetBPReturn(self)
        self.listTimeseriesWidgets.append(self.setBPReturn)
        self.grid.addWidget(self.setBPReturn, 10, 9, 1, 1)

        self.setNLogVol = su.SetNLogVol(self)
        self.listTimeseriesWidgets.append(self.setNLogVol)
        self.grid.addWidget(self.setNLogVol, 10, 10, 1, 1)
        self.setValueLogVol = su.SetValueLogVol(self)
        self.listTimeseriesWidgets.append(self.setValueLogVol)
        self.grid.addWidget(self.setValueLogVol, 10, 11, 1, 1)

        # Graphs
        self.timeseriesGraph = tgw.TimeseriesGraph(self)
        self.listTimeseriesWidgets.append(self.timeseriesGraph)
        self.grid.addWidget(self.timeseriesGraph, 1, 0, 8, 12)


    def setHistogramWidgets(self):
        self.listHistogramWidgets = []

        for thisWidget in self.symbolWidget:
            self.listHistogramWidgets.append(thisWidget)
        self.listHistogramWidgets.append(self.setTimeInterval)
        self.listHistogramWidgets.append(self.setRInterval)
        self.listHistogramWidgets.append(self.setPercReturn)
        self.listHistogramWidgets.append(self.setBPReturn)

        self.setLeastSquaresLine = sls.SetLeastSquaresLine(self)
        self.listHistogramWidgets.append(self.setLeastSquaresLine)
        self.grid.addWidget(self.setLeastSquaresLine, 10, 2, 1, 1)
        self.setStdLine = sls.SetStdLine(self)
        self.listHistogramWidgets.append(self.setStdLine)
        self.grid.addWidget(self.setStdLine, 10, 3, 1, 1)

        self.setNBins = shp.SetNBins(self)
        self.listHistogramWidgets.append(self.setNBins)
        self.grid.addWidget(self.setNBins, 10, 4, 1, 1)
        self.setLogHistogram = shp.SetLogHistogram(self)
        self.listHistogramWidgets.append(self.setLogHistogram)
        self.grid.addWidget(self.setLogHistogram, 10, 5, 1, 1)
        self.setLineHistogram = shp.SetLineHistogram(self)
        self.listHistogramWidgets.append(self.setLineHistogram)
        self.grid.addWidget(self.setLineHistogram, 10, 6, 1, 1)
        self.setColorVaR = shp.SetColorVaR(self)
        self.listHistogramWidgets.append(self.setColorVaR)
        self.grid.addWidget(self.setColorVaR, 10, 7, 1, 1)

        self.setCounts = su.SetCounts(self)
        self.listHistogramWidgets.append(self.setCounts)
        self.grid.addWidget(self.setCounts, 10, 10, 1, 1)
        self.setFrequency = su.SetFrequency(self)
        self.listHistogramWidgets.append(self.setFrequency)
        self.grid.addWidget(self.setFrequency, 10, 11, 1, 1)

        self.statSymbol = []
        for i in range(0, 20):
            self.statSymbol.append(QtGui.QLabel(""))
            self.listHistogramWidgets.append(self.statSymbol[i])
            self.statSymbol[i].setStatusTip("Statistics for the total period of available data for the symbol")

        self.grid.addWidget(self.statSymbol[0], 4, 0, 1, 3)
        self.grid.addWidget(self.statSymbol[1], 5, 0, 1, 3)
        self.grid.addWidget(self.statSymbol[2], 6, 0, 1, 3)
        self.grid.addWidget(self.statSymbol[3], 7, 0, 1, 3)
        self.grid.addWidget(self.statSymbol[4], 8, 0, 1, 3)

        self.grid.addWidget(self.statSymbol[5], 4, 3, 1, 3)
        self.grid.addWidget(self.statSymbol[6], 5, 3, 1, 3)
        self.grid.addWidget(self.statSymbol[7], 6, 3, 1, 3)
        self.grid.addWidget(self.statSymbol[8], 7, 3, 1, 3)
        self.grid.addWidget(self.statSymbol[9], 8, 3, 1, 3)

        self.grid.addWidget(self.statSymbol[10], 4, 6, 1, 3)
        self.grid.addWidget(self.statSymbol[11], 5, 6, 1, 3)
        self.grid.addWidget(self.statSymbol[12], 6, 6, 1, 3)
        self.grid.addWidget(self.statSymbol[13], 7, 6, 1, 3)
        self.grid.addWidget(self.statSymbol[14], 8, 6, 1, 3)

        self.grid.addWidget(self.statSymbol[15], 4, 9, 1, 3)
        self.grid.addWidget(self.statSymbol[16], 5, 9, 1, 3)
        self.grid.addWidget(self.statSymbol[17], 6, 9, 1, 3)
        self.grid.addWidget(self.statSymbol[18], 7, 9, 1, 3)
        self.grid.addWidget(self.statSymbol[19], 8, 9, 1, 3)

        # Graphs
        self.histogramGraph = hgw.HistogramGraph(self)
        self.listHistogramWidgets.append(self.histogramGraph)
        self.grid.addWidget(self.histogramGraph, 1, 0, 3, 12)

    def updatePlots(self):
        if self.timeseriesWidget.isDown() is True:
            self.timeseriesGraph.plotPrices()
        if self.histogramWidget.isDown() is True:
            if self.defineMarket.activeMarket != None:
                self.histogramGraph.plotStatistics()

    def showTimeseriesWidgets(self):
        self.timeseriesWidget.setDown(True)
        self.histogramWidget.setDown(False)
        for thisWidget in self.listHistogramWidgets:
            thisWidget.setVisible(False)
        for thisWidget in self.listTimeseriesWidgets:
            thisWidget.setVisible(True)
        self.timeseriesGraph.plotPrices()

    def showHistogramWidgets(self):
        self.timeseriesWidget.setDown(False)
        self.histogramWidget.setDown(True)
        for thisWidget in self.listTimeseriesWidgets:
            thisWidget.setVisible(False)
        for thisWidget in self.listHistogramWidgets:
            thisWidget.setVisible(True)
        if self.defineMarket.activeMarket != None:
            self.histogramGraph.plotStatistics()
