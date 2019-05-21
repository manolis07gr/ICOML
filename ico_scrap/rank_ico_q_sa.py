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

#OPTIONS: region,industry,team,raised,hardcap,price,telegram,N_google_news,N_twitter,hype,risk,bazaar-rate
#raised goes for completed ICOs not for in-progress or planned ICOs

ICO_name = input("Enter ICO Name: \n")
ICO_name = ICO_name.replace(" ","")
ICO_token = input("Enter ICO token Name: \n")

#Here we allow the user to import the features of the ICO that is under investigation
features_vec = ['region','industry','team','hardcap','price','telegram','N_google_news','N_twitter','N_daily_views','N_daily_time']
#user_input = ['united states', 'fintech', '4', '10000000', '0.20', '3210', '1', '5632','331','2.2']

bitcoin = func_btc()
top10s = func_top10()
ico_data = ico_data_collector([ICO_name,ICO_token,ICO_name],bitcoin,top10s)[1]
#revert to verbose region variable
if ico_data[5] == 1:
    reg = 'usa'
if ico_data[5] == 2:
    reg = 'russia'
if ico_data[5] == 3:
    reg = 'china'
if ico_data[5] == 4:
    reg = 'uk'
if ico_data[5] == 5:
    reg = 'estonia'
if ico_data[5] == 6:
    reg = 'switzerland'
if ico_data[5] == 7:
    reg = 'singapore'
if ico_data[5] == 8:
    reg = 'japan'
if ico_data[5] == 9:
    reg = 'australia'
if ico_data[5] == 10:
    reg = 'brazil'
if ico_data[5] == 11:
    reg = 'south africa'
if ico_data[5] == 12:
    reg = 'mongolia'

user_input = []
user_input.append(reg)
user_input.append(ico_data[6])
user_input.append(ico_data[7])
user_input.append(ico_data[9])
user_input.append(ico_data[11])
user_input.append(ico_data[12])
user_input.append(ico_data[13])
user_input.append(ico_data[14])
user_input.append(ico_data[15])
user_input.append(ico_data[16])

for i in range(0,len(user_input)):
    if user_input[i] != 'N/A':
        user_input[i] = str(user_input[i])
    if user_input[i] == 'N/A':
        user_input[i] = input("Enter ICO feature: "+features_vec[i]+"\n")

print('The following features were found for the ',ICO_name,' ICO:', user_input)

#Now the code will reduce the target data-set for rating and clustering only down to the same Quarter
#As the ICO under investigation
ico_end_date = ico_data[2].replace(" ","")
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
    if quarters[i] <= ico_end_date_o <= quarters[i+1]:
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

print('test',q_start,q_end,q_start_target,q_end_target)

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


with open("outdata/ico_data_rate_cluster.csv") as fff:
            reader_f = csv.reader(fff)
            data_f = [r for r in reader_f]

data_f = np.asarray(data_f)

columnTitles_rateCluster = "coin,start,end,duration,age,region,industry,team,raised,hardcap,success,price,telegram,N_google_news,N_twitter,N_daily_views,N_daily_time,hype,risk,bazaar-rate,ret_ico_to_day_one,vol_day1,sharpe_1,sharpe_3,sharpe_yr,sharpe_yr2,beta_btc,beta_top10,alpha_btc,alpha_top10\n"

with open('outdata/ico_data_rate_cluster_q.csv', 'w') as csvfile_bb:
    csvfile_bb.write(columnTitles_rateCluster)
    writer=csv.writer(csvfile_bb, delimiter=',')

    for i in range(1,len(data_f)):
        end_date_a = data_f[i][2].replace(" ","")
        end_day_o = datetime.strptime(end_date_a, '%d%b%Y')
        if (q_start_target <= end_day_o < q_end_target):
            all_data = [data_f[i][0],data_f[i][1],data_f[i][2],data_f[i][3],data_f[i][4],data_f[i][5],data_f[i][6],data_f[i][7],data_f[i][8],data_f[i][9],data_f[i][10],data_f[i][11],data_f[i][12],data_f[i][13],data_f[i][14],data_f[i][15],data_f[i][16],data_f[i][17],data_f[i][18],data_f[i][19],data_f[i][20],data_f[i][21],data_f[i][22],data_f[i][23],data_f[i][24],data_f[i][25],data_f[i][26],data_f[i][27],data_f[i][28],data_f[i][29]]
            writer.writerow(all_data)

columnTitles_rateCluster2 = "coin,start,end,duration,age,region,industry,team,raised,hardcap,success,price,telegram,N_google_news,N_twitter,N_daily_views,N_daily_time,hype,risk,bazaar-rate,ret_ico_to_day_one,vol_day1,sharpe_1,sharpe_3,sharpe_yr,sharpe_yr2,beta_btc,beta_top10,alpha_btc,alpha_top10\n"

with open('outdata/ico_data_rate_cluster_q2.csv', 'w') as csvfile_bb2:
    csvfile_bb2.write(columnTitles_rateCluster2)
    writer2=csv.writer(csvfile_bb2, delimiter=',')

    for i in range(1,len(data_f)):
        end_date_a = data_f[i][2].replace(" ","")
        end_day_o = datetime.strptime(end_date_a, '%d%b%Y')
        if (q_start_target2 <= end_day_o < q_end_target2):
            all_data2 = [data_f[i][0],data_f[i][1],data_f[i][2],data_f[i][3],data_f[i][4],data_f[i][5],data_f[i][6],data_f[i][7],data_f[i][8],data_f[i][9],data_f[i][10],data_f[i][11],data_f[i][12],data_f[i][13],data_f[i][14],data_f[i][15],data_f[i][16],data_f[i][17],data_f[i][18],data_f[i][19],data_f[i][20],data_f[i][21],data_f[i][22],data_f[i][23],data_f[i][24],data_f[i][25],data_f[i][26],data_f[i][27],data_f[i][28],data_f[i][29]]
            writer2.writerow(all_data2)

###Based on the ICO_DATA_REDUCED dataset

with open("outdata/ico_data_reduced.csv") as ffff:
    reader_ff = csv.reader(ffff)
    data_ff = [r for r in reader_ff]

data_ff = np.asarray(data_ff)

columnTitles_rateCluster22 = "coin,start,end,duration,age,region,industry,team,raised,hardcap,success,price,telegram,N_google_news,N_twitter,N_daily_views,N_daily_time,hype,risk,bazaar-rate,ret_ico_to_day_one,vol_day1,sharpe_1,sharpe_3,sharpe_yr,sharpe_yr2,beta_btc,beta_top10,alpha_btc,alpha_top10\n"

with open('outdata/ico_data_reduced_q.csv', 'w') as csvfile_bbb:
    csvfile_bbb.write(columnTitles_rateCluster22)
    writer_b=csv.writer(csvfile_bbb, delimiter=',')

    for i in range(1,len(data_ff)):
        end_date_a = data_ff[i][2].replace(" ","")
        end_day_o = datetime.strptime(end_date_a, '%d%b%Y')
        if (q_start_target <= end_day_o < q_end_target):
            all_data = [data_ff[i][0],data_ff[i][1],data_ff[i][2],data_ff[i][3],data_ff[i][4],data_ff[i][5],data_ff[i][6],data_ff[i][7],data_ff[i][8],data_ff[i][9],data_ff[i][10],data_ff[i][11],data_ff[i][12],data_ff[i][13],data_ff[i][14],data_ff[i][15],data_ff[i][16],data_ff[i][17],data_ff[i][18],data_ff[i][19],data_ff[i][20],data_ff[i][21],data_ff[i][22],data_ff[i][23],data_ff[i][24],data_ff[i][25],data_ff[i][26],data_ff[i][27],data_ff[i][28],data_ff[i][29]]
            writer_b.writerow(all_data)

columnTitles_rateCluster222 = "coin,start,end,duration,age,region,industry,team,raised,hardcap,success,price,telegram,N_google_news,N_twitter,N_daily_views,N_daily_time,hype,risk,bazaar-rate,ret_ico_to_day_one,vol_day1,sharpe_1,sharpe_3,sharpe_yr,sharpe_yr2,beta_btc,beta_top10,alpha_btc,alpha_top10\n"

with open('outdata/ico_data_reduced_q2.csv', 'w') as csvfile_bb22:
    csvfile_bb22.write(columnTitles_rateCluster222)
    writer2b=csv.writer(csvfile_bb22, delimiter=',')

    for i in range(1,len(data_ff)):
        end_date_a = data_ff[i][2].replace(" ","")
        end_day_o = datetime.strptime(end_date_a, '%d%b%Y')
        if (q_start_target2 <= end_day_o < q_end_target2):
            all_data2 = [data_ff[i][0],data_ff[i][1],data_ff[i][2],data_ff[i][3],data_ff[i][4],data_ff[i][5],data_ff[i][6],data_ff[i][7],data_ff[i][8],data_ff[i][9],data_ff[i][10],data_ff[i][11],data_ff[i][12],data_ff[i][13],data_ff[i][14],data_ff[i][15],data_ff[i][16],data_ff[i][17],data_ff[i][18],data_ff[i][19],data_ff[i][20],data_ff[i][21],data_ff[i][22],data_ff[i][23],data_ff[i][24],data_ff[i][25],data_ff[i][26],data_ff[i][27],data_ff[i][28],data_ff[i][29]]
            writer2b.writerow(all_data2)


#End quarterly subset selection
print('---------------------------------------------------------------------------------------')
print('---------------------------------------------------------------------------------------')
print('---------------------------------------------------------------------------------------')
print('---------------------------------------------------------------------------------------')
print('---------------------------------------------------------------------------------------')
print('RATING AND CLUSTERING WRT TO ICOs IN PREVIOUS QUARTER ')
print('---------------------------------------------------------------------------------------')
print('---------------------------------------------------------------------------------------')
print('---------------------------------------------------------------------------------------')
print('---------------------------------------------------------------------------------------')
print('---------------------------------------------------------------------------------------')

