from bs4 import BeautifulSoup
import urllib2
#import urllib2
from urllib2 import Request, urlopen
import re
import numpy as np
from numpy import *
from scipy import stats
import datetime as dt
from datetime import datetime
import tweepy
import googlesearch
from googlesearch import search_news
import time
import warnings
from coin_returns import func_coinret
warnings.filterwarnings("ignore")

def func_top10():

    data_all = urllib2.urlopen('https://coinmarketcap.com/all/views/all/')
    soup_all = BeautifulSoup(data_all, 'html.parser')
    table_all = soup_all.find("table")
    rows_all = table_all.findAll('tr')
    data2_all = [[td.findChildren(text=True) for td in tr.findAll("td")] for tr in rows_all]
    data2_all = [[u"".join(d).strip() for d in l] for l in data2_all]

    coin = []
    for k in range(0,10):
        coin.append(k)
        coin[k] = data2_all[k+1][1].split('\n')[1].lower().replace(" ","-")

    today = dt.datetime.now().date().isoformat().replace('-',"")

    rrr = []
    for i in range(0,len(coin)):
        rrr.append(i)
        rrr[i] = func_coinret(coin[i])

    lengths = []
    for i in range(0,len(coin)):
        lengths.append(i)
        lengths[i] = len(rrr[i])
      
    benchmark_coin = coin[np.argmin(lengths)]
    benchmark_length = len(rrr[np.argmin(lengths)])

    for i in range(0,len(coin)):
        if i != np.argmin(lengths):
            rrr[i] = rrr[i][len(rrr[i])-benchmark_length:len(rrr[i])]

#   Top 10 coin weights = market cap of coin / market cap of all top 10 coins together
    weights = [0.46,0.227,0.091,0.079,0.040,0.026,0.023,0.022,0.017,0.015]
    #weights = [1.,1.,1.,1.,1.,1.,1.,1.,1.,1.]

    rav = []
    for i in range(0,len(rrr[np.argmin(lengths)])):
        rav.append(i)
        ravs = 0.
        for j in range(0,len(coin)):
            ravs = ravs + rrr[j][i] * weights[j]
            
        rav[i] = round(ravs/10.,2)

    r_top10 = rav
           
    return r_top10
