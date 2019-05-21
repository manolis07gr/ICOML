import csv
from csv import *
from numpy import *
import numpy as np
import sys
from matplotlib import pyplot as plt
from region_category import func_region
from industry_category import func_industry
from scrap_icos_main_func import ico_data_collector
from top10_returns import func_top10
from bitcoin_returns import func_btc

#OPTIONS: region,industry,team,raised,hardcap,price,telegram,N_google_news,N_twitter,hype,risk,bazaar-rate
#raised goes for completed ICOs not for in-progress or planned ICOs

ico_inp = 'tune token'
ico_inp_token = 'tune'

def ico_rank(ico_inp,ico_inp_token):


    #Here we allow the user to import the features of the ICO that is under investigation
    features_vec = ['region','industry','team','hardcap','price','telegram','N_google_news','N_twitter']
    #user_input = ['united states', 'fintech', '4', '10000000', '0.20', '3210', '1', '5632']

    bitcoin = func_btc()
    top10s = func_top10()
    ico_data = ico_data_collector([ico_inp,ico_inp_token,ico_inp],bitcoin,top10s)[1]
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

    for i in range(0,len(user_input)):
        if user_input[i] != 'N/A':
            user_input[i] = str(user_input[i])
        if user_input[i] == 'N/A':
            user_input[i] = input("Enter ICO feature: "+features_vec[i]+"\n")

#user_input = []
#for i in range(0,len(features_vec)):
#    user_input.append(i)
#    user_input[i] = input("Enter ICO "+features_vec[i]+"\n")

    kk = -1
    ranks = []
    for feature in features_vec:
        kk = kk + 1
        ranks.append(kk)


        success_threshold = 0.7

        with open("ico_data_reduced.csv") as f:
            reader = csv.reader(f)
            data = [r for r in reader]

        data = np.asarray(data)

        indices, = np.where(data[:,10] != 'N/A')
        indices = np.delete(indices,0)

        success = [eval(data[i][10]) for i in indices]

        try:
            ind_feature = np.where(data[0,:]==feature)[0][0]
        except:
            print('ERROR: This feature does not exist in this dataset')
            sys.exit()

        if feature in ['hype','risk']:
            for i in range(0,len(data)):
                if data[i,ind_feature] == ' N/A':
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
        if feature in ['team','N_google_news']:
            for i in range(0,len(variable0)):
                variable0[i] = abs(eval(variable0[i]))

        if feature == 'hardcap':
            for i in range(0,len(variable0)):
                variable0[i] = abs(eval(variable0[i]))
                variable0[i] = np.log10(variable0[i])


        if feature in ['price','telegram','N_twitter']:
            for i in range(0,len(variable0)):
                if variable0[i] == '0':
                    variable0[i] = str(1)
                variable0[i] = np.log10(eval(variable0[i]))
                #print(variable0[i])

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
            print('-------BASIC FEATURE STATISTICS: FULL SAMPLE-------')
            print('For feature:',feature.upper(),'the sample size is: ',len(variable0))
            print('For feature:',feature.upper(),'the max value is: ',np.max(variable0))
            print('For feature:',feature.upper(),'the min value is: ',np.min(variable0))
            print('For feature:',feature.upper(),'the mean value is: ',round(np.mean(variable0),3))
            print('For feature:',feature.upper(),'the median value is: ',round(np.median(variable0),3))
            print('For feature:',feature.upper(),'the standard deviation is: ',round(np.std(variable0),3))
            print('---------------------------------------------------')
            print('---------------------------------------------------')
            print('-------BASIC FEATURE STATISTICS: SUCCESSFUL SAMPLE-------')
            print('For feature:',feature.upper(),'the sample size is: ',len(variable0b))
            print('For feature:',feature.upper(),'the max value is: ',np.max(variable0b))
            print('For feature:',feature.upper(),'the min value is: ',np.min(variable0b))
            print('For feature:',feature.upper(),'the mean value is: ',round(np.mean(variable0b),3))
            print('For feature:',feature.upper(),'the median value is: ',round(np.median(variable0b),3))
            print('For feature:',feature.upper(),'the standard deviation is: ',round(np.std(variable0b),3))
            print('---------------------------------------------------------')
            print('---------------------------------------------------------')
        except:
            print('Statistics Are Not Done for Categorical Features')
            print('For feature:',feature.upper(),'the sample size is: ',len(variable0))
            print('For feature:',feature.upper(),'the sample size is: ',len(variable0b))


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

        if feature not in ['region','industry']:

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

    print('The average BloxVerse ranking for this ICO is: ',round(ico_rating,2))
    print('In the 0-1 scale this is equivalent to: ',round(ico_rating0,2))

    return 'Normalized BloxVerse Rating: ',ico_rating0

print(ico_rank(ico_inp,ico_inp_token))

#Perform principal components analysis

#Perform k-means-based clustering grading