def ico_rank(user_input):

    features_vec = ['region','industry','team','hardcap','price','telegram','N_google_news','N_twitter','N_daily_views','N_daily_time']
    kk = -1
    ranks = []
    for feature in features_vec:
        kk = kk + 1
        ranks.append(kk)


        success_threshold = 0.7

        with open("outdata/ico_data_reduced_q.csv") as f:
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
            ##print(feature,np.std(variable0))


        if feature in ['price','telegram','N_twitter']:
            for i in range(0,len(variable0)):
                #print('BEFORE',variable0[i],i)
                if (variable0[i] == '0') or (variable0[i] == '0.0'):
                    variable0[i] = str(1)
                variable0[i] = np.log10(eval(variable0[i]))
                #print('AFTER',variable0[i],i)
            ##print(feature,np.std(variable0))

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

        #try:
        #    print('-------BASIC FEATURE STATISTICS: FULL SAMPLE-------')
        #    print('For feature:',feature.upper(),'the sample size is: ',len(variable0))
        #    print('For feature:',feature.upper(),'the max value is: ',np.max(variable0))
        #    print('For feature:',feature.upper(),'the min value is: ',np.min(variable0))
        #    print('For feature:',feature.upper(),'the mean value is: ',round(np.mean(variable0),3))
        #    print('For feature:',feature.upper(),'the median value is: ',round(np.median(variable0),3))
        #    print('For feature:',feature.upper(),'the standard deviation is: ',round(np.std(variable0),3))
        #    print('---------------------------------------------------')
        #    print('---------------------------------------------------')
        #    print('-------BASIC FEATURE STATISTICS: SUCCESSFUL SAMPLE-------')
        #    print('For feature:',feature.upper(),'the sample size is: ',len(variable0b))
        #    print('For feature:',feature.upper(),'the max value is: ',np.max(variable0b))
        #    print('For feature:',feature.upper(),'the min value is: ',np.min(variable0b))
        #    print('For feature:',feature.upper(),'the mean value is: ',round(np.mean(variable0b),3))
        #    print('For feature:',feature.upper(),'the median value is: ',round(np.median(variable0b),3))
        #    print('For feature:',feature.upper(),'the standard deviation is: ',round(np.std(variable0b),3))
        #    print('---------------------------------------------------------')
        #    print('---------------------------------------------------------')
        #except:
        #    print('Statistics Are Not Done for Categorical Features')
        #    print('For feature:',feature.upper(),'the sample size is: ',len(variable0))
        #    print('For feature:',feature.upper(),'the sample size is: ',len(variable0b))

        z,bins,p3 = plt.hist(variable0, bins = 'auto', rwidth=0.9, facecolor = 'blue')
        plt.xlabel(feature,fontsize=17)
        plt.ylabel('Number',fontsize=15)
        plt.xticks(size = 15)
        plt.yticks(size = 15)
        plt.show()


        #fig, ax = plt.subplots()
        #plt.xlabel(feature)
        #plt.ylabel('success')
        #ax.scatter(variable0, success0, c='k')
        #plt.show()
        #fig, ax = plt.subplots()
        #plt.xlabel(feature)
        #plt.ylabel('success')
        #ax.scatter(variable0b, success0b, c='k')
        #plt.show()

        try:
            avg = np.median(variable0b)
            stdev = np.std(variable0b)
            f = [0.5,1.0,1.5,2.0,2.5]

            z,bins,p3 = plt.hist(variable0b, bins = 5, rwidth=0.9, facecolor = 'blue')
            plt.axvline(x=avg,linestyle = "-", linewidth = 2, color = 'k')
        #    for i in f:
        #        plt.axvline(x=avg+i*stdev,linestyle = ":", linewidth = 1, color = 'r')
        #        plt.axvline(x=avg-i*stdev,linestyle = ":", linewidth = 1, color = 'r')

            plt.xlabel(feature,fontsize=17)
            plt.ylabel('Number',fontsize=15)
            plt.xticks(size = 15)
            plt.yticks(size = 15)
            plt.show()
        except:
            if feature not in ['region','industry']:
                print('Statistics Are Not Done for Categorical Features')
                z,bins,p3 = plt.hist(variable0b, bins = 5, rwidth=0.9, facecolor = 'blue')
                plt.xlabel(feature,fontsize=17)
                plt.ylabel('Number',fontsize=15)
                plt.xticks(size = 15)
                plt.yticks(size = 15)
                plt.show()
            if feature == 'region':
                print('Statistics Are Not Done for Categorical Features')
                z,bins,p3 = plt.hist(variable0b, bins = 12, rwidth=0.9, facecolor = 'blue')
                plt.xlabel(feature,fontsize=17)
                plt.ylabel('Number',fontsize=15)
                plt.xticks(size = 15)
                plt.yticks(size = 15)
                plt.show()
            if feature == 'industry':
                print('Statistics Are Not Done for Categorical Features')
                z,bins,p3 = plt.hist(variable0b, bins = 14, rwidth=0.9, facecolor = 'blue')
                plt.xlabel(feature,fontsize=17)
                plt.ylabel('Number',fontsize=15)
                plt.xticks(size = 15)
                plt.xticks(rotation=90)
                plt.tick_params(labelsize=7)
                plt.yticks(size = 15)
                plt.show()

    #Perform grading based on simple stat comparisons (std from median)
    #First Determine Input Data bin

        if feature not in ['region','industry','N_google_news']:

            if feature == 'team':
                feature_in = eval(user_input[2])
            if feature == 'hardcap':
                feature_in = np.log10(eval(user_input[3]))
            if feature == 'price':
                feature_in = np.log10(eval(user_input[4]))
            if feature == 'telegram':
                feature_in = np.log10(eval(user_input[5]))
            if feature == 'N_google_news':
                feature_in = eval(user_input[6])
            if feature == 'N_twitter':
                feature_in = np.log10(eval(user_input[7]))
            if feature == 'N_daily_views':
                feature_in = np.log10(eval(user_input[8]))
            if feature == 'N_daily_time':
                feature_in = np.log10(eval(user_input[9]))

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

            print('The ICO under investigation receives the grade: ',grade,' for feature: ',feature.upper())

            z,bins,p3 = plt.hist(variable0b, bins = 5, rwidth=0.9, facecolor = 'blue')
            plt.axvline(x=avg,linestyle = "-", linewidth = 2, color = 'k')
            plt.axvline(x=feature_in,linestyle = "-", linewidth = 2, color = 'r')
            plt.xlabel(feature,fontsize=17)
            plt.ylabel('Number',fontsize=15)
            plt.xticks(size = 15)
            plt.yticks(size = 15)
            plt.show()

        if feature == 'region':

            region_in = func_region(user_input[0])

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

            print('The ICO under investigation receives the grade: ',grade,' for feature: ',feature.upper())

            z,bins,p3 = plt.hist(variable0b, bins = 12, rwidth=0.9, facecolor = 'blue')
            plt.axvline(x=str(region_in), linestyle = "-", linewidth = 2, color = 'r')
            plt.xlabel(feature,fontsize=17)
            plt.ylabel('Number',fontsize=15)
            plt.xticks(size = 15)
            plt.yticks(size = 15)
            plt.show()

        if feature == 'industry':

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

            print('The ICO under investigation receives the grade: ',grade,' for feature: ',feature.upper())

            z,bins,p3 = plt.hist(variable0b, bins = 14, rwidth=0.9, facecolor = 'blue')
            plt.xlabel(feature,fontsize=17)
            plt.ylabel('Number',fontsize=15)
            plt.axvline(x=tag, linestyle = "-", linewidth = 2, color = 'r')
            plt.xticks(size = 15)
            plt.xticks(rotation=90)
            plt.tick_params(labelsize=7)
            plt.yticks(size = 15)
            plt.show()

        ranks[kk] = grade

    ico_rating = np.mean(ranks)
    ico_rating0 = ico_rating/5.0

    rate_verbose = 'Unrated'

    if (0.0 <= ico_rating < 1.0):
        rate_verbose = 'Very Low'
    if (1.0 <= ico_rating < 2.0):
        rate_verbose = 'Low'
    if (2.0 <= ico_rating < 3.0):
        rate_verbose = 'Medium'
    if (3.0 <= ico_rating < 4.0):
        rate_verbose = 'High'
    if (4.0 <= ico_rating <= 5.0):
        rate_verbose = 'Very High'

    print('The average BloxVerse ranking for this ICO is: ',round(ico_rating,2))
    print('In the 0-1 scale this is equivalent to: ',round(ico_rating0,2))
    print('In ICORating scale this is equivalent to a rating of: ',rate_verbose)

    return 'Normalized BloxVerse Rating: ',round(ico_rating0,2)

print(ico_rank(user_input))

wait = input("PRESS ENTER TO CONTINUE.")

#Perform k-means-based clustering grading - DBSCAN will be more appropriate
#Cannot include categorical data: country, industry
data = pd.read_csv('outdata/ico_data_rate_cluster_q.csv')
f1 = data['team'].values
f2 = data['hardcap'].values
f3 = data['price'].values
f4 = data['telegram'].values
f5 = data['N_twitter'].values
f6 = data['N_daily_views'].values
f7 = data['N_daily_time'].values

r0 = data['coin']
r1 = data['raised'].values
r2 = data['success'].values

##user_input = ['singapore', 'saas', '24', '30010280.0', '0.1', '25473', '8', '15439', '2.4', '210.0']

inp_ico = [eval(user_input[2]),eval(user_input[3]),eval(user_input[4]),eval(user_input[5]),eval(user_input[7]),eval(user_input[8]),eval(user_input[9])]
inp_ico = np.asarray(inp_ico)
inp_ico_orig = inp_ico
inp_ico = inp_ico.reshape(1,-1)

inp_ico2 =  [eval(user_input[5]),eval(user_input[7]),eval(user_input[8]),eval(user_input[9])]
inp_ico2 = np.asarray(inp_ico2)
inp_ico2 = inp_ico2.reshape(1,-1)

X = np.array(list(zip(f1,f2,f3,f4,f5,f6,f7)))
X = np.concatenate((X, inp_ico))
X = StandardScaler().fit_transform(X)
scaler = StandardScaler().fit(X)

with open("outdata/ico_data_rate_cluster_q.csv") as f2f:
    readerf = csv.reader(f2f)
    target_data2 = [r2 for r2 in readerf]

with open('outdata/ico_data_social_q.csv', 'w') as csvfile_bbbb:
    #csvfile_b.write(columnTitles_complete)
    writerbb=csv.writer(csvfile_bbbb, delimiter=',')

    for i in range(0,len(target_data2)):
        if ('N/A' not in target_data2[i][10]) and ('N/A' not in target_data2[i][12]) and ('N/A' not in target_data2[i][14]) and ('N/A' not in target_data2[i][15]) and ('N/A' not in target_data2[i][16]):
            all_databb = [target_data2[i][0],target_data2[i][1],target_data2[i][2],target_data2[i][3],target_data2[i][4],target_data2[i][5],target_data2[i][6],target_data2[i][7],target_data2[i][8],target_data2[i][9],target_data2[i][10],target_data2[i][11],target_data2[i][12],target_data2[i][13],target_data2[i][14],target_data2[i][15],target_data2[i][16],target_data2[i][17],target_data2[i][18],target_data2[i][19],target_data2[i][20],target_data2[i][21],target_data2[i][22],target_data2[i][23],target_data2[i][24],target_data2[i][25],target_data2[i][26],target_data2[i][27],target_data2[i][28],target_data2[i][29]]
            writerbb.writerow(all_databb)

