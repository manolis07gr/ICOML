from bs4 import BeautifulSoup
import urllib2
#import urllib
from urllib2 import Request, urlopen
import re
import numpy as np
from numpy import *
import datetime as dt
from datetime import datetime
import tweepy
import googlesearch
from googlesearch import search_news
import time
import warnings
warnings.filterwarnings("ignore")

def func_icorating(currency,token):
#################################################################################################
###ICORating Start###############################################################################
#################################################################################################
    source4b = 'ICORating.com'
    token = token.lower()

    try:
        req = Request('https://icorating.com/ico/'+currency+'-'+currency+'/',headers={'User-Agent': 'Mozilla/5.0'})
        data_s4 = urlopen(req).read()
        soup_s4 = BeautifulSoup(data_s4, 'html.parser')

        req2 = Request('https://icorating.com/ico/'+currency+'-'+currency+'/details',headers={'User-Agent': 'Mozilla/5.0'})
        data_s4b = urlopen(req2).read()
        soup_s4b = BeautifulSoup(data_s4b, 'html.parser')

        req3 = Request('https://icorating.com/ico/'+currency+'-'+currency+'/team',headers={'User-Agent': 'Mozilla/5.0'})
        data_s4c = urlopen(req3).read()
        soup_s4c = BeautifulSoup(data_s4c, 'html.parser')
    except:
        try:
            req = Request('https://icorating.com/ico/'+currency,headers={'User-Agent': 'Mozilla/5.0'})
            data_s4 = urlopen(req).read()
            soup_s4 = BeautifulSoup(data_s4, 'html.parser')

            req2 = Request('https://icorating.com/ico/'+currency+'/details',headers={'User-Agent': 'Mozilla/5.0'})
            data_s4b = urlopen(req2).read()
            soup_s4b = BeautifulSoup(data_s4b, 'html.parser')

            req3 = Request('https://icorating.com/ico/'+currency+'/team',headers={'User-Agent': 'Mozilla/5.0'})
            data_s4c = urlopen(req3).read()
            soup_s4c = BeautifulSoup(data_s4c, 'html.parser')
        except:
            try:
                req = Request('https://icorating.com/ico/'+currency+'-'+token,headers={'User-Agent': 'Mozilla/5.0'})
                data_s4 = urlopen(req).read()
                soup_s4 = BeautifulSoup(data_s4, 'html.parser')

                req2 = Request('https://icorating.com/ico/'+currency+'-'+token+'/details',headers={'User-Agent': 'Mozilla/5.0'})
                data_s4b = urlopen(req2).read()
                soup_s4b = BeautifulSoup(data_s4b, 'html.parser')

                req3 = Request('https://icorating.com/ico/'+currency+'-'+token+'/team',headers={'User-Agent': 'Mozilla/5.0'})
                data_s4c = urlopen(req3).read()
                soup_s4c = BeautifulSoup(data_s4c, 'html.parser')
            except:
                [ICO_s3,ICO_e3,ICO_duration3,ICO_industry3,team4,ico_raised3,ICO_hardcap3,success3,ICO_p3,ICO_Telegram_N3,ICO_rating_hype,ICO_rating_risk]=['N/A','N/A','N/A','N/A','N/A','N/A','N/A','N/A','N/A','N/A','N/A','N/A']
            

    #Find ICO start date and end date
    ICO_s_o3 = 'N/A'
    ICO_e_o3 = 'N/A'
    ICO_duration3 = 'N/A'
    ICO_s3 = 'N/A'
    ICO_e3 = 'N/A'
    team4 = 'N/A'
    ico_raised3 = 'N/A'
    industry3 = 'N/A'
    
    try:
        value_s4a =  soup_s4.findAll("table", {"class": "uk-table"})
        for tag4a in value_s4a:
            if 'ICO date' in tag4a.text:
                ICO_s3 = tag4a.text.strip("").replace(" ","").split("\n")[4].split("-")[0].replace(".","")
                ICO_e3 = tag4a.text.strip("").replace(" ","").split("\n")[4].split("-")[1].replace(".","")
                ICO_s_o3 = datetime.strptime(ICO_s3, '%d%m%Y')
                ICO_e_o3 = datetime.strptime(ICO_e3, '%d%m%Y')
                ICO_s3 = ICO_s_o3.strftime('%d %b %Y')
                ICO_e3 = ICO_e_o3.strftime('%d %b %Y')

            ICO_duration3 = ICO_e_o3-ICO_s_o3
            ICO_duration3 = round(float(ICO_duration3.total_seconds())/86400.,0)

    except:   
        ICO_s_o3 = 'N/A'
        ICO_e_o3 = 'N/A'
        ICO_duration3 = 'N/A'

    #Find ICO industry
    ICO_industry3 = 'N/A'

    try:
        value_s5a =  soup_s4.findAll("table", {"class": "uk-table"})
        for tag5a in value_s5a:
            if "Industry:" in tag5a.text:
                ICO_industry3 = tag5a.text.replace("\n","").split("Description:")[0].replace(" ","").split("Industry:")[1].lower()
    except:
        ICO_industry3 = 'N/A'

    #Find ICO rating
    ICO_rating_hype = 'N/A'
    ICO_rating_risk = 'N/A'
    
    try:
        value_s6a =  soup_s4.findAll("div", {"class": "white-block-area"})
        for tag6a in value_s6a:
            if 'score' in tag6a.text:
                ind1 = tag6a.text.replace('\n','').replace(' ',"").split('Hypescore')[1].find("/")
		ICO_rating_hype = round(eval(tag6a.text.replace('\n','').replace(' ',"").split('Hypescore')[1][ind1-3:ind1]) / 5.0,2)

    except:   
        ICO_rating_hype = 'N/A'
	
    try:
        value_s6a =  soup_s4.findAll("div", {"class": "white-block-area"})
        for tag6a in value_s6a:
            if 'score' in tag6a.text:
		ind1 = tag6a.text.replace('\n','').replace(' ',"").split('Riskscore')[1].find(".")
		ICO_rating_risk = round(eval(tag6a.text.replace('\n','').replace(' ',"").split('Riskscore')[1][ind1-3:ind1]) / 5.0,2)

    except:   
        ICO_rating_risk = 'N/A'	
	

    #Find ICO Money Raised
    ico_raised3 = 'N/A'

    try:
        value_s6b =  soup_s4b.findAll("div", {"class": "uk-width-1-2 table"})
        for tag6b in value_s6b:
            if 'Raised' in tag6b.text:
                ico_raised3 = float(eval(tag6b.text.strip("").split("Raised:")[1].replace("\n","").replace("$","").replace(" ","").replace(",","").replace("USD","")))

    except:   
        ico_raised3 = 'N/A'

    #Find ICO Team Size
    team4 = 'N/A'

    try:
        table = soup_s4c.find_all('table')[0]
        row_marker = 0
        for row in table.find_all('tr'):
            row_marker = row_marker+1

        
        try:
            table2 = soup_s4c.find_all('table')[1]
            row_marker2 = 0
            for row in table2.find_all('tr'):
                row_marker2 = row_marker2+1
            
            team4 = row_marker + row_marker2 - 2

        except:

            team4 = row_marker - 1

    except:
        team4 = 'N/A'

    #Find ICO Hardcap
    ICO_hardcap3 = 'N/A'

    try:
        value_s7b =  soup_s4b.findAll("div", {"class": "uk-width-1-2 table"})
        for tag7b in value_s7b:
            if 'Raised' in tag7b.text:
                ICO_hardcap3 = float(eval(tag7b.text.strip("").split("Hard cap size:")[1].replace("\n","").replace("$","").replace(" ","").replace(",","").replace("USD","").split("(fiat)")[0]))

    except:
        ICO_hardcap3 = 'N/A'

    #Find ICO success = raised/hardcap

    success3 = 'N/A'
    try:
        success3 = ico_raised3/ICO_hardcap3
    except:
        success3 = 'N/A'

    #Find ICO Token price
    ICO_p3 = 'N/A'

    try:
        value_s8b =  soup_s4b.findAll("div", {"class": "uk-width-1-2 table"})
        for tag8b in value_s8b:
            if 'Token price' in tag8b.text:
                ICO_p3 =round(float(tag8b.text.replace("\n","").replace(" ","").split("=")[1].split("USD")[0].replace(" ","")),3)

    except:   
        ICO_p3 = 'N/A'

    # Find Telegram group membership

    ICO_Telegram_s3 = 'N/A'
    try:
        for aaa in soup_s4b.find_all('a', href=True):
            if 'https://t.me/' in aaa['href'] and aaa['href'] != 'https://t.me/ico_rating':
                ICO_Telegram_s3 = aaa['href']
    except:
        ICO_Telegram_s3 = 'N/A'

    try:
        source222 = ICO_Telegram_s3
        data_cccc = urllib2.urlopen(source222)
        soup_cccc = BeautifulSoup(data_cccc, 'html.parser')

        value_eee1 =  soup_cccc.findAll("div", {"class": "tgme_page_extra"})
        ICO_Tgm3 = 'N/A'
        for tag666 in value_eee1:
            if 'members' in tag666.text:
                ICO_Tgm3 = tag666.text.replace("\n","").split("members")[0].replace(" ","")

    except:
        try:
            source222 = 'https://t.me/'+currency+'official'
            data_cccc = urllib2.urlopen(source222)
            soup_cccc = BeautifulSoup(data_cccc, 'html.parser')

            value_eee1 =  soup_cccc.findAll("div", {"class": "tgme_page_extra"})
            ICO_Tgm3 = 'N/A'
            for tag666 in value_eee1:
                if 'members' in tag666.text:
                    ICO_Tgm3 = tag666.text.replace("\n","").split("members")[0].replace(" ","")

        except:
            ICO_Tgm3 = 'N/A'

    try:
        ICO_Telegram_N3 = eval(ICO_Tgm3)
    except:
        ICO_Telegram_N3 = 'N/A'

    started = ICO_s3
    ended = ICO_e3
    lasted = ICO_duration3
    industry = ICO_industry3
    team = team4
    raised = ico_raised3
    hardcap = ICO_hardcap3
    success = success3
    price = ICO_p3
    telegram = ICO_Telegram_N3
    hype = ICO_rating_hype
    risk = ICO_rating_risk
        
#------------------------------------------------------------------------------------------------
##ICORating END##################################################################################
#------------------------------------------------------------------------------------------------

    return source4b,started,ended,lasted,industry,team,raised,hardcap,success,price,telegram,hype,risk
