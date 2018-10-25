from icobench import func_icobench
from icodrops import func_icodrops
from tokenmarket import func_tokenmarket
from icorating import func_icorating
from icomarks import func_icomarks
from icobazaar import func_icobazaar
from googletwitter import func_googletwitter
from top10_returns import func_top10
from bitcoin_returns import func_btc
from scrap_icos_main_func import ico_data_collector
import numpy as np
from numpy import *
import pandas as pd

currency = 'verge'
token = 'xvg'

bitcoin = func_btc()
top10s = func_top10()

#rt10 = func_top10()
#print(rt10)

#print(ico_data_collector(['delphy','dpy','delphy'],bitcoin,top10s))


res = func_icobench(currency)
res2 = func_icodrops(currency)
res3 = func_tokenmarket(currency)
res4 = func_icorating(currency,token)
res5 = func_icomarks(currency)
res6 = func_icobazaar(currency)
res7 = func_googletwitter(currency)
print(res,res2,res3,res4,res5,res6,res7)


#print(ico_data_collector(['bitcoin','btc','bitcoin'])[1])

        

