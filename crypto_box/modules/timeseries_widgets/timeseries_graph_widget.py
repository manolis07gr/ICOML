from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.figure as mfg
import matplotlib.dates as mdt
import matplotlib.ticker as mt
import numpy as np

import style_parameters as sp
from misc_parameters import rt, pc, bp
import misc_functions as mf
import misc_parameters as mp


class TimeseriesGraph(FigureCanvas):
    def __init__(self, mainWidget):
        fig = mfg.Figure(facecolor = sp.colorWindow)
        FigureCanvas.__init__(self, fig)
        self.mainWidget = mainWidget
        mainWidget.fig = fig

        self.ax = []
        self.axPrice = fig.add_axes([0.07, 0.50, 0.90, 0.45])
        self.ax.append(self.axPrice)

        self.axReturn = fig.add_axes([0.07, 0.17, 0.90, 0.33])
        self.ax.append(self.axReturn)

        self.axVolume = fig.add_axes([0.07, 0.07, 0.90, 0.10])
        self.ax.append(self.axVolume)

        self.tMax = mf.findLastWeekday(mp.today)
        self.dTimeInterval = mp.threeMonths
        self.tMin = mf.findLastWeekday(self.tMax - self.dTimeInterval)
        self.rInterval = mp.fivePc
        self.rMax = 2.0
        self.plotMovAvg = False
        self.plotMovStd = False
        self.movInterval = 0
        self.plotPAClose = True
        self.plotRPerc = True
        self.plotNLogVol = True
        self.plot1dolInv = False

        self.findLimits()
        self.decorateAxes()
        self.resetGraph()

    def plotPrices(self):
        self.axPrice.clear()
        self.axReturn.clear()
        self.axVolume.clear()
        isNone = 0
        k = self.movInterval
        for thisSymbol, thisColorLine in zip(self.mainWidget.symbolWidget, sp.colorLine):
            if thisSymbol.activeSymbol is not None:
                s = thisSymbol.activeSymbol
                iTMin, iTMax = self.getTMinTmax(s)
                if self.plotPAClose is True:
                    pData = s.pAClose.data
                    pMAvg = s.pAClose.mAvg[k].data
                    pMStd = s.pAClose.mStd[k].data
                    labelPrice = s.pAClose.name + ' [' + s.pAClose.unit + ']'
                    if self.plot1dolInv is True:
                        pData = np.divide(s.pAClose.data, s.pAClose.data[iTMin])
                        pMAvg = np.divide(s.pAClose.mAvg[k].data, s.pAClose.data[iTMin])
                        pMStd = np.divide(s.pAClose.mStd[k].data, s.pAClose.data[iTMin])
                        labelPrice = s.pAClose.name + ' (normalized)'
                else:
                    pData = s.pClose.data
                    pMAvg = s.pClose.mAvg[k].data
                    pMStd = s.pClose.mStd[k].data
                    labelPrice = s.pClose.name + ' [' + s.pClose.unit + ']'
                    if self.plot1dolInv is True:
                        pData = np.divide(s.pClose.data, s.pClose.data[iTMin])
                        pMAvg = np.divide(s.pClose.mAvg[k].data, s.pClose.data[iTMin])
                        pMStd = np.divide(s.pClose.mStd[k].data, s.pClose.data[iTMin])
                        labelPrice = s.pClose.name + ' (normalized)'
                if self.plotRPerc is True:
                    rData = s.rAClose[pc].data
                    rMAvg = s.rAClose[pc].mAvg[k].data
                    rMStd = s.rAClose[pc].mStd[k].data
                    labelReturn = 'Return [' + s.rAClose[pc].unit + ']'
                else:
                    rData = s.rAClose[bp].data
                    rMAvg = s.rAClose[bp].mAvg[k].data
                    rMStd = s.rAClose[bp].mStd[k].data
                    labelReturn = 'Return [' + s.rAClose[bp].unit + ']'
                if self.plotNLogVol is True:
                    vData = s.nLogVol.data
                    labelVolume = 'Vol [' + s.nLogVol.unit + ']'
                else:
                    vData = s.vLogVol.data
                    labelVolume = 'Vol [' + s.vLogVol.unit + ']'

                if self.plotMovAvg is False:
                    self.axPrice.plot(s.dDate.data, pData, linestyle = '-', color = thisColorLine, linewidth = 1.0, zorder = 10)
                    self.axReturn.plot(s.dDate.data, rData, marker = '.', linestyle = '-', color = thisColorLine, markersize = 4, linewidth = 0.3, zorder = 10)
                else:
                    self.axPrice.plot(s.dDate.data, pData, linestyle = '-', color = thisColorLine, linewidth = 1.0, alpha = 0.5, zorder = 10)
                    self.axReturn.plot(s.dDate.data, rData, marker = '.', linestyle = '-', color = thisColorLine, markersize = 4, linewidth = 0.3, alpha = 0.5, zorder = 10)
                    self.axPrice.plot(s.dDate.data, pMAvg, linestyle = '-', color = thisColorLine, linewidth = 2.0, zorder = 10)
                    self.axReturn.plot(s.dDate.data, rMAvg, linestyle = '-', color = thisColorLine, linewidth = 2.0, zorder = 10)
                if self.plotMovStd is True:
                    self.axPrice.fill_between(s.dDate.data, np.subtract(pMAvg, pMStd), np.add(pMAvg, pMStd), color = thisColorLine, alpha = 0.2, zorder = 10)
                    self.axReturn.fill_between(s.dDate.data, np.subtract(rMAvg, rMStd), np.add(rMAvg, rMStd), color = thisColorLine, alpha = 0.2, zorder = 10)
                self.axVolume.fill_between(s.dDate.data, 1.0, vData, color = thisColorLine, alpha = 0.3, zorder = 10)

                self.axPrice.set_ylabel(labelPrice)
                self.axReturn.set_ylabel(labelReturn)
                self.axVolume.set_ylabel(labelVolume)


            else:
                isNone += 1

        self.findLimits()
        self.decorateAxes()
        if len(self.mainWidget.symbolWidget) == isNone:
            self.resetGraph()
        self.draw()

    def findLimits(self):
        pMin = 1.0e8
        pMax = -pMin
        vMin = 1.0e8
        vMax = 1.0
        for thisSymbol in self.mainWidget.symbolWidget:
            if thisSymbol.activeSymbol is not None:
                s = thisSymbol.activeSymbol
                iTMin, iTMax = self.getTMinTmax(s)
                if self.plotPAClose is True:
                    pData = s.pAClose.data
                    if self.plot1dolInv is True:
                        pData = np.divide(s.pAClose.data, s.pAClose.data[iTMin])
                else:
                    pData = s.pClose.data
                    if self.plot1dolInv is True:
                        pData = np.divide(s.pClose.data, s.pClose.data[iTMin])
                if self.plotNLogVol is True:
                    vData = s.nLogVol.data
                else:
                    vData = s.vLogVol.data

                pMin = min(pMin, np.nanmin(pData[iTMin:iTMax]))
                pMax = max(pMax, np.nanmax(pData[iTMin:iTMax]))
                vMin = min(vMin, np.nanmin(vData[iTMin:iTMax]))
                vMax = max(vMax, np.nanmax(vData[iTMin:iTMax]))
                self.axPrice.set_ylim([0.95*pMin, 1.05*pMax])
                if self.plotRPerc is True:
                    rMin = -self.rMax
                    rMax = self.rMax
                else:
                    rMin = -100.0*self.rMax
                    rMax = 100.0*self.rMax
                self.axReturn.set_ylim([rMin, rMax])
                self.axVolume.set_ylim([0.95*vMin, 1.05*vMax])
        self.axPrice.set_xticklabels('')
        self.axReturn.set_xticklabels('')
        self.axVolume.yaxis.set_major_locator(mt.MaxNLocator(nbins = 3, integer = True))
        for thisAx in self.ax:
            thisAx.set_xlim([self.tMin, self.tMax])

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
            if self.dTimeInterval == mp.threeMonths:
                self.axPrice.xaxis.set_major_locator(mdt.WeekdayLocator(byweekday = mdt.MO))
                self.axReturn.xaxis.set_major_locator(mdt.WeekdayLocator(byweekday = mdt.MO))
                self.axVolume.xaxis.set_major_locator(mdt.WeekdayLocator(byweekday = mdt.MO))
                self.axVolume.xaxis.set_major_formatter(mdt.DateFormatter('%d%b%y'))
                self.axPrice.xaxis.set_minor_locator(mdt.WeekdayLocator(byweekday = (mdt.MO, mdt.TU, mdt.WE, mdt.TH, mdt.FR)))
                self.axReturn.xaxis.set_minor_locator(mdt.WeekdayLocator(byweekday = (mdt.MO, mdt.TU, mdt.WE, mdt.TH, mdt.FR)))
                self.axVolume.xaxis.set_minor_locator(mdt.WeekdayLocator(byweekday = (mdt.MO, mdt.TU, mdt.WE, mdt.TH, mdt.FR)))
            
    def resetGraph(self):
        for thisAx in self.ax:
            thisAx.tick_params(axis='x', which='both', colors = sp.colorWindow)
            thisAx.tick_params(axis='y', which='both', colors = sp.colorWindow)

    def getTMinTmax(self, symbol):
        tMax = self.tMax
        self.tMin = mf.findLastWeekday(tMax - self.dTimeInterval)
        tMin = self.tMin
        if tMin < symbol.dDate.data[0]:
            iTMin = 0
        else:
            for thisDate in symbol.dDate.data:
                if thisDate < tMin:
                    pass
                else:
                    iTMin = symbol.dDate.data.index(thisDate)
                    break
        iTMax = len(symbol.dDate.data) - 1
        return iTMin, iTMax
