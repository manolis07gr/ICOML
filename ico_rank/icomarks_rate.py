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

def func_icomarks_rate(currency):
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
        started,ended,lasted,country,team,raised,hardcap,price,rating = ['N/A','N/A','N/A','N/A','N/A','N/A','N/A','N/A','N/A']

    rating0 = 'N/A'

    #Find ICO Rating
    rating0 = 'N/A'

    try:
        value_rat = soup_s5.findAll("div", {"class": "ico-rating-overall"})
        for tag_rat in value_rat:
            rating0b = round(eval(tag_rat.text.replace("\n","").replace(" ",""))/10.,2)
     
        rating0 = rating0b
                	                        
    except:   
        rating0 = 'N/A'
    
    rating = rating0

#------------------------------------------------------------------------------------------------
##ICOMarks END###################################################################################
#------------------------------------------------------------------------------------------------

    return rating
