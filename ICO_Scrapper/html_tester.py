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

currency = 'holo'
token = 'hot'
#currency = 'bread'
#token = 'brd'

#print func_icorating(currency,token)

res = func_icobench(currency)
res2 = func_icodrops(currency)
res3 = func_tokenmarket(currency)
res4 = func_icorating(currency,token)
res5 = func_icomarks(currency)
res6 = func_googletwitter(currency)
print res,res2,res3,res4,res5,res6
