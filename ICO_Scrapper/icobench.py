from bs4 import BeautifulSoup
#import urllib2
import urllib2
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

def func_icobench(currency):

#################################################################################################
###ICO Bench Start###############################################################################
#################################################################################################
    try:
        source = 'ICObench.com'
        data_c = urllib2.urlopen('https://icobench.com/ico/'+currency)
        soup_c = BeautifulSoup(data_c, 'html.parser')
    except:
        try:
            source = 'ICObench.com'
            data_c = urllib2.urlopen('https://icobench.com/ico/'+currency.replace(" ","-"))
            soup_c = BeautifulSoup(data_c, 'html.parser')                
        except:
            try:
                source = 'ICObench.com'
                data_c = urllib2.urlopen('https://icobench.com/ico/'+currency.replace("token",""))
                soup_c = BeautifulSoup(data_c, 'html.parser')
            except:
                [started,ended,lasted,country,industry,team,raised,hardcap,success,price,telegram]=['N/A','N/A','N/A','N/A','N/A','N/A','N/A','N/A','N/A','N/A','N/A']

    ico_raised = 'N/A'

        
    try:
        value_c = soup_c.findAll("div", {"class": "value"})
        for tag in value_c:
            if '$' in tag.text:
                ttt = tag.text.split()[0].replace("$","")
                commas = [pos for pos, char in enumerate(ttt) if char == ","]
                if len(commas) == 2:
                    ico_raised = float(eval(ttt[0:10].replace(",","")))
                if len(commas) == 1:
                    ico_raised = float(eval(ttt[0:6].replace(",","")))
                if len(commas) == 3 and len(ttt.split(",")[0]) == 2:
                    ico_raised = float(eval(ttt[0:10].replace(",","")))
		if len(commas) == 3 and len(ttt.split(",")[0]) == 1:
		    ico_raised = float(eval(ttt[0:9].replace(",","")))
		if len(commas) == 3 and len(ttt.split(",")[0]) == 3:
		    ico_raised = float(eval(ttt[0:11].replace(",","")))	   
		   
    except:
        ico_raised = 'N/A'

    #Find country of origin
    country = 'N/A'
    try:
        for a in soup_c.find_all('a', href=True):
            if '/icos?filterCountry=' in a['href']:
                country = a['href'].split("=",1)[1].lower()
    except:
        country = 'N/A'

    #Find ICO start date and end date
    ICO_s_o = 'N/A'
    ICO_e_o = 'N/A'
    ICO_duration = 'N/A'
    ICO_s = 'N/A'
    ICO_e = 'N/A'

    try:
        value_d =  soup_c.findAll("div", {"class": "data_row"})
        for tag2 in value_d:
            if 'ICO start' in tag2.text:
                ICO_s = tag2.text.replace("\n","").split("ICO start",1)[1].strip().replace("th","").replace("st","").replace("nd","").replace("rd","")
                ICO_s_o = datetime.strptime(ICO_s, '%d %b %Y')
            if 'ICO end' in tag2.text:
                ICO_e = tag2.text.replace("\n","").split("ICO end",1)[1].strip().replace("th","").replace("st","").replace("nd","").replace("rd","")
                ICO_e_o = datetime.strptime(ICO_e, '%d %b %Y')

        ICO_duration = (ICO_e_o-ICO_s_o)
        ICO_duration = round(float(ICO_duration.total_seconds())/86400.,0)
        
        if ICO_duration < 0.:
            ICO_duration = abs(ICO_duration)
            ICO_s1 = ICO_s
            ICO_s = ICO_e
            ICO_e = ICO_s1

    except:

        ICO_s = 'N/A'
        ICO_e = 'N/A'

        ICO_s_o = 'N/A'
        ICO_e_o = 'N/A'
        ICO_duration = 'N/A'

    #Find team size
    team = 'N/A'
    try:
        team = 0
        for aa in soup_c.find_all('h3'):
            team = team + 1
        team = team - 8
	if team < 0:
		team = 'N/A'
    except:
        team = 'N/A'

    #Find tokens sold, tokens for sale
    #value_e =  soup_c.findAll("div", {"class": "box_left"})
    for_sale = 'N/A'
    sold = 'N/A'
    success = 'N/A'
    try:
        value_e =  soup_c.findAll("div", {"class": "box_left"})
        for tag3 in value_e:
            if 'Tokens for sale' in tag3.text:
                info = tag3.text
                for_sale = float(eval((info[info.find("for sale ")+1:info.find(" Sold")]).replace("or sale","").replace(",","").strip()))
                sold = float(eval((info[info.find("Sold tokens ")+1:info.find("Updated")]).replace("old tokens","").replace(",","").strip()))
        success = round(sold/for_sale,2)
    except:
        for_sale = 'N/A'
        sold = 'N/A'
        success = 'N/A'

    #Find ICO token price
    ICO_p = 'N/A'
    try:
        value_d =  soup_c.findAll("div", {"class": "data_row"})
        for tag4 in value_d:
            if 'Price in ICO' in tag4.text:
	        try:
			ICO_p = float(eval(tag4.text.strip("").replace(" ","").split("\n")[5].split("=")[1].replace("USD","")))
		except:
	        	ICO_p = float(eval(tag4.text.replace(" ","").replace("\n","").split("ICO")[1].split("USD")[0].strip()))

    except:
        ICO_p = 'N/A'

    #Find Hardcap

    ICO_hardcap = 'N/A'
    try:
        value_e =  soup_c.findAll("div", {"class": "row"})
        for tag5 in value_e:
            if 'Hard cap' in tag5.text:
                #print tag5.text
                #print tag5.text.replace(" ","").replace("USD","").replace("Hardcap","")
                if ('USD' not in tag5.text.strip("").split("\n")[0]) and ('ETH' not in tag5.text.strip("").split("\n")[0]):
                    ICO_hardcap = float(tag5.text.strip("").split("\n")[0].split(" ")[3].replace(",",""))*float(ICO_p)
                if 'USD' in tag5.text.strip("").split("\n")[0]:
                    #print tag5.text.strip("").split("\n")[0]
                    ICO_hardcap = float(eval(tag5.text.replace(" ","").replace(",","").replace("USD","").replace("Hardcap","")))


    except:
        ICO_hardcap = 'N/A'

    try:
        success1 = round(ico_raised/ICO_hardcap,2)
    except:
        success1 = 'N/A'
    
    if ICO_hardcap != 'N/A' and ico_raised != 'N/A':
        success = success1

    #Find Industry

    #value_eee =  soup_c.findAll("div", {"class": "categories"})
    ICO_industry = 'N/A'
    try:
        value_eee =  soup_c.findAll("div", {"class": "categories"})
        for tag5e in value_eee:
                ICO_industry = re.findall('[A-Z][^A-Z]*',tag5e.text)[0].lower()
    except:
        ICO_industry = 'N/A'

    #################################################################################################
    ###Telegram Followers Count Start################################################################
    #################################################################################################

    ICO_Telegram = 'N/A'
    try:
        for a in soup_c.find_all('a', href=True):
            if 'https://t.me/' in a['href'] and a['href'] != 'https://t.me/icobench':
                ICO_Telegram = a['href'].split("https://t.me/",1)[1]

    except:
        ICO_Telegram = 'N/A'

    try:
        source2 = 'https://t.me/'+ICO_Telegram
        data_cc = urllib2.urlopen(source2)
        soup_cc = BeautifulSoup(data_cc, 'html.parser')

        value_ee =  soup_cc.findAll("div", {"class": "tgme_page_extra"})
        ICO_Tgm1 = 'N/A'
        for tag6 in value_ee:
            if 'members' in tag6.text:
                ICO_Tgm1 = tag6.text.replace("\n","").strip().split("members",1)[0].strip().replace(" ","")
    except:
        ICO_Tgm1 = 'N/A'

    try:
        ICO_Telegram_N = eval(ICO_Tgm1)
    except:
        ICO_Telegram_N = 'N/A'

    #------------------------------------------------------------------------------------------------
    ###Telegram Followers Count END##################################################################
    #------------------------------------------------------------------------------------------------

    #------------------------------------------------------------------------------------------------
    ###ICO Bench END################################################################################
    #------------------------------------------------------------------------------------------------

    started = ICO_s
    ended = ICO_e
    lasted = ICO_duration
    country = country
    team = team
    raised = ico_raised
    price = ICO_p
    hardcap = ICO_hardcap
    success = success
    industry = ICO_industry
    telegram = ICO_Telegram_N


    return source,started,ended,lasted,country,industry,team,raised,hardcap,success,price,telegram
