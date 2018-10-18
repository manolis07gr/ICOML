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
warnings.filterwarnings("ignore")

#First the Coinmarketcap database of listed coins is scanned and the input data (coin name, symbol, weblink) extracted
response = requests.get('https://coinmarketcap.com/all/views/all/')
txt = response.text
soup = BeautifulSoup(txt, 'html.parser')
table_all = soup.find("table")
rows_all = table_all.findAll('tr')
data2_all = [[td.findChildren(text=True) for td in tr.findAll("td")] for tr in rows_all]
data2_all = [[u"".join(d).strip() for d in l] for l in data2_all]

symbol = []
coin = []
weblink = []
crypto_data = []
k = -1
for i in range(1,len(data2_all)):
    k = k + 1
    symbol.append(k)
    coin.append(k)
    weblink.append(k)
    crypto_data.append(k)

    symbol[k] = data2_all[i][1].split('\n')[0].lower().replace(" ","-")
    coin[k] = data2_all[i][1].split('\n')[2].lower().replace(" ","-")

    try:
        l = -1
        for a in rows_all[i].find_all('a', href=True):
            l = l + 1
            if l == 0:
                weblink[k] = (str(a).split('href="/currencies/')[1].split('/')[0]).lower()
    
    except:
        weblink[k] = coin[k]

    crypto_data[k] = [coin[k],symbol[k],weblink[k]]
    

#Second, the Coindesk data is extracted for failed ICOs
with open("coindesk_data.csv") as f1:
    reader = csv.reader(f1)
    cd_data = [r for r in reader]
    
cd_coin = []
cd_end = []
cd_end2 = []
cd_coin_symbol = []
cd_coin_weblink = []
cd_crypto_data = []
j = -1
for i in range(0,np.shape(cd_data)[0]):
    if i != 0:
        j = j + 1
        cd_coin.append(j)
        cd_end.append(j)
        cd_end2.append(j)
        cd_coin_symbol.append(j)
        cd_coin_weblink.append(j)
        cd_crypto_data.append(j)
        
        cd_coin[j] = cd_data[i][0].lower().replace(" ","-")
        cd_end[j] = str(cd_data[i][1]).replace("/"," ")
        cd_end2[j] = datetime.strptime(cd_end[j], '%m %d %Y')
        cd_end2[j] = cd_end2[j].strftime('%d %b %Y')
        cd_coin_symbol[j] = cd_coin[j]
        cd_coin_weblink[j] = cd_coin[j]

        cd_crypto_data[j] = [cd_coin[j],cd_coin_symbol[j],cd_coin_weblink[j]]

#Join Coinmarketcap and Coidesk data into unique array
crypto_data = np.concatenate((crypto_data, cd_crypto_data))

#Call rt10 and r_bitcoin only ONCE
bitcoin = func_btc()
top10s = func_top10()

#First formatting of two output datasets (full and reduced with ratings)
full_data = []
target_data = []
j = -1
for i in range(0,len(crypto_data)):
    #Filter out data with 'N/A' end date entries
    if ico_data_collector(crypto_data[i],bitcoin,top10s)[1][2] != 'N/A':
        j = j + 1
        full_data.append(j)
        target_data.append(j)
        full_data[j] = ico_data_collector(crypto_data[i],bitcoin,top10s)[0]
        target_data[j] = ico_data_collector(crypto_data[i],bitcoin,top10s)[1]
        ##print('BEFORE',j,target_data[j])

