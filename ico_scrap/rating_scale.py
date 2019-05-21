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


#1. FULL DATASET

features_vec = ['region','industry','team','hardcap','price','telegram','N_google_news','N_twitter','N_daily_views','N_daily_time']
kk = -1
ranks = []
z_out = []
bins_out = []
for feature in features_vec:
    kk = kk + 1
    ranks.append(kk)
    z_out.append(kk)
    bins_out.append(kk)

    success_threshold = 0.7

    with open("outdata/ico_data_reduced.csv") as f:
        reader = csv.reader(f)
        data = [r for r in reader]

    data = np.asarray(data)

    indices, = np.where(data[:,10] != 'N/A')
    indices = np.delete(indices,0)

    success = [eval(data[i][20]) for i in indices]


    try:
        ind_feature = np.where(data[0,:]==feature)[0][0]
    except:
        print('ERROR: This feature does not exist in this dataset')
        sys.exit()

    if feature in ['hype','risk']:
        for i in range(0,len(data)):
            if data[i,ind_feature] == ' N/A' or data[i,ind_feature] == 'other':
                data[i,ind_feature] = 'N/A'

    indices_f, = np.where(data[:,ind_feature] != 'N/A')
    indices_f = np.delete(indices_f,0)

    indices_over = []
    k = -1
    for i in range(0,len(indices)):
        for j in range(0,len(indices_f)):
            if indices_f[j] == indices[i]:
                k = k + 1
                indices_over.append(k)
                indices_over[k] = indices[i]

    success0 = [eval(data[i][10]) for i in indices_over]
    variable0 = [data[i][ind_feature] for i in indices_over]

    #Feature Controls
    if feature in ['team','N_google_news']: #,'N_daily_views']:
        for i in range(0,len(variable0)):
            variable0[i] = abs(eval(variable0[i]))

    if feature == 'N_daily_views':
        for i in range(0,len(variable0)):
            variable0[i] = np.log10(eval(variable0[i]))

    if feature in ['hardcap','N_daily_time']:
        for i in range(0,len(variable0)):
            variable0[i] = eval(variable0[i])
            variable0[i] = np.log10(variable0[i])


    if feature in ['price','telegram','N_twitter']:
        for i in range(0,len(variable0)):
            if (variable0[i] == '0') or (variable0[i] == '0.0'):
                variable0[i] = str(1)
            variable0[i] = np.log10(eval(variable0[i]))

    if feature == 'bazaar-rate':
        for i in range(0,len(variable0)):
            variable0[i] = eval(variable0[i])



    #Now reduce feature array to > 70% success values
    success0 = np.asarray(success0)
    indices2, = np.where(success0 > success_threshold)

    success0b = []
    variable0b = []
    k = -1
    for i in range(0,len(success0)):
        if i in indices2:
            k = k + 1
            success0b.append(k)
            variable0b.append(k)
            success0b[k] = success0[i]
            variable0b[k] = variable0[i]


    try:
        avg = np.median(variable0b)
        stdev = np.std(variable0b)
        f = [0.5,1.0,1.5,2.0,2.5]

        z,bins,p3 = plt.hist(variable0b, bins = 5, rwidth=0.9, facecolor = 'blue')
        plt.axvline(x=avg,linestyle = "-", linewidth = 2, color = 'k')


        plt.xlabel(feature,fontsize=17)
        plt.ylabel('Number',fontsize=15)
        plt.xticks(size = 15)
        plt.yticks(size = 15)
        #plt.show()
    except:
        if feature not in ['region','industry']:
            z,bins,p3 = plt.hist(variable0b, bins = 5, rwidth=0.9, facecolor = 'blue')
            plt.xlabel(feature,fontsize=17)
            plt.ylabel('Number',fontsize=15)
            plt.xticks(size = 15)
            plt.yticks(size = 15)
        if feature == 'region':
            z,bins,p3 = plt.hist(variable0b, bins = 12, rwidth=0.9, facecolor = 'blue')
            plt.xlabel(feature,fontsize=17)
            plt.ylabel('Number',fontsize=15)
            plt.xticks(size = 15)
            plt.yticks(size = 15)
        if feature == 'industry':
            z,bins,p3 = plt.hist(variable0b, bins = 14, rwidth=0.9, facecolor = 'blue')
            plt.xlabel(feature,fontsize=17)
            plt.ylabel('Number',fontsize=15)
            plt.xticks(size = 15)
            plt.xticks(rotation=90)
            plt.tick_params(labelsize=7)
            plt.yticks(size = 15)

    z_out[kk] = z
    bins_out[kk] = bins


