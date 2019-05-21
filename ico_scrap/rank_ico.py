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

def ico_rank(user_input):

    features_vec = ['region','industry','team','hardcap','price','telegram','N_google_news','N_twitter','N_daily_views','N_daily_time']
    kk = -1
    ranks = []
    for feature in features_vec:
        kk = kk + 1
        ranks.append(kk)


        success_threshold = 0.7 #(it did not matter when set to 0)

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

        if feature in ['hype','risk','industry']:
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
data = pd.read_csv('outdata/ico_data_rate_cluster.csv')
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

data2 = pd.read_csv('outdata/ico_data_social.csv')
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

N_CL = 9
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


### BELOW WE USE THE ADOPTED CLUSTERING ARRANGEMENT: INTERNET AND SOCIAL STATS DATASET

N_CL = 8
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


####################### LINEAR REGRESSION ANALYSIS START #################################

data = pd.read_csv('outdata/ico_data_complete.csv')
data_RC = pd.read_csv('outdata/ico_data_rate_cluster.csv')
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
r3 = data['ret_ico_to_day_one'].values
r4 = data['vol_day1'].values
r5 = data['sharpe_yr'].values
#r2 is success
#r1 is funding (money raised)
f1a = data_RC['team'].values
f2a = data_RC['hardcap'].values
f3a = data_RC['price'].values
f4a = data_RC['telegram'].values
f5a = data_RC['N_twitter'].values
f6a = data_RC['N_daily_views'].values
f7a = data_RC['N_daily_time'].values
r0a = data_RC['coin']
r1a = data_RC['raised'].values
r2a = data_RC['success'].values
################

DATA = np.array(list(zip(f1a,f2a,f3a,f4a,f5a,f6a,f7a,r2a)))
DATA = StandardScaler().fit_transform(DATA)
scaler = StandardScaler().fit(DATA)

DATA2 = np.array(list(zip(f1a,f2a,f3a,f4a,f5a,f6a,f7a,r1a)))
DATA2 = StandardScaler().fit_transform(DATA2)
scaler2 = StandardScaler().fit(DATA2)

DATA3 = np.array(list(zip(f1,f2,f3,f4,f5,f6,f7,r3)))
DATA3 = StandardScaler().fit_transform(DATA3)
scaler3 = StandardScaler().fit(DATA3)

DATA4 = np.array(list(zip(f1,f2,f3,f4,f5,f6,f7,r4)))
DATA4 = StandardScaler().fit_transform(DATA4)
scaler4 = StandardScaler().fit(DATA4)

DATA5 = np.array(list(zip(f1,f2,f3,f4,f5,f6,f7,r5)))
DATA5 = StandardScaler().fit_transform(DATA5)
scaler5 = StandardScaler().fit(DATA5)

xs = np.linspace(-10,10,1000)
horiz_line_data = np.array([(0.0) for i in range(len(xs))])