"""
f = open('dataset_restart2',"r")
i = -1
[name,sd,ed,dur,age,reg,indus,team,raised,hardcap,success,price,teleg,goog,twit,hype,risk,bazaar,ret1,vol1,s1,s3,syr,syr2,bbtc,b10,abtc,a10]=[[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
target_data = []
for line in f:
    i = i + 1
    (name.append(i),sd.append(i),ed.append(i),dur.append(i),age.append(i))
    (reg.append(i),indus.append(i),team.append(i),raised.append(i),hardcap.append(i),success.append(i),price.append(i),teleg.append(i),goog.append(i))
    (twit.append(i),hype.append(i),risk.append(i),bazaar.append(i))
    (ret1.append(i),vol1.append(i),s1.append(i),s3.append(i),syr.append(i),syr2.append(i),bbtc.append(i),b10.append(i),abtc.append(i),a10.append(i))
    target_data.append(i)

    name[i] = line.split('\n')[0].split(",")[0].replace("'","")
    sd[i] =  line.split('\n')[0].split(",")[1].replace("'","")
    ed[i] =  line.split('\n')[0].split(",")[2].replace("'","")
    
    try:
        dur[i] = eval(line.split('\n')[0].split(",")[3])
    except:
        dur[i] = 'N/A'
    try:
        age[i] = eval(line.split('\n')[0].split(",")[4])
    except:
        age[i] = 'N/A'
    try:
        reg[i] = int(eval(line.split('\n')[0].split(",")[5]))
    except:
        reg[i] = 'N/A'
        
    indus[i] = line.split('\n')[0].split(",")[6].replace("'","")
    
    try:
        team[i] = int(eval(line.split('\n')[0].split(",")[7]))
    except:
        team[i] = 'N/A'
    try:
        raised[i] = eval(line.split('\n')[0].split(",")[8])
    except:
        raised[i] = 'N/A'
    try:
        hardcap[i] = eval(line.split('\n')[0].split(",")[9])
    except:
        hardcap[i] = 'N/A'
    try:
        success[i] = eval(line.split('\n')[0].split(",")[10])
    except:
        success[i] = 'N/A'
    try:
        price[i] = eval(line.split('\n')[0].split(",")[11])
    except:
        price[i] = 'N/A'
    try:
        teleg[i] = int(eval(line.split('\n')[0].split(",")[12]))
    except:
        teleg[i] = 'N/A'
    try:
        goog[i] = int(eval(line.split('\n')[0].split(",")[13]))
    except:
        goog[i] = 'N/A'
    try:
        twit[i] = int(eval(line.split('\n')[0].split(",")[14]))
    except:
        twit[i] = 'N/A'
        
    hype[i] = line.split('\n')[0].split(",")[15].replace("'","")
    risk[i] = line.split('\n')[0].split(",")[16].replace("'","")

    try:
        bazaar[i] = eval(line.split('\n')[0].split(",")[17])
    except:
        bazaar[i] = 'N/A'        
    try:
        ret1[i] = eval(line.split('\n')[0].split(",")[18])
    except:
        ret1[i] = 'N/A'
    try:
        vol1[i] = eval(line.split('\n')[0].split(",")[19])
    except:
        vol1[i] = 'N/A'
    try:
        s1[i] = eval(line.split('\n')[0].split(",")[20])
    except:
        s1[i] = 'N/A'
    try:
        s3[i] = eval(line.split('\n')[0].split(",")[21])
    except:
        s3[i] = 'N/A'
    try:
        syr[i] = eval(line.split('\n')[0].split(",")[22])
    except:
        syr[i] = 'N/A'
    try:
        syr2[i] = eval(line.split('\n')[0].split(",")[23])
    except:
        syr2[i] = 'N/A'
    try:
        bbtc[i] = eval(line.split('\n')[0].split(",")[24])
    except:
        bbtc[i] = 'N/A'
    try:
        b10[i] = eval(line.split('\n')[0].split(",")[25])
    except:
        b10[i] = 'N/A'
    try:
        abtc[i] = eval(line.split('\n')[0].split(",")[26])
    except:
        abtc[i] = 'N/A'
    try:
        a10[i] = eval(line.split('\n')[0].split(",")[27])
    except:
        a10[i] = 'N/A'
        
    target_data[i] = [name[i],sd[i],ed[i],dur[i],age[i],reg[i],indus[i],team[i],raised[i],hardcap[i],success[i],price[i],teleg[i],goog[i],twit[i],hype[i],risk[i],bazaar[i],ret1[i],vol1[i],s1[i],s3[i],syr[i],syr2[i],bbtc[i],b10[i],abtc[i],a10[i]]

"""
#Restore Google News numbers from previous scan

with open("outdata2/ico_google_new.csv") as f2:
    reader = csv.reader(f2)
    google_data = [r2 for r2 in reader]

coin_g = []
news_g = []
j = -1
for i in range(0,len(google_data)):
    if i != 0:
        j = j + 1
        coin_g.append(j)
        news_g.append(j)
    
        coin_g[j] = google_data[i][0].lower().replace(" ","-")
        news_g[j] = google_data[i][1]
        
        for k in range(0,len(target_data)):
            if target_data[k][0] == coin_g[j]:
                target_data[k][13] = news_g[j]

#Removal of duplicate rows/entries
l = -1
target_data2 = []
for i in range(0,len(target_data)):
    temp = target_data[i][0]
    k = 0
    for j in range(i+1,len(target_data)):
        if target_data[j][0] == temp:
            k = k + 1

    if k == 0:
        l = l + 1
        target_data2.append(l)
        target_data2[l] = target_data[i]