reg0 = np.asarray(z_out[0])
np.savetxt('scaling_dataset/region_z.npy', reg0)
reg1 = np.asarray(bins_out[0])
np.savetxt('scaling_dataset/region_bin.npy', reg1)

ind0 = np.asarray(z_out[1])
np.savetxt('scaling_dataset/industry_z.npy', ind0)
ind1 = np.asarray(bins_out[1])
np.savetxt('scaling_dataset/industry_bin.npy', ind1)

team0 = np.asarray(z_out[2])
np.savetxt('scaling_dataset/team_z.npy', team0)
team1 = np.asarray(bins_out[2])
np.savetxt('scaling_dataset/team_bin.npy', team1)

hard0 = np.asarray(z_out[3])
np.savetxt('scaling_dataset/hardcap_z.npy', hard0)
hard1 = np.asarray(bins_out[3])
np.savetxt('scaling_dataset/hardcap_bin.npy', hard1)

price0 = np.asarray(z_out[4])
np.savetxt('scaling_dataset/price_z.npy', price0)
price1 = np.asarray(bins_out[4])
np.savetxt('scaling_dataset/price_bin.npy', price1)

teleg0 = np.asarray(z_out[5])
np.savetxt('scaling_dataset/telegram_z.npy', teleg0)
teleg1 = np.asarray(bins_out[5])
np.savetxt('scaling_dataset/telegram_bin.npy', teleg1)

twit0 = np.asarray(z_out[7])
np.savetxt('scaling_dataset/twitter_z.npy', twit0)
twit1 = np.asarray(bins_out[7])
np.savetxt('scaling_dataset/twitter_bin.npy', twit1)

dv0 = np.asarray(z_out[8])
np.savetxt('scaling_dataset/dailyviews_z.npy', dv0)
dv1 = np.asarray(bins_out[8])
np.savetxt('scaling_dataset/dailyviews_bin.npy', dv1)

dt0 = np.asarray(z_out[9])
np.savetxt('scaling_dataset/dailytime_z.npy', dt0)
dt1 = np.asarray(bins_out[9])
np.savetxt('scaling_dataset/dailytime_bin.npy', dt1)

############# CREATE FILES FOR QUARTERLY/SEMIANNUAL RATINGS

