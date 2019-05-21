from bs4 import BeautifulSoup
import urllib3
import re
import requests
import os
from icobench import func_icobench
from icodrops import func_icodrops
from tokenmarket import func_tokenmarket
from icorating import func_icorating
from icomarks import func_icomarks
from icobazaar import func_icobazaar
from googletwitter import func_googletwitter
from region_category import func_region
from industry_category import func_industry
from scrap_icos_main_func import ico_data_collector
from bitcoin_returns import func_btc
from coin_returns import func_coinret
from top10_returns import func_top10
import time
import datetime as dt
from datetime import datetime
import warnings
import csv
from csv import *
import numpy as np
from numpy import *
import json
import sys
import subprocess
warnings.filterwarnings("ignore")

#1. ICOBENCH ICO/STO NAMES/TOKEN NAMES/WEBSITE TOKENS

data1 = []
dd = - 1

for page in range(1,399):
#for page in range(1,4):
    print('ICOBench',page)
    dd = dd + 1
    data1.append(dd)

    try:
        response = requests.get('https://icobench.com/icos?page='+str(page))
        txt = response.text
        soup_c = BeautifulSoup(txt, 'html.parser')
    except:
        txt = 'N/A'
        soup_c = 'N/A'

    values =  soup_c.findAll("td", {"class": "ico_data"})
    values_2 =  soup_c.findAll("a", {"class": "name notranslate"})


    name = []
    i = -1
    for tag in values:
        i = i + 1
        name.append(i)
        name[i] = ((tag.text.split("\n")[3]).lower()).replace(" ","").replace("(preico)","").replace("\xa0","")

    web = []
    l = -1
    k = -1
    for a in soup_c.find_all('a', href=True):
        if (('/ico/') in a['href']):
            l = l + 1
            if (l%2==0):
                k = k + 1
                web.append(k)
                web[k] = a['href'].replace('/ico/','')

    coin = []
    icobench_data = []
    for i in range(0,len(web)):
        try:
            response2 = requests.get('https://icobench.com/ico/'+web[i])
            txt2 = response2.text
            soup_d = BeautifulSoup(txt2, 'html.parser')
        except:
            txt2 = 'N/A'
            soup_d = 'N/A'

        coin.append(i)
        try:
            coin[i] = soup_d.title.string.split("(")[1].split(")")[0].lower()
        except:
            coin[i] = name[i]

        icobench_data.append(i)
        icobench_data[i] = [name[i].replace(" ",""),coin[i].replace(" ",""),web[i].replace(" ","")]

    data1[dd] = icobench_data

ii = -1
data1b = []
for i in range(0,page-1):
    for j in range(0,len(data1[0])):
        ii = ii + 1
        data1b.append(ii)
        data1b[ii] = data1[i][j]


#2. ICOMARKS ICO/STO NAMES/TOKEN NAMES/WEBSITE TOKENS

jj = 0
off = 0
txt4 = 'Empty'
ee = - 1
data2 = []

while txt4 != 'N/A':
#while jj < 3:
    print('ICOmarks',jj+1)
    jj = jj + 1
    off = off + jj*20

    ee = ee + 1
    data2.append(ee)
    
    with requests.Session() as session:
        try:
            response4 = session.post("https://icomarks.com/icos/ajax_more", data={'offset':off})
            txt4 = response4.text
            soup_d = BeautifulSoup(txt4, 'html.parser')
        except:
            txt4 = 'N/A'
            soup_d = 'N/A'

    name2 = []
    web2 = []
    i = -1
    for a in soup_d.find_all('a', href=True):
            if (('ico') in a['href']):
                i = i + 1
                name2.append(i)
                web2.append(i)
                web2[i] = str(a['href'].split("ico\/")[1].replace('\"',''))[0:len(str(a['href'].split("ico\/")[1].replace('\"','')))-1]
                name2[i] = web2[i].replace("-"," ")
                #print(name2[i],web2[i])

    coin2 = []
    icomarks_data = []
    for i in range(0,len(web2)):
        
        coin2.append(i)
        icomarks_data.append(i)
        
        try:
            response22 = requests.get('https://icomarks.com/ico/'+web2[i])
            txt22 = response22.text
            soup_d2 = BeautifulSoup(txt22, 'html.parser')
        except:
            txt22 = 'N/A'
            soup_d2 = 'N/A'

        coin2[i] = soup_d2.title.string.split("(")[1].split(")")[0].lower()

        icomarks_data.append(i)
        icomarks_data[i] = [name2[i].replace(" ",""),coin2[i].replace(" ",""),web2[i].replace(" ","")]

    data2[ee] = icomarks_data[0:20]

    if '"offset":false' in txt4:
        break