"""
f, axarr = plt.subplots(4, 2)
axarr[0, 0].set_title('SUCCESS BASED')
axarr[0, 0].scatter(DATA[:,0], DATA[:,7],label = 'Team')
axarr[0, 0].yaxis.offsetText.set_visible(False)
axarr[0, 0].set_ylabel("Success",fontsize=11)
#axarr[0, 0].set_xlabel("Team",fontsize=11)
axarr[0, 0].legend()
axarr[0, 0].set_xlim([-4,4])
axarr[0, 0].set_ylim([-4,4])
axarr[0, 0].plot(xs,horiz_line_data, linestyle = ":", linewidth = 1, color = 'k')
axarr[0, 0].axvline(x=0.0,linestyle = ":", linewidth = 1, color = 'k')
axarr[0, 1].scatter(DATA[:,1], DATA[:,7],label = 'Hardcap')
axarr[0, 1].yaxis.offsetText.set_visible(False)
axarr[0, 1].set_ylabel("Success",fontsize=11)
#axarr[0, 1].set_xlabel("Hardcap",fontsize=11)
axarr[0, 1].legend()
axarr[0, 1].set_xlim([-5,5])
axarr[0, 1].set_ylim([-5,5])
axarr[0, 1].plot(xs,horiz_line_data, linestyle = ":", linewidth = 1, color = 'k')
axarr[0, 1].axvline(x=0.0,linestyle = ":", linewidth = 1, color = 'k')
axarr[1, 0].scatter(DATA[:,2], DATA[:,7],label = 'Price')
axarr[1, 0].yaxis.offsetText.set_visible(False)
axarr[1, 0].set_ylabel("Success",fontsize=11)
#axarr[1, 0].set_xlabel("Price",fontsize=11)
axarr[1, 0].legend()
axarr[1, 0].set_xlim([-3,3])
axarr[1, 0].set_ylim([-4,4])
axarr[1, 0].plot(xs,horiz_line_data, linestyle = ":", linewidth = 1, color = 'k')
axarr[1, 0].axvline(x=0.0,linestyle = ":", linewidth = 1, color = 'k')
axarr[1, 1].scatter(DATA[:,3], DATA[:,7],label = 'Telegram')
axarr[1, 1].yaxis.offsetText.set_visible(False)
axarr[1, 1].set_ylabel("Success",fontsize=11)
#axarr[1, 1].set_xlabel("Telegram",fontsize=11)
axarr[1, 1].legend()
axarr[1, 1].set_xlim([-5,5])
axarr[1, 1].set_ylim([-5,5])
axarr[1, 1].plot(xs,horiz_line_data, linestyle = ":", linewidth = 1, color = 'k')
axarr[1, 1].axvline(x=0.0,linestyle = ":", linewidth = 1, color = 'k')
axarr[2, 0].scatter(DATA[:,4], DATA[:,7],label = 'Twitter')
axarr[2, 0].yaxis.offsetText.set_visible(False)
axarr[2, 0].set_ylabel("Success",fontsize=11)
#axarr[2, 0].set_xlabel("Twitter",fontsize=11)
axarr[2, 0].legend()
axarr[2, 0].set_xlim([-4,4])
axarr[2, 0].set_ylim([-5,5])
axarr[2, 0].plot(xs,horiz_line_data, linestyle = ":", linewidth = 1, color = 'k')
axarr[2, 0].axvline(x=0.0,linestyle = ":", linewidth = 1, color = 'k')
axarr[2, 1].scatter(DATA[:,5], DATA[:,7],label = 'Daily Views')
axarr[2, 1].yaxis.offsetText.set_visible(False)
axarr[2, 1].set_ylabel("Success",fontsize=11)
#axarr[2, 1].set_xlabel("Daily Views",fontsize=11)
axarr[2, 1].legend()
axarr[2, 1].set_xlim([-5,5])
axarr[2, 1].set_ylim([-5,5])
axarr[2, 1].plot(xs,horiz_line_data, linestyle = ":", linewidth = 1, color = 'k')
axarr[2, 1].axvline(x=0.0,linestyle = ":", linewidth = 1, color = 'k')
axarr[3, 0].scatter(DATA[:,6], DATA[:,7],label = 'Daily Time')
axarr[3, 0].yaxis.offsetText.set_visible(False)
axarr[3, 0].set_ylabel("Success",fontsize=11)
#axarr[3, 0].set_xlabel("Daily Time",fontsize=11)
axarr[3, 0].legend()
axarr[3, 0].set_xlim([-4,4])
axarr[3, 0].set_ylim([-3,3])
axarr[3, 0].plot(xs,horiz_line_data, linestyle = ":", linewidth = 1, color = 'k')
axarr[3, 0].axvline(x=0.0,linestyle = ":", linewidth = 1, color = 'k')
axarr[3, 1].scatter(DATA[:,7], DATA[:,7],label = 'Success')
axarr[3, 1].yaxis.offsetText.set_visible(False)
axarr[3, 1].set_ylabel("Success",fontsize=11)
#axarr[3, 1].set_xlabel("Success",fontsize=11)
axarr[3, 1].legend()
axarr[3, 1].set_xlim([-3,3])
axarr[3, 1].set_ylim([-3,3])
axarr[3, 1].plot(xs,horiz_line_data, linestyle = ":", linewidth = 1, color = 'k')
axarr[3, 1].axvline(x=0.0,linestyle = ":", linewidth = 1, color = 'k')
plt.show()

f, axarr = plt.subplots(4, 2)
axarr[0, 0].set_title('FUNDING BASED')
axarr[0, 0].scatter(DATA2[:,0], DATA2[:,7],label = 'Team')
axarr[0, 0].yaxis.offsetText.set_visible(False)
axarr[0, 0].set_ylabel("Raised",fontsize=11)
#axarr[0, 0].set_xlabel("Team",fontsize=11)
axarr[0, 0].legend()
axarr[0, 0].set_xlim([-4,4])
axarr[0, 0].set_ylim([-4,4])
axarr[0, 0].plot(xs,horiz_line_data, linestyle = ":", linewidth = 1, color = 'k')
axarr[0, 0].axvline(x=0.0,linestyle = ":", linewidth = 1, color = 'k')
axarr[0, 1].scatter(DATA2[:,1], DATA2[:,7],label = 'Hardcap')
axarr[0, 1].yaxis.offsetText.set_visible(False)
axarr[0, 1].set_ylabel("Raised",fontsize=11)
#axarr[0, 1].set_xlabel("Hardcap",fontsize=11)
axarr[0, 1].legend()
axarr[0, 1].set_xlim([-5,5])
axarr[0, 1].set_ylim([-5,5])
axarr[0, 1].plot(xs,horiz_line_data, linestyle = ":", linewidth = 1, color = 'k')
axarr[0, 1].axvline(x=0.0,linestyle = ":", linewidth = 1, color = 'k')
axarr[1, 0].scatter(DATA2[:,2], DATA2[:,7],label = 'Price')
axarr[1, 0].yaxis.offsetText.set_visible(False)
axarr[1, 0].set_ylabel("Raised",fontsize=11)
#axarr[1, 0].set_xlabel("Price",fontsize=11)
axarr[1, 0].legend()
axarr[1, 0].set_xlim([-3,3])
axarr[1, 0].set_ylim([-4,4])
axarr[1, 0].plot(xs,horiz_line_data, linestyle = ":", linewidth = 1, color = 'k')
axarr[1, 0].axvline(x=0.0,linestyle = ":", linewidth = 1, color = 'k')
axarr[1, 1].scatter(DATA2[:,3], DATA2[:,7],label = 'Telegram')
axarr[1, 1].yaxis.offsetText.set_visible(False)
axarr[1, 1].set_ylabel("Raised",fontsize=11)
#axarr[1, 1].set_xlabel("Telegram",fontsize=11)
axarr[1, 1].legend()
axarr[1, 1].set_xlim([-5,5])
axarr[1, 1].set_ylim([-5,5])
axarr[1, 1].plot(xs,horiz_line_data, linestyle = ":", linewidth = 1, color = 'k')
axarr[1, 1].axvline(x=0.0,linestyle = ":", linewidth = 1, color = 'k')
axarr[2, 0].scatter(DATA2[:,4], DATA2[:,7],label = 'Twitter')
axarr[2, 0].yaxis.offsetText.set_visible(False)
axarr[2, 0].set_ylabel("Raised",fontsize=11)
#axarr[2, 0].set_xlabel("Twitter",fontsize=11)
axarr[2, 0].legend()
axarr[2, 0].set_xlim([-4,4])
axarr[2, 0].set_ylim([-5,5])
axarr[2, 0].plot(xs,horiz_line_data, linestyle = ":", linewidth = 1, color = 'k')
axarr[2, 0].axvline(x=0.0,linestyle = ":", linewidth = 1, color = 'k')
axarr[2, 1].scatter(DATA2[:,5], DATA2[:,7],label = 'Daily Views')
axarr[2, 1].yaxis.offsetText.set_visible(False)
axarr[2, 1].set_ylabel("Raised",fontsize=11)
#axarr[2, 1].set_xlabel("Daily Views",fontsize=11)
axarr[2, 1].legend()
axarr[2, 1].set_xlim([-5,5])
axarr[2, 1].set_ylim([-5,5])
axarr[2, 1].plot(xs,horiz_line_data, linestyle = ":", linewidth = 1, color = 'k')
axarr[2, 1].axvline(x=0.0,linestyle = ":", linewidth = 1, color = 'k')
axarr[3, 0].scatter(DATA2[:,6], DATA2[:,7],label = 'Daily Time')
axarr[3, 0].yaxis.offsetText.set_visible(False)
axarr[3, 0].set_ylabel("Raised",fontsize=11)
#axarr[3, 0].set_xlabel("Daily Time",fontsize=11)
axarr[3, 0].legend()
axarr[3, 0].set_xlim([-4,4])
axarr[3, 0].set_ylim([-3,3])
axarr[3, 0].plot(xs,horiz_line_data, linestyle = ":", linewidth = 1, color = 'k')
axarr[3, 0].axvline(x=0.0,linestyle = ":", linewidth = 1, color = 'k')
axarr[3, 1].scatter(DATA2[:,7], DATA2[:,7],label = 'Raised')
axarr[3, 1].yaxis.offsetText.set_visible(False)
axarr[3, 1].set_ylabel("Raised",fontsize=11)
#axarr[3, 1].set_xlabel("Success",fontsize=11)
axarr[3, 1].legend()
axarr[3, 1].set_xlim([-3,3])
axarr[3, 1].set_ylim([-3,3])
axarr[3, 1].plot(xs,horiz_line_data, linestyle = ":", linewidth = 1, color = 'k')
axarr[3, 1].axvline(x=0.0,linestyle = ":", linewidth = 1, color = 'k')
plt.show()

f, axarr = plt.subplots(4, 2)
axarr[0, 0].set_title('DAY 1 RETURN BASED')
axarr[0, 0].scatter(DATA3[:,0], DATA3[:,7],label = 'Team')
axarr[0, 0].yaxis.offsetText.set_visible(False)
axarr[0, 0].set_ylabel("Return D1",fontsize=11)
#axarr[0, 0].set_xlabel("Team",fontsize=11)
axarr[0, 0].legend()
axarr[0, 0].set_xlim([-4,4])
axarr[0, 0].set_ylim([-4,4])
axarr[0, 0].plot(xs,horiz_line_data, linestyle = ":", linewidth = 1, color = 'k')
axarr[0, 0].axvline(x=0.0,linestyle = ":", linewidth = 1, color = 'k')
axarr[0, 1].scatter(DATA3[:,1], DATA3[:,7],label = 'Hardcap')
axarr[0, 1].yaxis.offsetText.set_visible(False)
axarr[0, 1].set_ylabel("Return D1",fontsize=11)
#axarr[0, 1].set_xlabel("Hardcap",fontsize=11)
axarr[0, 1].legend()
axarr[0, 1].set_xlim([-5,5])
axarr[0, 1].set_ylim([-5,5])
axarr[0, 1].plot(xs,horiz_line_data, linestyle = ":", linewidth = 1, color = 'k')
axarr[0, 1].axvline(x=0.0,linestyle = ":", linewidth = 1, color = 'k')
axarr[1, 0].scatter(DATA3[:,2], DATA3[:,7],label = 'Price')
axarr[1, 0].yaxis.offsetText.set_visible(False)
axarr[1, 0].set_ylabel("Return D1",fontsize=11)
#axarr[1, 0].set_xlabel("Price",fontsize=11)
axarr[1, 0].legend()
axarr[1, 0].set_xlim([-3,3])
axarr[1, 0].set_ylim([-4,4])
axarr[1, 0].plot(xs,horiz_line_data, linestyle = ":", linewidth = 1, color = 'k')
axarr[1, 0].axvline(x=0.0,linestyle = ":", linewidth = 1, color = 'k')
axarr[1, 1].scatter(DATA3[:,3], DATA3[:,7],label = 'Telegram')
axarr[1, 1].yaxis.offsetText.set_visible(False)
axarr[1, 1].set_ylabel("Return D1",fontsize=11)
#axarr[1, 1].set_xlabel("Telegram",fontsize=11)
axarr[1, 1].legend()
axarr[1, 1].set_xlim([-5,5])
axarr[1, 1].set_ylim([-5,5])
axarr[1, 1].plot(xs,horiz_line_data, linestyle = ":", linewidth = 1, color = 'k')
axarr[1, 1].axvline(x=0.0,linestyle = ":", linewidth = 1, color = 'k')
axarr[2, 0].scatter(DATA3[:,4], DATA3[:,7],label = 'Twitter')
axarr[2, 0].yaxis.offsetText.set_visible(False)
axarr[2, 0].set_ylabel("Return D1",fontsize=11)
#axarr[2, 0].set_xlabel("Twitter",fontsize=11)
axarr[2, 0].legend()
axarr[2, 0].set_xlim([-4,4])
axarr[2, 0].set_ylim([-5,5])
axarr[2, 0].plot(xs,horiz_line_data, linestyle = ":", linewidth = 1, color = 'k')
axarr[2, 0].axvline(x=0.0,linestyle = ":", linewidth = 1, color = 'k')
axarr[2, 1].scatter(DATA3[:,5], DATA3[:,7],label = 'Daily Views')
axarr[2, 1].yaxis.offsetText.set_visible(False)
axarr[2, 1].set_ylabel("Return D1",fontsize=11)
#axarr[2, 1].set_xlabel("Daily Views",fontsize=11)
axarr[2, 1].legend()
axarr[2, 1].set_xlim([-5,5])
axarr[2, 1].set_ylim([-5,5])
axarr[2, 1].plot(xs,horiz_line_data, linestyle = ":", linewidth = 1, color = 'k')
axarr[2, 1].axvline(x=0.0,linestyle = ":", linewidth = 1, color = 'k')
axarr[3, 0].scatter(DATA3[:,6], DATA3[:,7],label = 'Daily Time')
axarr[3, 0].yaxis.offsetText.set_visible(False)
axarr[3, 0].set_ylabel("Return D1",fontsize=11)
#axarr[3, 0].set_xlabel("Daily Time",fontsize=11)
axarr[3, 0].legend()
axarr[3, 0].set_xlim([-4,4])
axarr[3, 0].set_ylim([-3,3])
axarr[3, 0].plot(xs,horiz_line_data, linestyle = ":", linewidth = 1, color = 'k')
axarr[3, 0].axvline(x=0.0,linestyle = ":", linewidth = 1, color = 'k')
axarr[3, 1].scatter(DATA3[:,7], DATA3[:,7],label = 'Return D1')
axarr[3, 1].yaxis.offsetText.set_visible(False)
axarr[3, 1].set_ylabel("Return D1",fontsize=11)
#axarr[3, 1].set_xlabel("Success",fontsize=11)
axarr[3, 1].legend()
axarr[3, 1].set_xlim([-3,3])
axarr[3, 1].set_ylim([-3,3])
axarr[3, 1].plot(xs,horiz_line_data, linestyle = ":", linewidth = 1, color = 'k')
axarr[3, 1].axvline(x=0.0,linestyle = ":", linewidth = 1, color = 'k')
plt.show()

f, axarr = plt.subplots(4, 2)
axarr[0, 0].set_title('VOLUME DAY 1 BASED')
axarr[0, 0].scatter(DATA4[:,0], DATA4[:,7],label = 'Team')
axarr[0, 0].yaxis.offsetText.set_visible(False)
axarr[0, 0].set_ylabel("Volume D1",fontsize=11)
#axarr[0, 0].set_xlabel("Team",fontsize=11)
axarr[0, 0].legend()
axarr[0, 0].set_xlim([-4,4])
axarr[0, 0].set_ylim([-4,4])
axarr[0, 0].plot(xs,horiz_line_data, linestyle = ":", linewidth = 1, color = 'k')
axarr[0, 0].axvline(x=0.0,linestyle = ":", linewidth = 1, color = 'k')
axarr[0, 1].scatter(DATA4[:,1], DATA4[:,7],label = 'Hardcap')
axarr[0, 1].yaxis.offsetText.set_visible(False)
axarr[0, 1].set_ylabel("Volume D1",fontsize=11)
#axarr[0, 1].set_xlabel("Hardcap",fontsize=11)
axarr[0, 1].legend()
axarr[0, 1].set_xlim([-5,5])
axarr[0, 1].set_ylim([-5,5])
axarr[0, 1].plot(xs,horiz_line_data, linestyle = ":", linewidth = 1, color = 'k')
axarr[0, 1].axvline(x=0.0,linestyle = ":", linewidth = 1, color = 'k')
axarr[1, 0].scatter(DATA4[:,2], DATA4[:,7],label = 'Price')
axarr[1, 0].yaxis.offsetText.set_visible(False)
axarr[1, 0].set_ylabel("Volume D1",fontsize=11)
#axarr[1, 0].set_xlabel("Price",fontsize=11)
axarr[1, 0].legend()
axarr[1, 0].set_xlim([-3,3])
axarr[1, 0].set_ylim([-4,4])
axarr[1, 0].plot(xs,horiz_line_data, linestyle = ":", linewidth = 1, color = 'k')
axarr[1, 0].axvline(x=0.0,linestyle = ":", linewidth = 1, color = 'k')
axarr[1, 1].scatter(DATA4[:,3], DATA4[:,7],label = 'Telegram')
axarr[1, 1].yaxis.offsetText.set_visible(False)
axarr[1, 1].set_ylabel("Volume D1",fontsize=11)
#axarr[1, 1].set_xlabel("Telegram",fontsize=11)
axarr[1, 1].legend()
axarr[1, 1].set_xlim([-5,5])
axarr[1, 1].set_ylim([-5,5])
axarr[1, 1].plot(xs,horiz_line_data, linestyle = ":", linewidth = 1, color = 'k')
axarr[1, 1].axvline(x=0.0,linestyle = ":", linewidth = 1, color = 'k')
axarr[2, 0].scatter(DATA4[:,4], DATA4[:,7],label = 'Twitter')
axarr[2, 0].yaxis.offsetText.set_visible(False)
axarr[2, 0].set_ylabel("Volume D1",fontsize=11)
#axarr[2, 0].set_xlabel("Twitter",fontsize=11)
axarr[2, 0].legend()
axarr[2, 0].set_xlim([-4,4])
axarr[2, 0].set_ylim([-5,5])
axarr[2, 0].plot(xs,horiz_line_data, linestyle = ":", linewidth = 1, color = 'k')
axarr[2, 0].axvline(x=0.0,linestyle = ":", linewidth = 1, color = 'k')
axarr[2, 1].scatter(DATA4[:,5], DATA4[:,7],label = 'Daily Views')
axarr[2, 1].yaxis.offsetText.set_visible(False)
axarr[2, 1].set_ylabel("Volume D1",fontsize=11)
#axarr[2, 1].set_xlabel("Daily Views",fontsize=11)
axarr[2, 1].legend()
axarr[2, 1].set_xlim([-5,5])
axarr[2, 1].set_ylim([-5,5])
axarr[2, 1].plot(xs,horiz_line_data, linestyle = ":", linewidth = 1, color = 'k')
axarr[2, 1].axvline(x=0.0,linestyle = ":", linewidth = 1, color = 'k')
axarr[3, 0].scatter(DATA4[:,6], DATA4[:,7],label = 'Daily Time')
axarr[3, 0].yaxis.offsetText.set_visible(False)
axarr[3, 0].set_ylabel("Volume D1",fontsize=11)
#axarr[3, 0].set_xlabel("Daily Time",fontsize=11)
axarr[3, 0].legend()
axarr[3, 0].set_xlim([-4,4])
axarr[3, 0].set_ylim([-3,3])
axarr[3, 0].plot(xs,horiz_line_data, linestyle = ":", linewidth = 1, color = 'k')
axarr[3, 0].axvline(x=0.0,linestyle = ":", linewidth = 1, color = 'k')
axarr[3, 1].scatter(DATA4[:,7], DATA4[:,7],label = 'Volume D1')
axarr[3, 1].yaxis.offsetText.set_visible(False)
axarr[3, 1].set_ylabel("Volume D1",fontsize=11)
#axarr[3, 1].set_xlabel("Success",fontsize=11)
axarr[3, 1].legend()
axarr[3, 1].set_xlim([-3,3])
axarr[3, 1].set_ylim([-3,3])
axarr[3, 1].plot(xs,horiz_line_data, linestyle = ":", linewidth = 1, color = 'k')
axarr[3, 1].axvline(x=0.0,linestyle = ":", linewidth = 1, color = 'k')
plt.show()

f, axarr = plt.subplots(4, 2)
axarr[0, 0].set_title('SHARPE BASED')
axarr[0, 0].scatter(DATA5[:,0], DATA5[:,7],label = 'Team')
axarr[0, 0].yaxis.offsetText.set_visible(False)
axarr[0, 0].set_ylabel("Sharpe",fontsize=11)
#axarr[0, 0].set_xlabel("Team",fontsize=11)
axarr[0, 0].legend()
axarr[0, 0].set_xlim([-4,4])
axarr[0, 0].set_ylim([-4,4])
axarr[0, 0].plot(xs,horiz_line_data, linestyle = ":", linewidth = 1, color = 'k')
axarr[0, 0].axvline(x=0.0,linestyle = ":", linewidth = 1, color = 'k')
axarr[0, 1].scatter(DATA5[:,1], DATA5[:,7],label = 'Hardcap')
axarr[0, 1].yaxis.offsetText.set_visible(False)
axarr[0, 1].set_ylabel("Sharpe",fontsize=11)
#axarr[0, 1].set_xlabel("Hardcap",fontsize=11)
axarr[0, 1].legend()
axarr[0, 1].set_xlim([-5,5])
axarr[0, 1].set_ylim([-5,5])
axarr[0, 1].plot(xs,horiz_line_data, linestyle = ":", linewidth = 1, color = 'k')
axarr[0, 1].axvline(x=0.0,linestyle = ":", linewidth = 1, color = 'k')
axarr[1, 0].scatter(DATA5[:,2], DATA5[:,7],label = 'Price')
axarr[1, 0].yaxis.offsetText.set_visible(False)
axarr[1, 0].set_ylabel("Sharpe",fontsize=11)
#axarr[1, 0].set_xlabel("Price",fontsize=11)
axarr[1, 0].legend()
axarr[1, 0].set_xlim([-3,3])
axarr[1, 0].set_ylim([-4,4])
axarr[1, 0].plot(xs,horiz_line_data, linestyle = ":", linewidth = 1, color = 'k')
axarr[1, 0].axvline(x=0.0,linestyle = ":", linewidth = 1, color = 'k')
axarr[1, 1].scatter(DATA5[:,3], DATA5[:,7],label = 'Telegram')
axarr[1, 1].yaxis.offsetText.set_visible(False)
axarr[1, 1].set_ylabel("Sharpe",fontsize=11)
#axarr[1, 1].set_xlabel("Telegram",fontsize=11)
axarr[1, 1].legend()
axarr[1, 1].set_xlim([-5,5])
axarr[1, 1].set_ylim([-5,5])
axarr[1, 1].plot(xs,horiz_line_data, linestyle = ":", linewidth = 1, color = 'k')
axarr[1, 1].axvline(x=0.0,linestyle = ":", linewidth = 1, color = 'k')
axarr[2, 0].scatter(DATA5[:,4], DATA5[:,7],label = 'Twitter')
axarr[2, 0].yaxis.offsetText.set_visible(False)
axarr[2, 0].set_ylabel("Sharpe",fontsize=11)
#axarr[2, 0].set_xlabel("Twitter",fontsize=11)
axarr[2, 0].legend()
axarr[2, 0].set_xlim([-4,4])
axarr[2, 0].set_ylim([-5,5])
axarr[2, 0].plot(xs,horiz_line_data, linestyle = ":", linewidth = 1, color = 'k')
axarr[2, 0].axvline(x=0.0,linestyle = ":", linewidth = 1, color = 'k')
axarr[2, 1].scatter(DATA5[:,5], DATA5[:,7],label = 'Daily Views')
axarr[2, 1].yaxis.offsetText.set_visible(False)
axarr[2, 1].set_ylabel("Sharpe",fontsize=11)
#axarr[2, 1].set_xlabel("Daily Views",fontsize=11)
axarr[2, 1].legend()
axarr[2, 1].set_xlim([-5,5])
axarr[2, 1].set_ylim([-5,5])
axarr[2, 1].plot(xs,horiz_line_data, linestyle = ":", linewidth = 1, color = 'k')
axarr[2, 1].axvline(x=0.0,linestyle = ":", linewidth = 1, color = 'k')
axarr[3, 0].scatter(DATA5[:,6], DATA5[:,7],label = 'Daily Time')
axarr[3, 0].yaxis.offsetText.set_visible(False)
axarr[3, 0].set_ylabel("Sharpe",fontsize=11)
#axarr[3, 0].set_xlabel("Daily Time",fontsize=11)
axarr[3, 0].legend()
axarr[3, 0].set_xlim([-4,4])
axarr[3, 0].set_ylim([-3,3])
axarr[3, 0].plot(xs,horiz_line_data, linestyle = ":", linewidth = 1, color = 'k')
axarr[3, 0].axvline(x=0.0,linestyle = ":", linewidth = 1, color = 'k')
axarr[3, 1].scatter(DATA5[:,7], DATA5[:,7],label = 'Sharpe')
axarr[3, 1].yaxis.offsetText.set_visible(False)
axarr[3, 1].set_ylabel("Sharpe",fontsize=11)
#axarr[3, 1].set_xlabel("Success",fontsize=11)
axarr[3, 1].legend()
axarr[3, 1].set_xlim([-3,3])
axarr[3, 1].set_ylim([-3,3])
axarr[3, 1].plot(xs,horiz_line_data, linestyle = ":", linewidth = 1, color = 'k')
axarr[3, 1].axvline(x=0.0,linestyle = ":", linewidth = 1, color = 'k')
plt.show()

"""

