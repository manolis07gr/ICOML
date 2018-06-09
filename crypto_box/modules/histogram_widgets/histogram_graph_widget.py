from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.figure as mfg
import scipy.stats as ss
import matplotlib.pylab as plb
import numpy as np

import style_parameters as sp
from misc_parameters import rt, pc, bp
import misc_functions as mf
import misc_parameters as mp


class HistogramGraph(FigureCanvas):
    def __init__(self, mainWidget):
        fig = mfg.Figure(facecolor = sp.colorWindow)
        FigureCanvas.__init__(self, fig)
        self.mainWidget = mainWidget
        mainWidget.fig = fig

        self.ax = []
        self.axScatter = fig.add_axes([0.07, 0.12, 0.40, 0.87])
        self.ax.append(self.axScatter)

        self.axHistogram = fig.add_axes([0.57, 0.12, 0.40, 0.87])
        self.ax.append(self.axHistogram)

        self.tMax = mf.findLastWeekday(mp.today)
        self.dTimeInterval = mp.threeMonths
        self.tMin = mf.findLastWeekday(self.tMax - self.dTimeInterval)
        self.plotLeastSquaresLine = False
        self.plotStdLine = False
        self.plotRPerc = True
        self.rMax = 5.0
        self.plotCounts = True
        self.nBins = 20
        self.plotLog = False
        self.plotLine = False
        self.plotVaR = False

        self.plotStatistics()
        self.decorateAxes()
        self.resetGraph()

    def plotStatistics(self):
        self.axScatter.clear()
        self.axHistogram.clear()
        isNone = 0
        for thisSymbol, thisColorLine in zip(self.mainWidget.symbolWidget, sp.colorLine):
            if thisSymbol.activeSymbol is not None:
                s = thisSymbol.activeSymbol
                m = self.mainWidget.defineMarket.activeMarket
                rSymbol, rMarket, HVaR5, HVaR1 = self.getCommonRange(s, m)
                self.axScatter.plot(rMarket, rSymbol, '.', color = thisColorLine, markersize = 3, alpha = 0.5, zorder = 10)
                if self.plotRPerc is True:
                    rMin = -self.rMax
                    rMax = self.rMax
                    rSym = '%'
                    rFormat = '%.2f'
                else:
                    rMin = -100.0*self.rMax
                    rMax = 100.0*self.rMax
                    rSym = 'bp'
                    rFormat = '%3d'
                self.axScatter.set_xlabel('Market/index return [' + rSym + ']')
                self.axScatter.set_ylabel('Symbol return [' + rSym + ']')
                self.axHistogram.set_xlabel('Symbol return [' + rSym + ']')
                self.axScatter.set_xlim([rMin, rMax])
                self.axScatter.set_ylim([rMin, rMax])

                nData = len(rSymbol)
                iID = sp.colorLine.index(thisColorLine)
                self.mainWidget.statSymbol[5*iID].setText('Day avg: ' + rFormat % np.mean(rSymbol) + rSym + \
                                                        '\tAnn avg: ' + rFormat % (np.mean(rSymbol)*260.0) + rSym)
                self.mainWidget.statSymbol[5*iID+1].setText('Day std: ' + rFormat % np.std(rSymbol) + rSym + \
                                                          '\tAnn std: ' + rFormat % (np.std(rSymbol)*np.sqrt(260.0)) + rSym)
                self.mainWidget.statSymbol[5*iID+2].setText('Max: ' + rFormat % max(rSymbol) + rSym + \
                                                          '\tMin: ' + rFormat % min(rSymbol) + rSym)
                self.mainWidget.statSymbol[5*iID+4].setText('Sharpe: ' + rFormat % (np.mean(rSymbol)*np.sqrt(260.0)/np.std(rSymbol)) + \
                                                          '\tHVaR1%: ' + rFormat % HVaR1[0] + rSym)
                beta, alpha, r_value, p_value, std_err = ss.linregress(rMarket, rSymbol)
                rEstimate = plb.poly1d([beta, alpha])
                rStd = np.sqrt( np.mean( (rSymbol - rEstimate(rMarket))**2 ) )
                betaEquation = np.cov(rMarket, rSymbol)[0,1]/np.var(rMarket)
                self.mainWidget.statSymbol[5*sp.colorLine.index(thisColorLine) + 3].setText('beta: ' + '%.2f' % betaEquation + \
                                                                                       '\talpha: ' + rFormat % alpha + rSym)
                if self.plotLeastSquaresLine is True:
                    self.axScatter.plot([rMin, rMax], rEstimate([rMin, rMax]), thisColorLine, linewidth = 2.0, zorder = 10)
                if self.plotStdLine is True:
                    self.axScatter.fill_between([rMin, rMax], np.subtract(rEstimate([rMin, rMax]), rStd), np.add(rEstimate([rMin, rMax]), rStd), color = thisColorLine, alpha = 0.2, zorder = 10)

                if self.plotCounts is True:
                    weights = np.ones_like(rSymbol)
                    self.axHistogram.set_ylabel('Counts')
                else:
                    weights = np.divide(np.ones_like(rSymbol), len(rSymbol))
                    self.axHistogram.set_ylabel('Frequency')
                if self.plotLine is False:
                    n, bins, patches = self.axHistogram.hist(rSymbol, self.nBins, color = thisColorLine, edgecolor = thisColorLine, weights = weights, log = self.plotLog, range = (-rMax, rMax), linewidth = 2.0, alpha = 0.3, zorder = 10)                    
                else:
                    n, bins, patches = self.axHistogram.hist(rSymbol, self.nBins, color = thisColorLine, edgecolor = thisColorLine, weights = weights, log = self.plotLog, range = (-rMax, rMax), linewidth = 2.0, alpha = 0.1, zorder = 10)
                    middleBins = []
                    for iBin in range(0, len(bins)-1):
                        middleBins.append(0.5*(bins[iBin] + bins[iBin+1]))
                    self.axHistogram.plot(middleBins, n, marker = '.', linestyle = '-', color = thisColorLine, markersize = 5, linewidth = 2.0, zorder = 10)

                self.axHistogram.set_xlim([rMin, rMax])
                if self.plotLog is True:
                    if self.plotCounts is True:
                        self.axHistogram.set_ylim([0.9, max(1.05*n)])
                    else:
                        self.axHistogram.set_ylim([1.0e-5, 1.0])
                if self.plotVaR is True:
                    if self.plotRPerc is True: j = pc
                    else: j = bp
                    for thisBin, thisPatches in zip(bins, patches):
                        if thisBin < HVaR5[0] and thisBin > HVaR1[0]:
                            thisPatches.set_facecolor(sp.colorNegative)
                            thisPatches.set_alpha(0.5)
                        elif thisBin < HVaR1[0]:
                            thisPatches.set_facecolor(sp.colorVeryNegative)
                            thisPatches.set_alpha(0.5)

            else:
                isNone += 1

        self.decorateAxes()
        if isNone == len(self.mainWidget.symbolWidget):
            self.resetGraph()
        self.draw()

    def decorateAxes(self):
        for thisAx in self.ax:
            thisAx.title.set_color(sp.colorLabel)
            thisAx.set_facecolor(sp.colorGraphBackground)
            thisAx.spines['bottom'].set_color(sp.colorLabel)
            thisAx.spines['top'].set_color(sp.colorLabel)
            thisAx.spines['left'].set_color(sp.colorLabel)
            thisAx.spines['right'].set_color(sp.colorLabel)
            thisAx.xaxis.label.set_color(sp.colorTitle)
            thisAx.yaxis.label.set_color(sp.colorTitle)
            thisAx.minorticks_on()
            thisAx.tick_params(axis='x', which='both', colors = sp.colorLabel)
            thisAx.tick_params(axis='y', which='both', colors = sp.colorLabel)
            thisAx.grid()
            thisAx.grid(which='major', axis='x', linewidth=0.50, linestyle='-', color = sp.colorGrid, zorder = 0)
            thisAx.grid(which='minor', axis='x', linewidth=0.25, linestyle='-', color = sp.colorGrid, zorder = 0)
            thisAx.grid(which='major', axis='y', linewidth=0.50, linestyle='-', color = sp.colorGrid, zorder = 0)
            thisAx.grid(which='minor', axis='y', linewidth=0.25, linestyle='-', color = sp.colorGrid, zorder = 0)
            thisAx.axhline(color = sp.colorLabel)
            thisAx.axvline(color = sp.colorLabel)
            yTickLabels = thisAx.get_yticks()
            yTickLabelsNew = []
            for label in yTickLabels:
                yTickLabelsNew.append(str(label))
            yTickLabelsNew[0] = ''
            yTickLabelsNew[-1] = ''
            thisAx.set_yticklabels(yTickLabelsNew)
            
    def resetGraph(self):
        for thisAx in self.ax:
            thisAx.tick_params(axis='x', which='both', colors = sp.colorWindow)
            thisAx.tick_params(axis='y', which='both', colors = sp.colorWindow)

    def getCommonRange(self, symbol, market):
        tMax = self.tMax
        self.tMin = mf.findLastWeekday(tMax - self.dTimeInterval)
        tMin = self.tMin
        tMin = max(tMin, symbol.dDate.data[0], market.dDate.data[0])
        tMax = min(tMax, symbol.dDate.data[-1], market.dDate.data[-1])
        rSymbol = []
        rMarket = []
        HVaR5   = []
        HVaR1   = []
        for iDateSymbol in range(0, len(symbol.dDate.data)):
            if symbol.dDate.data[iDateSymbol] > tMin and symbol.dDate.data[iDateSymbol] <= tMax:
                try:
                    dateSymbol = symbol.dDate.data[iDateSymbol]
                    iDateMarket = market.dDate.data.index(dateSymbol)
                    if self.plotRPerc is True:
                        rSymbol.append(symbol.rClose[pc].data[iDateSymbol])
                        rMarket.append(market.rClose[pc].data[iDateMarket])
                        HVaR5.append(symbol.histVaR5[pc].data[iDateSymbol])
                        HVaR1.append(symbol.histVaR1[pc].data[iDateSymbol])
                    else:
                        rSymbol.append(symbol.rClose[bp].data[iDateSymbol])
                        rMarket.append(market.rClose[bp].data[iDateMarket])
                        HVaR5.append(symbol.histVaR5[bp].data[iDateSymbol])
                        HVaR1.append(symbol.histVaR1[bp].data[iDateSymbol])
                except:
                    pass
        return rSymbol, rMarket, HVaR5, HVaR1
