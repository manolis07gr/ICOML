from bs4 import BeautifulSoup
import urllib3
import requests
import numpy as np
from numpy import *
from scipy import stats
import datetime as dt
from datetime import datetime
import time
import warnings
from coin_returns import func_coinret
warnings.filterwarnings("ignore")

def func_top10():

    response = requests.get('https://coinmarketcap.com/all/views/all/')
    txt = response.text
    soup_all = BeautifulSoup(txt, 'html.parser')

    
    table_all = soup_all.find("table")
    rows_all = table_all.findAll('tr')
    data2_all = [[td.findChildren(text=True) for td in tr.findAll("td")] for tr in rows_all]
    data2_all = [[u"".join(d).strip() for d in l] for l in data2_all]
    
    coin = []
    volume = []
    for k in range(0,10):
        coin.append(k)
        volume.append(k)
        coin[k] = data2_all[k+1][1].split('\n')[2].lower().replace(" ","-")
        volume[k] = float(eval(data2_all[k+1][3].replace("$","").replace(",","")))
        if coin[k] == 'xrp':
            coin[k] = 'ripple'

    top10_volume = sum(volume)
    volume_norm = []
    for k in range(0,10):
        volume_norm.append(k)
        volume_norm[k] = volume[k]/top10_volume

    today = dt.datetime.now().date().isoformat().replace('-',"")

    rrr = []
    for i in range(0,len(coin)):
        rrr.append(i)
        rrr[i] = func_coinret(coin[i])
        #print('COIN:',coin[i],volume[i],func_coinret(coin[i]))
        if rrr[i][0] == 'N/A':
            #print('HERE')
            rrr[i] = np.zeros(len(rrr[0]))


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
    weights = [volume_norm[0],volume_norm[1],volume_norm[2],volume_norm[3],volume_norm[4],volume_norm[5],volume_norm[6],volume_norm[7],volume_norm[8],volume_norm[9]]
    #print('WEIGHTS',weights)

    rav = []
    for i in range(0,len(rrr[np.argmin(lengths)])):
        rav.append(i)
        ravs = 0.
        for j in range(0,len(coin)):
            ravs = ravs + rrr[j][i] * weights[j]
            
        rav[i] = round(ravs/10.,3)

    r_top10 = rav
           
    return r_top10
