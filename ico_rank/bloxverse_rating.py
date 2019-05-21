import csv
from csv import *
from numpy import *
import numpy as np
import sys
from matplotlib import pyplot as plt
import matplotlib.cm as cm
from region_category import func_region
from industry_category import func_industry
from scrap_icos_main_func import ico_data_collector
from top10_returns import func_top10
from bitcoin_returns import func_btc
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import DBSCAN
from sklearn import metrics
from sklearn import datasets, linear_model
from sklearn.model_selection import train_test_split 
import pandas as pd
from scipy.spatial import distance
import seaborn as sns
import datetime as dt
from datetime import datetime

def ico_rank_full(user_input):

    kk = - 1
    ranks = []
    for i in range(0,len(user_input)):
        kk = kk + 1
        ranks.append(kk)

        z = []
        bins = []

        if i not in [0,1,6]:

            if i == 2:
                feature_in = eval(user_input[2])
                z = np.loadtxt('scaling_dataset/team_z.npy')
                bins = np.loadtxt('scaling_dataset/team_bin.npy')
            if i == 3:
                feature_in = np.log10(eval(user_input[3]))
                z = np.loadtxt('scaling_dataset/hardcap_z.npy')
                bins = np.loadtxt('scaling_dataset/hardcap_bin.npy')
            if i == 4:
                feature_in = np.log10(eval(user_input[4]))
                z = np.loadtxt('scaling_dataset/price_z.npy')
                bins = np.loadtxt('scaling_dataset/price_bin.npy')
            if i == 5:
                feature_in = np.log10(eval(user_input[5]))
                z = np.loadtxt('scaling_dataset/telegram_z.npy')
                bins = np.loadtxt('scaling_dataset/telegram_bin.npy')
            if i == 7:
                z = np.loadtxt('scaling_dataset/twitter_z.npy')
                bins = np.loadtxt('scaling_dataset/twitter_bin.npy')
                feature_in = np.log10(eval(user_input[7]))
            if i == 8:
                feature_in = np.log10(eval(user_input[8]))
                z = np.loadtxt('scaling_dataset/dailyviews_z.npy')
                bins = np.loadtxt('scaling_dataset/dailyviews_bin.npy')
            if i == 9:
                feature_in = np.log10(eval(user_input[9]))
                z = np.loadtxt('scaling_dataset/dailytime_z.npy')
                bins = np.loadtxt('scaling_dataset/dailytime_bin.npy')


            order = np.argsort(z)

            group = 0
            for i in range(0,5):
                if (bins[0] <= feature_in < bins[1]):
                    group = 1
                if (bins[1] <= feature_in < bins[2]):
                    group = 2
                if (bins[2] <= feature_in < bins[3]):
                    group = 3
                if (bins[3] <= feature_in < bins[4]):
                    group = 4
                if (bins[4] <= feature_in < bins[5]):
                    group = 5
                if (feature_in < bins[0]) or (feature_in > bins[5]):
                    group = 0

            location = group - 1

            try:
                grade = np.where(order == location)[0][0] + 1
            except:
                grade = 0


        if i == 0:

            region_in = eval(user_input[0])

            grade = 0

            if region_in == 7:
                grade = 5
            if region_in in [1,5]:
                grade = 4
            if region_in in [4,6]:
                grade = 3
            if region_in in [2,3]:
                grade = 2
            if region_in in [8,9]:
                grade = 1
            if region_in in [10,11,12]:
                grade = 0


        if i == 1:

            industry_in = func_industry(user_input[1])

            tag = 1

            if industry_in == 'blockchain':
                tag = 0
            if industry_in == 'other':
                tag = 1
            if industry_in  == 'saas':
                tag = 2
            if industry_in == 'fintech':
                tag = 3
            if industry_in == 'gaming':
                tag = 4
            if industry_in == 'social services':
                tag = 5
            if industry_in == 'energy':
                tag = 6
            if industry_in == 'insurance services':
                tag = 7
            if industry_in == 'telecommunications':
                tag = 8
            if industry_in == 'transportation':
                tag = 9
            if industry_in == 'real estate':
                tag = 10

            grade = 0

            if industry_in in ['blockchain']:
                grade = 5
            if industry_in in  ['fintech']:
                grade = 4
            if industry_in in  ['saas']:
                grade = 3
            if industry_in in  ['gaming']:
                grade = 2
            if industry_in in  ['insurance services','telecommunications']:
                grade = 1
            if industry_in not in ['blockchain','fintech','saas','gaming','insurance services','telecommunications']:
                grade = 0

        ranks[kk] = grade

    ico_rating = np.mean(ranks)
    ico_rating0 = ico_rating/5.0

    return round(ico_rating0,2)