data2 = pd.read_csv('outdata/ico_data_social_q.csv')
g4 = data2['telegram'].values
g5 = data2['N_twitter'].values
g6 = data2['N_daily_views'].values
g7 = data2['N_daily_time'].values

g0 = data2['coin']
g1 = data2['raised'].values
g2 = data2['success'].values

XX = np.array(list(zip(g4,g5,g6,g7)))
XX = np.concatenate((XX, inp_ico2))
XX = StandardScaler().fit_transform(XX)
scaler2 = StandardScaler().fit(XX)

### BELOW WE USE THE ADOPTED CLUSTERING ARRANGEMENT: FULL DATASET
try:
    
    N_CL = 6
    kmeans = KMeans(n_clusters=N_CL,random_state=3425)
    # Fitting the input data
    kmeans = kmeans.fit(X)
    # Getting the cluster labels
    labels3 = kmeans.predict(X)
    # Centroid values
    centroids = kmeans.cluster_centers_

    print('---------------------------------------------------------------------------------------')
    print('K-MEANS CLUSTERING METHOD (ENTIRE DATASET), k =',N_CL)
    print('---------------------------------------------------------------------------------------')

    print('Clustering Determined the Following Centroid Coordinates (x,y,z): ')
    print(centroids)
    print('Normalized error for k =',N_CL,'is: ',round(np.sqrt(kmeans.inertia_)/len(labels3),2))
    try:
        print('Sillhouette score is =',metrics.silhouette_score(X, labels3))
    except:
        print('Sillhouette score is =',-1.0)

    try:
        sample_silhouette_values = metrics.silhouette_samples(X, labels3)
    except:
        sample_silhouette_values = -1

    y_lower = 10
    for i in range(N_CL):
            # Aggregate the silhouette scores for samples belonging to
            # cluster i, and sort them
            ith_cluster_silhouette_values = \
                sample_silhouette_values[labels3 == i]

            ith_cluster_silhouette_values.sort()

            size_cluster_i = ith_cluster_silhouette_values.shape[0]
            y_upper = y_lower + size_cluster_i

            color = cm.nipy_spectral(float(i) / N_CL)
            plt.fill_betweenx(np.arange(y_lower, y_upper),
                              0, ith_cluster_silhouette_values,
                              facecolor=color, edgecolor=color, alpha=0.7)

            # Label the silhouette plots with their cluster numbers at the middle
            plt.text(-0.05, y_lower + 0.5 * size_cluster_i, str(i))

            # Compute the new y_lower for next plot
            y_lower = y_upper + 10  # 10 for the 0 samples

    plt.title("The silhouette plot for the various clusters: Full Dataset")
    plt.xlabel("The silhouette coefficient values")
    plt.ylabel("Cluster label")

        # The vertical line for average silhouette score of all the values
    plt.axvline(x=metrics.silhouette_score(X, labels3), color="red", linestyle="--")

    plt.yticks([])  # Clear the yaxis labels / ticks
    plt.xticks([-0.1, 0, 0.2, 0.4, 0.6, 0.8, 1])
    plt.show()

    ico_cluster_label = labels3[len(labels3)-1]
    ico_cluster_indices = [i for i,v in enumerate(labels3) if v == ico_cluster_label]

    coin_cl = []
    team_cl=[] 
    hardcap_cl=[]
    price_cl=[] 
    twitter_cl=[]
    telegram_cl=[]
    dailyviews_cl=[] 
    dailytime_cl=[]
    raised_cl=[]
    success_cl=[]
    clust_data = []

    for i in range(0,len(ico_cluster_indices)-1):
        ind = ico_cluster_indices[i]

        coin_cl.append(i)
        team_cl.append(i) 
        hardcap_cl.append(i)
        price_cl.append(i)
        twitter_cl.append(i)
        telegram_cl.append(i)
        dailyviews_cl.append(i)
        dailytime_cl.append(i)
        raised_cl.append(i)
        success_cl.append(i)
        clust_data.append(i)

        coin_cl[i] = np.array(r0)[ind]
        team_cl[i] = np.array(f1)[ind]
        hardcap_cl[i] = np.array(f2)[ind]
        price_cl[i] = np.array(f3)[ind]
        twitter_cl[i] = np.array(f4)[ind]
        telegram_cl[i] = np.array(f5)[ind]
        dailyviews_cl[i] = np.array(f6)[ind]
        dailytime_cl[i] = np.array(f7)[ind]

        clust_data[i] = [team_cl[i],hardcap_cl[i],price_cl[i],twitter_cl[i],telegram_cl[i],dailyviews_cl[i],dailytime_cl[i]]

        raised_cl[i] = np.array(r1)[ind]
        success_cl[i] = np.array(r2)[ind]

    min_succ = np.argmin(success_cl)

    team_max = max(team_cl)
    if inp_ico_orig[0] > team_max:
        team_max = inp_ico_orig[0]
    hardcap_max = max(hardcap_cl)
    if inp_ico_orig[1] > hardcap_max:
        hardcap_max = inp_ico_orig[1]
    price_max = max(price_cl)
    if inp_ico_orig[2] > price_max:
        price_max = inp_ico_orig[2]
    twitter_max = max(twitter_cl)
    if inp_ico_orig[3] > twitter_max:
        twitter_max = inp_ico_orig[3]
    telegram_max = max(telegram_cl)
    if inp_ico_orig[4] > telegram_max:
        telegram_max = inp_ico_orig[4]
    dailyviews_max = max(dailyviews_cl)
    if inp_ico_orig[5] > dailyviews_max:
        dailyviews_max = inp_ico_orig[5]
    dailytime_max = max(dailytime_cl)
    if inp_ico_orig[6] > dailytime_max:
        dailytime_max = inp_ico_orig[6]

    team_cl_n = team_cl/team_max
    hardcap_cl_n = hardcap_cl/hardcap_max
    price_cl_n = price_cl/price_max
    twitter_cl_n = twitter_cl/twitter_max
    telegram_cl_n = telegram_cl/telegram_max
    dailyviews_cl_n = dailyviews_cl/dailyviews_max
    dailytime_cl_n = dailytime_cl/dailytime_max



    inp_ico_n = [inp_ico_orig[0]/team_max,inp_ico_orig[1]/hardcap_max,inp_ico_orig[2]/price_max,inp_ico_orig[3]/twitter_max,inp_ico_orig[4]/telegram_max,inp_ico_orig[5]/dailyviews_max,inp_ico_orig[6]/dailytime_max]
    inp_ico_n = np.asarray(inp_ico_n)


    worse_ico_n = [team_cl_n[min_succ],hardcap_cl_n[min_succ],price_cl_n[min_succ],twitter_cl_n[min_succ],telegram_cl_n[min_succ],dailyviews_cl_n[min_succ],dailytime_cl_n[min_succ]]
    worse_ico_n = np.asarray(worse_ico_n)

    #Find most-similar ICO
    dist = []
    for i in range(0,len(clust_data)):
        dist.append(i)
        dist[i] = distance.euclidean(inp_ico, clust_data[i])

    min_dist = np.argmin(dist)

    avg_team = np.mean(team_cl)
    avg_hardcap = np.mean(hardcap_cl)
    avg_price = np.mean(price_cl)
    avg_twitter = np.mean(twitter_cl)
    avg_telegram = np.mean(telegram_cl)
    avg_dailyviews = np.mean(dailyviews_cl)
    avg_dailytime = np.mean(dailytime_cl)

    avg_cluster_vector = [avg_team/team_max,avg_hardcap/hardcap_max,avg_price/price_max,avg_twitter/twitter_max,avg_telegram/telegram_max,avg_dailyviews/dailyviews_max,avg_dailytime/dailytime_max]
    avg_cluster_vector = np.asarray(avg_cluster_vector)

    avg_raised = np.mean(raised_cl)
    avg_success = np.mean(success_cl)
    med_success = np.median(success_cl)

    successful_icos_cl = [i for i,v in enumerate(success_cl) if v == 1.0]

    coin_cl2 = []
    team_cl2=[] 
    hardcap_cl2=[]
    price_cl2=[] 
    twitter_cl2=[]
    telegram_cl2=[]
    dailyviews_cl2=[] 
    dailytime_cl2=[]
    raised_cl2=[]
    success_cl2=[]

    for i in range(0,len(successful_icos_cl)):
        ind2 = successful_icos_cl[i]

        coin_cl2.append(i)
        team_cl2.append(i) 
        hardcap_cl2.append(i)
        price_cl2.append(i)
        twitter_cl2.append(i)
        telegram_cl2.append(i)
        dailyviews_cl2.append(i)
        dailytime_cl2.append(i)
        raised_cl2.append(i)
        success_cl2.append(i)

        coin_cl2[i] = coin_cl[ind2]
        team_cl2[i] = team_cl[ind2]
        hardcap_cl2[i] = hardcap_cl[ind2]
        price_cl2[i] =  price_cl[ind2]
        twitter_cl2[i] =twitter_cl[ind2]
        telegram_cl2[i] = telegram_cl[ind2]
        dailyviews_cl2[i] = dailyviews_cl[ind2]
        dailytime_cl2[i] = dailytime_cl[ind2]

        raised_cl2[i] = raised_cl[ind2]
        success_cl2[i] = success_cl[ind2]

    if len(successful_icos_cl) == 0:
        coin_cl2 = coin_cl
        team_cl2 = team_cl
        hardcap_cl2 = hardcap_cl
        price_cl2 = price_cl
        twitter_cl2 = twitter_cl
        telegram_cl2 = telegram_cl
        dailyviews_cl2 = dailyviews_cl
        dailytime_cl2 = dailytime_cl
        raised_cl2 = raised_cl
        success_cl2 = success_cl

    max_raised = np.argmax(raised_cl2)

    team_cl2_n = team_cl2/team_max
    hardcap_cl2_n = hardcap_cl2/hardcap_max
    price_cl2_n = price_cl2/price_max
    twitter_cl2_n = twitter_cl2/twitter_max
    telegram_cl2_n = telegram_cl2/telegram_max
    dailyviews_cl2_n = dailyviews_cl2/dailyviews_max
    dailytime_cl2_n = dailytime_cl2/dailytime_max

    best_ico_n = [team_cl2_n[max_raised],hardcap_cl2_n[max_raised],price_cl2_n[max_raised],twitter_cl2_n[max_raised],telegram_cl2_n[max_raised],dailyviews_cl2_n[max_raised],dailytime_cl2_n[max_raised]]
    best_ico_n = np.asarray(best_ico_n)

    print('Input ICO belongs to cluster: ',ico_cluster_label)
    print('The most similar ICO in cluster is: ',coin_cl[min_dist])
    print('Average cluster ICO: Team: ',round(avg_team,0))
    print('Average cluster ICO: Hardcap: ',round(avg_hardcap,0))
    print('Average cluster ICO: Price: ',round(avg_price,4))
    print('Average cluster ICO: Twitter: ',round(avg_twitter,0))
    print('Average cluster ICO: Telegram: ',round(avg_telegram,0))
    print('Average cluster ICO: Daily Views: ',round(avg_dailyviews,0))
    print('Average cluster ICO: Daily Time: ',round(avg_dailytime,0))
    print('Average cluster ICO: Raised: ',round(avg_raised,0))
    print('Average cluster ICO: Success: ',round(avg_success,0))
    print('Median cluster ICO: Success: ',round(med_success,0))
    print('----------------------------------------')
    print('The least successful ICO in cluster is: ',coin_cl[min_succ])
    print('The least successful ICO raised: ',raised_cl[min_succ])
    print('The least successful ICO success rate was: ',success_cl[min_succ])
    print('The most successful ICO in cluster is: ',coin_cl2[max_raised])
    print('The most successful ICO raised: ',raised_cl2[max_raised])
    print('The most successful ICO success rate was: ',success_cl2[max_raised])

    #RADAR DIAGRAM
    plt.figure(figsize=(12,8))
    categories = ['Team', 'Hardcap', 'ICO Price', 'Twitter', 'Telegram', 'Website Visits', 'Daily Engagement']
    # ------- PART 1: Create background
    NN = len(categories)
    # What will be the angle of each axis in the plot? (we divide the plot / number of variable)
    angles = [n / float(NN) * 2 * pi for n in range(NN)]
    angles += angles[:1]
    # Initialise the spider plot
    ax = plt.subplot(111, polar=True)
    # If you want the first axis to be on top:
    ax.set_theta_offset(pi / 2)
    ax.set_theta_direction(-1)
    # Draw one axe per variable + add labels labels yet
    plt.xticks(angles[:-1], categories, size = '12', weight = 'bold')
    # Draw ylabels
    ax.set_rlabel_position(0)
    plt.yticks([0.25,0.50,0.75], ["0.25","0.50","0.75"], color="grey", size=7)
    plt.ylim(0,1)
    #plt.show()

    # ------- PART 2: Add plots
    # Plot each individual = each line of the data
    # I don't do a loop, because plotting more than 3 groups makes the chart unreadable
    # Ind1
    values = inp_ico_n.flatten().tolist()
    values += values[:1]
    ax.plot(angles, values, linewidth=1, linestyle='dashed', label="ICO under investigation")
    ax.fill(angles, values, 'b', alpha=0.1)
    # Ind2
    values = avg_cluster_vector.flatten().tolist()
    values += values[:1]
    ax.plot(angles, values, linewidth=1, linestyle='solid', label="Average ICO in cluster")
    ax.fill(angles, values, 'r', alpha=0.1)
    # Ind3
    values = worse_ico_n.flatten().tolist()
    values += values[:1]
    ax.plot(angles, values, linewidth=1, linestyle='solid', label="Worse ICO in cluster")
    ax.fill(angles, values, 'g', alpha=0.1)
    # Ind4
    values = best_ico_n.flatten().tolist()
    values += values[:1]
    ax.plot(angles, values, linewidth=1, linestyle='solid', label="Best ICO in cluster")
    ax.fill(angles, values, 'm', alpha=0.1)
    # Add legend
    plt.legend(loc='upper right', bbox_to_anchor=(0.1, 0.1))
    plt.show()