##ANALYTICS

###### SUCCESS ######

DATA = np.array(list(zip(f1a,f2a,f3a,f4a,f5a,f6a,f7a,r2a)))
feature_matrix = DATA[:,0:7]
target_vector = DATA[:,7]
target_vector = target_vector.reshape(-1,1)
scalerX = StandardScaler().fit(feature_matrix)
scalery = StandardScaler().fit(target_vector)
feature_matrix = scalerX.transform(feature_matrix)
target_vector = scalery.transform(target_vector)

x_new = inp_ico
x_new = scalerX.transform(x_new)

X_train, X_test, y_train, y_test = train_test_split(feature_matrix, target_vector, test_size=0.4, 
                                                    random_state=1)
reg = linear_model.LinearRegression()
reg.fit(X_train, y_train)
print('------------------------------------------')
print('LINEAR REGRESSION ANALYSIS: ICO SUCCESS \n')
print('Coefficients: \n', reg.coef_)
print('Variance score: {}'.format(reg.score(X_test, y_test)))
plot = False
if plot:
    # plot for residual error 
    ## setting plot style 
    plt.style.use('fivethirtyeight') 
    ## plotting residual errors in training data 
    plt.scatter(reg.predict(X_train), reg.predict(X_train) - y_train, 
                color = "green", s = 10, label = 'Train data') 
    ## plotting residual errors in test data 
    plt.scatter(reg.predict(X_test), reg.predict(X_test) - y_test, 
                color = "blue", s = 10, label = 'Test data') 
    ## plotting line for zero residual error 
    plt.hlines(y = 0, xmin = -2, xmax = 2, linewidth = 2) 
    ## plotting legend 
    plt.legend(loc = 'upper right') 
    ## plot title 
    plt.title("Residual errors: ICO SUCCESS") 
    ## function to show plot 
    plt.show()

