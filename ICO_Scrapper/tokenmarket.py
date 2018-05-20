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

def func_tokenmarket(currency):
#################################################################################################
###TokenMarket Start#############################################################################
#################################################################################################
    source3b = 'Tokenmarket.net'
    try:
        req = Request('https://tokenmarket.net/blockchain/'+currency+'/assets/'+currency+'/',headers={'User-Agent': 'Mozilla/5.0'})
        data_s3 = urlopen(req).read()
        soup_s3 = BeautifulSoup(data_s3, 'html.parser')
    except:
        try:
            req = Request('https://tokenmarket.net/blockchain/ethereum/assets/'+currency+'/',headers={'User-Agent': 'Mozilla/5.0'})
            data_s3 = urlopen(req).read()
            soup_s3 = BeautifulSoup(data_s3, 'html.parser')
        except:
            try:
                req = Request('https://tokenmarket.net/blockchain/bitcoin/assets/'+currency+'/',headers={'User-Agent': 'Mozilla/5.0'})
                data_s3 = urlopen(req).read()
                soup_s3 = BeautifulSoup(data_s3, 'html.parser')
            except:
                [started,ended,lasted,country,team]=['N/A','N/A','N/A','N/A','N/A']
                [ICO_s2,ICO_e2,ICO_duration2,country3,team3]=['N/A','N/A','N/A','N/A','N/A']

    #Find ICO start date and end date
    ICO_s_o2 = 'N/A'
    ICO_e_o2 = 'N/A'
    ICO_duration2 = 'N/A'

    try:
        value_s3a =  soup_s3.findAll("table", {"class": "table table-asset-data"})
        for tag3a in value_s3a:
            if 'opening' in tag3a.text:
                ICO_s2 = time.strftime("%d %b %Y",time.strptime(tag3a.text.strip("").replace(" ","").split("\n")[11].replace(".","").strip("\n"),"%d%b%Y"))
                ICO_e2 = time.strftime("%d %b %Y",time.strptime(tag3a.text.strip("").replace(" ","").split("\n")[27].replace(".","").strip("\n"),"%d%b%Y"))
                ICO_s_o2 = datetime.strptime(ICO_s2, '%d %b %Y')
                ICO_e_o2 = datetime.strptime(ICO_e2, '%d %b %Y')

        ICO_duration2 = ICO_e_o2-ICO_s_o2
        ICO_duration2 = round(float(ICO_duration2.total_seconds()/86400.),0)

    except:   
        ICO_s2 = 'N/A'
	ICO_e2 = 'N/A'
        ICO_s_o2 = 'N/A'
        ICO_e_o2 = 'N/A'
        ICO_duration2 = 'N/A'

    #Find ICO country of origin
    country3 = 'N/A'
    try:
        value_s4a =  soup_s3.findAll("table", {"class": "table table-asset-data"})
        for tag4a in value_s4a:
            if 'Country' in tag4a.text:
                country3 = tag4a.text.replace("\n","").split("Country of origin")[1].replace(" ","").lower()

    except:
        country3 = 'N/A'

    #Find ICO Team Size
    team3 = 'N/A'
    try:
        value_s5a =  soup_s3.findAll("table", {"class": "table table-asset-data"})
        for tag5a in value_s5a:
            if 'Members' in tag5a.text:
                team3 = len(tag5a.text.replace("\n","").split("Country of origin")[0].replace(" ","").strip("Members").split("-"))-1

    except:
        team3 = 'N/A'

    started = ICO_s2
    ended = ICO_e2
    lasted = ICO_duration2
    country = country3
    team = team3

#------------------------------------------------------------------------------------------------
###TokenMarket END###############################################################################
#------------------------------------------------------------------------------------------------

    return source3b,started,ended,lasted,country,team