except:
    print('Data size inadequate for clustering analysis in a per-quarter basis')

### BELOW WE USE THE ADOPTED CLUSTERING ARRANGEMENT: INTERNET AND SOCIAL STATS DATASET

try:
    N_CL = 5
    kmeans = KMeans(n_clusters=N_CL,random_state=3425)
    # Fitting the input data
    kmeans = kmeans.fit(XX)
    # Getting the cluster labels
    labels4 = kmeans.predict(XX)
    # Centroid values
    centroids = kmeans.cluster_centers_

    print('---------------------------------------------------------------------------------------')
    print('K-MEANS CLUSTERING METHOD (INTERNET STATS DATASET), k =',N_CL)
    print('---------------------------------------------------------------------------------------')

    print('Clustering Determined the Following Centroid Coordinates (x,y,z): ')
    print(centroids)
    print('Normalized error for k =',N_CL,'is: ',round(np.sqrt(kmeans.inertia_)/len(labels4),2))
    try:
        print('Sillhouette score is =',metrics.silhouette_score(XX, labels4))
    except:
        print('Sillhouette score is =',-1.0)

    try:
        sample_silhouette_values = metrics.silhouette_samples(XX, labels4)
    except:
         sample_silhouette_values = -1

    y_lower = 10
    for i in range(N_CL):
            # Aggregate the silhouette scores for samples belonging to
            # cluster i, and sort them
            ith_cluster_silhouette_values = \
                sample_silhouette_values[labels4 == i]

            ith_cluster_silhouette_values.sort()

            size_cluster_i = ith_cluster_silhouette_values.shape[0]
            y_upper = y_lower + size_cluster_i

            color = cm.nipy_spectral(float(i) / N_CL)
            plt.fill_betweenx(np.arange(y_lower, y_upper),
                              0, ith_cluster_silhouette_values,
                              facecolor=color, edgecolor=color, alpha=0.7)

            # Label the silhouette plots with their cluster numbers at the middle
            plt.text(-0.05, y_lower + 0.5 * size_cluster_i, str(i))

            # Compute the new y_lower for next plot
            y_lower = y_upper + 10  # 10 for the 0 samples

    plt.title("The silhouette plot for the various clusters: Internet and Social Stats Dataset")
    plt.xlabel("The silhouette coefficient values")
    plt.ylabel("Cluster label")

        # The vertical line for average silhouette score of all the values
    plt.axvline(x=metrics.silhouette_score(XX, labels4), color="red", linestyle="--")

    plt.yticks([])  # Clear the yaxis labels / ticks
    plt.xticks([-0.1, 0, 0.2, 0.4, 0.6, 0.8, 1])
    plt.show()

    #######################################################
    #######################################################

    ico_cluster_label2 = labels4[len(labels4)-1]
    ico_cluster_indices2 = [i for i,v in enumerate(labels4) if v == ico_cluster_label2]

    coin_cl = []
    twitter_cl=[]
    telegram_cl=[]
    dailyviews_cl=[] 
    dailytime_cl=[]
    raised_cl=[]
    success_cl=[]
    clust_data = []

    for i in range(0,len(ico_cluster_indices2)-1):
        ind = ico_cluster_indices2[i]

        coin_cl.append(i)
        twitter_cl.append(i)
        telegram_cl.append(i)
        dailyviews_cl.append(i)
        dailytime_cl.append(i)
        raised_cl.append(i)
        success_cl.append(i)
        clust_data.append(i)

        coin_cl[i] = np.array(g0)[ind]
        twitter_cl[i] = np.array(g4)[ind]
        telegram_cl[i] = np.array(g5)[ind]
        dailyviews_cl[i] = np.array(g6)[ind]
        dailytime_cl[i] = np.array(g7)[ind]

        clust_data[i] = [twitter_cl[i],telegram_cl[i],dailyviews_cl[i],dailytime_cl[i]]

        raised_cl[i] = np.array(g1)[ind]
        success_cl[i] = np.array(g2)[ind]

    min_succ = np.argmin(success_cl)

    twitter_max = max(twitter_cl)
    if inp_ico_orig[3] > twitter_max:
        twitter_max = inp_ico_orig[3]
    telegram_max = max(telegram_cl)
    if inp_ico_orig[4] > telegram_max:
        telegram_max = inp_ico_orig[4]
    dailyviews_max = max(dailyviews_cl)
    if inp_ico_orig[5] > dailyviews_max:
        dailyviews_max = inp_ico_orig[5]
    dailytime_max = max(dailytime_cl)
    if inp_ico_orig[6] > dailytime_max:
        dailytime_max = inp_ico_orig[6]

    twitter_cl_n = twitter_cl/twitter_max
    telegram_cl_n = telegram_cl/telegram_max
    dailyviews_cl_n = dailyviews_cl/dailyviews_max
    dailytime_cl_n = dailytime_cl/dailytime_max

    inp_ico_n = [inp_ico_orig[3]/twitter_max,inp_ico_orig[4]/telegram_max,inp_ico_orig[5]/dailyviews_max,inp_ico_orig[6]/dailytime_max]
    inp_ico_n = np.asarray(inp_ico_n)

    worse_ico_n = [twitter_cl_n[min_succ],telegram_cl_n[min_succ],dailyviews_cl_n[min_succ],dailytime_cl_n[min_succ]]
    worse_ico_n = np.asarray(worse_ico_n)

    #Find most-similar ICO
    dist = []
    for i in range(0,len(clust_data)):
        dist.append(i)
        dist[i] = distance.euclidean(inp_ico2, clust_data[i])

    min_dist = np.argmin(dist)

    avg_twitter = np.mean(twitter_cl)
    avg_telegram = np.mean(telegram_cl)
    avg_dailyviews = np.mean(dailyviews_cl)
    avg_dailytime = np.mean(dailytime_cl)

    avg_cluster_vector = [avg_twitter/twitter_max,avg_telegram/telegram_max,avg_dailyviews/dailyviews_max,avg_dailytime/dailytime_max]
    avg_cluster_vector = np.asarray(avg_cluster_vector)

    avg_raised = np.mean(raised_cl)
    avg_success = np.mean(success_cl)
    med_success = np.median(success_cl)

    successful_icos_cl = [i for i,v in enumerate(success_cl) if v == 1.0]

    coin_cl2 = []
    twitter_cl2=[]
    telegram_cl2=[]
    dailyviews_cl2=[] 
    dailytime_cl2=[]
    raised_cl2=[]
    success_cl2=[]

    for i in range(0,len(successful_icos_cl)):
        ind2 = successful_icos_cl[i]

        coin_cl2.append(i)
        twitter_cl2.append(i)
        telegram_cl2.append(i)
        dailyviews_cl2.append(i)
        dailytime_cl2.append(i)
        raised_cl2.append(i)
        success_cl2.append(i)

        coin_cl2[i] = coin_cl[ind2]
        twitter_cl2[i] =twitter_cl[ind2]
        telegram_cl2[i] = telegram_cl[ind2]
        dailyviews_cl2[i] = dailyviews_cl[ind2]
        dailytime_cl2[i] = dailytime_cl[ind2]

        raised_cl2[i] = raised_cl[ind2]
        success_cl2[i] = success_cl[ind2]


    max_raised = np.argmax(raised_cl2)

    twitter_cl2_n = twitter_cl2/twitter_max
    telegram_cl2_n = telegram_cl2/telegram_max
    dailyviews_cl2_n = dailyviews_cl2/dailyviews_max
    dailytime_cl2_n = dailytime_cl2/dailytime_max

    best_ico_n = [twitter_cl2_n[max_raised],telegram_cl2_n[max_raised],dailyviews_cl2_n[max_raised],dailytime_cl2_n[max_raised]]
    best_ico_n = np.asarray(best_ico_n)

    print('Input ICO belongs to cluster: ',ico_cluster_label)
    print('The most similar ICO in cluster is: ',coin_cl[min_dist])
    print('Average cluster ICO: Twitter: ',round(avg_twitter,0))
    print('Average cluster ICO: Telegram: ',round(avg_telegram,0))
    print('Average cluster ICO: Daily Views: ',round(avg_dailyviews,0))
    print('Average cluster ICO: Daily Time: ',round(avg_dailytime,0))
    print('Average cluster ICO: Raised: ',round(avg_raised,0))
    print('Average cluster ICO: Success: ',round(avg_success,0))
    print('Median cluster ICO: Success: ',round(med_success,0))
    print('----------------------------------------')
    print('The least successful ICO in cluster is: ',coin_cl[min_succ])
    print('The least successful ICO raised: ',raised_cl[min_succ])
    print('The least successful ICO success rate was: ',success_cl[min_succ])
    print('The most successful ICO in cluster is: ',coin_cl2[max_raised])
    print('The most successful ICO raised: ',raised_cl2[max_raised])
    print('The most successful ICO success rate was: ',success_cl2[max_raised])

    #RADAR DIAGRAM
    plt.figure(figsize=(12,8))
    categories = ['Twitter', 'Telegram', 'Website Visits', 'Daily Engagement']
    # ------- PART 1: Create background
    NN = len(categories)
    # What will be the angle of each axis in the plot? (we divide the plot / number of variable)
    angles = [n / float(NN) * 2 * pi for n in range(NN)]
    angles += angles[:1]
    # Initialise the spider plot
    ax = plt.subplot(111, polar=True)
    # If you want the first axis to be on top:
    ax.set_theta_offset(pi / 2)
    ax.set_theta_direction(-1)
    # Draw one axe per variable + add labels labels yet
    plt.xticks(angles[:-1], categories, size = '12', weight = 'bold')
    # Draw ylabels
    ax.set_rlabel_position(0)
    plt.yticks([0.25,0.50,0.75], ["0.25","0.50","0.75"], color="grey", size=7)
    plt.ylim(0,1)
    #plt.show()

    # ------- PART 2: Add plots
    # Plot each individual = each line of the data
    # I don't do a loop, because plotting more than 3 groups makes the chart unreadable
    # Ind1
    values = inp_ico_n.flatten().tolist()
    values += values[:1]
    ax.plot(angles, values, linewidth=1, linestyle='dashed', label="ICO under investigation")
    ax.fill(angles, values, 'b', alpha=0.1)
    # Ind2
    values = avg_cluster_vector.flatten().tolist()
    values += values[:1]
    ax.plot(angles, values, linewidth=1, linestyle='solid', label="Average ICO in cluster")
    ax.fill(angles, values, 'r', alpha=0.1)
    # Ind3
    values = worse_ico_n.flatten().tolist()
    values += values[:1]
    ax.plot(angles, values, linewidth=1, linestyle='solid', label="Worse ICO in cluster")
    ax.fill(angles, values, 'g', alpha=0.1)
    # Ind4
    values = best_ico_n.flatten().tolist()
    values += values[:1]
    ax.plot(angles, values, linewidth=1, linestyle='solid', label="Best ICO in cluster")
    ax.fill(angles, values, 'm', alpha=0.1)
    # Add legend
    plt.legend(loc='upper right', bbox_to_anchor=(0.1, 0.1))
    plt.show()