prediction0 = reg.predict(x_new)
prediction = round(scalery.inverse_transform(prediction0)[0][0], 2)

print('The LR model prediction for SUCCESS is: ', prediction)

###### FUNDING ######

DATA = np.array(list(zip(f1a,f2a,f3a,f4a,f5a,f6a,f7a,r1a)))
feature_matrix = DATA[:,0:7]
target_vector = DATA[:,7]
target_vector = target_vector.reshape(-1,1)
scalerX = StandardScaler().fit(feature_matrix)
scalery = StandardScaler().fit(target_vector)
feature_matrix = scalerX.transform(feature_matrix)
target_vector = scalery.transform(target_vector)

x_new = inp_ico
x_new = scalerX.transform(x_new)

X_train, X_test, y_train, y_test = train_test_split(feature_matrix, target_vector, test_size=0.4, 
                                                    random_state=1)
reg = linear_model.LinearRegression()
#reg = linear_model.SGDRegressor(loss='squared_loss', penalty=None, random_state=42)

reg.fit(X_train, y_train)
print('------------------------------------------')
print('LINEAR REGRESSION ANALYSIS: MONEY RAISED \n')
print('Coefficients: \n', reg.coef_)
print('Variance score: {}'.format(reg.score(X_test, y_test)))

# plot for residual error 
## setting plot style
if plot:
    plt.style.use('fivethirtyeight') 
    ## plotting residual errors in training data 
    plt.scatter(reg.predict(X_train), reg.predict(X_train) - y_train, 
                color = "green", s = 10, label = 'Train data') 
    ## plotting residual errors in test data 
    plt.scatter(reg.predict(X_test), reg.predict(X_test) - y_test, 
                color = "blue", s = 10, label = 'Test data') 
    ## plotting line for zero residual error 
    plt.hlines(y = 0, xmin = -2.5, xmax = 2.5, linewidth = 2) 
    ## plotting legend 
    plt.legend(loc = 'upper right') 
    ## plot title 
    plt.title("Residual errors: MONEY RAISED") 
    ## function to show plot 
    plt.show()

