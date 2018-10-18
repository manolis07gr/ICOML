from bs4 import BeautifulSoup
import urllib3
import requests
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

def func_googletwitter(currency):

    #################################################################################################
    ###Twitter Followers Count Start#################################################################
    #################################################################################################

    [Ntwitter, Ngoogle, Alexa, Alexa2] = ['N/A','N/A','N/A','N/A']
    
    try:
        response = requests.get('https://icobench.com/ico/'+currency)
        txt = response.text
        soup_c = BeautifulSoup(txt, 'html.parser')

        j = -1
        for a in soup_c.find_all('a', href=True):
            if 'https://twitter.com/' in a['href']:
                j = j + 1
                if j == 0:
                    ICO_Twitter = a['href'].split("https://twitter.com/",1)[1]


        ICO_WebA = []
        j = -1
        for a in soup_c.find_all('a', href=True):
            if (('http') in a['href']) and ('?utm_source=icobench' in a['href']):
                j = j + 1
                ICO_WebA.append(j)
                ICO_WebA[j] = a['href'][0:a['href'].index("?")]

        ICO_Twitter1 = ICO_Twitter
        ICO_Web1 = ICO_WebA[0]
        
    except:

        ICO_Twitter1 = 'N/A'
        ICO_Web1 = 'N/A'
        
    try:
        response = requests.get('https://icorating.com/ico/'+currency+'/#details',headers={'User-Agent': 'Mozilla/5.0'})
        txt = response.text
        soup_c = BeautifulSoup(txt, 'html.parser')

        j = -1
        ICO_Twitter22 = []
        for a in soup_c.find_all('a', href=True):
            if 'https://twitter.com/' in a['href']:
                j = j + 1
                ICO_Twitter22.append(j)
                ICO_Twitter22[j] = a['href'].split("https://twitter.com/",1)[1]

        ICO_Twitter2 = ICO_Twitter22[len(ICO_Twitter22)-2]


        ICO_WebB = []
        j = -1
        for a in soup_c.find_all('a', href=True):
            if (('http') in a['href']) and ('?utm_source=icorating' in a['href']):
                j = j + 1
                ICO_WebB.append(j)
                ICO_WebB[j] = a['href'][0:a['href'].index("?")]

        ICO_Web2 = ICO_WebB[0]

    except:
            
        ICO_Twitter2 = 'N/A'
        ICO_Web2 = 'N/A'

    try:
        response = requests.get('https://icomarks.com/ico/'+currency,headers={'User-Agent': 'Mozilla/5.0'})
        txt = response.text
        soup_c = BeautifulSoup(txt, 'html.parser')

        j = -1
        ICO_Twitter33 = []
        for a in soup_c.find_all('a', href=True):
            if 'https://twitter.com/' in a['href']:
                j = j + 1
                ICO_Twitter33.append(j)
                ICO_Twitter33[j] = a['href'].split("https://twitter.com/",1)[1]

        ICO_Twitter3 = ICO_Twitter33[1]

        ICO_WebC = []
        j = -1
        for a in soup_c.find_all('a', href=True):
            if (('http') in a['href']) and ('?utm_source=icomarks' in a['href']):
                j = j + 1
                ICO_WebC.append(j)
                ICO_WebC[j] = a['href'][0:a['href'].index("?")]

        ICO_Web3 = ICO_WebC[0]

    except:
            
        ICO_Twitter3 = 'N/A'
        ICO_Web3 = 'N/A'
    

    ICO_T = [ICO_Twitter1,ICO_Twitter2,ICO_Twitter3]
    ICO_Web = [ICO_Web1,ICO_Web2,ICO_Web3]

    ICO_T = [item for item in ICO_T if item not in ['N/A','icorating','ICO_marks','ICObench']]
    ICO_Web = [item for item in ICO_Web if item not in ['N/A','icorating','ICO_marks','ICObench']]

    if len(ICO_T) >= 1:
        ICO_Twitter = ICO_T[0]
    if len(ICO_T) == 0:
        ICO_Twitter = 'N/A'

    if len(ICO_Web) >= 1:
        ICO_Website = ICO_Web[0]
    if len(ICO_Web) == 0:
        ICO_Website = 'N/A'

    consumer_key = "fsee9ncfK3XqnTtQnCZt1aFq2"
    consumer_secret = "qmTxu9b26kSYCTkv2nsd6zvump4Ryesjr8mGRtkuja7bflLdpu"
    access_token = "3220981051-MM5xca27lheZTUI6q5lcESPbyJzIBLUHuv52Ap7"
    access_token_secret = "UkbSVaeK7oFspAeF9435VLDwbxiasYqB2CvZRjp9NhYeL"

    # Tweepy OAuthHandler
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)

    try:
        user = api.get_user(ICO_Twitter)
        ICO_Twitter_N = eval(str(user.followers_count))
    except:
        ICO_Twitter_N = 'N/A'

    #------------------------------------------------------------------------------------------------
    ###Twitter Followers Count END###################################################################
    #------------------------------------------------------------------------------------------------



    #################################################################################################
    ###Google News Articles Count Start##############################################################
    #################################################################################################

    query = '"'+currency+' ICO'+'"'

    try:
        k_news = 0
        for j in search_news(query, tld="com", lang="en", num=30, stop=1, pause=2, tbs='cdr:1,cd_min:1/1/2015,cd_max:'+dt.datetime.now().date().isoformat().replace('-',"/")):
            k_news = k_news + 1

    except:
        k_news = 0

    #------------------------------------------------------------------------------------------------
    ###Google News Articles Count END################################################################
    #------------------------------------------------------------------------------------------------


    #################################################################################################
    ###Alexa Rank Start##############################################################################
    #################################################################################################
    #Warning: These are updated every 3 months
    
    Alexa_N = 'N/A'
    Alexa_N2 = 'N/A'

    try:
        response = requests.get('https://www.alexa.com/siteinfo/'+ICO_Website,headers={'User-Agent': 'Mozilla/5.0'})
        txt = response.text
        soup_d = BeautifulSoup(txt, 'html.parser')

        value_d =  soup_d.findAll("strong", {"class": "metrics-data align-vmiddle"})
        j = -1
        metric = []
        for tag in value_d:
            j = j + 1
            metric.append(j)
            metric[j] = tag.text


        if len(metric) == 5:
            daily_views = float(eval(metric[2].replace(" ","").replace("\n","")))
            alexa_rank = float(eval(metric[0].replace(" ","").replace("\n","").replace(",","")))
            bounce_rate = round(float(eval(metric[1].replace(" ","").replace("\n","").replace("%",""))/100.),2) #Percentage
            daily_time_min = float(eval(metric[3].replace(" ","").replace("\n","")[0:(metric[3].replace(" ","").replace("\n","")).index(":")]))
            daily_time_sec = metric[3].replace(" ","").replace("\n","")[metric[3].replace(" ","").replace("\n","").index(":")+1:len(metric[3].replace(" ","").replace("\n",""))]
        
            if daily_time_sec[0] == '0':
                daily_time_sec_1 = float(eval(daily_time_sec[1]))
            if daily_time_sec[0] != '0':
                daily_time_sec_1 = float(eval(daily_time_sec))

            daily_time = daily_time_min * 60 + daily_time_sec_1
            
            Alexa_N = daily_views
            Alexa_N2 = daily_time


        if len(metric) == 6:
            daily_views = float(eval(metric[3].replace(" ","").replace("\n","")))
            alexa_rank = float(eval(metric[0].replace(" ","").replace("\n","").replace(",","")))
            bounce_rate = round(float(eval(metric[2].replace(" ","").replace("\n","").replace("%",""))/100.),2) #Percentage
            daily_time_min = float(eval(metric[4].replace(" ","").replace("\n","")[0:(metric[4].replace(" ","").replace("\n","")).index(":")]))
            daily_time_sec = metric[4].replace(" ","").replace("\n","")[(metric[4].replace(" ","").replace("\n","")).index(":")+1:len(metric[4].replace(" ","").replace("\n",""))]
        
            if daily_time_sec[0] == '0':
                daily_time_sec_1 = float(eval(daily_time_sec[1]))
            if daily_time_sec[0] != '0':
                daily_time_sec_1 = float(eval(daily_time_sec))

            daily_time = daily_time_min * 60 + daily_time_sec_1
            
            Alexa_N = daily_views
            Alexa_N2 = daily_time
        
    except:
        Alexa_N = 'N/A'
        Alexa_N2 = 'N/A'

    #------------------------------------------------------------------------------------------------
    ###Alexa Rank END################################################################################
    #------------------------------------------------------------------------------------------------
    

    Ntwitter = ICO_Twitter_N
    Ngoogle = k_news
    Alexa = Alexa_N
    Alexa2 = Alexa_N2

    return 'Twitter/Google/Alexa',Ntwitter,Ngoogle,Alexa,Alexa2