target_data = target_data2

l = -1
full_data2 = []
for i in range(0,len(full_data)):
    temp = full_data[i][0]
    k = 0
    for j in range(i+1,len(full_data)):
        if full_data[j][0] == temp:
            k = k + 1

    if k == 0:
        l = l + 1
        full_data2.append(l)
        full_data2[l] = full_data[i]

full_data = full_data2

with open('ico_data_full.txt', 'w') as f:
    for k in range(0,len(full_data)):
        print(full_data[k], file=f) 

columnTitles = "coin,start,end,duration,age,region,industry,team,raised,hardcap,success,price,telegram,N_google_news,N_twitter,hype,risk,bazaar-rate,ret_ico_to_day_one,vol_day1,sharpe_1,sharpe_3,sharpe_yr,sharpe_yr2,beta_btc,beta_top10,alpha_btc,alpha_top10\n"

with open('outdata/ico_data_reduced.csv', 'w') as csvfile:
    csvfile.write(columnTitles)
    writer=csv.writer(csvfile, delimiter=',')

    for k in range(0,len(target_data)):   
        currency = target_data[k][0]
        start = target_data[k][1] 
        end = target_data[k][2]
        duration = target_data[k][3]
        age = target_data[k][4]
        region = target_data[k][5]
        industry = target_data[k][6]
        team = target_data[k][7]
        raised = target_data[k][8]
        hardcap = target_data[k][9]
        success = target_data[k][10]
        price = target_data[k][11]
        telegram = target_data[k][12]
        N_google_news = target_data[k][13]
        N_twitter = target_data[k][14]
        hype = target_data[k][15]
        risk = target_data[k][16]
        bazaar = target_data[k][17]
        ret_icoday1 = target_data[k][18]
        vol_day1 = target_data[k][19]
        sharpe_1 = target_data[k][20]
        sharpe_3 = target_data[k][21]
        sharpe_yr = target_data[k][22]
        sharpe_yr2 = target_data[k][23]
        beta_btc = target_data[k][24]
        beta_top10 = target_data[k][25]
        alpha_btc = target_data[k][26]
        alpha_top10 = target_data[k][27]
    
        writer.writerow([currency,start,end,duration,age,region,industry,team,raised,hardcap,success,price,telegram,N_google_news,N_twitter,hype,risk,bazaar,ret_icoday1,vol_day1,sharpe_1,sharpe_3,sharpe_yr,sharpe_yr2,beta_btc,beta_top10,alpha_btc,alpha_top10])

#Open csv file from within code
os.system('open outdata/ico_data_reduced.csv')

today_day = dt.datetime.now().date().isoformat().replace('-',"")

with open("outdata/ico_data_reduced.csv") as f2:
    reader = csv.reader(f2)
    data = [r for r in reader]
        
[sd,sm,sy,ed,em,ey,name,google_prev]=[[],[],[],[],[],[],[],[]]
j = -1
for i in range(1,np.shape(data)[0]):
    [sd.append(j),sm.append(j),sy.append(j),ed.append(j),em.append(j),ey.append(j),name.append(j),google_prev.append(j)]
    name[j] = data[i][0]
    google_prev[j] = data[i][13]
    if google_prev[j] == 'N/A':
        try:
            sd[j] = str(datetime.strptime(data[i][1], '%d %b %Y').day)
            sm[j] = str(datetime.strptime(data[i][1], '%d %b %Y').month)
            sy[j] = str(datetime.strptime(data[i][1], '%d %b %Y').year)
        except:
            sd[j] = str(1)
            sm[j] = str(1)
            sy[j] = str(2015)

        try:
            ed[j] = str(datetime.strptime(data[i][2], '%d %b %Y').day)
            em[j] = str(datetime.strptime(data[i][2], '%d %b %Y').month)
            ey[j] = str(datetime.strptime(data[i][2], '%d %b %Y').year)
        except:
            ed[j] = str(datetime.strptime(today_day, '%Y%m%d').day)
            em[j] = str(datetime.strptime(today_day, '%Y%m%d').month)
            ey[j] = str(datetime.strptime(today_day, '%Y%m%d').year)
				
        start_day = sd[j]
        start_month = sm[j]
        start_year = sy[j]
        end_day = ed[j]
        end_month = em[j]
        end_year = ey[j]
        key = name[j]
				
        os.system('open "https://www.google.com/search?q=%22'+key+'+ICO%22&client=safari&rls=en&biw=1662&bih=920&source=lnt&tbs=cdr%3A1%2Ccd_min%3A'+start_month+'%2F'+start_day+'%2F'+start_year+'%2Ccd_max%3A'+end_month+'%2F'+end_day+'%2F'+end_year+'&tbm=nws"')