prediction0 = reg.predict(x_new)
prediction = round(scalery.inverse_transform(prediction0)[0][0], 2)

print('The LR model prediction for MONEY RAISED is: ', prediction)

###### DAY 1 RETURNS ######

DATA = np.array(list(zip(f1,f2,f3,f4,f5,f6,f7,r3)))
feature_matrix = DATA[:,0:7]
target_vector = DATA[:,7]
target_vector = target_vector.reshape(-1,1)
scalerX = StandardScaler().fit(feature_matrix)
scalery = StandardScaler().fit(target_vector)
feature_matrix = scalerX.transform(feature_matrix)
target_vector = scalery.transform(target_vector)

x_new = inp_ico
x_new = scalerX.transform(x_new)

X_train, X_test, y_train, y_test = train_test_split(feature_matrix, target_vector, test_size=0.4, 
                                                    random_state=1)
reg = linear_model.LinearRegression()
reg.fit(X_train, y_train)
print('------------------------------------------')
print('LINEAR REGRESSION ANALYSIS: DAY 1 RETURN \n')
print('Coefficients: \n', reg.coef_)
print('Variance score: {}'.format(reg.score(X_test, y_test)))
# plot for residual error 
## setting plot style
if plot:
    plt.style.use('fivethirtyeight') 
    ## plotting residual errors in training data 
    plt.scatter(reg.predict(X_train), reg.predict(X_train) - y_train, 
                color = "green", s = 10, label = 'Train data') 
    ## plotting residual errors in test data 
    plt.scatter(reg.predict(X_test), reg.predict(X_test) - y_test, 
                color = "blue", s = 10, label = 'Test data') 
    ## plotting line for zero residual error 
    plt.hlines(y = 0, xmin = -3, xmax = 3, linewidth = 2) 
    ## plotting legend 
    plt.legend(loc = 'upper right') 
    ## plot title 
    plt.title("Residual errors: DAY 1 RETURN") 
    ## function to show plot 
    plt.show()