except:
    print('Data size inadequate for clustering analysis in a per-quarter basis')

print('---------------------------------------------------------------------------------------')
print('---------------------------------------------------------------------------------------')
print('---------------------------------------------------------------------------------------')
print('---------------------------------------------------------------------------------------')
print('---------------------------------------------------------------------------------------')
print('RATING AND CLUSTERING WRT TO ICOs TWO QUARTERS AGO')
print('---------------------------------------------------------------------------------------')
print('---------------------------------------------------------------------------------------')
print('---------------------------------------------------------------------------------------')
print('---------------------------------------------------------------------------------------')
print('---------------------------------------------------------------------------------------')


def ico_rank(user_input):

    features_vec = ['region','industry','team','hardcap','price','telegram','N_google_news','N_twitter','N_daily_views','N_daily_time']
    kk = -1
    ranks = []
    for feature in features_vec:
        kk = kk + 1
        ranks.append(kk)


        success_threshold = 0.7

        with open("outdata/ico_data_reduced_q2.csv") as f:
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
            ##print(feature,np.std(variable0))


        if feature in ['price','telegram','N_twitter']:
            for i in range(0,len(variable0)):
                #print('BEFORE',variable0[i],i)
                if (variable0[i] == '0') or (variable0[i] == '0.0'):
                    variable0[i] = str(1)
                variable0[i] = np.log10(eval(variable0[i]))
                #print('AFTER',variable0[i],i)
            ##print(feature,np.std(variable0))

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

        #try:
        #    print('-------BASIC FEATURE STATISTICS: FULL SAMPLE-------')
        #    print('For feature:',feature.upper(),'the sample size is: ',len(variable0))
        #    print('For feature:',feature.upper(),'the max value is: ',np.max(variable0))
        #    print('For feature:',feature.upper(),'the min value is: ',np.min(variable0))
        #    print('For feature:',feature.upper(),'the mean value is: ',round(np.mean(variable0),3))
        #    print('For feature:',feature.upper(),'the median value is: ',round(np.median(variable0),3))
        #    print('For feature:',feature.upper(),'the standard deviation is: ',round(np.std(variable0),3))
        #    print('---------------------------------------------------')
        #    print('---------------------------------------------------')
        #    print('-------BASIC FEATURE STATISTICS: SUCCESSFUL SAMPLE-------')
        #    print('For feature:',feature.upper(),'the sample size is: ',len(variable0b))
        #    print('For feature:',feature.upper(),'the max value is: ',np.max(variable0b))
        #    print('For feature:',feature.upper(),'the min value is: ',np.min(variable0b))
        #    print('For feature:',feature.upper(),'the mean value is: ',round(np.mean(variable0b),3))
        #    print('For feature:',feature.upper(),'the median value is: ',round(np.median(variable0b),3))
        #    print('For feature:',feature.upper(),'the standard deviation is: ',round(np.std(variable0b),3))
        #    print('---------------------------------------------------------')
        #    print('---------------------------------------------------------')
        #except:
        #    print('Statistics Are Not Done for Categorical Features')
        #    print('For feature:',feature.upper(),'the sample size is: ',len(variable0))
        #    print('For feature:',feature.upper(),'the sample size is: ',len(variable0b))

        z,bins,p3 = plt.hist(variable0, bins = 'auto', rwidth=0.9, facecolor = 'blue')
        plt.xlabel(feature,fontsize=17)
        plt.ylabel('Number',fontsize=15)
        plt.xticks(size = 15)
        plt.yticks(size = 15)
        plt.show()


        #fig, ax = plt.subplots()
        #plt.xlabel(feature)
        #plt.ylabel('success')
        #ax.scatter(variable0, success0, c='k')
        #plt.show()
        #fig, ax = plt.subplots()
        #plt.xlabel(feature)
        #plt.ylabel('success')
        #ax.scatter(variable0b, success0b, c='k')
        #plt.show()

        try:
            avg = np.median(variable0b)
            stdev = np.std(variable0b)
            f = [0.5,1.0,1.5,2.0,2.5]

            z,bins,p3 = plt.hist(variable0b, bins = 5, rwidth=0.9, facecolor = 'blue')
            plt.axvline(x=avg,linestyle = "-", linewidth = 2, color = 'k')
        #    for i in f:
        #        plt.axvline(x=avg+i*stdev,linestyle = ":", linewidth = 1, color = 'r')
        #        plt.axvline(x=avg-i*stdev,linestyle = ":", linewidth = 1, color = 'r')

            plt.xlabel(feature,fontsize=17)
            plt.ylabel('Number',fontsize=15)
            plt.xticks(size = 15)
            plt.yticks(size = 15)
            plt.show()
        except:
            if feature not in ['region','industry']:
                print('Statistics Are Not Done for Categorical Features')
                z,bins,p3 = plt.hist(variable0b, bins = 5, rwidth=0.9, facecolor = 'blue')
                plt.xlabel(feature,fontsize=17)
                plt.ylabel('Number',fontsize=15)
                plt.xticks(size = 15)
                plt.yticks(size = 15)
                plt.show()
            if feature == 'region':
                print('Statistics Are Not Done for Categorical Features')
                z,bins,p3 = plt.hist(variable0b, bins = 12, rwidth=0.9, facecolor = 'blue')
                plt.xlabel(feature,fontsize=17)
                plt.ylabel('Number',fontsize=15)
                plt.xticks(size = 15)
                plt.yticks(size = 15)
                plt.show()
            if feature == 'industry':
                print('Statistics Are Not Done for Categorical Features')
                z,bins,p3 = plt.hist(variable0b, bins = 14, rwidth=0.9, facecolor = 'blue')
                plt.xlabel(feature,fontsize=17)
                plt.ylabel('Number',fontsize=15)
                plt.xticks(size = 15)
                plt.xticks(rotation=90)
                plt.tick_params(labelsize=7)
                plt.yticks(size = 15)
                plt.show()

    #Perform grading based on simple stat comparisons (std from median)
    #First Determine Input Data bin

        if feature not in ['region','industry','N_google_news']:

            if feature == 'team':
                feature_in = eval(user_input[2])
            if feature == 'hardcap':
                feature_in = np.log10(eval(user_input[3]))
            if feature == 'price':
                feature_in = np.log10(eval(user_input[4]))
            if feature == 'telegram':
                feature_in = np.log10(eval(user_input[5]))
            if feature == 'N_google_news':
                feature_in = eval(user_input[6])
            if feature == 'N_twitter':
                feature_in = np.log10(eval(user_input[7]))
            if feature == 'N_daily_views':
                feature_in = np.log10(eval(user_input[8]))
            if feature == 'N_daily_time':
                feature_in = np.log10(eval(user_input[9]))

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

            print('The ICO under investigation receives the grade: ',grade,' for feature: ',feature.upper())

            z,bins,p3 = plt.hist(variable0b, bins = 5, rwidth=0.9, facecolor = 'blue')
            plt.axvline(x=avg,linestyle = "-", linewidth = 2, color = 'k')
            plt.axvline(x=feature_in,linestyle = "-", linewidth = 2, color = 'r')
            plt.xlabel(feature,fontsize=17)
            plt.ylabel('Number',fontsize=15)
            plt.xticks(size = 15)
            plt.yticks(size = 15)
            plt.show()

        if feature == 'region':

            region_in = func_region(user_input[0])

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

            print('The ICO under investigation receives the grade: ',grade,' for feature: ',feature.upper())

            z,bins,p3 = plt.hist(variable0b, bins = 12, rwidth=0.9, facecolor = 'blue')
            plt.axvline(x=str(region_in), linestyle = "-", linewidth = 2, color = 'r')
            plt.xlabel(feature,fontsize=17)
            plt.ylabel('Number',fontsize=15)
            plt.xticks(size = 15)
            plt.yticks(size = 15)
            plt.show()

        if feature == 'industry':

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

            print('The ICO under investigation receives the grade: ',grade,' for feature: ',feature.upper())

            z,bins,p3 = plt.hist(variable0b, bins = 14, rwidth=0.9, facecolor = 'blue')
            plt.xlabel(feature,fontsize=17)
            plt.ylabel('Number',fontsize=15)
            plt.axvline(x=tag, linestyle = "-", linewidth = 2, color = 'r')
            plt.xticks(size = 15)
            plt.xticks(rotation=90)
            plt.tick_params(labelsize=7)
            plt.yticks(size = 15)
            plt.show()

        ranks[kk] = grade

    ico_rating = np.mean(ranks)
    ico_rating0 = ico_rating/5.0

    rate_verbose = 'Unrated'

    if (0.0 <= ico_rating < 1.0):
        rate_verbose = 'Very Low'
    if (1.0 <= ico_rating < 2.0):
        rate_verbose = 'Low'
    if (2.0 <= ico_rating < 3.0):
        rate_verbose = 'Medium'
    if (3.0 <= ico_rating < 4.0):
        rate_verbose = 'High'
    if (4.0 <= ico_rating <= 5.0):
        rate_verbose = 'Very High'

    print('The average BloxVerse ranking for this ICO is: ',round(ico_rating,2))
    print('In the 0-1 scale this is equivalent to: ',round(ico_rating0,2))
    print('In ICORating scale this is equivalent to a rating of: ',rate_verbose)

    return 'Normalized BloxVerse Rating: ',round(ico_rating0,2)