def ico_rank_quarter(user_input,ico_end_date):

    ico_end_date = ico_end_date.replace(" ","")
    ico_end_date_o = datetime.strptime(ico_end_date, '%d%b%Y')
    ico_year = str(ico_end_date_o.year)
    
    bound1 = ('01 Jan '+ico_year).replace(" ","")
    bound1_o = datetime.strptime(bound1, '%d%b%Y')

    bound2 = ('31 Mar '+ico_year).replace(" ","")
    bound2_o = datetime.strptime(bound2, '%d%b%Y')

    bound3 = ('01 Apr '+ico_year).replace(" ","")
    bound3_o = datetime.strptime(bound3, '%d%b%Y')

    bound4 = ('30 Jun '+ico_year).replace(" ","")
    bound4_o = datetime.strptime(bound4, '%d%b%Y')

    bound5 = ('01 Jul '+ico_year).replace(" ","")
    bound5_o = datetime.strptime(bound5, '%d%b%Y')

    bound6 = ('30 Sep '+ico_year).replace(" ","")
    bound6_o = datetime.strptime(bound6, '%d%b%Y')

    bound7 = ('01 Oct '+ico_year).replace(" ","")
    bound7_o = datetime.strptime(bound7, '%d%b%Y')

    bound8 = ('31 Dec '+ico_year).replace(" ","")
    bound8_o = datetime.strptime(bound8, '%d%b%Y')    

    if bound1_o <= ico_end_date_o <= bound2_o:
        q_str = 'q_1_'
    if bound3_o <= ico_end_date_o <= bound4_o:
        q_str = 'q_2_'
    if bound5_o <= ico_end_date_o <= bound6_o:
        q_str = 'q_3_'
    if bound7_o <= ico_end_date_o <= bound8_o:
        q_str = 'q_4_'
    if  ico_end_date_o > bound8_o:
        q_str = 'q_4_'

    if ico_year == '2016':
        yr_str = '16'
    if ico_year == '2017':
        yr_str = '17'
    if ico_year == '2018':
        yr_str = '18'

    kk = - 1
    ranks = []
    for i in range(0,len(user_input)):
        kk = kk + 1
        ranks.append(kk)

        z = []
        bins = []

        if i not in [0,1,6]:

            if i == 2:
                feature_in = eval(user_input[2])
                z = np.loadtxt('scaling_dataset/team_z_'+q_str+yr_str+'.npy')
                bins = np.loadtxt('scaling_dataset/team_bin_'+q_str+yr_str+'.npy')
            if i == 3:
                feature_in = np.log10(eval(user_input[3]))
                z = np.loadtxt('scaling_dataset/hardcap_z_'+q_str+yr_str+'.npy')
                bins = np.loadtxt('scaling_dataset/hardcap_bin_'+q_str+yr_str+'.npy')
            if i == 4:
                feature_in = np.log10(eval(user_input[4]))
                z = np.loadtxt('scaling_dataset/price_z_'+q_str+yr_str+'.npy')
                bins = np.loadtxt('scaling_dataset/price_bin_'+q_str+yr_str+'.npy')
            if i == 5:
                feature_in = np.log10(eval(user_input[5]))
                z = np.loadtxt('scaling_dataset/telegram_z_'+q_str+yr_str+'.npy')
                bins = np.loadtxt('scaling_dataset/telegram_bin_'+q_str+yr_str+'.npy')
            if i == 7:
                z = np.loadtxt('scaling_dataset/twitter_z_'+q_str+yr_str+'.npy')
                bins = np.loadtxt('scaling_dataset/twitter_bin_'+q_str+yr_str+'.npy')
                feature_in = np.log10(eval(user_input[7]))
            if i == 8:
                feature_in = np.log10(eval(user_input[8]))
                z = np.loadtxt('scaling_dataset/dailyviews_z_'+q_str+yr_str+'.npy')
                bins = np.loadtxt('scaling_dataset/dailyviews_bin_'+q_str+yr_str+'.npy')
            if i == 9:
                feature_in = np.log10(eval(user_input[9]))
                z = np.loadtxt('scaling_dataset/dailytime_z_'+q_str+yr_str+'.npy')
                bins = np.loadtxt('scaling_dataset/dailytime_bin_'+q_str+yr_str+'.npy')


            order = np.argsort(z)

            group = 0
            for i in range(0,5):
                if (bins[0] <= feature_in < bins[1]):
                    group = 1
                if (bins[1] <= feature_in < bins[2]):
                    group = 2
                if (bins[2] <= feature_in < bins[3]):
                    group = 3
                if (bins[3] <= feature_in < bins[4]):
                    group = 4
                if (bins[4] <= feature_in < bins[5]):
                    group = 5
                if (feature_in < bins[0]) or (feature_in > bins[5]):
                    group = 0

            location = group - 1

            try:
                grade = np.where(order == location)[0][0] + 1
            except:
                grade = 0


        if i == 0:

            region_in = eval(user_input[0])

            grade = 0

            if region_in == 7:
                grade = 5
            if region_in in [1,5]:
                grade = 4
            if region_in in [4,6]:
                grade = 3
            if region_in in [2,3]:
                grade = 2
            if region_in in [8,9]:
                grade = 1
            if region_in in [10,11,12]:
                grade = 0


        if i == 1:

            industry_in = func_industry(user_input[1])

            tag = 1

            if industry_in == 'blockchain':
                tag = 0
            if industry_in == 'other':
                tag = 1
            if industry_in  == 'saas':
                tag = 2
            if industry_in == 'fintech':
                tag = 3
            if industry_in == 'gaming':
                tag = 4
            if industry_in == 'social services':
                tag = 5
            if industry_in == 'energy':
                tag = 6
            if industry_in == 'insurance services':
                tag = 7
            if industry_in == 'telecommunications':
                tag = 8
            if industry_in == 'transportation':
                tag = 9
            if industry_in == 'real estate':
                tag = 10

            grade = 0

            if industry_in in ['blockchain']:
                grade = 5
            if industry_in in  ['fintech']:
                grade = 4
            if industry_in in  ['saas']:
                grade = 3
            if industry_in in  ['gaming']:
                grade = 2
            if industry_in in  ['insurance services','telecommunications']:
                grade = 1
            if industry_in not in ['blockchain','fintech','saas','gaming','insurance services','telecommunications']:
                grade = 0

        ranks[kk] = grade

    ico_rating = np.mean(ranks)
    ico_rating0 = ico_rating/5.0

    return round(ico_rating0,2)

