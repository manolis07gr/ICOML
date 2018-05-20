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
import csv
warnings.filterwarnings("ignore")


def func_googlenews(currency):

    #################################################################################################
    ###Google News Articles Count Start##############################################################
    #################################################################################################

    query = '"'+currency+' ICO'+'"'

    try:
        k_news = 0
        for j in search_news(query, tld="com", lang="en", num=100, stop=1, pause=2, tbs='cdr:1,cd_min:1/1/2015,cd_max:'+dt.datetime.now().date().isoformat().replace('-',"/")):
            k_news = k_news + 1

    except:
        k_news = 0

    #------------------------------------------------------------------------------------------------
    ###Google News Articles Count END################################################################
    #------------------------------------------------------------------------------------------------

    Ngoogle = k_news

    return Ngoogle

if __name__ == '__main__':

    start = 43
    end = 93
    
    with open("outdata/ico_data_full.csv") as f:
        reader = csv.reader(f)
        data = [r for r in reader]

    with open('outdata/ico_data_full_2.csv', 'w') as csvfile:
        writer=csv.writer(csvfile, delimiter=',')

        for i in range(start,end):
            writer.writerow([data[i][0],func_googlenews(data[i][0])])
    