print(ico_rank(user_input))

wait = input("PRESS ENTER TO CONTINUE.")

#Perform k-means-based clustering grading - DBSCAN will be more appropriate
#Cannot include categorical data: country, industry
data = pd.read_csv('outdata/ico_data_rate_cluster_q2.csv')
f1 = data['team'].values
f2 = data['hardcap'].values
f3 = data['price'].values
f4 = data['telegram'].values
f5 = data['N_twitter'].values
f6 = data['N_daily_views'].values
f7 = data['N_daily_time'].values

r0 = data['coin']
r1 = data['raised'].values
r2 = data['success'].values

##user_input = ['singapore', 'saas', '24', '30010280.0', '0.1', '25473', '8', '15439', '2.4', '210.0']

inp_ico = [eval(user_input[2]),eval(user_input[3]),eval(user_input[4]),eval(user_input[5]),eval(user_input[7]),eval(user_input[8]),eval(user_input[9])]
inp_ico = np.asarray(inp_ico)
inp_ico_orig = inp_ico
inp_ico = inp_ico.reshape(1,-1)

inp_ico2 =  [eval(user_input[5]),eval(user_input[7]),eval(user_input[8]),eval(user_input[9])]
inp_ico2 = np.asarray(inp_ico2)
inp_ico2 = inp_ico2.reshape(1,-1)

X = np.array(list(zip(f1,f2,f3,f4,f5,f6,f7)))
X = np.concatenate((X, inp_ico))
X = StandardScaler().fit_transform(X)
scaler = StandardScaler().fit(X)

with open("outdata/ico_data_rate_cluster_q2.csv") as f2f:
    readerf = csv.reader(f2f)
    target_data2 = [r2 for r2 in readerf]

with open('outdata/ico_data_social_q2.csv', 'w') as csvfile_bbbb:
    #csvfile_b.write(columnTitles_complete)
    writerbb=csv.writer(csvfile_bbbb, delimiter=',')

    for i in range(0,len(target_data2)):
        if ('N/A' not in target_data2[i][10]) and ('N/A' not in target_data2[i][12]) and ('N/A' not in target_data2[i][14]) and ('N/A' not in target_data2[i][15]) and ('N/A' not in target_data2[i][16]):
            all_databb = [target_data2[i][0],target_data2[i][1],target_data2[i][2],target_data2[i][3],target_data2[i][4],target_data2[i][5],target_data2[i][6],target_data2[i][7],target_data2[i][8],target_data2[i][9],target_data2[i][10],target_data2[i][11],target_data2[i][12],target_data2[i][13],target_data2[i][14],target_data2[i][15],target_data2[i][16],target_data2[i][17],target_data2[i][18],target_data2[i][19],target_data2[i][20],target_data2[i][21],target_data2[i][22],target_data2[i][23],target_data2[i][24],target_data2[i][25],target_data2[i][26],target_data2[i][27],target_data2[i][28],target_data2[i][29]]
            writerbb.writerow(all_databb)

data2 = pd.read_csv('outdata/ico_data_social_q2.csv')
g4 = data2['telegram'].values
g5 = data2['N_twitter'].values
g6 = data2['N_daily_views'].values
g7 = data2['N_daily_time'].values

g0 = data2['coin']
g1 = data2['raised'].values
g2 = data2['success'].values

XX = np.array(list(zip(g4,g5,g6,g7)))
XX = np.concatenate((XX, inp_ico2))
XX = StandardScaler().fit_transform(XX)
scaler2 = StandardScaler().fit(XX)

