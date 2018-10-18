from bs4 import BeautifulSoup
import urllib3
import requests
import numpy as np
from numpy import *
import datetime as dt
from datetime import datetime
import time
import warnings
warnings.filterwarnings("ignore")

def func_icobazaar(currency):

#################################################################################################
###ICO Bench Start###############################################################################
#################################################################################################

    try:
        source = 'ICObazaar.com'
        response = requests.get('https://icobazaar.com/v2/'+currency)
        txt = response.text
        soup_c = BeautifulSoup(txt, 'html.parser')
    except:
        txt = 'N/A'
        soup_c = 'N/A'

    [ICO_s,ICO_e,ICO_duration,team,ICO_p,ICO_hardcap,ICOBazaar_rating] = ['N/A','N/A','N/A','N/A','N/A','N/A','N/A']


    #Find ICO start date and end date
    ICO_s_o = 'N/A'
    ICO_e_o = 'N/A'
    ICO_duration = 'N/A'
    ICO_s = 'N/A'
    ICO_e = 'N/A'

    try:
        value_d =  soup_c.findAll("div", {"class": "com-sidebar__info-line"})
        for tag2 in value_d:
            if ("Publicsale:") in (tag2.text.replace(" ","").split("\n")):
                aaa = (tag2.text.replace(" ","").split("\n")[3])
                ICO_s = aaa.split("-")[0].replace("`","")
                ICO_s_o = datetime.strptime(ICO_s, '%d%b%y')
                ICO_e = aaa.split("-")[1].replace("`","")
                ICO_e_o = datetime.strptime(ICO_e, '%d%b%y')
                ICO_duration = (ICO_e_o-ICO_s_o)
                ICO_duration = round(float(ICO_duration.total_seconds())/86400.,0)
    except:

        ICO_s = 'N/A'
        ICO_e = 'N/A'

        ICO_s_o = 'N/A'
        ICO_e_o = 'N/A'
        ICO_duration = 'N/A'

    #Find ICO price
    try:
        value_e =  soup_c.findAll("div", {"class": "com-sidebar__info-line"})
        for tag3 in value_e:
            if ("Price:") in (tag3.text.replace(" ","").split("\n")):
                ICO_p = float(eval((tag3.text.replace(" ","").split("\n"))[2].split("=")[1].replace("USD","")))
    except:
        ICO_p = 'N/A'

    #Find ICO hardcap
    try:
        ll = -1
        loc = 0
        value_f =  soup_c.findAll("div", {"class": "com-sidebar__info-line"})
        for tag4 in value_f:
            ll = ll + 1
            if ("Cap:") in (tag4.text.replace(" ","").split("\n")):
                loc = ll
                if ("USD") in (tag4.text.replace(" ","").split("\n"))[2]:
                    ICO_hardcap = float(eval((tag4.text.replace(" ","").split("\n"))[2].replace("USD","")))
                if ("USD") not in (tag4.text.replace(" ","").split("\n"))[2]:
                    kk = -1
                    for tag4 in value_f:
                        kk = kk + 1
                        if kk == loc+1:
                            ICO_hardcap = float(eval((tag4.text.replace(" ","").split("\n"))[2].replace("USD","").replace("(","").replace(")","")))                                                                    
    except:
        ICO_hardcap = 'N/A'

    #Find ICO Bazaar rating
    try:
        value_g =  soup_c.findAll("div", {"class": "ico-rating__count"})
        for tag5 in value_g:
            ICOBazaar_rating = round(float(eval(tag5.text))/5.0,2)
    except:
        ICOBazaar_rating = 'N/A'

    #Find team size
    try:
        response2 = requests.get('https://icobazaar.com/v2/'+currency+'/team')
        txt2 = response2.text
        soup_cc = BeautifulSoup(txt2, 'html.parser')
        value_gg =  soup_cc.findAll("ul", {"class": "com-teams__wrapper"})

        for tag6 in value_gg:
            bbb = (tag6.text.split("\n"))
            bbb2 = list(filter(None, bbb))

            matching = [s for s in bbb2 if "CEO" in s]
            matching2 = [s for s in bbb2 if "Founder" in s]
            matching3 = [s for s in bbb2 if "Co-Founder" in s]
            matching4 = [s for s in bbb2 if "Chief" in s]

            team = int(len(bbb2)/2)

            if (len(matching) == 0) and (len(matching2) == 0) and (len(matching3) == 0) and (len(matching4) == 0):
                team = int(len(bbb2))
            
    except:
        team = 'N/A'


    started = ICO_s
    ended = ICO_e
    lasted = ICO_duration
    team = team
    price = ICO_p
    hardcap = ICO_hardcap
    rating = ICOBazaar_rating


    return source,started,ended,lasted,team,hardcap,price,rating