prediction0 = reg.predict(x_new)
prediction = round(scalery.inverse_transform(prediction0)[0][0], 2)

print('The LR model prediction for DAY 1 RETURN is: ', prediction)

###### DAY 1 VOLUME ######

DATA = np.array(list(zip(f1,f2,f3,f4,f5,f6,f7,r4)))
feature_matrix = DATA[:,0:7]
target_vector = DATA[:,7]
target_vector = target_vector.reshape(-1,1)
scalerX = StandardScaler().fit(feature_matrix)
scalery = StandardScaler().fit(target_vector)
feature_matrix = scalerX.transform(feature_matrix)
target_vector = scalery.transform(target_vector)

x_new = inp_ico
x_new = scalerX.transform(x_new)

X_train, X_test, y_train, y_test = train_test_split(feature_matrix, target_vector, test_size=0.4, 
                                                    random_state=1)
reg = linear_model.LinearRegression()
reg.fit(X_train, y_train)
print('------------------------------------------')
print('LINEAR REGRESSION ANALYSIS: DAY 1 VOLUME \n')
print('Coefficients: \n', reg.coef_)
print('Variance score: {}'.format(reg.score(X_test, y_test)))
# plot for residual error 
## setting plot style
if plot:
    plt.style.use('fivethirtyeight') 
    ## plotting residual errors in training data 
    plt.scatter(reg.predict(X_train), reg.predict(X_train) - y_train, 
                color = "green", s = 10, label = 'Train data') 
    ## plotting residual errors in test data 
    plt.scatter(reg.predict(X_test), reg.predict(X_test) - y_test, 
                color = "blue", s = 10, label = 'Test data') 
    ## plotting line for zero residual error 
    plt.hlines(y = 0, xmin = -2, xmax = 2, linewidth = 2) 
    ## plotting legend 
    plt.legend(loc = 'upper right') 
    ## plot title 
    plt.title("Residual errors: DAY 1 VOLUME") 
    ## function to show plot 
    plt.show()