### BELOW WE USE THE ADOPTED CLUSTERING ARRANGEMENT: FULL DATASET
try:

    N_CL = 6
    kmeans = KMeans(n_clusters=N_CL,random_state=3425)
    # Fitting the input data
    kmeans = kmeans.fit(X)
    # Getting the cluster labels
    labels3 = kmeans.predict(X)
    # Centroid values
    centroids = kmeans.cluster_centers_

    print('---------------------------------------------------------------------------------------')
    print('K-MEANS CLUSTERING METHOD (ENTIRE DATASET), k =',N_CL)
    print('---------------------------------------------------------------------------------------')

    print('Clustering Determined the Following Centroid Coordinates (x,y,z): ')
    print(centroids)
    print('Normalized error for k =',N_CL,'is: ',round(np.sqrt(kmeans.inertia_)/len(labels3),2))
    try:
        print('Sillhouette score is =',metrics.silhouette_score(X, labels3))
    except:
        print('Sillhouette score is =',-1.0)

    try:
        sample_silhouette_values = metrics.silhouette_samples(X, labels3)
    except:
        sample_silhouette_values = -1

    y_lower = 10
    for i in range(N_CL):
            # Aggregate the silhouette scores for samples belonging to
            # cluster i, and sort them
            ith_cluster_silhouette_values = \
                sample_silhouette_values[labels3 == i]

            ith_cluster_silhouette_values.sort()

            size_cluster_i = ith_cluster_silhouette_values.shape[0]
            y_upper = y_lower + size_cluster_i

            color = cm.nipy_spectral(float(i) / N_CL)
            plt.fill_betweenx(np.arange(y_lower, y_upper),
                              0, ith_cluster_silhouette_values,
                              facecolor=color, edgecolor=color, alpha=0.7)

            # Label the silhouette plots with their cluster numbers at the middle
            plt.text(-0.05, y_lower + 0.5 * size_cluster_i, str(i))

            # Compute the new y_lower for next plot
            y_lower = y_upper + 10  # 10 for the 0 samples

    plt.title("The silhouette plot for the various clusters: Full Dataset")
    plt.xlabel("The silhouette coefficient values")
    plt.ylabel("Cluster label")

        # The vertical line for average silhouette score of all the values
    plt.axvline(x=metrics.silhouette_score(X, labels3), color="red", linestyle="--")

    plt.yticks([])  # Clear the yaxis labels / ticks
    plt.xticks([-0.1, 0, 0.2, 0.4, 0.6, 0.8, 1])
    plt.show()

    ico_cluster_label = labels3[len(labels3)-1]
    ico_cluster_indices = [i for i,v in enumerate(labels3) if v == ico_cluster_label]

    coin_cl = []
    team_cl=[] 
    hardcap_cl=[]
    price_cl=[] 
    twitter_cl=[]
    telegram_cl=[]
    dailyviews_cl=[] 
    dailytime_cl=[]
    raised_cl=[]
    success_cl=[]
    clust_data = []

    for i in range(0,len(ico_cluster_indices)-1):
        ind = ico_cluster_indices[i]

        coin_cl.append(i)
        team_cl.append(i) 
        hardcap_cl.append(i)
        price_cl.append(i)
        twitter_cl.append(i)
        telegram_cl.append(i)
        dailyviews_cl.append(i)
        dailytime_cl.append(i)
        raised_cl.append(i)
        success_cl.append(i)
        clust_data.append(i)

        coin_cl[i] = np.array(r0)[ind]
        team_cl[i] = np.array(f1)[ind]
        hardcap_cl[i] = np.array(f2)[ind]
        price_cl[i] = np.array(f3)[ind]
        twitter_cl[i] = np.array(f4)[ind]
        telegram_cl[i] = np.array(f5)[ind]
        dailyviews_cl[i] = np.array(f6)[ind]
        dailytime_cl[i] = np.array(f7)[ind]

        clust_data[i] = [team_cl[i],hardcap_cl[i],price_cl[i],twitter_cl[i],telegram_cl[i],dailyviews_cl[i],dailytime_cl[i]]

        raised_cl[i] = np.array(r1)[ind]
        success_cl[i] = np.array(r2)[ind]

    min_succ = np.argmin(success_cl)

    team_max = max(team_cl)
    if inp_ico_orig[0] > team_max:
        team_max = inp_ico_orig[0]
    hardcap_max = max(hardcap_cl)
    if inp_ico_orig[1] > hardcap_max:
        hardcap_max = inp_ico_orig[1]
    price_max = max(price_cl)
    if inp_ico_orig[2] > price_max:
        price_max = inp_ico_orig[2]
    twitter_max = max(twitter_cl)
    if inp_ico_orig[3] > twitter_max:
        twitter_max = inp_ico_orig[3]
    telegram_max = max(telegram_cl)
    if inp_ico_orig[4] > telegram_max:
        telegram_max = inp_ico_orig[4]
    dailyviews_max = max(dailyviews_cl)
    if inp_ico_orig[5] > dailyviews_max:
        dailyviews_max = inp_ico_orig[5]
    dailytime_max = max(dailytime_cl)
    if inp_ico_orig[6] > dailytime_max:
        dailytime_max = inp_ico_orig[6]

    team_cl_n = team_cl/team_max
    hardcap_cl_n = hardcap_cl/hardcap_max
    price_cl_n = price_cl/price_max
    twitter_cl_n = twitter_cl/twitter_max
    telegram_cl_n = telegram_cl/telegram_max
    dailyviews_cl_n = dailyviews_cl/dailyviews_max
    dailytime_cl_n = dailytime_cl/dailytime_max



    inp_ico_n = [inp_ico_orig[0]/team_max,inp_ico_orig[1]/hardcap_max,inp_ico_orig[2]/price_max,inp_ico_orig[3]/twitter_max,inp_ico_orig[4]/telegram_max,inp_ico_orig[5]/dailyviews_max,inp_ico_orig[6]/dailytime_max]
    inp_ico_n = np.asarray(inp_ico_n)


    worse_ico_n = [team_cl_n[min_succ],hardcap_cl_n[min_succ],price_cl_n[min_succ],twitter_cl_n[min_succ],telegram_cl_n[min_succ],dailyviews_cl_n[min_succ],dailytime_cl_n[min_succ]]
    worse_ico_n = np.asarray(worse_ico_n)

    #Find most-similar ICO
    dist = []
    for i in range(0,len(clust_data)):
        dist.append(i)
        dist[i] = distance.euclidean(inp_ico, clust_data[i])

    min_dist = np.argmin(dist)

    avg_team = np.mean(team_cl)
    avg_hardcap = np.mean(hardcap_cl)
    avg_price = np.mean(price_cl)
    avg_twitter = np.mean(twitter_cl)
    avg_telegram = np.mean(telegram_cl)
    avg_dailyviews = np.mean(dailyviews_cl)
    avg_dailytime = np.mean(dailytime_cl)

    avg_cluster_vector = [avg_team/team_max,avg_hardcap/hardcap_max,avg_price/price_max,avg_twitter/twitter_max,avg_telegram/telegram_max,avg_dailyviews/dailyviews_max,avg_dailytime/dailytime_max]
    avg_cluster_vector = np.asarray(avg_cluster_vector)

    avg_raised = np.mean(raised_cl)
    avg_success = np.mean(success_cl)
    med_success = np.median(success_cl)

    successful_icos_cl = [i for i,v in enumerate(success_cl) if v == 1.0]

    coin_cl2 = []
    team_cl2=[] 
    hardcap_cl2=[]
    price_cl2=[] 
    twitter_cl2=[]
    telegram_cl2=[]
    dailyviews_cl2=[] 
    dailytime_cl2=[]
    raised_cl2=[]
    success_cl2=[]

    for i in range(0,len(successful_icos_cl)):
        ind2 = successful_icos_cl[i]

        coin_cl2.append(i)
        team_cl2.append(i) 
        hardcap_cl2.append(i)
        price_cl2.append(i)
        twitter_cl2.append(i)
        telegram_cl2.append(i)
        dailyviews_cl2.append(i)
        dailytime_cl2.append(i)
        raised_cl2.append(i)
        success_cl2.append(i)

        coin_cl2[i] = coin_cl[ind2]
        team_cl2[i] = team_cl[ind2]
        hardcap_cl2[i] = hardcap_cl[ind2]
        price_cl2[i] =  price_cl[ind2]
        twitter_cl2[i] =twitter_cl[ind2]
        telegram_cl2[i] = telegram_cl[ind2]
        dailyviews_cl2[i] = dailyviews_cl[ind2]
        dailytime_cl2[i] = dailytime_cl[ind2]

        raised_cl2[i] = raised_cl[ind2]
        success_cl2[i] = success_cl[ind2]

    if len(successful_icos_cl) == 0:
        coin_cl2 = coin_cl
        team_cl2 = team_cl
        hardcap_cl2 = hardcap_cl
        price_cl2 = price_cl
        twitter_cl2 = twitter_cl
        telegram_cl2 = telegram_cl
        dailyviews_cl2 = dailyviews_cl
        dailytime_cl2 = dailytime_cl
        raised_cl2 = raised_cl
        success_cl2 = success_cl

    max_raised = np.argmax(raised_cl2)

    team_cl2_n = team_cl2/team_max
    hardcap_cl2_n = hardcap_cl2/hardcap_max
    price_cl2_n = price_cl2/price_max
    twitter_cl2_n = twitter_cl2/twitter_max
    telegram_cl2_n = telegram_cl2/telegram_max
    dailyviews_cl2_n = dailyviews_cl2/dailyviews_max
    dailytime_cl2_n = dailytime_cl2/dailytime_max

    best_ico_n = [team_cl2_n[max_raised],hardcap_cl2_n[max_raised],price_cl2_n[max_raised],twitter_cl2_n[max_raised],telegram_cl2_n[max_raised],dailyviews_cl2_n[max_raised],dailytime_cl2_n[max_raised]]
    best_ico_n = np.asarray(best_ico_n)

    print('Input ICO belongs to cluster: ',ico_cluster_label)
    print('The most similar ICO in cluster is: ',coin_cl[min_dist])
    print('Average cluster ICO: Team: ',round(avg_team,0))
    print('Average cluster ICO: Hardcap: ',round(avg_hardcap,0))
    print('Average cluster ICO: Price: ',round(avg_price,4))
    print('Average cluster ICO: Twitter: ',round(avg_twitter,0))
    print('Average cluster ICO: Telegram: ',round(avg_telegram,0))
    print('Average cluster ICO: Daily Views: ',round(avg_dailyviews,0))
    print('Average cluster ICO: Daily Time: ',round(avg_dailytime,0))
    print('Average cluster ICO: Raised: ',round(avg_raised,0))
    print('Average cluster ICO: Success: ',round(avg_success,0))
    print('Median cluster ICO: Success: ',round(med_success,0))
    print('----------------------------------------')
    print('The least successful ICO in cluster is: ',coin_cl[min_succ])
    print('The least successful ICO raised: ',raised_cl[min_succ])
    print('The least successful ICO success rate was: ',success_cl[min_succ])
    print('The most successful ICO in cluster is: ',coin_cl2[max_raised])
    print('The most successful ICO raised: ',raised_cl2[max_raised])
    print('The most successful ICO success rate was: ',success_cl2[max_raised])

    #RADAR DIAGRAM
    plt.figure(figsize=(12,8))
    categories = ['Team', 'Hardcap', 'ICO Price', 'Twitter', 'Telegram', 'Website Visits', 'Daily Engagement']
    # ------- PART 1: Create background
    NN = len(categories)
    # What will be the angle of each axis in the plot? (we divide the plot / number of variable)
    angles = [n / float(NN) * 2 * pi for n in range(NN)]
    angles += angles[:1]
    # Initialise the spider plot
    ax = plt.subplot(111, polar=True)
    # If you want the first axis to be on top:
    ax.set_theta_offset(pi / 2)
    ax.set_theta_direction(-1)
    # Draw one axe per variable + add labels labels yet
    plt.xticks(angles[:-1], categories, size = '12', weight = 'bold')
    # Draw ylabels
    ax.set_rlabel_position(0)
    plt.yticks([0.25,0.50,0.75], ["0.25","0.50","0.75"], color="grey", size=7)
    plt.ylim(0,1)
    #plt.show()

    # ------- PART 2: Add plots
    # Plot each individual = each line of the data
    # I don't do a loop, because plotting more than 3 groups makes the chart unreadable
    # Ind1
    values = inp_ico_n.flatten().tolist()
    values += values[:1]
    ax.plot(angles, values, linewidth=1, linestyle='dashed', label="ICO under investigation")
    ax.fill(angles, values, 'b', alpha=0.1)
    # Ind2
    values = avg_cluster_vector.flatten().tolist()
    values += values[:1]
    ax.plot(angles, values, linewidth=1, linestyle='solid', label="Average ICO in cluster")
    ax.fill(angles, values, 'r', alpha=0.1)
    # Ind3
    values = worse_ico_n.flatten().tolist()
    values += values[:1]
    ax.plot(angles, values, linewidth=1, linestyle='solid', label="Worse ICO in cluster")
    ax.fill(angles, values, 'g', alpha=0.1)
    # Ind4
    values = best_ico_n.flatten().tolist()
    values += values[:1]
    ax.plot(angles, values, linewidth=1, linestyle='solid', label="Best ICO in cluster")
    ax.fill(angles, values, 'm', alpha=0.1)
    # Add legend
    plt.legend(loc='upper right', bbox_to_anchor=(0.1, 0.1))
    plt.show()

except:
    print('Data size inadequate for clustering analysis in a per-half year basis')



### BELOW WE USE THE ADOPTED CLUSTERING ARRANGEMENT: INTERNET AND SOCIAL STATS DATASET