data2 = data2[:-1]

data2=np.asarray(data2)

iii = -1
data2b = []
for i in range(0,len(data2)):
    for j in range(0,len(data2[i])):
        iii = iii + 1
        data2b.append(iii)
        data2b[iii] = data2[i][j]

           
#iii = -1
#data2b = []
#for i in range(0,ee):
#    for j in range(0,len(data2[ee])):
#        iii = iii + 1
#        data2b.append(iii)
#        data2b[iii] = data2[i][j]


#3. ICORATING ICO/STO NAMES/TOKEN NAMES/WEBSITE TOKENS


page3 = 0
data3 = []
ff = -1

while 1:
#while page3 < 3:
    print('ICOrating',page3+1)
    page3 = page3 + 1

    ff = ff + 1
    data3.append(ff)
        
    try:
        response5 = requests.get('https://icorating.com/ico/all/load/?page='+str(page3))
        txt5 = response5.text
        soup_c5 = BeautifulSoup(txt5, 'html.parser')
    except:
        txt5 = 'N/A'
        soup_c5 = 'N/A'

    newDictionary=json.loads(str(soup_c5))

    name3 = []
    coin3 = []
    web3 = []
    icorating_data = []
    lengths = []
    
    for i in range(0,len(newDictionary['icos']['data'])):
        name3.append(i)
        coin3.append(i)
        web3.append(i)
        lengths.append(i)

        try:
            name3[i] = newDictionary['icos']['data'][i]['name'].lower()
        except:
            name3[i] = newDictionary['icos']['data'][i]['name']
        try:
            coin3[i] = newDictionary['icos']['data'][i]['ticker'].lower()
        except:
            coin3[i] = newDictionary['icos']['data'][i]['ticker']
        try:
            web3[i] = newDictionary['icos']['data'][i]['link'].lower().split("/ico/")[1].replace("/","")
        except:
            web3[i] = newDictionary['icos']['data'][i]['link'].split("/ico/")[1]

        icorating_data.append(i)
        icorating_data[i] = [str(name3[i]).replace(" ",""),str(coin3[i]).replace(" ",""),str(web3[i]).replace(" ","")]

    data3[ff] = icorating_data
    

    if '"data":[]' in txt5:
        break

data3 = data3[:-2]

data3=np.asarray(data3)

mmm = -1
data3b = []
for i in range(0,len(data3)):
    for j in range(0,len(data3[i])):
        mmm = mmm + 1
        data3b.append(mmm)
        data3b[mmm] = data3[i][j]

print('TEST concatenate',np.shape(data1b),np.shape(data2b),np.shape(data3b))

unlisted_icos0 = np.concatenate((data1b,data2b,data3b))

g = -1
unlisted_icos1 = []
for i in range(0,len(unlisted_icos0)):
    if ('') not in unlisted_icos0[i]:
        g = g + 1
        unlisted_icos1.append(g)
        unlisted_icos1[g] = unlisted_icos0[i]

#Removal of duplicate rows/entries
l = -1
unlisted_icos = []
for i in range(0,len(unlisted_icos1)):
    temp = unlisted_icos1[i][0]
    k = 0
    for j in range(i+1,len(unlisted_icos1)):
        if unlisted_icos1[j][0] == temp:
            k = k + 1

    if k == 0:
        l = l + 1
        unlisted_icos.append(l)
        unlisted_icos[l] = unlisted_icos1[i]

columnTitles = "name,coin,web\n"

with open('outdata/ico_unlisted.csv', 'w') as csvfile:
    csvfile.write(columnTitles)
    writer=csv.writer(csvfile, delimiter=',')

    for k in range(1,len(unlisted_icos)):
         writer.writerow([unlisted_icos[k][0],unlisted_icos[k][1],unlisted_icos[k][2]])

