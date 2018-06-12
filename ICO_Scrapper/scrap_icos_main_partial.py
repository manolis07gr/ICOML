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

with open('nan_coins2.txt', 'r') as myfile:
    data111=myfile.read().split('\n')

data111 = data111[0:len(data111)-1]

data222 = []
k = -1
for i in range(0,len(data111)):
    for j in range(0,len(coin)):
        if data111[i] == coin[j]:
            k = k + 1
            data222.append(k)
            data222[k] = symbol[j]

#Lines below need to be enabled only for tokens with different link names
data111 = ['nebulas','ambrosus','crypto20','decentbet','bloom','medicalchain','cofound.it','matchpool','agrello','locktrip','friendz','wetrust','spectiv','eboost','bitjob','escroco','peerguess']
data222 = ['nas','amb','c20','dbet','blt','mtn','cfi','gup','dlt','loc','fdz','trst','sig','ebst','stu','esc','guess']
data333 = ['nebulas-token','amber','c20','decent-bet','bloomtoken','medical-chain','cofound-it','guppy','agrello-delta','lockchain','friends','trust','signal-token','eboostcoin','student-coin','escoro','guess']
    
#Bitcoin returns
rbtc = func_btc() 
#Average returns of Top 10 coins
rt10 = func_top10()

today = dt.datetime.now().date().isoformat().replace('-',"")

columnTitles = "coin,start1,end1,duration1,age1,start3,end3,duration3,age3,start4,end4,duration4,age4,start5,end5,duration5,age5,country1,country2,country3,country5,industry1,industry2,industry4,team1,team2,team3,team4,team5,raised1,raised2,raised4,raised5,hardcap1,hardcap2,hardcap4,hardcap5,success1,success2,success4,price1,price2,price4,price5,telegram1,telegram2,telegram4,N_google_news,N_twitter,hype4,risk4,ret_day1,vol_day1,sharpe_1,sharpe_3,sharpe_yr,sharpe_yr2,beta_btc,beta_top10,alpha_btc,alpha_top10\n"

columnTitles2 = "coin,start,end,duration,age,region,industry,team,raised,hardcap,success,price,telegram,N_google_news,N_twitter,ret_ico_to_day_one,vol_day1,sharpe_1,sharpe_3,sharpe_yr,sharpe_yr2,beta_btc,beta_top10,alpha_btc,alpha_top10\n"

columnTitles3 = "coin,start,end,duration,age,region,industry,team,raised,hardcap,success,price,telegram,N_google_news,N_twitter,hype,risk,ret_ico_to_day_one,vol_day1,sharpe_1,sharpe_3,sharpe_yr,sharpe_yr2,beta_btc,beta_top10,alpha_btc,alpha_top10\n"