# Pause before next step

wait = input("PRESS ENTER TO CONTINUE.")

# Update Google News File after user inputs new values in place of N/As
# User will input data and save the *csv FORMAT using the same name in the outdata Directory!

with open("outdata/ico_data_reduced.csv") as f3:
    reader3 = csv.reader(f3)
    data3 = [r for r in reader3]
    goog_new = []
    for k in range(0,len(target_data)):
        goog_new.append(k)
        goog_new[k] = data3[k][13]

columnTitles_goog = "coin,N_google_news\n"

with open('outdata/ico_google_new.csv', 'w') as csvfile_goog:
    csvfile_goog.write(columnTitles_goog)
    writer=csv.writer(csvfile_goog, delimiter=',')

    for k in range(1,len(target_data)):
         writer.writerow([target_data[k][0],goog_new[k]])

os.system('cp outdata/ico_google_new.csv outdata2/')
         
#Now the Google News File is updated

#Next step is to remove N/A crypto coin performance entries from the reduced file

columnTitles_renew = "coin,start,end,duration,age,region,industry,team,raised,hardcap,success,price,telegram,N_google_news,N_twitter,hype,risk,bazaar-rate,ret_ico_to_day_one,vol_day1,sharpe_1,sharpe_3,sharpe_yr,sharpe_yr2,beta_btc,beta_top10,alpha_btc,alpha_top10\n"

with open('outdata/ico_data_reduced2.csv', 'w') as csvfile_renew:
    csvfile_renew.write(columnTitles_renew)
    writer=csv.writer(csvfile_renew, delimiter=',')

    for i in range(1,len(target_data)):
        if (target_data[i][18] == 'N/A') or (target_data[i][18] == 'nan') or (target_data[i][18] == 'inf') :
            (target_data[i][18],target_data[i][19],target_data[i][20],target_data[i][21],target_data[i][22],target_data[i][23],target_data[i][24],target_data[i][25],target_data[i][26],target_data[i][27]) = (-1.0,0.0,-100.,-100.,-100.,-100,-100.,-100.,-100.,-100.)

        writer.writerow([target_data[i][0],target_data[i][1],target_data[i][2],target_data[i][3],target_data[i][4],target_data[i][5],target_data[i][6],target_data[i][7],target_data[i][8],target_data[i][9],target_data[i][10],target_data[i][11],target_data[i][12],target_data[i][13],target_data[i][14],target_data[i][15],target_data[i][16],target_data[i][17],target_data[i][18],target_data[i][19],target_data[i][20],target_data[i][21],target_data[i][22],target_data[i][23],target_data[i][24],target_data[i][25],target_data[i][26],target_data[i][27]])
        continue

os.system('mv outdata/ico_data_reduced2.csv outdata/ico_data_reduced.csv')        

#Final step is to produce the "complete" reduced database with no N/A entries at all.


columnTitles_complete = "coin,start,end,duration,age,region,industry,team,raised,hardcap,success,price,telegram,N_google_news,N_twitter,hype,risk,bazaar-rate,ret_ico_to_day_one,vol_day1,sharpe_1,sharpe_3,sharpe_yr,sharpe_yr2,beta_btc,beta_top10,alpha_btc,alpha_top10\n"

with open('outdata/ico_data_complete.csv', 'w') as csvfile_b:
    csvfile_b.write(columnTitles_complete)
    writer=csv.writer(csvfile_b, delimiter=',')

    for i in range(0,len(target_data)):
        if 'N/A' not in target_data[i]:
            all_data = [target_data[i][0],target_data[i][1],target_data[i][2],target_data[i][3],target_data[i][4],target_data[i][5],target_data[i][6],target_data[i][7],target_data[i][8],target_data[i][9],target_data[i][10],target_data[i][11],target_data[i][12],target_data[i][13],target_data[i][14],target_data[i][15],target_data[i][16],target_data[i][17],target_data[i][18],target_data[i][19],target_data[i][20],target_data[i][21],target_data[i][22],target_data[i][23],target_data[i][24],target_data[i][25],target_data[i][26],target_data[i][27]]
            writer.writerow(all_data)

os.system('cp outdata/* outdata2/') 