try:

    N_CL = 5
    kmeans = KMeans(n_clusters=N_CL,random_state=3425)
    # Fitting the input data
    kmeans = kmeans.fit(XX)
    # Getting the cluster labels
    labels4 = kmeans.predict(XX)
    # Centroid values
    centroids = kmeans.cluster_centers_

    print('---------------------------------------------------------------------------------------')
    print('K-MEANS CLUSTERING METHOD (INTERNET STATS DATASET), k =',N_CL)
    print('---------------------------------------------------------------------------------------')

    print('Clustering Determined the Following Centroid Coordinates (x,y,z): ')
    print(centroids)
    print('Normalized error for k =',N_CL,'is: ',round(np.sqrt(kmeans.inertia_)/len(labels4),2))
    try:
        print('Sillhouette score is =',metrics.silhouette_score(XX, labels4))
    except:
        print('Sillhouette score is =',-1.0)

    try:
        sample_silhouette_values = metrics.silhouette_samples(XX, labels4)
    except:
         sample_silhouette_values = -1

    y_lower = 10
    for i in range(N_CL):
            # Aggregate the silhouette scores for samples belonging to
            # cluster i, and sort them
            ith_cluster_silhouette_values = \
                sample_silhouette_values[labels4 == i]

            ith_cluster_silhouette_values.sort()

            size_cluster_i = ith_cluster_silhouette_values.shape[0]
            y_upper = y_lower + size_cluster_i

            color = cm.nipy_spectral(float(i) / N_CL)
            plt.fill_betweenx(np.arange(y_lower, y_upper),
                              0, ith_cluster_silhouette_values,
                              facecolor=color, edgecolor=color, alpha=0.7)

            # Label the silhouette plots with their cluster numbers at the middle
            plt.text(-0.05, y_lower + 0.5 * size_cluster_i, str(i))

            # Compute the new y_lower for next plot
            y_lower = y_upper + 10  # 10 for the 0 samples

    plt.title("The silhouette plot for the various clusters: Internet and Social Stats Dataset")
    plt.xlabel("The silhouette coefficient values")
    plt.ylabel("Cluster label")

        # The vertical line for average silhouette score of all the values
    plt.axvline(x=metrics.silhouette_score(XX, labels4), color="red", linestyle="--")

    plt.yticks([])  # Clear the yaxis labels / ticks
    plt.xticks([-0.1, 0, 0.2, 0.4, 0.6, 0.8, 1])
    plt.show()

    #######################################################
    #######################################################

    ico_cluster_label2 = labels4[len(labels4)-1]
    ico_cluster_indices2 = [i for i,v in enumerate(labels4) if v == ico_cluster_label2]

    coin_cl = []
    twitter_cl=[]
    telegram_cl=[]
    dailyviews_cl=[] 
    dailytime_cl=[]
    raised_cl=[]
    success_cl=[]
    clust_data = []

    for i in range(0,len(ico_cluster_indices2)-1):
        ind = ico_cluster_indices2[i]

        coin_cl.append(i)
        twitter_cl.append(i)
        telegram_cl.append(i)
        dailyviews_cl.append(i)
        dailytime_cl.append(i)
        raised_cl.append(i)
        success_cl.append(i)
        clust_data.append(i)

        coin_cl[i] = np.array(g0)[ind]
        twitter_cl[i] = np.array(g4)[ind]
        telegram_cl[i] = np.array(g5)[ind]
        dailyviews_cl[i] = np.array(g6)[ind]
        dailytime_cl[i] = np.array(g7)[ind]

        clust_data[i] = [twitter_cl[i],telegram_cl[i],dailyviews_cl[i],dailytime_cl[i]]

        raised_cl[i] = np.array(g1)[ind]
        success_cl[i] = np.array(g2)[ind]

    min_succ = np.argmin(success_cl)

    twitter_max = max(twitter_cl)
    if inp_ico_orig[3] > twitter_max:
        twitter_max = inp_ico_orig[3]
    telegram_max = max(telegram_cl)
    if inp_ico_orig[4] > telegram_max:
        telegram_max = inp_ico_orig[4]
    dailyviews_max = max(dailyviews_cl)
    if inp_ico_orig[5] > dailyviews_max:
        dailyviews_max = inp_ico_orig[5]
    dailytime_max = max(dailytime_cl)
    if inp_ico_orig[6] > dailytime_max:
        dailytime_max = inp_ico_orig[6]

    twitter_cl_n = twitter_cl/twitter_max
    telegram_cl_n = telegram_cl/telegram_max
    dailyviews_cl_n = dailyviews_cl/dailyviews_max
    dailytime_cl_n = dailytime_cl/dailytime_max

    inp_ico_n = [inp_ico_orig[3]/twitter_max,inp_ico_orig[4]/telegram_max,inp_ico_orig[5]/dailyviews_max,inp_ico_orig[6]/dailytime_max]
    inp_ico_n = np.asarray(inp_ico_n)

    worse_ico_n = [twitter_cl_n[min_succ],telegram_cl_n[min_succ],dailyviews_cl_n[min_succ],dailytime_cl_n[min_succ]]
    worse_ico_n = np.asarray(worse_ico_n)

    #Find most-similar ICO
    dist = []
    for i in range(0,len(clust_data)):
        dist.append(i)
        dist[i] = distance.euclidean(inp_ico2, clust_data[i])

    min_dist = np.argmin(dist)

    avg_twitter = np.mean(twitter_cl)
    avg_telegram = np.mean(telegram_cl)
    avg_dailyviews = np.mean(dailyviews_cl)
    avg_dailytime = np.mean(dailytime_cl)

    avg_cluster_vector = [avg_twitter/twitter_max,avg_telegram/telegram_max,avg_dailyviews/dailyviews_max,avg_dailytime/dailytime_max]
    avg_cluster_vector = np.asarray(avg_cluster_vector)

    avg_raised = np.mean(raised_cl)
    avg_success = np.mean(success_cl)
    med_success = np.median(success_cl)

    successful_icos_cl = [i for i,v in enumerate(success_cl) if v == 1.0]

    coin_cl2 = []
    twitter_cl2=[]
    telegram_cl2=[]
    dailyviews_cl2=[] 
    dailytime_cl2=[]
    raised_cl2=[]
    success_cl2=[]

    for i in range(0,len(successful_icos_cl)):
        ind2 = successful_icos_cl[i]

        coin_cl2.append(i)
        twitter_cl2.append(i)
        telegram_cl2.append(i)
        dailyviews_cl2.append(i)
        dailytime_cl2.append(i)
        raised_cl2.append(i)
        success_cl2.append(i)

        coin_cl2[i] = coin_cl[ind2]
        twitter_cl2[i] =twitter_cl[ind2]
        telegram_cl2[i] = telegram_cl[ind2]
        dailyviews_cl2[i] = dailyviews_cl[ind2]
        dailytime_cl2[i] = dailytime_cl[ind2]

        raised_cl2[i] = raised_cl[ind2]
        success_cl2[i] = success_cl[ind2]

    max_raised = np.argmax(raised_cl2)

    twitter_cl2_n = twitter_cl2/twitter_max
    telegram_cl2_n = telegram_cl2/telegram_max
    dailyviews_cl2_n = dailyviews_cl2/dailyviews_max
    dailytime_cl2_n = dailytime_cl2/dailytime_max

    best_ico_n = [twitter_cl2_n[max_raised],telegram_cl2_n[max_raised],dailyviews_cl2_n[max_raised],dailytime_cl2_n[max_raised]]
    best_ico_n = np.asarray(best_ico_n)

    print('Input ICO belongs to cluster: ',ico_cluster_label)
    print('The most similar ICO in cluster is: ',coin_cl[min_dist])
    print('Average cluster ICO: Twitter: ',round(avg_twitter,0))
    print('Average cluster ICO: Telegram: ',round(avg_telegram,0))
    print('Average cluster ICO: Daily Views: ',round(avg_dailyviews,0))
    print('Average cluster ICO: Daily Time: ',round(avg_dailytime,0))
    print('Average cluster ICO: Raised: ',round(avg_raised,0))
    print('Average cluster ICO: Success: ',round(avg_success,0))
    print('Median cluster ICO: Success: ',round(med_success,0))
    print('----------------------------------------')
    print('The least successful ICO in cluster is: ',coin_cl[min_succ])
    print('The least successful ICO raised: ',raised_cl[min_succ])
    print('The least successful ICO success rate was: ',success_cl[min_succ])
    print('The most successful ICO in cluster is: ',coin_cl2[max_raised])
    print('The most successful ICO raised: ',raised_cl2[max_raised])
    print('The most successful ICO success rate was: ',success_cl2[max_raised])

    #RADAR DIAGRAM
    plt.figure(figsize=(12,8))
    categories = ['Twitter', 'Telegram', 'Website Visits', 'Daily Engagement']
    # ------- PART 1: Create background
    NN = len(categories)
    # What will be the angle of each axis in the plot? (we divide the plot / number of variable)
    angles = [n / float(NN) * 2 * pi for n in range(NN)]
    angles += angles[:1]
    # Initialise the spider plot
    ax = plt.subplot(111, polar=True)
    # If you want the first axis to be on top:
    ax.set_theta_offset(pi / 2)
    ax.set_theta_direction(-1)
    # Draw one axe per variable + add labels labels yet
    plt.xticks(angles[:-1], categories, size = '12', weight = 'bold')
    # Draw ylabels
    ax.set_rlabel_position(0)
    plt.yticks([0.25,0.50,0.75], ["0.25","0.50","0.75"], color="grey", size=7)
    plt.ylim(0,1)
    #plt.show()

    # ------- PART 2: Add plots
    # Plot each individual = each line of the data
    # I don't do a loop, because plotting more than 3 groups makes the chart unreadable
    # Ind1
    values = inp_ico_n.flatten().tolist()
    values += values[:1]
    ax.plot(angles, values, linewidth=1, linestyle='dashed', label="ICO under investigation")
    ax.fill(angles, values, 'b', alpha=0.1)
    # Ind2
    values = avg_cluster_vector.flatten().tolist()
    values += values[:1]
    ax.plot(angles, values, linewidth=1, linestyle='solid', label="Average ICO in cluster")
    ax.fill(angles, values, 'r', alpha=0.1)
    # Ind3
    values = worse_ico_n.flatten().tolist()
    values += values[:1]
    ax.plot(angles, values, linewidth=1, linestyle='solid', label="Worse ICO in cluster")
    ax.fill(angles, values, 'g', alpha=0.1)
    # Ind4
    values = best_ico_n.flatten().tolist()
    values += values[:1]
    ax.plot(angles, values, linewidth=1, linestyle='solid', label="Best ICO in cluster")
    ax.fill(angles, values, 'm', alpha=0.1)
    # Add legend
    plt.legend(loc='upper right', bbox_to_anchor=(0.1, 0.1))
    plt.show()

except:
    print('Data size inadequate for clustering analysis in a per-half year basis')