with open('outdata/ico_data_full_nans2.csv', 'w') as csvfile1, open('outdata/ico_data_reduced_nans2.csv', 'w') as csvfile2, open('outdata/ico_data_reduced_wratings_nans2.csv', 'w') as csvfile3:
    csvfile1.write(columnTitles)
    writer=csv.writer(csvfile1, delimiter=',')
    csvfile2.write(columnTitles2)
    writer2=csv.writer(csvfile2, delimiter=',')
    csvfile3.write(columnTitles3)
    writer3=csv.writer(csvfile3, delimiter=',')

    for i in range(0,len(coin)):
        currency = data111[i].replace(' ','-')
        token = data222[i]
        #link_web = currency
        link_web = data333[i]

        try:
            data = urllib2.urlopen('https://coinmarketcap.com/currencies/'+link_web+'/historical-data/?start=20130428&end='+today)
            soup = BeautifulSoup(data, 'html.parser')

            table = soup.find("table")
            rows = table.findAll('tr')
            data2 = [[td.findChildren(text=True) for td in tr.findAll("td")] for tr in rows]
            data2 = [[u"".join(d).strip() for d in l] for l in data2]

            date = []
            o = []
            h = []
            l = []
            c = []
            vol = []
            mc =[]
            j = -1
            for i in range(1,len(data2)):
                j = j + 1

                date.append(j)
                o.append(j)
                h.append(j)
                l.append(j)
                c.append(j)
                vol.append(j)
                mc.append(j)

                date[j] = data2[i][0]
                o[j] = eval(data2[i][1])
                h[j] = eval(data2[i][2])
                l[j] = eval(data2[i][3])
                c[j] = eval(data2[i][4])
                vol[j] = eval(data2[i][5].replace(",","").replace("-","0.0"))
                mc[j] = eval((data2[i][6].replace(",","")).replace("-","0.0"))

            [date,o,h,l,c,vol,mc] = [date[::-1],o[::-1],h[::-1],l[::-1],c[::-1],vol[::-1],mc[::-1]]

            #Calculated daily returns array

            r = [round((c[0]-o[0])/o[0],2),]
            for i in range(1,len(c)):
                r.append(i)
                r[i] = round((c[i]-c[i-1])/c[i-1],2)

            #Calculate average returns and standard deviation of average returns
            r_av = np.mean(r)
            r_std = np.std(r)

            #Calculate 1-month, 3-month and annualized Sharpe ratios
            wd_month = 21
            wd_month3 = 3 * wd_month
            wd_annual = 252

            if len(c) < wd_month:
                s_1 = round(r_av*wd_month/(r_std*np.sqrt(wd_month)),2)
            if len(c) >= wd_month:
                r_av = np.mean(r[0:wd_month])
                r_std = np.std(r[0:wd_month])
                s_1 = round(r_av/r_std,2)

            if len(c) < wd_month3:
                s_3 = round(r_av*wd_month3/(r_std*np.sqrt(wd_month3)),2)
            if len(c) >= wd_month3:
                r_av = np.mean(r[0:wd_month3])
                r_std = np.std(r[0:wd_month3])
                s_3 = round(r_av/r_std,2)

            s_annual =  round(r_av*wd_annual/(r_std*np.sqrt(wd_annual)),2)
            rav10 = np.mean(rt10)
            rstd10 = np.std(rt10)
            s_annual2 = round((r_av-rav10)*wd_annual/(r_std*np.sqrt(wd_annual)),2)

            #Calculation of coin beta based on BTC daily returns (~1/3 of market dominance)
            displacement = len(rbtc)-len(r)
            rbtc_2 = rbtc[displacement:len(rbtc)]
            beta_btc = round(stats.linregress(rbtc_2,r)[0],3)
            alpha_btc = round(stats.linregress(rbtc_2,r)[1],3)


            #Calculation of coin beta based on mean return of top 10 coins on coinmarketcap.com (~80% of cumulative market dominance)
            if len(rt10) > len(r):
                displacement2 = len(rt10)-len(r)
                rt10 = rt10[displacement2:len(rt10)]
                beta_top10 = round(stats.linregress(rt10,r)[0],3)
                alpha_top10 = round(stats.linregress(rt10,r)[1],3)

            if len(rt10) <= len(r):
                displacement2 = len(r)-len(rt10)
                r = r[displacement2:len(r)]
                beta_top10 = round(stats.linregress(rt10,r)[0],3)
                alpha_top10 = round(stats.linregress(rt10,r)[1],3)


        except:
            c = ['N/A']
            vol = ['N/A']
            [s_1,s_3,s_annual,s_annual2] = ['N/A','N/A','N/A','N/A']
            [beta_btc,beta_top10,alpha_btc,alpha_top10] = ['N/A','N/A','N/A','N/A']


        res = func_icobench(currency)
        res2 = func_icodrops(currency)
        res3 = func_tokenmarket(currency)
        res4 = func_icorating(currency,token)
        res5 = func_icomarks(currency)
        res6 = func_googletwitter(currency)

        [start1,end1,duration1,country1,industry1,team1,raised1,hardcap1,success1,price1,telegram1]=[res[1],res[2],res[3],res[4],res[5],res[6],res[7],res[8],res[9],res[10],res[11]]
        [country2,industry2,team2,raised2,hardcap2,success2,price2,telegram2]=[res2[1],res2[2],res2[3],res2[4],res2[5],res2[6],res2[7],res2[8]]
        [start3,end3,duration3,country3,team3]=[res3[1],res3[2],res3[3],res3[4],res3[5]]
        try:
            [start4,end4,duration4,industry4,team4,raised4,hardcap4,success4,price4,telegram4,hype4,risk4]=[res4[1],res4[2],res4[3],res4[4],res4[5],res4[6],res4[7],res4[8],res4[9],res4[10],res4[11]/100.,res4[12]/100.]
        except:
            [start4,end4,duration4,industry4,team4,raised4,hardcap4,success4,price4,telegram4,hype4,risk4]=[res4[1],res4[2],res4[3],res4[4],res4[5],res4[6],res4[7],res4[8],res4[9],res4[10],'N/A','N/A']
        [start5,end5,duration5,country5,team5,raised5,hardcap5,price5]=[res5[1],res5[2],res5[3],res5[4],res5[5],res5[6],res5[7],res5[8]]
        [N_google_news,N_twitter]=[res6[2],res6[1]]

        try:
            ret_day1a = round(c[0],2)
        except:
            ret_day1a = 'N/A'

        [ret_day1,vol_day1,sharpe_1,sharpe_3,sharpe_yr,sharpe_yr2,beta_btc,beta_top10,alpha_btc,alpha_top10]=[ret_day1a,vol[0],s_1,s_3,s_annual,s_annual2,beta_btc,beta_top10,alpha_btc,alpha_top10]

        #Calculation of age since last day of ICO
        today_a = datetime.strptime(today, '%Y%m%d')
        try:
            age1 = today_a - datetime.strptime(end1, '%d %b %Y')
            age1 = round(age1.total_seconds()/86400.,1)
        except:
            age1 = 'N/A'
        try:
            age3 = today_a - datetime.strptime(end3, '%d %b %Y')
            age3 = round(age3.total_seconds()/86400.,1)
        except:
            age3 = 'N/A'
        try:
            age4 = today_a - datetime.strptime(end4, '%d %b %Y')
            age4 = round(age4.total_seconds()/86400.,1)
        except:
            age4 = 'N/A'
        try:
            age5 = today_a - datetime.strptime(end5, '%d %b %Y')
            age5 = round(age5.total_seconds()/86400.,1)
        except:
            age5 = 'N/A'

        #GENERIC OUTPUT-----------------------------------------------------------------
        #1 - ICOBench, 2 - ICODrops, 3 - TokenMarket, 4 - ICORating, 5 - ICOMarks


        writer.writerow([currency,start1,end1,duration1,age1,start3,end3,duration3,age3,start4,end4,duration4,age4,start5,end5,duration5,age5,country1,country2,country3,country5,industry1,industry2,industry4,team1,team2,team3,team4,team5,raised1,raised2,raised4,raised5,hardcap1,hardcap2,hardcap4,hardcap5,success1,success2,success4,price1,price2,price4,price5,telegram1,telegram2,telegram4,N_google_news,N_twitter,hype4,risk4,ret_day1,vol_day1,sharpe_1,sharpe_3,sharpe_yr,sharpe_yr2,beta_btc,beta_top10,alpha_btc,alpha_top10])

        #--------------------------------------------------------------------------------
        #--------------------------------------------------------------------------------
        #--------------------------------------------------------------------------------
        #HIERARCHICAL OUTPUT (No Ratings by ICOrating.com)-------------------------------
        #1 - ICOBench, 2 - ICODrops, 3 - TokenMarket, 4 - ICORating, 5 - ICOMarks

        start_date_all=[start1,start3,start4,start5]
        end_date_all=[end1,end3,end4,end5]
        duration_all=[duration1,duration3,duration4,duration5]
        age_all = [age1,age3,age4,age5]
        country_all=[country1,country2,country3,country5]
        industry_all=[industry1,industry2,industry4]
        team_all=[team1,team2,team3,team4,team5]
        raised_all=[raised1,raised2,raised4,raised5]
        hardcap_all=[hardcap1,hardcap2,hardcap4,hardcap5]
        success_all=[success1,success2,success4]
        price_all=[price1,price2,price4,price5]
        telegram_all=[telegram1,telegram2,telegram4]

        #1. Determining start date, end date and duration
        #1A) First remove all 'N/A' occurences
        duration_all = [item for item in duration_all if item != 'N/A']
        start_date_all = [item for item in start_date_all if item != 'N/A']
        end_date_all = [item for item in end_date_all if item != 'N/A']
        age_all = [item for item in age_all if item != 'N/A']

        #1B) If length of array is zero after removals, then final values are 'N/A'
        if len(duration_all) == 0:
            duration = 'N/A'
            start = 'N/A'
            end = 'N/A'
            age = 'N/A'
            [duration_all,start_date_all,end_date_all,age_all]=[['N/A'],['N/A'],['N/A'],['N/A']]

        #1C) If all values are the same then adopt that value as the final value
        if duration_all.count(duration_all[0]) == len(duration_all):
            duration = duration_all[0]
            start = start_date_all[0]
            end = end_date_all[0]
            age = age_all[0]

        #1D) If values are not the same then adopt the value that appears most times. If failure adopt first elements.
        try:
            if duration_all.count(duration_all[0]) != len(duration_all):
                (values,counts) = np.unique(duration_all,return_counts=True)
                (values2,counts2) = np.unique(start_date_all,return_counts=True)
                (values3,counts3) = np.unique(end_date_all,return_counts=True)
                (values4,counts4) = np.unique(age_all,return_counts=True)
                if counts.count(counts[0]) == len(counts):
                    duration = duration_all[0]
                if counts2.count(counts2[0]) == len(counts2):
                    start = start_date_all[0]
                if counts3.count(counts3[0]) == len(counts3):
                    end = end_date_all[0]
                if counts4.count(counts4[0]) == len(counts4):
                    age =age_all[0]
                ind=np.argmax(counts)
                ind2=np.argmax(counts2)
                ind3=np.argmax(counts3)
                ind4=np.argmax(counts4)
                duration = values[ind]
                start = values2[ind2]
                end = values3[ind3]
                age = values4[ind4]
        except:
            duration = duration_all[0]
            start = start_date_all[0]
            end = end_date_all[0]
            age = age_all[0]

        if duration < 0:
            start = end_date_all[0]
            end = start_date_all[0]
            duration = -duration

        #2. Determining geographical region
        #2A) First remove all 'N/A' occurences
        country_all = [item for item in country_all if item != 'N/A']

        #2B) If length of array is zero after removals, then final values are 'N/A'
        if len(country_all) == 0:
            region = 'N/A'
            country_all = ['N/A']

        #2C) If all values are the same then adopt that value as the final value
        if country_all.count(country_all[0]) == len(country_all):
            region = country_all[0]
            region = func_region(region)

        #2D) If values are not the same then adopt the value that appears most times. If failure adopt first element.
        try:
            if country_all.count(country_all[0]) != len(country_all):
                (values,counts) = np.unique(country_all,return_counts=True)
                if counts.count(counts[0]) == len(counts):
                    region = func_region(country_all[0])
                ind=np.argmax(counts)
                region = values[ind]
                region = func_region(region)
        except:
            region = func_region(country_all[0])

        #3. Determining industry category
        #3A) First remove all 'N/A' occurences
        industry_all = [item for item in industry_all if item != 'N/A']

        #3B) If length of array is zero after removals, then final values are 'N/A'
        if len(industry_all) == 0:
            industry = 'N/A'
            industry_all = ['N/A']

        #3C) If all values are the same then adopt that value as the final value
        if industry_all.count(industry_all[0]) == len(industry_all):
            industry_a = industry_all[0]
            industry = func_industry(industry_a)

        #3D) If values are not the same then adopt the value that appears most times. If failure adopt last element (ICOrating/ICOdrops/ICObench).
        try:
            if industry_all.count(industry_all[0]) != len(industry_all):
                (values,counts) = np.unique(industry_all,return_counts=True)
                if counts.count(counts[0]) == len(counts):
                    industry = func_industry(industry_all[len(industry_all)-1])
                ind=np.argmax(counts)
                industry_a = values[ind]
                industry = func_industry(industry_a)
        except:
            industry = func_industry(industry_all[0])

        #4. Determining team size

        #4A) Check if data availabe from tokenmarket or icomarks. If yes adopt this as team size value

        if (team_all[2] != 'N/A') or (team_all[4] != 'N/A'):
            if team_all[2] == team_all[4]:
                team = team_all[2]
            if team_all[2] != team_all[4]:
                team = team_all[4]

        #4B) In the opposite case, proceed as before

        #4C) First remove all 'N/A' occurences

        if (team_all[4] == 'N/A') or (team == 'N/A'):
            team_all = [item for item in team_all if item != 'N/A']

        #4D) If length of array is zero after removals, then final values are 'N/A'
            if len(team_all) == 0:
                team = 'N/A'
                team_all = ['N/A']

        #4E) If all values are the same then adopt that value as the final value
            if team_all.count(team_all[0]) == len(team_all):
                team = team_all[0]

        #4F) If values are not the same then adopt the value that appears most times if failure adopt first element
            try:
                if team_all.count(team_all[0]) != len(team_all):
                    (values,counts) = np.unique(team_all,return_counts=True)
                    if counts.count(counts[0]) == len(counts):
                        team = team_all[0]
                    ind=np.argmax(counts)
                    team = values[ind]
            except:
                team = team_all[0]

        #5. Determining success, money raised, hardcap

        success = 'N/A'

        ###

        raised_all2 = [item for item in raised_all if item != 'N/A']
        hardcap_all2 = [item for item in hardcap_all if item != 'N/A']

        if len(raised_all2) == 0:
            raised_all2 = ['N/A']
            raised = raised_all2[0]

        if len(hardcap_all2) == 0:
            hardcap_all2 = ['N/A']
            hardcap = hardcap_all2[0]

        if raised_all2.count(raised_all2[0]) == len(raised_all2):
            raised = raised_all2[0]

        if hardcap_all2.count(hardcap_all2[0]) == len(hardcap_all2):
            hardcap = hardcap_all2[0]

        try:
            if raised_all2.count(raised_all2[0]) != len(raised_all2):
                (values,counts) = np.unique(raised_all2,return_counts=True)
                ind=np.argmax(counts)
                raised = values[ind]

                if counts.count(counts[0]) == len(counts):
                    raised = raised_all2[0]

        except:
            raised = raised_all2[0]

        try:
            if hardcap_all2.count(hardcap_all2[0]) != len(hardcap_all2):
                (values,counts) = np.unique(hardcap_all2,return_counts=True)
                ind=np.argmax(counts)
                hardcap = values[ind]

                if counts.count(counts[0]) == len(counts):
                    hardcap = hardcap_all2[0]

        except:
            hardcap = hardcap_all2[0]

        if success == 'N/A':
            try:
                success = min(round(raised/hardcap, 2),1.0)
            except:
                success = 'N/A'

        success_all2 = [item for item in success_all if item != 'N/A']

        if len(success_all2) == 0:
            success_all2 = ['N/A']
            success = success_all2[0]


        if (success_all[0] != 'N/A') and (success_all[1] == 'N/A') and (success_all[2] == 'N/A'):
            success = min(success_all[0],1.0)
            raised = raised_all[0]
            hardcap = hardcap_all[0]

        if (success_all[0] == 'N/A') and (success_all[1] != 'N/A') and (success_all[2] == 'N/A'):
            success = min(success_all[1],1.0)
            raised = raised_all[1]
            hardcap = hardcap_all[1]

        if (success_all[0] != 'N/A') and (success_all[1] != 'N/A') and (success_all[2] == 'N/A'):
            success = min(success_all[1],1.0)
            raised = raised_all[1]
            hardcap = hardcap_all[1]

        if (success_all[0] == 'N/A') and (success_all[1] == 'N/A') and (success_all[2] != 'N/A'):
            success = min(success_all[2],1.0)
            raised = raised_all[2]
            hardcap = hardcap_all[2]

        if success == 'N/A':
            try:
                success = min(round(raised/hardcap, 2),1.0)
            except:
                success = 'N/A'

        try:
            hardcap = round(hardcap,0)
        except:
            hardcap = 'N/A'
	
        if raised != 'N/A' and success != 'N/A':
            hardcap = round(raised/success,0)

        if team == 0:
            team = 'N/A'


        #9. Determining ICO token price
        #9A) Check if data availabe from icobench or icodrops or icomarks. If yes adopt this money raised value
        if (price_all[0] != 'N/A') or (price_all[1] != 'N/A') or (price_all[3] != 'N/A'):
            try:
                price = round(price_all[0],5)
            except:
                try:
                    price = round(price_all[1],5)
                except:
                    price = round(price_all[3],5)

        #9B) In the opposite case, proceed as before
        if (price_all[0] == 'N/A') or (price_all[1] == 'N/A') or (price_all[3] == 'N/A'):

        #9C) First remove all 'N/A' occurences
            price_all = [item for item in price_all if item != 'N/A']

        #9D) If length of array is zero after removals, then final values are 'N/A'
            if len(price_all) == 0:
                price_all = ['N/A']
                price = 'N/A'

        #9E) If all values are the same then adopt that value as the final value
            if price_all.count(price_all[0]) == len(price_all):
                try:
                    price = round(price_all[0],5)
                except:
                    price = 'N/A'

        #9F) If values are not the same then adopt the value that appears most times. If failure adopt first element.
            try:
                if price_all.count(price_all[0]) != len(price_all):
                    (values,counts) = np.unique(price_all,return_counts=True)
                    if counts.count(counts[0]) == len(counts):
                        price = round(price_all[0],5)
                    ind=np.argmax(counts)
                    price = round(values[ind],5)
            except:
                try:
                    price = round(price_all[0],5)
                except:
                    try:
                        price = round(price_all[1],5)
                    except:
                        price = 'N/A'

        #10. Determining telegram follower count

        #10A) First remove all 'N/A' occurences
        telegram_all = [item for item in telegram_all if item != 'N/A']

        #10B) If length of array is zero after removals, then final values are 'N/A'
        if len(telegram_all) == 0:
            telegram = 'N/A'
            telegram_all = ['N/A']

        #10C) If all values are the same then adopt that value as the final value
        if telegram_all.count(telegram_all[0]) == len(telegram_all):
            telegram = telegram_all[0]

        #10D) If values are not the same then adopt the value that appears most times. If failure adopt first element.
        try:
            if telegram_all.count(telegram_all[0]) != len(telegram_all):
                (values,counts) = np.unique(telegram_all,return_counts=True)
                if counts.count(counts[0]) == len(counts):
                    telegram = telegram_all[0]
                ind=np.argmax(counts)
                telegram = values[ind]
        except:
            telegram = telegram_all[0]

        #11) Calculating first day exchange returns compared to ICO token price

        try:
            ret_icoday1 = round((c[0] - price)/price,3)
        except:
            #ret_icoday1 = 'N/A'
	    ret_icoday1 = 0.0

        ret_icoday1 = ret_icoday1

        writer2.writerow([currency,start,end,duration,age,region,industry,team,raised,hardcap,success,price,telegram,N_google_news,N_twitter,ret_icoday1,vol_day1,sharpe_1,sharpe_3,sharpe_yr,sharpe_yr2,beta_btc,beta_top10,alpha_btc,alpha_top10])

        #--------------------------------------------------------------------------------
        #--------------------------------------------------------------------------------
        #--------------------------------------------------------------------------------
        #HIERARCHICAL OUTPUT (Ratings by ICOrating.com included)-------------------------
        #1 - ICOBench, 2 - ICODrops, 3 - TokenMarket, 4 - ICORating, 5 - ICOMarks

        hype = hype4
        risk = risk4

        writer3.writerow([currency,start,end,duration,age,region,industry,team,raised,hardcap,success,price,telegram,N_google_news,N_twitter,hype,risk,ret_icoday1,vol_day1,sharpe_1,sharpe_3,sharpe_yr,sharpe_yr2,beta_btc,beta_top10,alpha_btc,alpha_top10])

        #--------------------------------------------------------------------------------
        #--------------------------------------------------------------------------------
        #--------------------------------------------------------------------------------