def ico_rank_semiannual(user_input,ico_end_date):

    ico_end_date = ico_end_date.replace(" ","")
    ico_end_date_o = datetime.strptime(ico_end_date, '%d%b%Y')
    ico_year = str(ico_end_date_o.year)
    
    bound1 = ('01 Jan '+ico_year).replace(" ","")
    bound1_o = datetime.strptime(bound1, '%d%b%Y')

    bound2 = ('31 Mar '+ico_year).replace(" ","")
    bound2_o = datetime.strptime(bound2, '%d%b%Y')

    bound3 = ('01 Apr '+ico_year).replace(" ","")
    bound3_o = datetime.strptime(bound3, '%d%b%Y')

    bound4 = ('30 Jun '+ico_year).replace(" ","")
    bound4_o = datetime.strptime(bound4, '%d%b%Y')

    bound5 = ('01 Jul '+ico_year).replace(" ","")
    bound5_o = datetime.strptime(bound5, '%d%b%Y')

    bound6 = ('30 Sep '+ico_year).replace(" ","")
    bound6_o = datetime.strptime(bound6, '%d%b%Y')

    bound7 = ('01 Oct '+ico_year).replace(" ","")
    bound7_o = datetime.strptime(bound7, '%d%b%Y')

    bound8 = ('31 Dec '+ico_year).replace(" ","")
    bound8_o = datetime.strptime(bound8, '%d%b%Y')    

    if bound1_o <= ico_end_date_o <= bound2_o:
        sa_str = 'sa_1_'
    if bound3_o <= ico_end_date_o <= bound4_o:
        sa_str = 'sa_2_'
    if bound5_o <= ico_end_date_o <= bound6_o:
        sa_str = 'sa_3_'
    if bound7_o <= ico_end_date_o <= bound8_o:
        sa_str = 'sa_4_'
    if  ico_end_date_o > bound8_o:
        sa_str = 'sa_4_'
    

    if ico_year == '2016':
        yr_str = '16'
    if ico_year == '2017':
        yr_str = '17'
    if ico_year == '2018':
        yr_str = '18'

    kk = - 1
    ranks = []
    for i in range(0,len(user_input)):
        kk = kk + 1
        ranks.append(kk)

        z = []
        bins = []

        if i not in [0,1,6]:

            if i == 2:
                feature_in = eval(user_input[2])
                z = np.loadtxt('scaling_dataset/team_z_'+sa_str+yr_str+'.npy')
                bins = np.loadtxt('scaling_dataset/team_bin_'+sa_str+yr_str+'.npy')
            if i == 3:
                feature_in = np.log10(eval(user_input[3]))
                z = np.loadtxt('scaling_dataset/hardcap_z_'+sa_str+yr_str+'.npy')
                bins = np.loadtxt('scaling_dataset/hardcap_bin_'+sa_str+yr_str+'.npy')
            if i == 4:
                feature_in = np.log10(eval(user_input[4]))
                z = np.loadtxt('scaling_dataset/price_z_'+sa_str+yr_str+'.npy')
                bins = np.loadtxt('scaling_dataset/price_bin_'+sa_str+yr_str+'.npy')
            if i == 5:
                feature_in = np.log10(eval(user_input[5]))
                z = np.loadtxt('scaling_dataset/telegram_z_'+sa_str+yr_str+'.npy')
                bins = np.loadtxt('scaling_dataset/telegram_bin_'+sa_str+yr_str+'.npy')
            if i == 7:
                z = np.loadtxt('scaling_dataset/twitter_z_'+sa_str+yr_str+'.npy')
                bins = np.loadtxt('scaling_dataset/twitter_bin_'+sa_str+yr_str+'.npy')
                feature_in = np.log10(eval(user_input[7]))
            if i == 8:
                feature_in = np.log10(eval(user_input[8]))
                z = np.loadtxt('scaling_dataset/dailyviews_z_'+sa_str+yr_str+'.npy')
                bins = np.loadtxt('scaling_dataset/dailyviews_bin_'+sa_str+yr_str+'.npy')
            if i == 9:
                feature_in = np.log10(eval(user_input[9]))
                z = np.loadtxt('scaling_dataset/dailytime_z_'+sa_str+yr_str+'.npy')
                bins = np.loadtxt('scaling_dataset/dailytime_bin_'+sa_str+yr_str+'.npy')


            order = np.argsort(z)

            group = 0
            for i in range(0,5):
                if (bins[0] <= feature_in < bins[1]):
                    group = 1
                if (bins[1] <= feature_in < bins[2]):
                    group = 2
                if (bins[2] <= feature_in < bins[3]):
                    group = 3
                if (bins[3] <= feature_in < bins[4]):
                    group = 4
                if (bins[4] <= feature_in < bins[5]):
                    group = 5
                if (feature_in < bins[0]) or (feature_in > bins[5]):
                    group = 0

            location = group - 1

            try:
                grade = np.where(order == location)[0][0] + 1
            except:
                grade = 0


        if i == 0:

            region_in = eval(user_input[0])

            grade = 0

            if region_in == 7:
                grade = 5
            if region_in in [1,5]:
                grade = 4
            if region_in in [4,6]:
                grade = 3
            if region_in in [2,3]:
                grade = 2
            if region_in in [8,9]:
                grade = 1
            if region_in in [10,11,12]:
                grade = 0


        if i == 1:

            industry_in = func_industry(user_input[1])

            tag = 1

            if industry_in == 'blockchain':
                tag = 0
            if industry_in == 'other':
                tag = 1
            if industry_in  == 'saas':
                tag = 2
            if industry_in == 'fintech':
                tag = 3
            if industry_in == 'gaming':
                tag = 4
            if industry_in == 'social services':
                tag = 5
            if industry_in == 'energy':
                tag = 6
            if industry_in == 'insurance services':
                tag = 7
            if industry_in == 'telecommunications':
                tag = 8
            if industry_in == 'transportation':
                tag = 9
            if industry_in == 'real estate':
                tag = 10

            grade = 0

            if industry_in in ['blockchain']:
                grade = 5
            if industry_in in  ['fintech']:
                grade = 4
            if industry_in in  ['saas']:
                grade = 3
            if industry_in in  ['gaming']:
                grade = 2
            if industry_in in  ['insurance services','telecommunications']:
                grade = 1
            if industry_in not in ['blockchain','fintech','saas','gaming','insurance services','telecommunications']:
                grade = 0

        ranks[kk] = grade

    ico_rating = np.mean(ranks)
    ico_rating0 = ico_rating/5.0

    return round(ico_rating0,2)