prediction0 = reg.predict(x_new)
prediction = round(scalery.inverse_transform(prediction0)[0][0], 2)

print('The LR model prediction for DAY 1 VOLUME is: ', prediction)

###### SHARPE RATIO ######

DATA = np.array(list(zip(f1,f2,f3,f4,f5,f6,f7,r5)))
feature_matrix = DATA[:,0:7]
target_vector = DATA[:,7]
target_vector = target_vector.reshape(-1,1)
scalerX = StandardScaler().fit(feature_matrix)
scalery = StandardScaler().fit(target_vector)
feature_matrix = scalerX.transform(feature_matrix)
target_vector = scalery.transform(target_vector)

x_new = inp_ico
x_new = scalerX.transform(x_new)

X_train, X_test, y_train, y_test = train_test_split(feature_matrix, target_vector, test_size=0.4, 
                                                    random_state=1)
reg = linear_model.LinearRegression()
reg.fit(X_train, y_train)
print('------------------------------------------')
print('LINEAR REGRESSION ANALYSIS: SHARPE RATIO \n')
print('Coefficients: \n', reg.coef_)
print('Variance score: {}'.format(reg.score(X_test, y_test)))
# plot for residual error 
## setting plot style
if plot:
    plt.style.use('fivethirtyeight') 
    ## plotting residual errors in training data 
    plt.scatter(reg.predict(X_train), reg.predict(X_train) - y_train, 
                color = "green", s = 10, label = 'Train data') 
    ## plotting residual errors in test data 
    plt.scatter(reg.predict(X_test), reg.predict(X_test) - y_test, 
                color = "blue", s = 10, label = 'Test data') 
    ## plotting line for zero residual error 
    plt.hlines(y = 0, xmin = -5, xmax = 5, linewidth = 2) 
    ## plotting legend 
    plt.legend(loc = 'upper right') 
    ## plot title 
    plt.title("Residual errors: SHARPE RATIO") 
    ## function to show plot 
    plt.show()

