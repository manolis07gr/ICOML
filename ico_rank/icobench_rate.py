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

def func_icobench_rate(currency):

#################################################################################################
###ICO Bench Start###############################################################################
#################################################################################################

    try:
        source = 'ICObench.com'
        response = requests.get('https://icobench.com/ico/'+currency)
        txt = response.text
        soup_c = BeautifulSoup(txt, 'html.parser')
    except:
        txt = 'N/A'
        soup_c = 'N/A'

    rating0 = 'N/A'
        
            
    #------------------------------------------------------------------------------------------------
    ###ICObench Rating ##################################################################
    #------------------------------------------------------------------------------------------------

    try:
        value_eee =  soup_c.findAll("div", {"class": "rate color3"})
        for tag in value_eee:
            rating0 = round(eval(tag.text.replace("\n","").replace(" ",""))/5.0,2)
    except:
        rating0 = 'N/A'

    #------------------------------------------------------------------------------------------------
    ###ICO Bench END################################################################################
    #------------------------------------------------------------------------------------------------

    rating = rating0


    return rating
