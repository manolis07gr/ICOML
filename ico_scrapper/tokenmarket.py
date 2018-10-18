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

def func_tokenmarket(currency):
#################################################################################################
###TokenMarket Start#############################################################################
#################################################################################################
    source3b = 'Tokenmarket.net'  

    try:
        response = requests.get('https://tokenmarket.net/blockchain/'+currency+'/assets/'+currency+'/',headers={'User-Agent': 'Mozilla/5.0'})
        txt = response.text
        soup_s3 = BeautifulSoup(txt, 'html.parser')
    except:
        txt = 'N/A'
        soup_s3 = 'N/A'
        
    if 'Not found' in txt:
        try:
            response = requests.get('https://tokenmarket.net/blockchain/ethereum/assets/'+currency+'/',headers={'User-Agent': 'Mozilla/5.0'})
            txt = response.text
            soup_s3 = BeautifulSoup(txt, 'html.parser')
        except:
            soup_s3 = 'N/A'
        if 'Not found' in txt:
            try:
                response = requests.get('https://tokenmarket.net/blockchain/bitcoin/assets/'+currency+'/',headers={'User-Agent': 'Mozilla/5.0'})
                txt = response.text
                soup_s3 = BeautifulSoup(txt, 'html.parser')
            except:
                soup_s3 = 'N/A'

                
    #Find ICO start date and end date

    ICO_s_o2 = 'N/A'
    ICO_e_o2 = 'N/A'
    ICO_duration2 = 'N/A'
    country3 = 'N/A'
    team3 = 'N/A'

    try:
        value_s3a =  soup_s3.findAll("div", {"class": "dates-wrapper"})
        for tag3a in value_s3a:
            if 'Token sale:' in tag3a.text:
                ss = tag3a.text.replace("\n","").replace(" ","").split("-")[0].strip("Tokensale:").replace(".","")
                ee = tag3a.text.replace("\n","").replace(" ","").split("-")[1].replace(".","")
                ICO_s2 = time.strftime("%d %b %Y",time.strptime(ss,"%d%b%Y"))
                ICO_e2 = time.strftime("%d %b %Y",time.strptime(ee,"%d%b%Y"))
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
                if country3 == '(datamissing)':
                    country3 = 'N/A'

    except:
        country3 = 'N/A'

    #Find ICO Team Size
    team3 = 'N/A'
    try:
        value_s5a =  soup_s3.findAll("table", {"class": "table table-asset-data"})
        for tag5a in value_s5a:
            if 'Members' in tag5a.text:
                full_length = len(tag5a.text.replace(" ","").strip("").split("Members")[1].split("Countryoforigin")[0].split("\n"))
                gaps = tag5a.text.replace(" ","").strip("").split("Members")[1].split("Countryoforigin")[0].split("\n").count("")
                team3 = full_length - gaps

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