prediction0 = reg.predict(x_new)
prediction = round(scalery.inverse_transform(prediction0)[0][0], 2)

print('The LR model prediction for ANNUALIZED SHARPE RATIO is: ', prediction)

###### END ######

####################### LINEAR REGRESSION ANALYSIS END ####################################


"""
eps_choice = np.linspace(0.1,5.0,1000)
#sample_choice = [3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
sample_choice = [5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

var1a = []
var2a = []
clust = []
sillh = []
labs = []

k = -1

for var1 in eps_choice:
    for var2 in sample_choice:
        k = k + 1
        var1a.append(k)
        var2a.append(k)
        clust.append(k)
        sillh.append(k)
        labs.append(k)

        var1a[k] = var1
        var2a[k] = var2

# Compute DBSCAN
        try:
            db = DBSCAN(eps=var1, min_samples=var2).fit(X)
            core_samples_mask = np.zeros_like(db.labels_, dtype=bool)
            core_samples_mask[db.core_sample_indices_] = True
            labels = db.labels_
            labs[k] = labels

# Number of clusters in labels, ignoring noise if present.
            clust[k] = len(set(labels)) - (1 if -1 in labels else 0)
            sillh[k] = metrics.silhouette_score(X, labels)

        except:           
            clust[k] = -1
            sillh[k] = -1

clust_ind = [i for i,v in enumerate(clust) if v > 2]

print('The maximum number of clusters found is: ',np.max(clust),' with Sillhouette Coefficient =',sillh[np.argmax(clust)])

for i in range(0,len(clust_ind)):
    indexx = clust_ind[i]
    print(var1a[indexx],var2a[indexx],clust[indexx],labs[indexx],sillh[indexx])

    try:
        sample_silhouette_values = metrics.silhouette_samples(X, labs[indexx])
    except:
        sample_silhouette_values = -1

    y_lower = 10
    for i in range(clust[indexx]):
            # Aggregate the silhouette scores for samples belonging to
            # cluster i, and sort them
            ith_cluster_silhouette_values = \
                sample_silhouette_values[labels == i]

            ith_cluster_silhouette_values.sort()

            size_cluster_i = ith_cluster_silhouette_values.shape[0]
            y_upper = y_lower + size_cluster_i

            color = cm.nipy_spectral(float(i) / clust[indexx])
            plt.fill_betweenx(np.arange(y_lower, y_upper),
                              0, ith_cluster_silhouette_values,
                              facecolor=color, edgecolor=color, alpha=0.7)

            # Label the silhouette plots with their cluster numbers at the middle
            plt.text(-0.05, y_lower + 0.5 * size_cluster_i, str(i))

            # Compute the new y_lower for next plot
            y_lower = y_upper + 10  # 10 for the 0 samples

    plt.title("The silhouette plot for the various clusters.")
    plt.xlabel("The silhouette coefficient values")
    plt.ylabel("Cluster label")

        # The vertical line for average silhouette score of all the values
    plt.axvline(x=metrics.silhouette_score(X, labs[indexx]), color="red", linestyle="--")

    plt.yticks([])  # Clear the yaxis labels / ticks
    plt.xticks([-0.1, 0, 0.2, 0.4, 0.6, 0.8, 1])

    plt.show()


"""

"""

for N_CL in range(2,11):

    # Number of clusters
    #N_CL = 4
    kmeans = KMeans(n_clusters=N_CL)
    # Fitting the input data
    kmeans = kmeans.fit(X)
    # Getting the cluster labels
    labels2 = kmeans.predict(X)
    # Centroid values
    centroids = kmeans.cluster_centers_

    print('---------------------------------------------------------------------------------------')
    print('K-MEANS CLUSTERING METHOD, k =',N_CL)
    print('---------------------------------------------------------------------------------------')

    print('Clustering Determined the Following Centroid Coordinates (x,y,z): ')
    print(centroids)
    print('Normalized error for k =',N_CL,'is: ',round(np.sqrt(kmeans.inertia_)/len(labels2),2))
    try:
        print('Sillhouette score is =',metrics.silhouette_score(X, labels2))
    except:
        print('Sillhouette score is =',-1.0)
        
    try:
        sample_silhouette_values = metrics.silhouette_samples(X, labels2)
    except:
         sample_silhouette_values = -1

    y_lower = 10
    for i in range(N_CL):
            # Aggregate the silhouette scores for samples belonging to
            # cluster i, and sort them
            ith_cluster_silhouette_values = \
                sample_silhouette_values[labels2 == i]

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

    plt.title("The silhouette plot for the various clusters.")
    plt.xlabel("The silhouette coefficient values")
    plt.ylabel("Cluster label")

        # The vertical line for average silhouette score of all the values
    plt.axvline(x=metrics.silhouette_score(X, labels2), color="red", linestyle="--")

    plt.yticks([])  # Clear the yaxis labels / ticks
    plt.xticks([-0.1, 0, 0.2, 0.4, 0.6, 0.8, 1])

    plt.show()

"""
