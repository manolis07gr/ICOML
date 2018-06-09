from PyQt5 import QtWidgets
import datetime as dt
import numpy as np
import pandas as pd
from urllib.request import urlopen
from bs4 import BeautifulSoup

import file_parameters as fp
import misc_functions as mf
from misc_parameters import rt, pc, bp, td, fw, tm, mDur
import all_coins as ac


class Symbol(object):

    def __init__(self, name, description):

        self.name        = name
        self.description = description

        self.downloadHistoricalData()
        nLines = mf.countLinesFile(fp.dirSymbolData + name + '.csv')

        self.dDate       = SymbolVariable(nLines, 'Date', 'Python format', date = True)
        self.pClose      = SymbolVariable(nLines, 'Close price', '\$', movAvg=True)
        self.pOpen       = SymbolVariable(nLines, 'Open price', '\$')
        self.pHigh       = SymbolVariable(nLines, 'High price', '\$')
        self.pLow        = SymbolVariable(nLines, 'Low price', '\$')
        self.nLogVol     = SymbolVariable(nLines, 'Logarithm of traded volume', 'log(#)')
        self.vLogVol     = SymbolVariable(nLines, 'Logarithm of traded volume', 'log(\$)')
        self.rClose      = []
        self.rClose.append(SymbolVariable(nLines, 'Return of close price', 'rate', movAvg = True))
        self.rClose.append(SymbolVariable(nLines, 'Return of close price', '%', movAvg = True))
        self.rClose.append(SymbolVariable(nLines, 'Return of close price', 'bp', movAvg = True))
        self.histVaR1    = []
        self.histVaR1.append(SymbolVariable(nLines, 'Historical value at risk 1%', 'rate'))
        self.histVaR1.append(SymbolVariable(nLines, 'Historical value at risk 1%', '%'))
        self.histVaR1.append(SymbolVariable(nLines, 'Historical value at risk 1%', 'bp'))
        self.histVaR5    = []
        self.histVaR5.append(SymbolVariable(nLines, 'Historical value at risk 5%', 'rate'))
        self.histVaR5.append(SymbolVariable(nLines, 'Historical value at risk 5%', '%'))
        self.histVaR5.append(SymbolVariable(nLines, 'Historical value at risk 5%', 'bp'))

        self.populateFields(nLines)
        self.calculateReturnMAvgVaR()

    def populateFields(self, nLines):
        df = pd.read_csv(fp.dirSymbolData + self.name + '.csv')
        for col in df.columns.tolist():
            df.rename(columns={col: col.replace('*', '')}, inplace=True)
        df['Date'] = df['Date'].map(lambda x: dt.datetime.strptime(x, '%b %d, %Y').date())
        self.dDate.data = df['Date'].tolist()
        self.pOpen.data = df['Open'].tolist()
        self.pHigh.data = df['High'].tolist()
        self.pLow.data = df['Low'].tolist()
        self.pClose.data = df['Close'].tolist()
        self.nLogVol.data = df['Volume'].map(lambda x: np.log10(int(x.replace(',', '').replace('-', '1')))).tolist()

        self.dDate.data   = self.dDate.data[::-1]
        self.pOpen.data   = self.pOpen.data[::-1]
        self.pHigh.data   = self.pHigh.data[::-1]
        self.pLow.data    = self.pLow.data[::-1]
        self.pClose.data  = self.pClose.data[::-1]
        self.nLogVol.data = self.nLogVol.data[::-1]
        self.vLogVol.data = np.add(np.log10(self.pClose.data), self.nLogVol.data)

    def calculateReturnMAvgVaR(self):
        for j in [rt, pc, bp]:
            self.rClose[j].data[0] = 0.0
        nData = len(self.pClose.data)
        for i in range(1, nData):
            self.rClose[rt].data[i] = (self.pClose.data[i] - self.pClose.data[i-1]) / self.pClose.data[i-1]
            self.rClose[pc].data[i] = self.rClose[rt].data[i]*100.0
            self.rClose[bp].data[i] = self.rClose[rt].data[i]*10000.0
        for k in [td, fw, tm]:
            QtWidgets.QApplication.processEvents()
            for i in range(0, nData):
                if i < mDur[k]-1:
                    self.pClose.mAvg[k].data[i] = np.nan
                    self.pClose.mStd[k].data[i] = np.nan
                    self.pClose.mAvg[k].data[i] = np.nan
                    self.pClose.mStd[k].data[i] = np.nan
                    for j in [rt, pc, bp]:
                        self.rClose[j].mAvg[k].data[i] = np.nan
                        self.rClose[j].mStd[k].data[i] = np.nan
                else:
                    self.pClose.mAvg[k].data[i] = np.mean(self.pClose.data[i-mDur[k]+1:i+1])
                    self.pClose.mStd[k].data[i] = np.std(self.pClose.data[i-mDur[k]+1:i+1])
                    self.pClose.mAvg[k].data[i] = np.mean(self.pClose.data[i-mDur[k]+1:i+1])
                    self.pClose.mStd[k].data[i] = np.std(self.pClose.data[i-mDur[k]+1:i+1])
                    self.rClose[rt].mAvg[k].data[i] = np.mean(self.rClose[rt].data[i-mDur[k]+1:i+1])
                    self.rClose[rt].mStd[k].data[i] = np.std(self.rClose[rt].data[i-mDur[k]+1:i+1])
                    self.rClose[pc].mAvg[k].data[i] = self.rClose[rt].mAvg[k].data[i]*100.0
                    self.rClose[pc].mStd[k].data[i] = self.rClose[rt].mStd[k].data[i]*100.0
                    self.rClose[bp].mAvg[k].data[i] = self.rClose[rt].mAvg[k].data[i]*10000.0
                    self.rClose[bp].mStd[k].data[i] = self.rClose[rt].mStd[k].data[i]*10000.0

        sortReturns = np.empty_like(self.rClose[rt].data)
        np.copyto(sortReturns, self.rClose[rt].data)
        sortReturns.sort()
        self.histVaR5[rt].data[0] = sortReturns[int(0.05*nData)]
        self.histVaR1[rt].data[0] = sortReturns[int(0.01*nData)]
        self.histVaR5[pc].data[0] = sortReturns[int(0.05*nData)]*100.0
        self.histVaR1[pc].data[0] = sortReturns[int(0.01*nData)]*100.0
        self.histVaR5[bp].data[0] = sortReturns[int(0.05*nData)]*10000.0
        self.histVaR1[bp].data[0] = sortReturns[int(0.01*nData)]*10000.0
        for i in range(1, nData):
            QtWidgets.QApplication.processEvents()
            sortReturns = np.empty_like(self.rClose[rt].data[nData-1:i-1:-1])
            np.copyto(sortReturns, self.rClose[rt].data[nData-1:i-1:-1])
            sortReturns.sort()
            nRet = len(sortReturns)
            self.histVaR5[rt].data[i] = sortReturns[int(0.05*nRet)]
            self.histVaR1[rt].data[i] = sortReturns[int(0.01*nRet)]
            self.histVaR5[pc].data[i] = sortReturns[int(0.05*nRet)]*100.0
            self.histVaR1[pc].data[i] = sortReturns[int(0.01*nRet)]*100.0
            self.histVaR5[bp].data[i] = sortReturns[int(0.05*nRet)]*10000.0
            self.histVaR1[bp].data[i] = sortReturns[int(0.01*nRet)]*10000.0


    def downloadHistoricalData(self):
        today = dt.datetime.now().date().isoformat().replace('-', '')
        try:
            html = urlopen('https://coinmarketcap.com/currencies/' + self.description.lower().replace(' ', '-')
                           + '/historical-data/?start=20130428&end=' + today)
            soup = BeautifulSoup(html, 'html.parser')

            cols = []
            tr = soup.find('tr')
            ths = tr.findAll('th')
            for th in ths:
                cols.append(th.text.strip())

            df = pd.DataFrame(columns=cols)

            trs = soup.findAll('tr')
            for i_row, tr in enumerate(trs):
                tds = tr.findAll('td')
                for td, col in zip(tds, cols):
                    if col == 'Name':
                        df.at[i_row, col] = td.text.strip().split('\n')[1]
                    else:
                        df.at[i_row, col] = td.text.strip().split('\n')[0]
            df.to_csv(fp.dirSymbolData + self.name + '.csv', index=False)
        except:
            mf.errorMessage('Error: Unable to connect to coinmarketcap.com to download data for ' + self.name + '.\n')
            #mf.quitApp()


class SymbolVariable(object):
    def __init__(self, nLines, description, unit, movAvg = False, date = False):
        if date is False:
            self.data = np.zeros(nLines)
        else:
            self.data = nLines*[None]
        self.name = description
        self.unit = unit
        if movAvg is True:
            self.mAvg = []
            self.mStd = []
            for i in range(0, 3):
                self.mAvg.append([])
                self.mStd.append([])
                self.mAvg[i] = MovingStat(nLines)
                self.mStd[i] = MovingStat(nLines)


class MovingStat(object):
    def __init__(self, nLines):
        self.data = np.zeros(nLines)


class SymbolListAll(object):
    def __init__(self):
        self.name        = []
        self.description = []
        ac.FullCoinList()
        self.readSymbolListAll()

    def readSymbolListAll(self):
        df = pd.read_csv(fp.fileSymbolListAll)
        self.name = df['Symbol'].tolist()
        self.description = df['Name'].tolist()
