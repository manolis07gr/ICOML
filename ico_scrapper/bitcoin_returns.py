from bs4 import BeautifulSoup
import urllib3
import requests
import numpy as np
from numpy import *
import datetime as dt
from datetime import datetime
import time
import warnings
warnings.filterwarnings("ignore")

def func_btc():

    today = dt.datetime.now().date().isoformat().replace('-',"")
    
    try:
        response = requests.get('https://coinmarketcap.com/currencies/bitcoin/historical-data/?start=20130428&end='+today)
        txt = response.text
        soup = BeautifulSoup(txt, 'html.parser')

        table = soup.find("table")
        rows = table.findAll('tr')
        data2 = [[td.findChildren(text=True) for td in tr.findAll("td")] for tr in rows]
        data2 = [[u"".join(d).strip() for d in l] for l in data2]

        o = []
        c = []
        j = -1
        for i in range(1,len(data2)):
            j = j + 1

            o.append(j)
            c.append(j)


            o[j] = eval(data2[i][1])
            c[j] = eval(data2[i][4])

        [o,c] = [o[::-1],c[::-1]]

        #Calculated daily returns array

        r = [round((c[0]-o[0])/o[0],3),]
        for i in range(1,len(c)):
            r.append(i)
            r[i] = round((c[i]-c[i-1])/c[i-1],3)

        r_btc = r[0:len(r)-1]

    except:
        r_btc = ['N/A']

    return r_btc
