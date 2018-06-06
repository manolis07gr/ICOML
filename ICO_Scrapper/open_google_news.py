from bs4 import BeautifulSoup
#import urllib2
import urllib
#from urllib2 import Request, urlopen
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
import os
import csv
warnings.filterwarnings("ignore")

with open("new_google_news.csv") as f:
    reader = csv.reader(f)
    data = [r for r in reader]
        
[sd,sm,sy,ed,em,ey,name]=[[],[],[],[],[],[],[]]
j = -1
for i in range(1,np.shape(data)[0]):
	if data[i][13] == 'N/A':
		[sd.append(j),sm.append(j),sy.append(j),ed.append(j),em.append(j),ey.append(j),name.append(j)]
		name[j] = data[i][0]
		sd[j] = str(datetime.strptime(data[i][1], '%d %b %Y').day)
		sm[j] = str(datetime.strptime(data[i][1], '%d %b %Y').month)
		sy[j] = str(datetime.strptime(data[i][1], '%d %b %Y').year)
		ed[j] = str(datetime.strptime(data[i][2], '%d %b %Y').day)
		em[j] = str(datetime.strptime(data[i][2], '%d %b %Y').month)
		ey[j] = str(datetime.strptime(data[i][2], '%d %b %Y').year)
				
		start_day = sd[j]
		start_month = sm[j]
		start_year = sy[j]
		end_day = ed[j]
		end_month = em[j]
		end_year = ey[j]
		key = name[j]
				
		os.system('open "https://www.google.com/search?q=%22'+key+'+ICO%22&client=safari&rls=en&biw=1662&bih=920&source=lnt&tbs=cdr%3A1%2Ccd_min%3A'+start_month+'%2F'+start_day+'%2F'+start_year+'%2Ccd_max%3A'+end_month+'%2F'+end_day+'%2F'+end_year+'&tbm=nws"')
