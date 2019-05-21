from icobench import func_icobench
from icodrops import func_icodrops
from tokenmarket import func_tokenmarket
from icorating import func_icorating
from icomarks import func_icomarks
from icomarks_rate import func_icomarks_rate
from icobench_rate import func_icobench_rate
from icobazaar import func_icobazaar
from googletwitter import func_googletwitter
from top10_returns import func_top10
from bitcoin_returns import func_btc
from scrap_icos_main_func import ico_data_collector
import numpy as np
from numpy import *
import pandas as pd
from bloxverse_rating import ico_rank_full, ico_rank_quarter, ico_rank_semiannual
import csv
from csv import *

user_input = ['12', 'blockchain', '4', '35000000.0', '2.1', '28832', '0', '53293', '1.9', '163.0']
##user_input = ['7', 'saas', '24', '30010280.0', '0.1', '25473', '8', '15439', '2.4', '210.0']
print(ico_rank_full(user_input))
print(ico_rank_semiannual(user_input,'21 Jan 2018'))
print(ico_rank_quarter(user_input,'21 Jan 2018'))

currency = 'radioyo'
token = 'radioyo'

#bitcoin = func_btc()
#top10s = func_top10()
#rt10 = func_top10()
#print(rt10)

#print(ico_data_collector(['coti','coti','coti'],bitcoin,top10s))


"""
res = func_icobench(currency)
res2 = func_icodrops(currency)
res3 = func_tokenmarket(currency)
res4 = func_icorating(currency,token)
res5 = func_icomarks(currency)
res6 = func_icobazaar(currency)
res7 = func_googletwitter(currency)
print(res,res2,res3,res4,res5,res6,res7)
"""

#print(ico_data_collector(['bitcoin','btc','bitcoin'])[1])

        

