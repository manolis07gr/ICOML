from bs4 import BeautifulSoup
import urllib2
#import urllib2
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

def func_icodrops(currency):
#################################################################################################
###ICO Drops Start###############################################################################
#################################################################################################
    source2b = 'ICOdrops.com'
    try:
        req = Request('https://icodrops.com/'+currency,headers={'User-Agent': 'Mozilla/5.0'})
        data_s2 = urlopen(req).read()
        soup_s2 = BeautifulSoup(data_s2, 'html.parser')
    except:
        country,industry,team,raised,hardcap,success,price,telegram = ['N/A','N/A','N/A','N/A','N/A','N/A','N/A','N/A']

    #Find Industry
    ICO_industry2 = 'N/A'
    try:
        value_s2a =  soup_s2.findAll("div", {"class": "ico-main-info"})
        for tag1a in value_s2a:
            if "(" in tag1a.text:
                #ICO_industry2 = tag1a.text[tag1a.text.find("(")+1:tag1a.text.find(")")].replace("\n","").lower()
                ICO_industry2 = tag1a.text.replace("\n","").split("(")[1].split(")")[0].lower()
    except:
        ICO_industry2 = 'N/A'


    #Find Money Raised, Hardcap, Success
    ico_raised2 = 'N/A'
    ICO_hardcap2 = 'N/A'
    sucess2 = 'N/A'
    team2 = 'N/A'


    try:
        value_s2b =  soup_s2.findAll("div", {"class": "fund-goal"})
        for tag1b in value_s2b:
            if "$" in tag1b.text:
                ico_raised2 = float(eval(tag1b.text[tag1b.text.find("$")+1:tag1b.text.find("OF")].replace("$","").replace(",","").replace("\n","").strip()))

    except:
        ico_raised2 = 'N/A'

    try:
        for tag1b in value_s2b:
            if "$" in tag1b.text:
                ICO_hardcap2 = float(eval(tag1b.text[tag1b.text.find(" $")+1:tag1b.text.find(" (")].replace("$","").replace(",","").replace("\n","").strip()))

    except:
        ICO_hardcap2 = 'N/A'

    try:
        success2 = round((ico_raised2/ICO_hardcap2), 2)
    except:
        success2 = 'N/A'

    #Find ICO token price
    ICO_p2 = 'N/A'

    try:
        value_s2c =  soup_s2.findAll("div", {"class": "col-12 col-md-6"})
        for tag1c in value_s2c:
            if ('ICO Token Price' in tag1c.text) and ('=' in tag1c.text):
                ICO_p2 = float(eval(tag1c.text.strip()[tag1c.text.strip().find("=")+1:tag1c.text.strip().find("USD")].replace("\n","").strip()))

    except:
        ICO_p2 = 'N/A'

    #Find ICO country
    country2 = 'N/A'

    try:
        value_s2d =  soup_s2.findAll("div", {"class": "col-12 info-analysis-list"})
        for tag1d in value_s2d:
            #print tag1d.text.replace("\n","").split("Team from:")[1]
            if 'Prototype' not in tag1d.text.replace("\n","").split("Team from:")[1]:
                country2 = tag1d.text.split('\n')[3].replace("Team from:","").strip().lower()
            if 'Prototype' in tag1d.text.replace("\n","").split("Team from:")[1]:
                country2 = tag1d.text.replace("\n","").split("Team from:")[1].replace(" ","").split("Prototype")[0].lower()

    except:
        country2 = 'N/A'

    #Find ICO team size
    team2 = 'N/A'

    try:
        value_s2e =  soup_s2.findAll("div", {"class": "col-12 info-analysis-list"})
        for tag1e in value_s2e:
            team2 = eval(tag1e.text.split('\n')[2][tag1e.text.split('\n')[2].find("Number of Team Members:")+len("Number of Team Members:"):tag1e.text.split('\n')[2].find("ICO")].strip())

    except:
        team2 = 'N/A'

    # Find Telegram group membership

    ICO_Telegram_s2 = 'N/A'
    try:
        for aa in soup_s2.find_all('a', href=True):
            if 'https://t.me/' in aa['href'] and aa['href'] != 'https://t.me/icodrops'  and aa['href'] != 'https://t.me/joinchat/FoisO0k4-XXBkPEikfdgow':
                ICO_Telegram_s2 = aa['href']
    except:
        ICO_Telegram_s2 = 'N/A'

    try:
        source22 = ICO_Telegram_s2
        data_ccc = urllib2.urlopen(source22)
        soup_ccc = BeautifulSoup(data_ccc, 'html.parser')

        value_ee1 =  soup_ccc.findAll("div", {"class": "tgme_page_extra"})
        ICO_Tgm2 = 'N/A'
        for tag66 in value_ee1:
            if 'members' in tag66.text:
                ICO_Tgm2 = tag66.text.replace("\n","").strip().split("members",1)[0].strip().replace(" ","")

    except:
        ICO_Tgm2 = 'N/A'

    try:
        ICO_Telegram_N2 = eval(ICO_Tgm2)
    except:
        ICO_Telegram_N2 = 'N/A'

    #------------------------------------------------------------------------------------------------
    ###ICO Drops END################################################################################
    #------------------------------------------------------------------------------------------------

    country = country2
    industry = ICO_industry2
    team = team2
    raised = ico_raised2
    hardcap = ICO_hardcap2
    success = success2
    price = ICO_p2
    telegram = ICO_Telegram_N2

    return source2b,country,industry,team,raised,hardcap,success,price,telegram
