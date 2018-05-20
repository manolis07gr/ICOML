from bs4 import BeautifulSoup
#import urllib2
from urllib2 import Request, urlopen
import urllib2
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
import csv
from csv import *
from collections import Counter
from icobench import func_icobench
from icodrops import func_icodrops
from tokenmarket import func_tokenmarket
from icorating import func_icorating
from icomarks import func_icomarks
from googletwitter import func_googletwitter
from bitcoin_returns import func_btc
from coin_returns import func_coinret
from top10_returns import func_top10
from region_category import func_region
from industry_category import func_industry
warnings.filterwarnings("ignore")

###
data_all = urllib2.urlopen('https://coinmarketcap.com/all/views/all/')
soup_all = BeautifulSoup(data_all, 'html.parser')
table_all = soup_all.find("table")
rows_all = table_all.findAll('tr')
data2_all = [[td.findChildren(text=True) for td in tr.findAll("td")] for tr in rows_all]
data2_all = [[u"".join(d).strip() for d in l] for l in data2_all]

symbol = []
coin = []
k = -1
for i in range(1,len(data2_all)):
    k = k + 1
    symbol.append(k)
    coin.append(k)

    symbol[k] = data2_all[i][1].split('\n')[0]
    coin[k] = data2_all[i][1].split('\n')[1].lower()

with open("coindesk_data.csv") as f:
    reader = csv.reader(f)
    data = [r for r in reader]

coin2 = []
cd_end2 = []
coin3 = []
cd_end3 = []
j = -1
for i in range(0,np.shape(data)[0]):
    coin2.append(i)
    cd_end2.append(i)
    coin2[i] = data[i][0].lower().replace(" ","")
    cd_end2[i] = data[i][1]
    if coin2[i] not in coin:
        j = j + 1
        coin3.append(j)
        cd_end3.append(j)
        coin3[j] = coin2[i]
        cd_end3[j] = cd_end2[i]
    
coin3 = coin3[1:len(coin3)]
cd_end3 = cd_end3[1:len(cd_end3)]

for i in range(0,len(cd_end3)):
    cd_end3[i] = datetime.strptime(cd_end3[i], '%m/%d/%Y')
    cd_end3[i] = cd_end3[i].strftime('%d %b %Y')

with open('outdata/coindesk_na_data.csv', 'w') as csvfile_c:
    writer=csv.writer(csvfile_c, delimiter=',')

    for i in range(0,len(coin3)):
        writer.writerow([coin3[i],'N/A',cd_end3[i],'N/A','N/A','N/A','N/A','N/A','N/A','N/A','N/A','N/A','N/A','N/A','N/A',-1.0,0.0,-100.,-100.,-100.,-100,-100.,-100.,-100.,-100.])

with open('outdata/coindesk_na_wr_data.csv', 'w') as csvfile_d:
    writer=csv.writer(csvfile_d, delimiter=',')

    for i in range(0,len(coin3)):
        writer.writerow([coin3[i],'N/A',cd_end3[i],'N/A','N/A','N/A','N/A','N/A','N/A','N/A','N/A','N/A','N/A','N/A','N/A','N/A','N/A',-1.0,0.0,-100.,-100.,-100.,-100,-100.,-100.,-100.,-100.])