def create_ico_q_sa_files(end_date_in,file_id):

    #Now the code will reduce the target data-set for rating and clustering only down to the same Quarter
    #As the ICO under investigation
    ico_end_date = end_date_in.replace(" ","")
    ico_end_date_o = datetime.strptime(ico_end_date, '%d%b%Y')
    ico_year = ico_end_date_o.year

    #Define quarter start/end dates from 2016 through 2019
    [y2016_q1_s,y2016_q1_e,y2016_q2_s,y2016_q2_e,y2016_q3_s,y2016_q3_e,y2016_q4_s,y2016_q4_e] = ['01Jan2016','31Mar2016','01Apr2016','30Jun2016','01Jul2016','30Sep2016','01Oct2016','31Dec2016']

    [y2016_q1_s_o,y2016_q1_e_o,y2016_q2_s_o,y2016_q2_e_o,y2016_q3_s_o,y2016_q3_e_o,y2016_q4_s_o,y2016_q4_e_o] = [datetime.strptime(y2016_q1_s, '%d%b%Y'),datetime.strptime(y2016_q1_e, '%d%b%Y'),datetime.strptime(y2016_q2_s, '%d%b%Y'),datetime.strptime(y2016_q2_e, '%d%b%Y'),datetime.strptime(y2016_q3_s, '%d%b%Y'),datetime.strptime(y2016_q3_e, '%d%b%Y'),datetime.strptime(y2016_q4_s, '%d%b%Y'),datetime.strptime(y2016_q4_e, '%d%b%Y')]

    y2016 = np.asarray([y2016_q1_s_o,y2016_q1_e_o,y2016_q2_s_o,y2016_q2_e_o,y2016_q3_s_o,y2016_q3_e_o,y2016_q4_s_o,y2016_q4_e_o])

    [y2017_q1_s,y2017_q1_e,y2017_q2_s,y2017_q2_e,y2017_q3_s,y2017_q3_e,y2017_q4_s,y2017_q4_e] = ['01Jan2017','31Mar2017','01Apr2017','30Jun2017','01Jul2017','30Sep2017','01Oct2017','31Dec2017']

    [y2017_q1_s_o,y2017_q1_e_o,y2017_q2_s_o,y2017_q2_e_o,y2017_q3_s_o,y2017_q3_e_o,y2017_q4_s_o,y2017_q4_e_o] = [datetime.strptime(y2017_q1_s, '%d%b%Y'),datetime.strptime(y2017_q1_e, '%d%b%Y'),datetime.strptime(y2017_q2_s, '%d%b%Y'),datetime.strptime(y2017_q2_e, '%d%b%Y'),datetime.strptime(y2017_q3_s, '%d%b%Y'),datetime.strptime(y2017_q3_e, '%d%b%Y'),datetime.strptime(y2017_q4_s, '%d%b%Y'),datetime.strptime(y2017_q4_e, '%d%b%Y')]

    y2017 = np.asarray([y2017_q1_s_o,y2017_q1_e_o,y2017_q2_s_o,y2017_q2_e_o,y2017_q3_s_o,y2017_q3_e_o,y2017_q4_s_o,y2017_q4_e_o])

    [y2018_q1_s,y2018_q1_e,y2018_q2_s,y2018_q2_e,y2018_q3_s,y2018_q3_e,y2018_q4_s,y2018_q4_e] = ['01Jan2018','31Mar2018','01Apr2018','30Jun2018','01Jul2018','30Sep2018','01Oct2018','31Dec2018']

    [y2018_q1_s_o,y2018_q1_e_o,y2018_q2_s_o,y2018_q2_e_o,y2018_q3_s_o,y2018_q3_e_o,y2018_q4_s_o,y2018_q4_e_o] = [datetime.strptime(y2018_q1_s, '%d%b%Y'),datetime.strptime(y2018_q1_e, '%d%b%Y'),datetime.strptime(y2018_q2_s, '%d%b%Y'),datetime.strptime(y2018_q2_e, '%d%b%Y'),datetime.strptime(y2018_q3_s, '%d%b%Y'),datetime.strptime(y2018_q3_e, '%d%b%Y'),datetime.strptime(y2018_q4_s, '%d%b%Y'),datetime.strptime(y2018_q4_e, '%d%b%Y')]

    y2018 = np.asarray([y2018_q1_s_o,y2018_q1_e_o,y2018_q2_s_o,y2018_q2_e_o,y2018_q3_s_o,y2018_q3_e_o,y2018_q4_s_o,y2018_q4_e_o])

    [y2019_q1_s,y2019_q1_e,y2019_q2_s,y2019_q2_e,y2019_q3_s,y2019_q3_e,y2019_q4_s,y2019_q4_e] = ['01Jan2019','31Mar2019','01Apr2019','30Jun2019','01Jul2019','30Sep2019','01Oct2019','31Dec2019']

    [y2019_q1_s_o,y2019_q1_e_o,y2019_q2_s_o,y2019_q2_e_o,y2019_q3_s_o,y2019_q3_e_o,y2019_q4_s_o,y2019_q4_e_o] = [datetime.strptime(y2019_q1_s, '%d%b%Y'),datetime.strptime(y2019_q1_e, '%d%b%Y'),datetime.strptime(y2019_q2_s, '%d%b%Y'),datetime.strptime(y2019_q2_e, '%d%b%Y'),datetime.strptime(y2019_q3_s, '%d%b%Y'),datetime.strptime(y2019_q3_e, '%d%b%Y'),datetime.strptime(y2019_q4_s, '%d%b%Y'),datetime.strptime(y2019_q4_e, '%d%b%Y')]

    y2019 = np.asarray([y2019_q1_s_o,y2019_q1_e_o,y2019_q2_s_o,y2019_q2_e_o,y2019_q3_s_o,y2019_q3_e_o,y2019_q4_s_o,y2019_q4_e_o])

    if ico_year == 2016:
        quarters = y2016
    if ico_year == 2017:
        quarters = y2017
    if ico_year == 2018:
        quarters = y2018
    if ico_year == 2019:
        quarters = y2019

    for i in range(0,len(quarters)-1):
        #print('TEST',quarters[i],quarters[i+1])
        #print('TEST 2',quarters[i] <= ico_end_date_o < quarters[i+1])
        if quarters[i] <= ico_end_date_o < quarters[i+1]:
            q_start = quarters[i]
            q_start_index = i
            q_end = quarters[i+1]
            q_end_index = i+1

    #q_start and q_end give the beggining and the end of the quarter that the ICO end date belongs to
    #Now we need to instruct the ico_data_rate_cluster database to reduce to ICO data that correspond
    #to the immediately previous quarter OR the immediately two previous quarters.

    #Immediately previous quarter
    if q_start != datetime.strptime('01Jan'+str(ico_year), '%d%b%Y'):
        q_start_target = quarters[q_start_index-1]
        q_end_target = quarters[q_end_index-1]

    if q_start == datetime.strptime('01Jan'+str(ico_year), '%d%b%Y'):
        q_start_target = datetime.strptime('01Oct'+str(ico_year-1), '%d%b%Y')
        q_end_target = datetime.strptime('31Dec'+str(ico_year-1), '%d%b%Y')

    #print('test',q_start,q_end,q_start_target,q_end_target)

    #2 quarters ago
    if q_start not in [datetime.strptime('01Jan'+str(ico_year), '%d%b%Y'),datetime.strptime('01Apr'+str(ico_year), '%d%b%Y')]:
        q_start_target2 = quarters[q_start_index-2]
        q_end_target2 = quarters[q_end_index-2]

    if (q_start == datetime.strptime('01Jan'+str(ico_year), '%d%b%Y')):
        q_start_target2 = datetime.strptime('01Jul'+str(ico_year-1), '%d%b%Y')
        q_end_target2 = datetime.strptime('30Sep'+str(ico_year-1), '%d%b%Y')

    if (q_start == datetime.strptime('01Apr'+str(ico_year), '%d%b%Y')):
        q_start_target2 = datetime.strptime('01Oct'+str(ico_year-1), '%d%b%Y')
        q_end_target2 = datetime.strptime('31Dec'+str(ico_year-1), '%d%b%Y')


    with open("outdata/ico_data_reduced.csv") as ffff:
        reader_ff = csv.reader(ffff)
        data_ff = [r for r in reader_ff]

    data_ff = np.asarray(data_ff)

    columnTitles_rateCluster22 = "coin,start,end,duration,age,region,industry,team,raised,hardcap,success,price,telegram,N_google_news,N_twitter,N_daily_views,N_daily_time,hype,risk,bazaar-rate,ret_ico_to_day_one,vol_day1,sharpe_1,sharpe_3,sharpe_yr,sharpe_yr2,beta_btc,beta_top10,alpha_btc,alpha_top10\n"

    with open('scaling_dataset/ico_data_reduced_q_'+file_id+'.csv', 'w') as csvfile_bbb:
        csvfile_bbb.write(columnTitles_rateCluster22)
        writer_b=csv.writer(csvfile_bbb, delimiter=',')

        for i in range(1,len(data_ff)):
            end_date_a = data_ff[i][2].replace(" ","")
            end_day_o = datetime.strptime(end_date_a, '%d%b%Y')
            if (q_start_target <= end_day_o < q_end_target):
                all_data = [data_ff[i][0],data_ff[i][1],data_ff[i][2],data_ff[i][3],data_ff[i][4],data_ff[i][5],data_ff[i][6],data_ff[i][7],data_ff[i][8],data_ff[i][9],data_ff[i][10],data_ff[i][11],data_ff[i][12],data_ff[i][13],data_ff[i][14],data_ff[i][15],data_ff[i][16],data_ff[i][17],data_ff[i][18],data_ff[i][19],data_ff[i][20],data_ff[i][21],data_ff[i][22],data_ff[i][23],data_ff[i][24],data_ff[i][25],data_ff[i][26],data_ff[i][27],data_ff[i][28],data_ff[i][29]]
                writer_b.writerow(all_data)

    columnTitles_rateCluster222 = "coin,start,end,duration,age,region,industry,team,raised,hardcap,success,price,telegram,N_google_news,N_twitter,N_daily_views,N_daily_time,hype,risk,bazaar-rate,ret_ico_to_day_one,vol_day1,sharpe_1,sharpe_3,sharpe_yr,sharpe_yr2,beta_btc,beta_top10,alpha_btc,alpha_top10\n"

    with open('scaling_dataset/ico_data_reduced_sa_'+file_id+'.csv', 'w') as csvfile_bb22:
        csvfile_bb22.write(columnTitles_rateCluster222)
        writer2b=csv.writer(csvfile_bb22, delimiter=',')

        for i in range(1,len(data_ff)):
            end_date_a = data_ff[i][2].replace(" ","")
            end_day_o = datetime.strptime(end_date_a, '%d%b%Y')
            if (q_start_target2 <= end_day_o < q_end_target2):
                all_data2 = [data_ff[i][0],data_ff[i][1],data_ff[i][2],data_ff[i][3],data_ff[i][4],data_ff[i][5],data_ff[i][6],data_ff[i][7],data_ff[i][8],data_ff[i][9],data_ff[i][10],data_ff[i][11],data_ff[i][12],data_ff[i][13],data_ff[i][14],data_ff[i][15],data_ff[i][16],data_ff[i][17],data_ff[i][18],data_ff[i][19],data_ff[i][20],data_ff[i][21],data_ff[i][22],data_ff[i][23],data_ff[i][24],data_ff[i][25],data_ff[i][26],data_ff[i][27],data_ff[i][28],data_ff[i][29]]
                writer2b.writerow(all_data2)

    return

