from bs4 import BeautifulSoup
#import urllib
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

def func_googletwitter(currency):

    #################################################################################################
    ###Twitter Followers Count Start#################################################################
    #################################################################################################
    try:
        data_c = urllib2.urlopen('https://icobench.com/ico/'+currency)
        soup_c = BeautifulSoup(data_c, 'html.parser')
    except:
        Ntwitter = 'N/A'
    

    ICO_Twitter = 'N/A'
    try:
        for a in soup_c.find_all('a', href=True):
            if 'https://twitter.com/' in a['href']:
                ICO_Twitter = a['href'].split("https://twitter.com/",1)[1]
    except:
        ICO_Twitter = 'N/A'


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

    Ntwitter = ICO_Twitter_N
    Ngoogle = k_news

    return 'Twitter/Google',Ntwitter,Ngoogle
