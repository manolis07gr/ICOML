from bs4 import BeautifulSoup
import urllib3
import re
import requests
import numpy as np
from numpy import *
import datetime as dt
from datetime import datetime
import time
import warnings
warnings.filterwarnings("ignore")

def func_icomarks(currency):
#################################################################################################
###ICOMarks Start################################################################################
#################################################################################################

    source5b = 'ICOmarks.com'

    try:
        response = requests.get('https://icomarks.com/ico/'+currency,headers={'User-Agent': 'Mozilla/5.0'})
        txt = response.text
        soup_s5 = BeautifulSoup(txt, 'html.parser')
    except:
        txt = 'N/A'
        soup_s5 = 'N/A'
        started,ended,lasted,country,team,raised,hardcap,price = ['N/A','N/A','N/A','N/A','N/A','N/A','N/A','N/A']

    #Find ICO start date and end date
    ICO_s_o4 = 'N/A'
    ICO_e_o4 = 'N/A'
    ICO_duration4 = 'N/A'
    ICO_s4 = 'N/A'
    ICO_e4 = 'N/A'
    country4 = 'N/A'
    team5 = 'N/A'
    ico_raised4 = 'N/A'
    ICO_hardcap4 = 'N/A'
    ICO_p4 = 'N/A'

    try:
        value_s5a =  soup_s5.findAll("div", {"class": "icoinfo-block__item"})
        for tag5a in value_s5a:
            if 'ICOTime' in tag5a.text.replace(" ",""):
                ICO_s4 = str(tag5a.text.replace(" ","").replace("ICOTime:","").replace("\n","").split("-")[0]).replace(" ","").strip().replace("\n","")
                ICO_e4 = str(tag5a.text.replace(" ","").replace("ICOTime:","").replace("\n","").split("-")[1]).replace(" ","").strip().replace("\n","")
                if (len(ICO_s4)) >= 10:
                    ICO_s4 = ICO_s4[0:5]+ICO_s4[6:10]
                if (len(ICO_e4)) >= 10:
                    ICO_e4 = ICO_e4[0:5]+ICO_e4[6:10]
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
                    val1 = tag_nnn.text.replace(" ","").replace("ICOPrice:","").replace("\n","").replace("USD","").replace(u'\u2248',"").replace("\r","")
                    ICO_p4 = float(eval(val1))
                if u'\u2248' not in tag_nnn.text.replace(" ",""):
                    val1 = tag_nnn.text.replace(" ","").replace("ICOPrice:","").replace("\n","").split("=")[1].replace('USD',"").replace("\r","")
                    ICO_p4 = float(eval(val1))

    except:   
        ICO_p4 = 'N/A'

    #Find ICO Hardcap
    ICO_hardcap4 = 'N/A'

    try:

        value_nnn2 =  soup_s5.findAll("div", {"class": "icoinfo-right"})
        for tag_nnn2 in value_nnn2:
            if 'Hard cap' in tag_nnn2.text:
                ICO_hardcap4a = tag_nnn2.text.replace(" ","").replace("\r","").split("\n").index("Hardcap:")
                index = tag_nnn2.text.replace(" ","").replace("\r","").split("\n").index("Hardcap:") + 1
                if ("USD" in tag_nnn2.text.replace(" ","").replace("\r","").split("\n")[index]):
                    ICO_hardcap4b = tag_nnn2.text.replace(" ","").replace("\r","").split("\n")[index].replace("USD","").replace(",","")
                    ICO_hardcap4 = float(eval(ICO_hardcap4b))
                if ("USD" not in tag_nnn2.text.replace(" ","").replace("\r","").split("\n")[index]):
                    ICO_hardcap4b = tag_nnn2.text.replace(" ","").replace("\r","").split("\n")[index].replace(" ","").strip("")
                    ICO_hardcap4b = [int(s) for s in ICO_hardcap4b if s.isdigit()]
                    for i in range(0,len(ICO_hardcap4b)):
                        ICO_hardcap4b[i] = str(ICO_hardcap4b[i])

                    ICO_hardcap4b = float(eval("".join(ICO_hardcap4b)))
                    ICO_hardcap4 = ICO_hardcap4b * ICO_p4

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
