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

def func_icomarks(currency):
#################################################################################################
###ICOMarks Start################################################################################
#################################################################################################

    source5b = 'ICOmarks.com'

    try:
        reqq = Request('https://icomarks.com/ico/'+currency,headers={'User-Agent': 'Mozilla/5.0'})
        data_s5 = urlopen(reqq).read()
        soup_s5 = BeautifulSoup(data_s5, 'html.parser')
    except:
        started,ended,lasted,country,team,raised,hardcap,price = ['N/A','N/A','N/A','N/A','N/A','N/A','N/A','N/A']

    #Find ICO start date and end date
    ICO_s_o4 = 'N/A'
    ICO_e_o4 = 'N/A'
    ICO_duration4 = 'N/A'
    ICO_s4 = 'N/A'
    ICO_e4 = 'N/A'

    try:
        value_s5a =  soup_s5.findAll("div", {"class": "icoinfo-block__item"})
        for tag5a in value_s5a:
            if 'ICOTime' in tag5a.text.replace(" ",""):
                ICO_s4 = str(tag5a.text.replace(" ","").replace("ICOTime:","").replace("\n","").split("-")[0]).replace(" ","").strip().replace("\n","")
                ICO_e4 = str(tag5a.text.replace(" ","").replace("ICOTime:","").replace("\n","").split("-")[1]).replace(" ","").strip().replace("\n","")
                ICO_s_o4 = datetime.strptime(ICO_s4, '%d%b%Y')
                ICO_e_o4 = datetime.strptime(ICO_e4, '%d%b%Y')
                ICO_s4 = ICO_s_o4.strftime('%d %b %Y')
                ICO_e4 = ICO_e_o4.strftime('%d %b %Y')

                ICO_duration4 = ICO_e_o4-ICO_s_o4
                ICO_duration4 = round(float(ICO_duration4.total_seconds())/86400.,0)

    except:   
        ICO_s_o4 = 'N/A'
        ICO_e_o4 = 'N/A'
        ICO_duration4 = 'N/A'

    #Find ICO Token price
    ICO_p4 = 'N/A'

    try:

        value_nnn =  soup_s5.findAll("div", {"class": "icoinfo-block__item"})
        for tag_nnn in value_nnn:
            if 'Price' in tag_nnn.text.replace(" ",""):
                if u'\u2248' in tag_nnn.text.replace(" ",""):
                    ICO_p4 = float(eval(tag_nnn.text.replace(" ","").replace("Price:","").replace("\n","").replace("USD","").replace(u'\u2248',"")))
                if u'\u2248' not in tag_nnn.text.replace(" ",""):
                    ICO_p4 = float(eval(tag_nnn.text.replace(" ","").replace("Price:","").replace("\n","").split("=")[1].replace("USD","")))

    except:   
        ICO_p4 = 'N/A'

    #Find ICO Hardcap
    ICO_hardcap4 = 'N/A'

    try:

        value_nnn2 =  soup_s5.findAll("div", {"class": "icoinfo-block__item"})
        for tag_nnn2 in value_nnn2:
            if 'Hardcap' in tag_nnn2.text.replace(" ",""):
                ICO_hardcap4a = tag_nnn2.text.replace(" ","").replace("Hardcap:","").replace("\n","")
                if 'USD' not in ICO_hardcap4a and 'ETH' not in ICO_hardcap4a:
                    ICO_hardcap4 = float(eval((re.findall('\d+', ICO_hardcap4a ))[0]))
                    ICO_hardcap4 = ICO_hardcap4 * ICO_p4
                if 'USD' in ICO_hardcap4a:
                    ICO_hardcap4 = float(eval(tag_nnn2.text.replace(" ","").replace("Hardcap:","").replace("\n","").replace("USD","")))

    except:   
        ICO_hardcap4 = 'N/A'

    #Find Money Raised
    ico_raised4 = 'N/A'

    try:

        value_nnn3 =  soup_s5.findAll("div", {"class": "icoinfo-block__item"})
        for tag_nnn3 in value_nnn3:
            if 'Raised' in tag_nnn3.text.replace(" ",""):
                ico_raised4a = tag_nnn3.text.replace(" ","").replace("$","").replace(",","").replace("\n","")
                ico_raised4 = float(eval((re.findall('\d+', ico_raised4a ))[0]))

    except:   
        ico_raised4 = 'N/A'

    #Find ICO Country
    country4 = 'N/A'

    try:

        value_nnn4 =  soup_s5.findAll("div", {"class": "icoinfo-block__item"})
        for tag_nnn4 in value_nnn4:
            if 'Country' in tag_nnn4.text.replace(" ",""):
                country4 = tag_nnn4.text.replace(" ","").replace("Country:","").replace("\n","").lower().replace("\r","")

    except:   
        country4 = 'N/A'

    #Find ICO Team
    team5 = 'N/A'

    try:

        value_nnn5 =  soup_s5.findAll("div", {"class": "container"})
        for tag_nnn5 in value_nnn5:
            if 'Team' in tag_nnn5.text.replace(" ",""):
                team5a = tag_nnn5.text.replace(" ","")
                mmm = team5a.split("Team(")[1].split(")")[0]
                team5 = int(float(eval(mmm)))
                break
                	                        
    except:   
        team5 = 'N/A'

    started = ICO_s4
    ended = ICO_e4
    lasted = ICO_duration4
    country = country4
    team = team5
    raised = ico_raised4
    hardcap = ICO_hardcap4
    price = ICO_p4

#------------------------------------------------------------------------------------------------
##ICOMarks END###################################################################################
#------------------------------------------------------------------------------------------------

    return source5b,started,ended,lasted,country,team,raised,hardcap,price