arg1 = ['01Feb2016','01May2016','01Aug2016','01Nov2016','01Feb2017','01May2017','01Aug2017','01Nov2017','01Feb2018','01May2018','01Aug2018','01Nov2018']
arg2 = ['1_16','2_16','3_16','4_16','1_17','2_17','3_17','4_17','1_18','2_18','3_18','4_18']

#for i in range(0,len(arg1)):
#    create_ico_q_sa_files(arg1[i],arg2[i])


# ALL COMPARISON BASIS DATA FILES HAVE NOW BEEN GENERATED
### QUARTERLY ARRAYS WILL NOW BE GENERATED

def generate_sa(quarter):

    features_vec = ['region','industry','team','hardcap','price','telegram','N_google_news','N_twitter','N_daily_views','N_daily_time']
    kk = -1
    ranks = []
    z_out = []
    bins_out = []
    for feature in features_vec:
        kk = kk + 1
        ranks.append(kk)
        z_out.append(kk)
        bins_out.append(kk)

        success_threshold = 0.7

        with open("scaling_dataset/ico_data_reduced_sa_"+quarter+".csv") as f:
            reader = csv.reader(f)
            data = [r for r in reader]

        data = np.asarray(data)

        indices, = np.where(data[:,10] != 'N/A')
        indices = np.delete(indices,0)

        success = [eval(data[i][20]) for i in indices]


        try:
            ind_feature = np.where(data[0,:]==feature)[0][0]
        except:
            print('ERROR: This feature does not exist in this dataset')
            sys.exit()

        if feature in ['hype','risk']:
            for i in range(0,len(data)):
                if data[i,ind_feature] == ' N/A' or data[i,ind_feature] == 'other':
                    data[i,ind_feature] = 'N/A'

        indices_f, = np.where(data[:,ind_feature] != 'N/A')
        indices_f = np.delete(indices_f,0)

        indices_over = []
        k = -1
        for i in range(0,len(indices)):
            for j in range(0,len(indices_f)):
                if indices_f[j] == indices[i]:
                    k = k + 1
                    indices_over.append(k)
                    indices_over[k] = indices[i]

        success0 = [eval(data[i][10]) for i in indices_over]
        variable0 = [data[i][ind_feature] for i in indices_over]

        #Feature Controls
        if feature in ['team','N_google_news']: #,'N_daily_views']:
            for i in range(0,len(variable0)):
                variable0[i] = abs(eval(variable0[i]))

        if feature == 'N_daily_views':
            for i in range(0,len(variable0)):
                variable0[i] = np.log10(eval(variable0[i]))

        if feature in ['hardcap','N_daily_time']:
            for i in range(0,len(variable0)):
                variable0[i] = eval(variable0[i])
                variable0[i] = np.log10(variable0[i])


        if feature in ['price','telegram','N_twitter']:
            for i in range(0,len(variable0)):
                if (variable0[i] == '0') or (variable0[i] == '0.0'):
                    variable0[i] = str(1)
                variable0[i] = np.log10(eval(variable0[i]))

        if feature == 'bazaar-rate':
            for i in range(0,len(variable0)):
                variable0[i] = eval(variable0[i])



        #Now reduce feature array to > 70% success values
        success0 = np.asarray(success0)
        indices2, = np.where(success0 > success_threshold)

        success0b = []
        variable0b = []
        k = -1
        for i in range(0,len(success0)):
            if i in indices2:
                k = k + 1
                success0b.append(k)
                variable0b.append(k)
                success0b[k] = success0[i]
                variable0b[k] = variable0[i]


        try:
            avg = np.median(variable0b)
            stdev = np.std(variable0b)
            f = [0.5,1.0,1.5,2.0,2.5]

            z,bins,p3 = plt.hist(variable0b, bins = 5, rwidth=0.9, facecolor = 'blue')
            plt.axvline(x=avg,linestyle = "-", linewidth = 2, color = 'k')


            plt.xlabel(feature,fontsize=17)
            plt.ylabel('Number',fontsize=15)
            plt.xticks(size = 15)
            plt.yticks(size = 15)
            #plt.show()
        except:
            if feature not in ['region','industry']:
                z,bins,p3 = plt.hist(variable0b, bins = 5, rwidth=0.9, facecolor = 'blue')
                plt.xlabel(feature,fontsize=17)
                plt.ylabel('Number',fontsize=15)
                plt.xticks(size = 15)
                plt.yticks(size = 15)
            if feature == 'region':
                z,bins,p3 = plt.hist(variable0b, bins = 12, rwidth=0.9, facecolor = 'blue')
                plt.xlabel(feature,fontsize=17)
                plt.ylabel('Number',fontsize=15)
                plt.xticks(size = 15)
                plt.yticks(size = 15)
            if feature == 'industry':
                z,bins,p3 = plt.hist(variable0b, bins = 14, rwidth=0.9, facecolor = 'blue')
                plt.xlabel(feature,fontsize=17)
                plt.ylabel('Number',fontsize=15)
                plt.xticks(size = 15)
                plt.xticks(rotation=90)
                plt.tick_params(labelsize=7)
                plt.yticks(size = 15)

        z_out[kk] = z
        bins_out[kk] = bins


    reg0 = np.asarray(z_out[0])
    np.savetxt('scaling_dataset/region_z_sa_'+quarter+'.npy', reg0)
    reg1 = np.asarray(bins_out[0])
    np.savetxt('scaling_dataset/region_bin_sa_'+quarter+'.npy', reg1)

    ind0 = np.asarray(z_out[1])
    np.savetxt('scaling_dataset/industry_z_sa_'+quarter+'.npy', ind0)
    ind1 = np.asarray(bins_out[1])
    np.savetxt('scaling_dataset/industry_bin_sa_'+quarter+'.npy', ind1)

    team0 = np.asarray(z_out[2])
    np.savetxt('scaling_dataset/team_z_sa_'+quarter+'.npy', team0)
    team1 = np.asarray(bins_out[2])
    np.savetxt('scaling_dataset/team_bin_sa_'+quarter+'.npy', team1)

    hard0 = np.asarray(z_out[3])
    np.savetxt('scaling_dataset/hardcap_z_sa_'+quarter+'.npy', hard0)
    hard1 = np.asarray(bins_out[3])
    np.savetxt('scaling_dataset/hardcap_bin_sa_'+quarter+'.npy', hard1)

    price0 = np.asarray(z_out[4])
    np.savetxt('scaling_dataset/price_z_sa_'+quarter+'.npy', price0)
    price1 = np.asarray(bins_out[4])
    np.savetxt('scaling_dataset/price_bin_sa_'+quarter+'.npy', price1)

    teleg0 = np.asarray(z_out[5])
    np.savetxt('scaling_dataset/telegram_z_sa_'+quarter+'.npy', teleg0)
    teleg1 = np.asarray(bins_out[5])
    np.savetxt('scaling_dataset/telegram_bin_sa_'+quarter+'.npy', teleg1)

    twit0 = np.asarray(z_out[7])
    np.savetxt('scaling_dataset/twitter_z_sa_'+quarter+'.npy', twit0)
    twit1 = np.asarray(bins_out[7])
    np.savetxt('scaling_dataset/twitter_bin_sa_'+quarter+'.npy', twit1)

    dv0 = np.asarray(z_out[8])
    np.savetxt('scaling_dataset/dailyviews_z_sa_'+quarter+'.npy', dv0)
    dv1 = np.asarray(bins_out[8])
    np.savetxt('scaling_dataset/dailyviews_bin_sa_'+quarter+'.npy', dv1)

    dt0 = np.asarray(z_out[9])
    np.savetxt('scaling_dataset/dailytime_z_sa_'+quarter+'.npy', dt0)
    dt1 = np.asarray(bins_out[9])
    np.savetxt('scaling_dataset/dailytime_bin_sa_'+quarter+'.npy', dt1)

    return

