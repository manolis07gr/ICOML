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

def func_icorating(currency,token):
#################################################################################################
###ICORating Start###############################################################################
#################################################################################################
    source4b = 'ICORating.com'
    token = token.lower()

    try:
        response = requests.get('https://icorating.com/ico/'+currency+'-'+currency+'/#details',headers={'User-Agent': 'Mozilla/5.0'})
        txt = response.text
        soup_s4 = BeautifulSoup(txt, 'html.parser')

        if ("404 - page not found" in txt):
            response = requests.get('https://icorating.com/ico/'+currency+'/#details',headers={'User-Agent': 'Mozilla/5.0'})
            txt = response.text
            soup_s4 = BeautifulSoup(txt, 'html.parser')
        
            if  ("404 - page not found" in txt):
                response = requests.get('https://icorating.com/ico/'+currency+'-'+token+'/#details',headers={'User-Agent': 'Mozilla/5.0'})
                txt = response.text
                soup_s4 = BeautifulSoup(txt, 'html.parser')
    
                if  ("404 - page not found" in txt):
                    response = requests.get('https://icorating.com/ico/'+currency+'-',headers={'User-Agent': 'Mozilla/5.0'})
                    txt = response.text
                    soup_s4 = BeautifulSoup(txt, 'html.parser')

    except:
        txt = 'N/A'
        soup_s4 = 'N/A'

    [ICO_s3,ICO_e3,ICO_duration3,ICO_industry3,team4,ico_raised3,ICO_hardcap3,success3,ICO_p3,ICO_Telegram_N3,ICO_rating_hype,ICO_rating_risk]=['N/A','N/A','N/A','N/A','N/A','N/A','N/A','N/A','N/A','N/A','N/A','N/A']
                
    #Find ICO start date and end date
    ICO_s_o3 = 'N/A'
    ICO_e_o3 = 'N/A'
    ICO_duration3 = 'N/A'
    ICO_s3 = 'N/A'
    ICO_e3 = 'N/A'
    team4 = 'N/A'
    ico_raised3 = 'N/A'
    industry3 = 'N/A'
    
    try:
        value_s4a =  soup_s4.findAll("table", {"class": "c-card-info__table"})
        for tag4a in value_s4a:
            if 'Start ICO' in tag4a.text:
                ICO_s3 = tag4a.text.strip("").replace("\n","").replace(" ","").split("StartICO")[1].split("EndICO")[0]
                ICO_e3 = tag4a.text.strip("").replace("\n","").replace(" ","").split("EndICO")[1].split("Token")[0]
                ICO_s_o3 = datetime.strptime(ICO_s3, '%d%b%Y')
                ICO_e_o3 = datetime.strptime(ICO_e3, '%d%b%Y')
                ICO_s3 = ICO_s_o3.strftime('%d %b %Y')
                ICO_e3 = ICO_e_o3.strftime('%d %b %Y')

            ICO_duration3 = ICO_e_o3-ICO_s_o3
            ICO_duration3 = round(float(ICO_duration3.total_seconds())/86400.,0)

    except:   
        ICO_s_o3 = 'N/A'
        ICO_e_o3 = 'N/A'
        ICO_duration3 = 'N/A'

    #Find ICO industry
    ICO_industry3 = 'N/A'

    try:
        value_s5a =  soup_s4.findAll("p", {"class": "c-card-media__status c-card-media__status--live"})
        ii = -1
        for tag5a in value_s5a:
            ii = ii + 1
            if ii == 0:
                ICO_industry3 = tag5a.text.split("\n")[1].replace(" ","").lower()
    except:
        ICO_industry3 = 'N/A'

    #Find ICO rating
    ICO_rating_hype = 'N/A'
    ICO_rating_risk = 'N/A'
    
    try:
        value_s6a =  soup_s4.findAll("span", {"class": "c-card-info__status fwn"})
        kk = - 1
        for tag6a in value_s6a:
            kk = kk + 1
            if kk == 0:
                ICO_rating_hype = tag6a.text.replace(" ","").split("\n")[1]
            if kk == 1: 
                ICO_rating_risk = tag6a.text.replace(" ","").split("\n")[1]

    except:   
        ICO_rating_hype = 'N/A'
        ICO_rating_risk = 'N/A'
	

    #Find ICO Money Raised
    ico_raised3 = 'N/A'

    try:
        value_s6b =  soup_s4.findAll("table", {"class": "c-info-table c-info-table--va-top"})
        for tag6b in value_s6b:
            if 'Raised' in tag6b.text:
                ico_raised3 = float(eval(tag6b.text.replace(" ","").strip(" ").split("Raised")[1].replace(",","").replace("USD","").replace("\n","")))

    except:   
        ico_raised3 = 'N/A'

    #Find ICO Team Size
    team4 = 'N/A'

    try:
        value_7 = soup_s4.find(id='team')
        rows = value_7.findAll('tr')
        data = [[td.findChildren(text=True) for td in tr.findAll("td")] for tr in rows]
        team4 = len(data)-2

    except:
        team4 = 'N/A'


    #Find ICO Token price
    ICO_p3 = 'N/A'

    try:
        value_s8b = soup_s4.findAll("table", {"class": "c-card-info__table"})
        for tag8b in value_s8b:
            if 'Price' in tag8b.text:
                ICO_p3 =round(float(tag8b.text.replace("\n","").replace(" ","").split("=")[1].split("USD")[0].replace(" ","")),3)

    except:   
        ICO_p3 = 'N/A'

    #Find Number of Tokens Sold

    try:
        value_s9b = soup_s4.findAll("table", {"class": "c-info-table c-info-table--va-top"})
        for tag9b in value_s9b:
            if 'ICO token supply' in tag9b.text:
                index = (tag9b.text.replace(" ","").split("\n")).index("ICOtokensupply")+3
                ICO_supply = float(eval(tag9b.text.replace(" ","").split("\n")[index].replace(",","")))

    except:   
        ICO_supply = 'N/A'


    #Find ICO Hardcap (direct)
    ICO_hardcap_dir = 'N/A'

    try:
        value_s10b = soup_s4.findAll("table", {"class": "c-info-table c-info-table--va-top"})
        for tag10b in value_s10b:
            if 'Hard cap size' in tag10b.text:
                index2 = (tag10b.text.replace(" ","").split("\n")).index("Hardcapsize")+3
                hard_dir = float(eval(tag10b.text.replace(" ","").split("\n")[index2].replace(",","").replace("USD","")))
                ICO_hardcap_dir = hard_dir                

    except:   
        ICO_hardcap_dir = 'N/A'

    #Find ICO Hardcap (indirect)
    ICO_hardcap3 = 'N/A'

    try:
        ICO_hardcap3 = ICO_hardcap_dir
        if ICO_hardcap_dir == 'N/A':
            ICO_hardcap3 = ICO_supply * ICO_p3
    except:
        ICO_hardcap3 = 'N/A'

    #Find ICO success = raised/hardcap

    success3 = 'N/A'
    try:
        success3 = round(ico_raised3/ICO_hardcap3,2)
    except:
        success3 = 'N/A'

    # Find Telegram group membership

    ICO_Telegram_s3 = 'N/A'
    try:
        for a in soup_s4.find_all('a', href=True):
            if ('https://t.me/' in a['href']) and ('joinchat' not in a['href']) and a['href'] != 'https://t.me/ico_rating':
                ICO_Telegram_s3 = a['href'].split("https://t.me/",1)[1]
    except:
        ICO_Telegram_s3 = 'N/A'


    try:
        source3 = 'https://t.me/'+ICO_Telegram_s3
        
        response3 = requests.get(source3)
        txt3 = response3.text
        soup_cc = BeautifulSoup(txt3, 'html.parser')

        value_ee =  soup_cc.findAll("div", {"class": "tgme_page_extra"})
        ICO_Tgm3 = 'N/A'
        for tag6 in value_ee:
            if 'members' in tag6.text:
                ICO_Tgm3 = tag6.text.replace("\n","").strip().split("members",1)[0].strip().replace(" ","")
    except:
        ICO_Tgm3 = 'N/A'

    try:
        ICO_Telegram_N3 = eval(ICO_Tgm3)
    except:
        ICO_Telegram_N3 = 'N/A'

    started = ICO_s3
    ended = ICO_e3
    lasted = ICO_duration3
    industry = ICO_industry3
    team = team4
    raised = ico_raised3
    hardcap = ICO_hardcap3
    success = success3
    price = ICO_p3
    telegram = ICO_Telegram_N3
    hype = ICO_rating_hype
    risk = ICO_rating_risk
        
#------------------------------------------------------------------------------------------------
##ICORating END##################################################################################
#------------------------------------------------------------------------------------------------

    return source4b,started,ended,lasted,industry,team,raised,hardcap,success,price,telegram,hype,risk