def generate_q(quarter):

    features_vec = ['region','industry','team','hardcap','price','telegram','N_google_news','N_twitter','N_daily_views','N_daily_time']
    kk = -1
    ranks = []
    z_out = []
    bins_out = []
    for feature in features_vec:
        kk = kk + 1
        ranks.append(kk)
        z_out.append(kk)
        bins_out.append(kk)

        success_threshold = 0.7

        with open("scaling_dataset/ico_data_reduced_q_"+quarter+".csv") as f:
            reader = csv.reader(f)
            data = [r for r in reader]

        data = np.asarray(data)

        indices, = np.where(data[:,10] != 'N/A')
        indices = np.delete(indices,0)

        success = [eval(data[i][20]) for i in indices]


        try:
            ind_feature = np.where(data[0,:]==feature)[0][0]
        except:
            print('ERROR: This feature does not exist in this dataset')
            sys.exit()

        if feature in ['hype','risk']:
            for i in range(0,len(data)):
                if data[i,ind_feature] == ' N/A' or data[i,ind_feature] == 'other':
                    data[i,ind_feature] = 'N/A'

        indices_f, = np.where(data[:,ind_feature] != 'N/A')
        indices_f = np.delete(indices_f,0)

        indices_over = []
        k = -1
        for i in range(0,len(indices)):
            for j in range(0,len(indices_f)):
                if indices_f[j] == indices[i]:
                    k = k + 1
                    indices_over.append(k)
                    indices_over[k] = indices[i]

        success0 = [eval(data[i][10]) for i in indices_over]
        variable0 = [data[i][ind_feature] for i in indices_over]

        #Feature Controls
        if feature in ['team','N_google_news']: #,'N_daily_views']:
            for i in range(0,len(variable0)):
                variable0[i] = abs(eval(variable0[i]))

        if feature == 'N_daily_views':
            for i in range(0,len(variable0)):
                variable0[i] = np.log10(eval(variable0[i]))

        if feature in ['hardcap','N_daily_time']:
            for i in range(0,len(variable0)):
                variable0[i] = eval(variable0[i])
                variable0[i] = np.log10(variable0[i])


        if feature in ['price','telegram','N_twitter']:
            for i in range(0,len(variable0)):
                if (variable0[i] == '0') or (variable0[i] == '0.0'):
                    variable0[i] = str(1)
                variable0[i] = np.log10(eval(variable0[i]))

        if feature == 'bazaar-rate':
            for i in range(0,len(variable0)):
                variable0[i] = eval(variable0[i])



        #Now reduce feature array to > 70% success values
        success0 = np.asarray(success0)
        indices2, = np.where(success0 > success_threshold)

        success0b = []
        variable0b = []
        k = -1
        for i in range(0,len(success0)):
            if i in indices2:
                k = k + 1
                success0b.append(k)
                variable0b.append(k)
                success0b[k] = success0[i]
                variable0b[k] = variable0[i]


        try:
            avg = np.median(variable0b)
            stdev = np.std(variable0b)
            f = [0.5,1.0,1.5,2.0,2.5]

            z,bins,p3 = plt.hist(variable0b, bins = 5, rwidth=0.9, facecolor = 'blue')
            plt.axvline(x=avg,linestyle = "-", linewidth = 2, color = 'k')


            plt.xlabel(feature,fontsize=17)
            plt.ylabel('Number',fontsize=15)
            plt.xticks(size = 15)
            plt.yticks(size = 15)
            #plt.show()
        except:
            if feature not in ['region','industry']:
                z,bins,p3 = plt.hist(variable0b, bins = 5, rwidth=0.9, facecolor = 'blue')
                plt.xlabel(feature,fontsize=17)
                plt.ylabel('Number',fontsize=15)
                plt.xticks(size = 15)
                plt.yticks(size = 15)
            if feature == 'region':
                z,bins,p3 = plt.hist(variable0b, bins = 12, rwidth=0.9, facecolor = 'blue')
                plt.xlabel(feature,fontsize=17)
                plt.ylabel('Number',fontsize=15)
                plt.xticks(size = 15)
                plt.yticks(size = 15)
            if feature == 'industry':
                z,bins,p3 = plt.hist(variable0b, bins = 14, rwidth=0.9, facecolor = 'blue')
                plt.xlabel(feature,fontsize=17)
                plt.ylabel('Number',fontsize=15)
                plt.xticks(size = 15)
                plt.xticks(rotation=90)
                plt.tick_params(labelsize=7)
                plt.yticks(size = 15)

        z_out[kk] = z
        bins_out[kk] = bins


    reg0 = np.asarray(z_out[0])
    np.savetxt('scaling_dataset/region_z_q_'+quarter+'.npy', reg0)
    reg1 = np.asarray(bins_out[0])
    np.savetxt('scaling_dataset/region_bin_q_'+quarter+'.npy', reg1)

    ind0 = np.asarray(z_out[1])
    np.savetxt('scaling_dataset/industry_z_q_'+quarter+'.npy', ind0)
    ind1 = np.asarray(bins_out[1])
    np.savetxt('scaling_dataset/industry_bin_q_'+quarter+'.npy', ind1)

    team0 = np.asarray(z_out[2])
    np.savetxt('scaling_dataset/team_z_q_'+quarter+'.npy', team0)
    team1 = np.asarray(bins_out[2])
    np.savetxt('scaling_dataset/team_bin_q_'+quarter+'.npy', team1)

    hard0 = np.asarray(z_out[3])
    np.savetxt('scaling_dataset/hardcap_z_q_'+quarter+'.npy', hard0)
    hard1 = np.asarray(bins_out[3])
    np.savetxt('scaling_dataset/hardcap_bin_q_'+quarter+'.npy', hard1)

    price0 = np.asarray(z_out[4])
    np.savetxt('scaling_dataset/price_z_q_'+quarter+'.npy', price0)
    price1 = np.asarray(bins_out[4])
    np.savetxt('scaling_dataset/price_bin_q_'+quarter+'.npy', price1)

    teleg0 = np.asarray(z_out[5])
    np.savetxt('scaling_dataset/telegram_z_q_'+quarter+'.npy', teleg0)
    teleg1 = np.asarray(bins_out[5])
    np.savetxt('scaling_dataset/telegram_bin_q_'+quarter+'.npy', teleg1)

    twit0 = np.asarray(z_out[7])
    np.savetxt('scaling_dataset/twitter_z_q_'+quarter+'.npy', twit0)
    twit1 = np.asarray(bins_out[7])
    np.savetxt('scaling_dataset/twitter_bin_q_'+quarter+'.npy', twit1)

    dv0 = np.asarray(z_out[8])
    np.savetxt('scaling_dataset/dailyviews_z_q_'+quarter+'.npy', dv0)
    dv1 = np.asarray(bins_out[8])
    np.savetxt('scaling_dataset/dailyviews_bin_q_'+quarter+'.npy', dv1)

    dt0 = np.asarray(z_out[9])
    np.savetxt('scaling_dataset/dailytime_z_q_'+quarter+'.npy', dt0)
    dt1 = np.asarray(bins_out[9])
    np.savetxt('scaling_dataset/dailytime_bin_q_'+quarter+'.npy', dt1)

    return

#arg1 = ['01Feb2016','01May2016','01Aug2016','01Nov2016','01Feb2017','01May2017','01Aug2017','01Nov2017','01Feb2018','01May2018','01Aug2018','01Nov2018']
#arg2 = ['1_16','2_16','3_16','4_16','1_17','2_17','3_17','4_17','1_18','2_18','3_18','4_18']

# ALL COMPARISON BASIS DATA FILES HAVE NOW BEEN GENERATED
### QUARTERLY ARRAYS WILL NOW BE GENERATED

for i in range(0,len(arg1)):
    generate_q(arg2[i])
    generate_sa(arg2[i])
