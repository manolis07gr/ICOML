import csv
from csv import *
from numpy import *
import numpy as np
import sys
from matplotlib import pyplot as plt
import matplotlib.cm as cm
from region_category import func_region
from industry_category import func_industry
from top10_returns import func_top10
from bitcoin_returns import func_btc
from icomarks_rate import func_icomarks_rate
from icobench_rate import func_icobench_rate
import pandas as pd
import datetime as dt
from datetime import datetime
from bloxverse_rating import ico_rank_full, ico_rank_quarter, ico_rank_semiannual
import time
import scipy.stats as stats

#data = pd.read_csv('outdata/ico_data_reduced.csv')
data = pd.read_csv('outdata/ico_data_rate_cluster.csv')
f1 = data['coin'].values
f2 = data['start'].values
f3 = data['end'].values
f4 = data['industry'].values
f5 = data['team'].values
f6 = data['raised'].values
f7 = data['hardcap'].values
f8 = data['success'].values
f9 = data['price'].values
f10 = data['telegram'].values
f11 = data['N_twitter'].values
f12 = data['N_daily_views'].values
f13 = data['N_daily_time'].values
f14 = data['hype'].values
f15 = data['risk'].values
f16 = data['bazaar-rate'].values
f17 = data['ret_ico_to_day_one'].values
f18 = data['vol_day1'].values
f19 = data['sharpe_yr2'].values
f20 = data['region'].values
f21 = data['N_google_news'].values

X = np.array(list(zip(f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f11,f12,f13,f14,f15,f16,f17,f18,f19,f20,f21)))

columnTitles = "coin,bloxverse_yr,bloxverse_sa,bloxverse_qr,icorating_hype,icorating_risk,icobazaar,icomarks,icobench,success,return_day1,volume_day1,sharpe_annual\n"

with open('outdata/ico_data_ratings.csv', 'w') as csvfile:
    csvfile.write(columnTitles)
    writer=csv.writer(csvfile, delimiter=',')

    k = -1
    [name,bloxverse_yr,bloxverse_sa,bloxverse_qr,icorating_hype,icorating_risk,icobazaar,icomarks,icobench,success,return_day1,volume_day1,sharpe_annual] = [[],[],[],[],[],[],[],[],[],[],[],[],[]]

    for i in range(0,len(X)):
        ico_end_date = X[i][2].replace(" ","")
        ico_end_date_o = datetime.strptime(ico_end_date, '%d%b%Y')
        ico_year = ico_end_date_o.year
        #time.sleep(1)

        if ico_year == 2018 and X[i][7] != 'N/A':
            k = k + 1

            name.append(k)
            bloxverse_yr.append(k)
            bloxverse_sa.append(k)
            bloxverse_qr.append(k)
            icorating_hype.append(k)
            icorating_risk.append(k)
            icobazaar.append(k)
            icomarks.append(k)
            icobench.append(k)
            success.append(k)
            return_day1.append(k)
            volume_day1.append(k)
            sharpe_annual.append(k)

            name[k] = X[i][0]

            if X[i][13] == 'VeryHigh':
                icorating_hype[k] = 0.9
            if X[i][13] == 'High':
                icorating_hype[k] = 0.7
            if X[i][13] == 'Medium':
                icorating_hype[k] = 0.5
            if X[i][13] == 'Low':
                icorating_hype[k] = 0.3
            if X[i][13] == 'Very Low':
                icorating_hype[k] = 0.1
            if X[i][13] == 'nan':
                icorating_hype[k] = 'N/A'


            if X[i][14] == 'VeryHigh':
                icorating_risk[k] = 0.9
            if X[i][14] == 'High':
                icorating_risk[k] = 0.7
            if X[i][14] == 'Medium':
                icorating_risk[k] = 0.5
            if X[i][14] == 'Low':
                icorating_risk[k] = 0.3
            if X[i][14] == 'Very Low':
                icorating_risk[k] = 0.1
            if X[i][14] == 'nan':
                icorating_risk[k] = 'N/A'

            icomarks[k] = func_icomarks_rate(X[i][0])
            icobench[k] = func_icobench_rate(X[i][0])


            if math.isnan(eval(X[i][15])):
                icobazaar[k] = 'N/A'
            if not math.isnan(eval(X[i][15])):
                icobazaar[k] = round(eval(X[i][15]),2)

            success[k] = round(eval(X[i][7]),2)

            try:
                return_day1[k] = round(eval(X[i][16]),3)
                volume_day1[k] = round(eval(X[i][17]),0)
                sharpe_annual[k] = round(eval(X[i][18]),3)
            except:
                return_day1[k] = 'N/A'
                volume_day1[k] = 'N/A'
                sharpe_annual[k] = 'N/A'            

            bloxverse_yr[k] = ico_rank_full([X[i][19],X[i][3],X[i][4],X[i][6],X[i][8],X[i][9],X[i][20],X[i][10],X[i][11],X[i][12]])
            bloxverse_sa[k] = ico_rank_semiannual([X[i][19],X[i][3],X[i][4],X[i][6],X[i][8],X[i][9],X[i][20],X[i][10],X[i][11],X[i][12]],X[i][2])
            bloxverse_qr[k] = ico_rank_quarter([X[i][19],X[i][3],X[i][4],X[i][6],X[i][8],X[i][9],X[i][20],X[i][10],X[i][11],X[i][12]],X[i][2])

            writer.writerow([name[k],bloxverse_yr[k],bloxverse_sa[k],bloxverse_qr[k],icorating_hype[k],icorating_risk[k],icobazaar[k],icomarks[k],icobench[k],success[k],return_day1[k],volume_day1[k],sharpe_annual[k]])

            #print(i,name[k],bloxverse_yr[k],bloxverse_sa[k],bloxverse_qr[k],icorating_hype[k],icorating_risk[k],icobazaar[k],icomarks[k],icobench[k],success[k],return_day1[k],volume_day1[k],sharpe_annual[k])


###1. BLOXVERSE VERSUS ICORATING HYPE SCORE
print('----------------------------------------------------------------')
print('BLOXVERSE VS. ICORATING HYPE')
print('----------------------------------------------------------------')

#First find indices for which ICORATING HYPE entries are not equal to N/A
icorating_hype = np.asarray(icorating_hype)
indices2 = np.argwhere(icorating_hype != 'N/A')

indices = []
bloxverse_yr_c1 = []
bloxverse_sa_c1 = []
bloxverse_qr_c1 = []
icorating_hype_c1 = []
success_c1 = []

for i in range(0,len(indices2)):
    indices.append(i)
    icorating_hype_c1.append(i)
    bloxverse_yr_c1.append(i)
    bloxverse_sa_c1.append(i)
    bloxverse_qr_c1.append(i)

    success_c1.append(i)
    
    indices[i] = indices2[i][0]
    icorating_hype_c1[i] = round(eval(icorating_hype[indices[i]]),2)
    bloxverse_yr_c1[i] = bloxverse_yr[indices[i]]
    bloxverse_sa_c1[i] = bloxverse_sa[indices[i]]
    bloxverse_qr_c1[i] = bloxverse_qr[indices[i]]

    success_c1[i] = success[indices[i]]

#Calculate Kendall's tau for each correlation with success.
#Method with better correlation wins

tau_bloxverse_yr, p_value_bloxverse_yr = stats.kendalltau(bloxverse_yr_c1, success_c1)
tau_bloxverse_sa, p_value_bloxverse_sa = stats.kendalltau(bloxverse_sa_c1, success_c1)
tau_bloxverse_qr, p_value_bloxverse_qr = stats.kendalltau(bloxverse_qr_c1, success_c1)
tau_icorating_hype, p_value_icorating_hype = stats.kendalltau(icorating_hype_c1, success_c1)
print('Bloxverse/Full Score Kendall Tau: ',round(tau_bloxverse_yr,3))
print('Bloxverse/Semiannual Score Kendall Tau: ',round(tau_bloxverse_sa,3))
print('Bloxverse/Quarterly Score Kendall Tau: ',round(tau_bloxverse_qr,3))
print('ICO Rating Hype Score Kendall Tau: ',round(tau_icorating_hype,3))

#Calculate Linear Fit for all Methods and Compute Fit Error
fit_bloxverse_yr = np.polyfit(bloxverse_yr_c1, success_c1, 1, full = True)
fit_bloxverse_sa = np.polyfit(bloxverse_sa_c1, success_c1, 1, full = True)
fit_bloxverse_qr = np.polyfit(bloxverse_qr_c1, success_c1, 1, full = True)
fit_icorating_hype = np.polyfit(icorating_hype_c1, success_c1, 1, full = True)
bloxverse_yr_error = np.sum((np.polyval(np.polyfit(bloxverse_yr_c1, success_c1, 1), bloxverse_yr_c1) - success_c1)**2)
bloxverse_sa_error = np.sum((np.polyval(np.polyfit(bloxverse_sa_c1, success_c1, 1), bloxverse_sa_c1) - success_c1)**2)
bloxverse_qr_error = np.sum((np.polyval(np.polyfit(bloxverse_qr_c1, success_c1, 1), bloxverse_qr_c1) - success_c1)**2)
icorating_hype_error = np.sum((np.polyval(np.polyfit(icorating_hype_c1, success_c1, 1), icorating_hype_c1) - success_c1)**2)
print('Bloxverse/Full Linear Fit Error: ',round(bloxverse_yr_error,3))
print('Bloxverse/Semiannual Linear Fit Error: ',round(bloxverse_sa_error,3))
print('Bloxverse/Quarterly Linear Fit Error: ',round(bloxverse_qr_error,3))
print('ICO Rating Hype Linear Fit Error: ',round(icorating_hype_error,3))

#Define linear fit functions
x_grid = np.linspace(0,1,100)
f1 = lambda x_grid: fit_bloxverse_yr[0][0]*x_grid+fit_bloxverse_yr[0][1]
f2 = lambda x_grid: fit_bloxverse_sa[0][0]*x_grid+fit_bloxverse_sa[0][1]
f3 = lambda x_grid: fit_bloxverse_qr[0][0]*x_grid+fit_bloxverse_qr[0][1]
f4 = lambda x_grid: fit_icorating_hype[0][0]*x_grid+fit_icorating_hype[0][1]

#Plot fit over data with matplotlib
plt.figure(figsize=(12,8))
plt.title('Bloxverse vs ICO Rating (hype)',fontweight="bold",fontsize=15)
plt.xlabel('Rating Score',fontweight="bold",fontsize=12)
plt.ylabel('Success Score',fontweight="bold",fontsize=12)
plt.plot(success_c1, success_c1,'gray',markersize=10,marker='o',linestyle='none',linewidth=2.0,label='ICO Success')
plt.plot(x_grid,f1(x_grid),'k',linestyle='-',linewidth=6.0,label='Bloxverse/Full')
plt.plot(x_grid,f2(x_grid),'r',linestyle='-',linewidth=6.0,label='Bloxverse/Semiannual')
plt.plot(x_grid,f3(x_grid),'b',linestyle='-',linewidth=6.0,label='Bloxverse/Quarterly')
plt.plot(x_grid,f4(x_grid),'g',linestyle='--',linewidth=6.0,label='ICO Rating Hype')
plt.xlim([-0.01,1.01])
plt.ylim([-0.01,1.01])
plt.xticks(size = '12', weight = 'bold')
plt.yticks(size = '12', weight = 'bold')
legend = plt.legend(loc='lower right',shadow='True')
plt.minorticks_on()
plt.show()

###2. BLOXVERSE VERSUS ICORATING RISK SCORE
print('----------------------------------------------------------------')
print('BLOXVERSE VS. ICORATING RISK')
print('----------------------------------------------------------------')

#First find indices for which ICORATING RISK entries are not equal to N/A
icorating_risk = np.asarray(icorating_risk)
indices2 = np.argwhere(icorating_risk != 'N/A')

indices = []
bloxverse_yr_c2 = []
bloxverse_sa_c2 = []
bloxverse_qr_c2 = []
icorating_risk_c2 = []
success_c2 = []

for i in range(0,len(indices2)):
    indices.append(i)
    icorating_risk_c2.append(i)
    bloxverse_yr_c2.append(i)
    bloxverse_sa_c2.append(i)
    bloxverse_qr_c2.append(i)

    success_c2.append(i)
    
    indices[i] = indices2[i][0]
    icorating_risk_c2[i] = round(eval(icorating_risk[indices[i]]),2)
    bloxverse_yr_c2[i] = bloxverse_yr[indices[i]]
    bloxverse_sa_c2[i] = bloxverse_sa[indices[i]]
    bloxverse_qr_c2[i] = bloxverse_qr[indices[i]]

    success_c2[i] = success[indices[i]]

#Calculate Kendall's tau for each correlation with success.
#Method with better correlation wins

tau_bloxverse_yr, p_value_bloxverse_yr = stats.kendalltau(bloxverse_yr_c2, success_c2)
tau_bloxverse_sa, p_value_bloxverse_sa = stats.kendalltau(bloxverse_sa_c2, success_c2)
tau_bloxverse_qr, p_value_bloxverse_qr = stats.kendalltau(bloxverse_qr_c2, success_c2)
tau_icorating_risk, p_value_icorating_risk = stats.kendalltau(icorating_risk_c2, success_c2)
print('Bloxverse/Full Score Kendall Tau: ',round(tau_bloxverse_yr,3))
print('Bloxverse/Semiannual Score Kendall Tau: ',round(tau_bloxverse_sa,3))
print('Bloxverse/Quarterly Score Kendall Tau: ',round(tau_bloxverse_qr,3))
print('ICO Rating Risk Score Kendall Tau: ',round(tau_icorating_risk,3))

#Calculate Linear Fit for all Methods and Compute Fit Error
fit_bloxverse_yr = np.polyfit(bloxverse_yr_c2, success_c2, 1, full = True)
fit_bloxverse_sa = np.polyfit(bloxverse_sa_c2, success_c2, 1, full = True)
fit_bloxverse_qr = np.polyfit(bloxverse_qr_c2, success_c2, 1, full = True)
fit_icorating_risk = np.polyfit(icorating_risk_c2, success_c2, 1, full = True)
bloxverse_yr_error = np.sum((np.polyval(np.polyfit(bloxverse_yr_c2, success_c2, 1), bloxverse_yr_c2) - success_c2)**2)
bloxverse_sa_error = np.sum((np.polyval(np.polyfit(bloxverse_sa_c2, success_c2, 1), bloxverse_sa_c2) - success_c2)**2)
bloxverse_qr_error = np.sum((np.polyval(np.polyfit(bloxverse_qr_c2, success_c2, 1), bloxverse_qr_c2) - success_c2)**2)
icorating_risk_error = np.sum((np.polyval(np.polyfit(icorating_risk_c2, success_c2, 1), icorating_risk_c2) - success_c2)**2)
print('Bloxverse/Full Linear Fit Error: ',round(bloxverse_yr_error,3))
print('Bloxverse/Semiannual Linear Fit Error: ',round(bloxverse_sa_error,3))
print('Bloxverse/Quarterly Linear Fit Error: ',round(bloxverse_qr_error,3))
print('ICO Rating Risk Linear Fit Error: ',round(icorating_risk_error,3))

#Define linear fit functions
x_grid = np.linspace(0,1,100)
f1 = lambda x_grid: fit_bloxverse_yr[0][0]*x_grid+fit_bloxverse_yr[0][1]
f2 = lambda x_grid: fit_bloxverse_sa[0][0]*x_grid+fit_bloxverse_sa[0][1]
f3 = lambda x_grid: fit_bloxverse_qr[0][0]*x_grid+fit_bloxverse_qr[0][1]
f4 = lambda x_grid: fit_icorating_risk[0][0]*x_grid+fit_icorating_risk[0][1]

#Plot fit over data with matplotlib
plt.figure(figsize=(12,8))
plt.title('Bloxverse vs ICO Rating (Risk)',fontweight="bold",fontsize=15)
plt.xlabel('Rating Score',fontweight="bold",fontsize=12)
plt.ylabel('Success Score',fontweight="bold",fontsize=12)
plt.plot(success_c2, success_c2,'gray',markersize=10,marker='o',linestyle='none',linewidth=2.0,label='ICO Success')
plt.plot(x_grid,f1(x_grid),'k',linestyle='-',linewidth=6.0,label='Bloxverse/Full')
plt.plot(x_grid,f2(x_grid),'r',linestyle='-',linewidth=6.0,label='Bloxverse/Semiannual')
plt.plot(x_grid,f3(x_grid),'b',linestyle='-',linewidth=6.0,label='Bloxverse/Quarterly')
plt.plot(x_grid,f4(x_grid),'g',linestyle='--',linewidth=6.0,label='ICO Rating Risk')
plt.xlim([-0.01,1.01])
plt.ylim([-0.01,1.01])
plt.xticks(size = '12', weight = 'bold')
plt.yticks(size = '12', weight = 'bold')
legend = plt.legend(loc='lower right',shadow='True')
plt.minorticks_on()
plt.show()

###3. BLOXVERSE VERSUS ICOBAZAAR RATING
print('----------------------------------------------------------------')
print('BLOXVERSE VS. ICO BAZAAR RATING')
print('----------------------------------------------------------------')

#First find indices for which ICOBAZAAR RATING entries are not equal to N/A
icobazaar = np.asarray(icobazaar)
indices2 = np.argwhere(icobazaar != 'N/A')

indices = []
bloxverse_yr_c3 = []
bloxverse_sa_c3 = []
bloxverse_qr_c3 = []
icobazaar_c3 = []
success_c3 = []

for i in range(0,len(indices2)):
    indices.append(i)
    icobazaar_c3.append(i)
    bloxverse_yr_c3.append(i)
    bloxverse_sa_c3.append(i)
    bloxverse_qr_c3.append(i)

    success_c3.append(i)
    
    indices[i] = indices2[i][0]
    icobazaar_c3[i] = round(eval(icobazaar[indices[i]]),2)
    bloxverse_yr_c3[i] = bloxverse_yr[indices[i]]
    bloxverse_sa_c3[i] = bloxverse_sa[indices[i]]
    bloxverse_qr_c3[i] = bloxverse_qr[indices[i]]

    success_c3[i] = success[indices[i]]

#Calculate Kendall's tau for each correlation with success.
#Method with better correlation wins

tau_bloxverse_yr, p_value_bloxverse_yr = stats.kendalltau(bloxverse_yr_c3, success_c3)
tau_bloxverse_sa, p_value_bloxverse_sa = stats.kendalltau(bloxverse_sa_c3, success_c3)
tau_bloxverse_qr, p_value_bloxverse_qr = stats.kendalltau(bloxverse_qr_c3, success_c3)
tau_icobazaar, p_value_icobazaar = stats.kendalltau(icobazaar_c3, success_c3)
print('Bloxverse/Full Score Kendall Tau: ',round(tau_bloxverse_yr,3))
print('Bloxverse/Semiannual Score Kendall Tau: ',round(tau_bloxverse_sa,3))
print('Bloxverse/Quarterly Score Kendall Tau: ',round(tau_bloxverse_qr,3))
print('ICO Bazaar Score Kendall Tau: ',round(tau_icobazaar,3))

#Calculate Linear Fit for all Methods and Compute Fit Error
fit_bloxverse_yr = np.polyfit(bloxverse_yr_c3, success_c3, 1, full = True)
fit_bloxverse_sa = np.polyfit(bloxverse_sa_c3, success_c3, 1, full = True)
fit_bloxverse_qr = np.polyfit(bloxverse_qr_c3, success_c3, 1, full = True)
fit_icobazaar = np.polyfit(icobazaar_c3, success_c3, 1, full = True)
bloxverse_yr_error = np.sum((np.polyval(np.polyfit(bloxverse_yr_c3, success_c3, 1), bloxverse_yr_c3) - success_c3)**2)
bloxverse_sa_error = np.sum((np.polyval(np.polyfit(bloxverse_sa_c3, success_c3, 1), bloxverse_sa_c3) - success_c3)**2)
bloxverse_qr_error = np.sum((np.polyval(np.polyfit(bloxverse_qr_c3, success_c3, 1), bloxverse_qr_c3) - success_c3)**2)
icobazaar_error = np.sum((np.polyval(np.polyfit(icobazaar_c3, success_c3, 1), icobazaar_c3) - success_c3)**2)
print('Bloxverse/Full Linear Fit Error: ',round(bloxverse_yr_error,3))
print('Bloxverse/Semiannual Linear Fit Error: ',round(bloxverse_sa_error,3))
print('Bloxverse/Quarterly Linear Fit Error: ',round(bloxverse_qr_error,3))
print('ICO Bazaar Linear Fit Error: ',round(icobazaar_error,3))

#Define linear fit functions
x_grid = np.linspace(0,1,100)
f1 = lambda x_grid: fit_bloxverse_yr[0][0]*x_grid+fit_bloxverse_yr[0][1]
f2 = lambda x_grid: fit_bloxverse_sa[0][0]*x_grid+fit_bloxverse_sa[0][1]
f3 = lambda x_grid: fit_bloxverse_qr[0][0]*x_grid+fit_bloxverse_qr[0][1]
f4 = lambda x_grid: fit_icobazaar[0][0]*x_grid+fit_icobazaar[0][1]

#Plot fit over data with matplotlib
plt.figure(figsize=(12,8))
plt.title('Bloxverse vs ICO Bazaar',fontweight="bold",fontsize=15)
plt.xlabel('Rating Score',fontweight="bold",fontsize=12)
plt.ylabel('Success Score',fontweight="bold",fontsize=12)
plt.plot(success_c3, success_c3,'gray',markersize=10,marker='o',linestyle='none',linewidth=2.0,label='ICO Success')
plt.plot(x_grid,f1(x_grid),'k',linestyle='-',linewidth=6.0,label='Bloxverse/Full')
plt.plot(x_grid,f2(x_grid),'r',linestyle='-',linewidth=6.0,label='Bloxverse/Semiannual')
plt.plot(x_grid,f3(x_grid),'b',linestyle='-',linewidth=6.0,label='Bloxverse/Quarterly')
plt.plot(x_grid,f4(x_grid),'g',linestyle='--',linewidth=6.0,label='ICO Bazaar Rating')
plt.xlim([-0.01,1.01])
plt.ylim([-0.01,1.01])
plt.xticks(size = '12', weight = 'bold')
plt.yticks(size = '12', weight = 'bold')
legend = plt.legend(loc='lower right',shadow='True')
plt.minorticks_on()
plt.show()

###4. BLOXVERSE VERSUS ICO MARKS RATING
print('----------------------------------------------------------------')
print('BLOXVERSE VS. ICO MARKS RATING')
print('----------------------------------------------------------------')

#First find indices for which ICO MARKS RATING entries are not equal to N/A
icomarks = np.asarray(icomarks)
indices2 = np.argwhere(icomarks != 'N/A')

indices = []
bloxverse_yr_c4 = []
bloxverse_sa_c4 = []
bloxverse_qr_c4 = []
icomarks_c4 = []
success_c4 = []

for i in range(0,len(indices2)):
    indices.append(i)
    icomarks_c4.append(i)
    bloxverse_yr_c4.append(i)
    bloxverse_sa_c4.append(i)
    bloxverse_qr_c4.append(i)

    success_c4.append(i)
    
    indices[i] = indices2[i][0]
    icomarks_c4[i] = round(eval(icomarks[indices[i]]),2)
    bloxverse_yr_c4[i] = bloxverse_yr[indices[i]]
    bloxverse_sa_c4[i] = bloxverse_sa[indices[i]]
    bloxverse_qr_c4[i] = bloxverse_qr[indices[i]]

    success_c4[i] = success[indices[i]]

#Calculate Kendall's tau for each correlation with success.
#Method with better correlation wins

tau_bloxverse_yr, p_value_bloxverse_yr = stats.kendalltau(bloxverse_yr_c4, success_c4)
tau_bloxverse_sa, p_value_bloxverse_sa = stats.kendalltau(bloxverse_sa_c4, success_c4)
tau_bloxverse_qr, p_value_bloxverse_qr = stats.kendalltau(bloxverse_qr_c4, success_c4)
tau_icomarks, p_value_icomarks = stats.kendalltau(icomarks_c4, success_c4)
print('Bloxverse/Full Score Kendall Tau: ',round(tau_bloxverse_yr,3))
print('Bloxverse/Semiannual Score Kendall Tau: ',round(tau_bloxverse_sa,3))
print('Bloxverse/Quarterly Score Kendall Tau: ',round(tau_bloxverse_qr,3))
print('ICO Marks Score Kendall Tau: ',round(tau_icomarks,3))

#Calculate Linear Fit for all Methods and Compute Fit Error
fit_bloxverse_yr = np.polyfit(bloxverse_yr_c4, success_c4, 1, full = True)
fit_bloxverse_sa = np.polyfit(bloxverse_sa_c4, success_c4, 1, full = True)
fit_bloxverse_qr = np.polyfit(bloxverse_qr_c4, success_c4, 1, full = True)
fit_icomarks = np.polyfit(icomarks_c4, success_c4, 1, full = True)
bloxverse_yr_error = np.sum((np.polyval(np.polyfit(bloxverse_yr_c4, success_c4, 1), bloxverse_yr_c4) - success_c4)**2)
bloxverse_sa_error = np.sum((np.polyval(np.polyfit(bloxverse_sa_c4, success_c4, 1), bloxverse_sa_c4) - success_c4)**2)
bloxverse_qr_error = np.sum((np.polyval(np.polyfit(bloxverse_qr_c4, success_c4, 1), bloxverse_qr_c4) - success_c4)**2)
icomarks_error = np.sum((np.polyval(np.polyfit(icomarks_c4, success_c4, 1), icomarks_c4) - success_c4)**2)
print('Bloxverse/Full Linear Fit Error: ',round(bloxverse_yr_error,3))
print('Bloxverse/Semiannual Linear Fit Error: ',round(bloxverse_sa_error,3))
print('Bloxverse/Quarterly Linear Fit Error: ',round(bloxverse_qr_error,3))
print('ICO Marks Linear Fit Error: ',round(icomarks_error,3))

#Define linear fit functions
x_grid = np.linspace(0,1,100)
f1 = lambda x_grid: fit_bloxverse_yr[0][0]*x_grid+fit_bloxverse_yr[0][1]
f2 = lambda x_grid: fit_bloxverse_sa[0][0]*x_grid+fit_bloxverse_sa[0][1]
f3 = lambda x_grid: fit_bloxverse_qr[0][0]*x_grid+fit_bloxverse_qr[0][1]
f4 = lambda x_grid: fit_icomarks[0][0]*x_grid+fit_icomarks[0][1]

#Plot fit over data with matplotlib
plt.figure(figsize=(12,8))
plt.title('Bloxverse vs ICO Marks',fontweight="bold",fontsize=15)
plt.xlabel('Rating Score',fontweight="bold",fontsize=12)
plt.ylabel('Success Score',fontweight="bold",fontsize=12)
plt.plot(success_c4, success_c4,'gray',markersize=10,marker='o',linestyle='none',linewidth=2.0,label='ICO Success')
plt.plot(x_grid,f1(x_grid),'k',linestyle='-',linewidth=6.0,label='Bloxverse/Full')
plt.plot(x_grid,f2(x_grid),'r',linestyle='-',linewidth=6.0,label='Bloxverse/Semiannual')
plt.plot(x_grid,f3(x_grid),'b',linestyle='-',linewidth=6.0,label='Bloxverse/Quarterly')
plt.plot(x_grid,f4(x_grid),'g',linestyle='--',linewidth=6.0,label='ICO Marks Rating')
plt.xlim([-0.01,1.01])
plt.ylim([-0.01,1.01])
plt.xticks(size = '12', weight = 'bold')
plt.yticks(size = '12', weight = 'bold')
legend = plt.legend(loc='lower right',shadow='True')
plt.minorticks_on()
plt.show()

###5. BLOXVERSE VERSUS ICO BENCH RATING
print('----------------------------------------------------------------')
print('BLOXVERSE VS. ICO BENCH RATING')
print('----------------------------------------------------------------')

#First find indices for which ICO BENCH RATING entries are not equal to N/A
icobench = np.asarray(icobench)
indices2 = np.argwhere(icobench != 'N/A')

indices = []
bloxverse_yr_c5 = []
bloxverse_sa_c5 = []
bloxverse_qr_c5 = []
icobench_c5 = []
success_c5 = []

for i in range(0,len(indices2)):
    indices.append(i)
    icobench_c5.append(i)
    bloxverse_yr_c5.append(i)
    bloxverse_sa_c5.append(i)
    bloxverse_qr_c5.append(i)

    success_c5.append(i)
    
    indices[i] = indices2[i][0]
    icobench_c5[i] = round(eval(icobench[indices[i]]),2)
    bloxverse_yr_c5[i] = bloxverse_yr[indices[i]]
    bloxverse_sa_c5[i] = bloxverse_sa[indices[i]]
    bloxverse_qr_c5[i] = bloxverse_qr[indices[i]]

    success_c5[i] = success[indices[i]]

#Calculate Kendall's tau for each correlation with success.
#Method with better correlation wins

tau_bloxverse_yr, p_value_bloxverse_yr = stats.kendalltau(bloxverse_yr_c5, success_c5)
tau_bloxverse_sa, p_value_bloxverse_sa = stats.kendalltau(bloxverse_sa_c5, success_c5)
tau_bloxverse_qr, p_value_bloxverse_qr = stats.kendalltau(bloxverse_qr_c5, success_c5)
tau_icobench, p_value_icobench = stats.kendalltau(icobench_c5, success_c5)
print('Bloxverse/Full Score Kendall Tau: ',round(tau_bloxverse_yr,3))
print('Bloxverse/Semiannual Score Kendall Tau: ',round(tau_bloxverse_sa,3))
print('Bloxverse/Quarterly Score Kendall Tau: ',round(tau_bloxverse_qr,3))
print('ICO Bench Score Kendall Tau: ',round(tau_icobench,3))

#Calculate Linear Fit for all Methods and Compute Fit Error
fit_bloxverse_yr = np.polyfit(bloxverse_yr_c5, success_c5, 1, full = True)
fit_bloxverse_sa = np.polyfit(bloxverse_sa_c5, success_c5, 1, full = True)
fit_bloxverse_qr = np.polyfit(bloxverse_qr_c5, success_c5, 1, full = True)
fit_icobench = np.polyfit(icobench_c5, success_c5, 1, full = True)
bloxverse_yr_error = np.sum((np.polyval(np.polyfit(bloxverse_yr_c5, success_c5, 1), bloxverse_yr_c5) - success_c5)**2)
bloxverse_sa_error = np.sum((np.polyval(np.polyfit(bloxverse_sa_c5, success_c5, 1), bloxverse_sa_c5) - success_c5)**2)
bloxverse_qr_error = np.sum((np.polyval(np.polyfit(bloxverse_qr_c5, success_c5, 1), bloxverse_qr_c5) - success_c5)**2)
icobench_error = np.sum((np.polyval(np.polyfit(icobench_c5, success_c5, 1), icobench_c5) - success_c5)**2)
print('Bloxverse/Full Linear Fit Error: ',round(bloxverse_yr_error,3))
print('Bloxverse/Semiannual Linear Fit Error: ',round(bloxverse_sa_error,3))
print('Bloxverse/Quarterly Linear Fit Error: ',round(bloxverse_qr_error,3))
print('ICO Bench Linear Fit Error: ',round(icobench_error,3))

#Define linear fit functions
x_grid = np.linspace(0,1,100)
f1 = lambda x_grid: fit_bloxverse_yr[0][0]*x_grid+fit_bloxverse_yr[0][1]
f2 = lambda x_grid: fit_bloxverse_sa[0][0]*x_grid+fit_bloxverse_sa[0][1]
f3 = lambda x_grid: fit_bloxverse_qr[0][0]*x_grid+fit_bloxverse_qr[0][1]
f4 = lambda x_grid: fit_icobench[0][0]*x_grid+fit_icobench[0][1]

#Plot fit over data with matplotlib
plt.figure(figsize=(12,8))
plt.title('Bloxverse vs ICO Bench',fontweight="bold",fontsize=15)
plt.xlabel('Rating Score',fontweight="bold",fontsize=12)
plt.ylabel('Success Score',fontweight="bold",fontsize=12)
plt.plot(success_c5, success_c5,'gray',markersize=10,marker='o',linestyle='none',linewidth=2.0,label='ICO Success')
plt.plot(x_grid,f1(x_grid),'k',linestyle='-',linewidth=6.0,label='Bloxverse/Full')
plt.plot(x_grid,f2(x_grid),'r',linestyle='-',linewidth=6.0,label='Bloxverse/Semiannual')
plt.plot(x_grid,f3(x_grid),'b',linestyle='-',linewidth=6.0,label='Bloxverse/Quarterly')
plt.plot(x_grid,f4(x_grid),'g',linestyle='--',linewidth=6.0,label='ICO Bench Rating')
plt.xlim([-0.01,1.01])
plt.ylim([-0.01,1.01])
plt.xticks(size = '12', weight = 'bold')
plt.yticks(size = '12', weight = 'bold')
legend = plt.legend(loc='lower right',shadow='True')
plt.minorticks_on()
plt.show()

### DISTRIBUTION OF TRUE SUCCESS VERSUS RATING PREDICTIONS
print('----------------------------------------------------------------')
print('DISTRIBUTION OF TRUE SUCCESS VERSUS RATING PREDICTIONS')
print('----------------------------------------------------------------')
plt.figure(figsize=(12,8))
plt.title('Bloxverse (Quarterly) vs ICO Rating (Hype)',fontweight="bold",fontsize=15)
z,bins,p = plt.hist(success_c1, bins = 'auto', rwidth=0.9, facecolor = 'k',label='ICO Success')
z2,bin2,p2 = plt.hist(bloxverse_qr_c1, bins = 'auto', rwidth=0.9, facecolor = 'blue',label='Bloxverse (Quarterly) Rating',alpha = 0.7)
z3,bin3,p3 = plt.hist(icorating_hype_c1, bins = 'auto', rwidth=0.9, facecolor = 'green',label='ICO Rating (Hype Score)',alpha = 0.5)
plt.xlabel('Success',fontweight="bold",fontsize=13)
plt.ylabel('Size',fontweight="bold",fontsize=13)
plt.xticks(size = 15)
plt.yticks(size = 15)
legend = plt.legend(loc='upper left',shadow='True')
plt.show()

plt.figure(figsize=(12,8))
plt.title('Bloxverse (Quarterly) vs ICO Rating (Risk)',fontweight="bold",fontsize=15)
z,bins,p = plt.hist(success_c2, bins = 'auto', rwidth=0.9, facecolor = 'k',label='ICO Success')
z2,bin2,p2 = plt.hist(bloxverse_qr_c2, bins = 'auto', rwidth=0.9, facecolor = 'blue',label='Bloxverse (Quarterly) Rating',alpha = 0.7)
z3,bin3,p3 = plt.hist(icorating_risk_c2, bins = 'auto', rwidth=0.9, facecolor = 'green',label='ICO Rating (Risk Score)',alpha = 0.5)
plt.xlabel('Success',fontweight="bold",fontsize=13)
plt.ylabel('Size',fontweight="bold",fontsize=13)
plt.xticks(size = 15)
plt.yticks(size = 15)
legend = plt.legend(loc='upper left',shadow='True')
plt.show()

plt.figure(figsize=(12,8))
plt.title('Bloxverse (Quarterly) vs ICO Bazaar',fontweight="bold",fontsize=15)
z,bins,p = plt.hist(success_c3, bins = 'auto', rwidth=0.9, facecolor = 'k',label='ICO Success')
z2,bin2,p2 = plt.hist(bloxverse_qr_c3, bins = 'auto', rwidth=0.9, facecolor = 'blue',label='Bloxverse (Quarterly) Rating',alpha = 0.7)
z3,bin3,p3 = plt.hist(icobazaar_c3, bins = 'auto', rwidth=0.9, facecolor = 'green',label='ICO Bazaar',alpha = 0.5)
plt.xlabel('Success',fontweight="bold",fontsize=13)
plt.ylabel('Size',fontweight="bold",fontsize=13)
plt.xticks(size = 15)
plt.yticks(size = 15)
legend = plt.legend(loc='upper left',shadow='True')
plt.show()

plt.figure(figsize=(12,8))
plt.title('Bloxverse (Quarterly) vs ICO Marks',fontweight="bold",fontsize=15)
z,bins,p = plt.hist(success_c4, bins = 'auto', rwidth=0.9, facecolor = 'k',label='ICO Success')
z2,bin2,p2 = plt.hist(bloxverse_qr_c4, bins = 'auto', rwidth=0.9, facecolor = 'blue',label='Bloxverse (Quarterly) Rating',alpha = 0.7)
z3,bin3,p3 = plt.hist(icomarks_c4, bins = 'auto', rwidth=0.9, facecolor = 'green',label='ICO Marks',alpha = 0.5)
plt.xlabel('Success',fontweight="bold",fontsize=13)
plt.ylabel('Size',fontweight="bold",fontsize=13)
plt.xticks(size = 15)
plt.yticks(size = 15)
legend = plt.legend(loc='upper left',shadow='True')
plt.show()

plt.figure(figsize=(12,8))
plt.title('Bloxverse (Quarterly) vs ICO Bench',fontweight="bold",fontsize=15)
z,bins,p = plt.hist(success_c5, bins = 'auto', rwidth=0.9, facecolor = 'k',label='ICO Success')
z2,bin2,p2 = plt.hist(bloxverse_qr_c5, bins = 'auto', rwidth=0.9, facecolor = 'blue',label='Bloxverse (Quarterly) Rating',alpha = 0.7)
z3,bin3,p3 = plt.hist(icobench_c5, bins = 'auto', rwidth=0.9, facecolor = 'green',label='ICO Bench',alpha = 0.5)
plt.xlabel('Success',fontweight="bold",fontsize=13)
plt.ylabel('Size',fontweight="bold",fontsize=13)
plt.xticks(size = 15)
plt.yticks(size = 15)
legend = plt.legend(loc='upper left',shadow='True')
plt.show()

####################################################################################################################
####################################################################################################################
####################################################################################################################
####################################################################################################################
####################################################################################################################

###1. BLOXVERSE VERSUS ICORATING HYPE SCORE: DAY 1 RETURNS
print('----------------------------------------------------------------')
print('BLOXVERSE VS. ICORATING HYPE: DAY 1 RETURNS')
print('----------------------------------------------------------------')

#First find indices for which ICORATING HYPE entries are not equal to N/A
icorating_hype = np.asarray(icorating_hype)
indices2 = np.argwhere(icorating_hype != 'N/A')

indices = []
bloxverse_yr_c1 = []
bloxverse_sa_c1 = []
bloxverse_qr_c1 = []
icorating_hype_c1 = []
rday1_c1 = []

for i in range(0,len(indices2)):
    indices.append(i)
    icorating_hype_c1.append(i)
    bloxverse_yr_c1.append(i)
    bloxverse_sa_c1.append(i)
    bloxverse_qr_c1.append(i)

    rday1_c1.append(i)
    
    indices[i] = indices2[i][0]
    icorating_hype_c1[i] = round(eval(icorating_hype[indices[i]]),2)
    bloxverse_yr_c1[i] = bloxverse_yr[indices[i]]
    bloxverse_sa_c1[i] = bloxverse_sa[indices[i]]
    bloxverse_qr_c1[i] = bloxverse_qr[indices[i]]

    rday1_c1[i] = return_day1[indices[i]]

#Calculate Kendall's tau for each correlation with day 1 return.
#Method with better correlation wins

tau_bloxverse_yr, p_value_bloxverse_yr = stats.kendalltau(bloxverse_yr_c1, rday1_c1)
tau_bloxverse_sa, p_value_bloxverse_sa = stats.kendalltau(bloxverse_sa_c1, rday1_c1)
tau_bloxverse_qr, p_value_bloxverse_qr = stats.kendalltau(bloxverse_qr_c1, rday1_c1)
tau_icorating_hype, p_value_icorating_hype = stats.kendalltau(icorating_hype_c1, rday1_c1)
print('Bloxverse/Full Score Kendall Tau: ',round(tau_bloxverse_yr,3))
print('Bloxverse/Semiannual Score Kendall Tau: ',round(tau_bloxverse_sa,3))
print('Bloxverse/Quarterly Score Kendall Tau: ',round(tau_bloxverse_qr,3))
print('ICO Rating Hype Score Kendall Tau: ',round(tau_icorating_hype,3))

#Calculate Linear Fit for all Methods and Compute Fit Error
fit_bloxverse_yr = np.polyfit(bloxverse_yr_c1, rday1_c1, 1, full = True)
fit_bloxverse_sa = np.polyfit(bloxverse_sa_c1, rday1_c1, 1, full = True)
fit_bloxverse_qr = np.polyfit(bloxverse_qr_c1, rday1_c1, 1, full = True)
fit_icorating_hype = np.polyfit(icorating_hype_c1, rday1_c1, 1, full = True)
bloxverse_yr_error = np.sum((np.polyval(np.polyfit(bloxverse_yr_c1, rday1_c1, 1), bloxverse_yr_c1) - rday1_c1)**2)
bloxverse_sa_error = np.sum((np.polyval(np.polyfit(bloxverse_sa_c1, rday1_c1, 1), bloxverse_sa_c1) - rday1_c1)**2)
bloxverse_qr_error = np.sum((np.polyval(np.polyfit(bloxverse_qr_c1, rday1_c1, 1), bloxverse_qr_c1) - rday1_c1)**2)
icorating_hype_error = np.sum((np.polyval(np.polyfit(icorating_hype_c1, rday1_c1, 1), icorating_hype_c1) - rday1_c1)**2)
print('Bloxverse/Full Linear Fit Error: ',round(bloxverse_yr_error,3))
print('Bloxverse/Semiannual Linear Fit Error: ',round(bloxverse_sa_error,3))
print('Bloxverse/Quarterly Linear Fit Error: ',round(bloxverse_qr_error,3))
print('ICO Rating Hype Linear Fit Error: ',round(icorating_hype_error,3))

###2. BLOXVERSE VERSUS ICORATING RISK SCORE: DAY 1 RETURNS
print('----------------------------------------------------------------')
print('BLOXVERSE VS. ICORATING RISK: DAY 1 RETURNS')
print('----------------------------------------------------------------')

#First find indices for which ICORATING HYPE entries are not equal to N/A
icorating_risk = np.asarray(icorating_risk)
indices2 = np.argwhere(icorating_risk != 'N/A')

indices = []
bloxverse_yr_c2 = []
bloxverse_sa_c2 = []
bloxverse_qr_c2 = []
icorating_risk_c2 = []
rday1_c2 = []

for i in range(0,len(indices2)):
    indices.append(i)
    icorating_risk_c2.append(i)
    bloxverse_yr_c2.append(i)
    bloxverse_sa_c2.append(i)
    bloxverse_qr_c2.append(i)

    rday1_c2.append(i)
    
    indices[i] = indices2[i][0]
    icorating_risk_c2[i] = round(eval(icorating_risk[indices[i]]),2)
    bloxverse_yr_c2[i] = bloxverse_yr[indices[i]]
    bloxverse_sa_c2[i] = bloxverse_sa[indices[i]]
    bloxverse_qr_c2[i] = bloxverse_qr[indices[i]]

    rday1_c2[i] = return_day1[indices[i]]

#Calculate Kendall's tau for each correlation with day 1 return.
#Method with better correlation wins

tau_bloxverse_yr, p_value_bloxverse_yr = stats.kendalltau(bloxverse_yr_c2, rday1_c2)
tau_bloxverse_sa, p_value_bloxverse_sa = stats.kendalltau(bloxverse_sa_c2, rday1_c2)
tau_bloxverse_qr, p_value_bloxverse_qr = stats.kendalltau(bloxverse_qr_c2, rday1_c2)
tau_icorating_risk, p_value_icorating_risk = stats.kendalltau(icorating_risk_c2, rday1_c2)
print('Bloxverse/Full Score Kendall Tau: ',round(tau_bloxverse_yr,3))
print('Bloxverse/Semiannual Score Kendall Tau: ',round(tau_bloxverse_sa,3))
print('Bloxverse/Quarterly Score Kendall Tau: ',round(tau_bloxverse_qr,3))
print('ICO Rating Risk Score Kendall Tau: ',round(tau_icorating_risk,3))

#Calculate Linear Fit for all Methods and Compute Fit Error
fit_bloxverse_yr = np.polyfit(bloxverse_yr_c2, rday1_c2, 1, full = True)
fit_bloxverse_sa = np.polyfit(bloxverse_sa_c2, rday1_c2, 1, full = True)
fit_bloxverse_qr = np.polyfit(bloxverse_qr_c2, rday1_c2, 1, full = True)
fit_icorating_risk = np.polyfit(icorating_risk_c2, rday1_c2, 1, full = True)
bloxverse_yr_error = np.sum((np.polyval(np.polyfit(bloxverse_yr_c2, rday1_c2, 1), bloxverse_yr_c2) - rday1_c2)**2)
bloxverse_sa_error = np.sum((np.polyval(np.polyfit(bloxverse_sa_c2, rday1_c2, 1), bloxverse_sa_c2) - rday1_c2)**2)
bloxverse_qr_error = np.sum((np.polyval(np.polyfit(bloxverse_qr_c2, rday1_c2, 1), bloxverse_qr_c2) - rday1_c2)**2)
icorating_risk_error = np.sum((np.polyval(np.polyfit(icorating_risk_c2, rday1_c2, 1), icorating_risk_c2) - rday1_c2)**2)
print('Bloxverse/Full Linear Fit Error: ',round(bloxverse_yr_error,3))
print('Bloxverse/Semiannual Linear Fit Error: ',round(bloxverse_sa_error,3))
print('Bloxverse/Quarterly Linear Fit Error: ',round(bloxverse_qr_error,3))
print('ICO Rating Risk Linear Fit Error: ',round(icorating_risk_error,3))

###3. BLOXVERSE VERSUS ICOBAZAAR SCORE: DAY 1 RETURNS
print('----------------------------------------------------------------')
print('BLOXVERSE VS. ICOBAZAAR: DAY 1 RETURNS')
print('----------------------------------------------------------------')

#First find indices for which ICORATING HYPE entries are not equal to N/A
icobazaar = np.asarray(icobazaar)
indices2 = np.argwhere(icobazaar != 'N/A')

indices = []
bloxverse_yr_c3 = []
bloxverse_sa_c3 = []
bloxverse_qr_c3 = []
icobazaar_c3 = []
rday1_c3 = []

for i in range(0,len(indices2)):
    indices.append(i)
    icobazaar_c3.append(i)
    bloxverse_yr_c3.append(i)
    bloxverse_sa_c3.append(i)
    bloxverse_qr_c3.append(i)

    rday1_c3.append(i)
    
    indices[i] = indices2[i][0]
    icobazaar_c3[i] = round(eval(icobazaar[indices[i]]),2)
    bloxverse_yr_c3[i] = bloxverse_yr[indices[i]]
    bloxverse_sa_c3[i] = bloxverse_sa[indices[i]]
    bloxverse_qr_c3[i] = bloxverse_qr[indices[i]]

    rday1_c3[i] = return_day1[indices[i]]

#Calculate Kendall's tau for each correlation with day 1 return.
#Method with better correlation wins

tau_bloxverse_yr, p_value_bloxverse_yr = stats.kendalltau(bloxverse_yr_c3, rday1_c3)
tau_bloxverse_sa, p_value_bloxverse_sa = stats.kendalltau(bloxverse_sa_c3, rday1_c3)
tau_bloxverse_qr, p_value_bloxverse_qr = stats.kendalltau(bloxverse_qr_c3, rday1_c3)
tau_icobazaar, p_value_icobazaar = stats.kendalltau(icobazaar_c3, rday1_c3)
print('Bloxverse/Full Score Kendall Tau: ',round(tau_bloxverse_yr,3))
print('Bloxverse/Semiannual Score Kendall Tau: ',round(tau_bloxverse_sa,3))
print('Bloxverse/Quarterly Score Kendall Tau: ',round(tau_bloxverse_qr,3))
print('ICO Rating Risk Score Kendall Tau: ',round(tau_icobazaar,3))

#Calculate Linear Fit for all Methods and Compute Fit Error
fit_bloxverse_yr = np.polyfit(bloxverse_yr_c3, rday1_c3, 1, full = True)
fit_bloxverse_sa = np.polyfit(bloxverse_sa_c3, rday1_c3, 1, full = True)
fit_bloxverse_qr = np.polyfit(bloxverse_qr_c3, rday1_c3, 1, full = True)
fit_icobazaar = np.polyfit(icobazaar_c3, rday1_c3, 1, full = True)
bloxverse_yr_error = np.sum((np.polyval(np.polyfit(bloxverse_yr_c3, rday1_c3, 1), bloxverse_yr_c3) - rday1_c3)**2)
bloxverse_sa_error = np.sum((np.polyval(np.polyfit(bloxverse_sa_c3, rday1_c3, 1), bloxverse_sa_c3) - rday1_c3)**2)
bloxverse_qr_error = np.sum((np.polyval(np.polyfit(bloxverse_qr_c3, rday1_c3, 1), bloxverse_qr_c3) - rday1_c3)**2)
icobazaar_error = np.sum((np.polyval(np.polyfit(icobazaar_c3, rday1_c3, 1), icobazaar_c3) - rday1_c3)**2)
print('Bloxverse/Full Linear Fit Error: ',round(bloxverse_yr_error,3))
print('Bloxverse/Semiannual Linear Fit Error: ',round(bloxverse_sa_error,3))
print('Bloxverse/Quarterly Linear Fit Error: ',round(bloxverse_qr_error,3))
print('ICO Rating Risk Linear Fit Error: ',round(icobazaar_error,3))

###4. BLOXVERSE VERSUS ICOMARKS SCORE: DAY 1 RETURNS
print('----------------------------------------------------------------')
print('BLOXVERSE VS. ICOMARKS: DAY 1 RETURNS')
print('----------------------------------------------------------------')

#First find indices for which ICORATING HYPE entries are not equal to N/A
icomarks = np.asarray(icomarks)
indices2 = np.argwhere(icomarks != 'N/A')

indices = []
bloxverse_yr_c4 = []
bloxverse_sa_c4 = []
bloxverse_qr_c4 = []
icomarks_c4 = []
rday1_c4 = []

for i in range(0,len(indices2)):
    indices.append(i)
    icomarks_c4.append(i)
    bloxverse_yr_c4.append(i)
    bloxverse_sa_c4.append(i)
    bloxverse_qr_c4.append(i)

    rday1_c4.append(i)
    
    indices[i] = indices2[i][0]
    icomarks_c4[i] = round(eval(icomarks[indices[i]]),2)
    bloxverse_yr_c4[i] = bloxverse_yr[indices[i]]
    bloxverse_sa_c4[i] = bloxverse_sa[indices[i]]
    bloxverse_qr_c4[i] = bloxverse_qr[indices[i]]

    rday1_c4[i] = return_day1[indices[i]]

#Calculate Kendall's tau for each correlation with day 1 return.
#Method with better correlation wins

tau_bloxverse_yr, p_value_bloxverse_yr = stats.kendalltau(bloxverse_yr_c4, rday1_c4)
tau_bloxverse_sa, p_value_bloxverse_sa = stats.kendalltau(bloxverse_sa_c4, rday1_c4)
tau_bloxverse_qr, p_value_bloxverse_qr = stats.kendalltau(bloxverse_qr_c4, rday1_c4)
tau_icomarks, p_value_icomarks = stats.kendalltau(icomarks_c4, rday1_c4)
print('Bloxverse/Full Score Kendall Tau: ',round(tau_bloxverse_yr,3))
print('Bloxverse/Semiannual Score Kendall Tau: ',round(tau_bloxverse_sa,3))
print('Bloxverse/Quarterly Score Kendall Tau: ',round(tau_bloxverse_qr,3))
print('ICO Rating Risk Score Kendall Tau: ',round(tau_icomarks,3))

#Calculate Linear Fit for all Methods and Compute Fit Error
fit_bloxverse_yr = np.polyfit(bloxverse_yr_c4, rday1_c4, 1, full = True)
fit_bloxverse_sa = np.polyfit(bloxverse_sa_c4, rday1_c4, 1, full = True)
fit_bloxverse_qr = np.polyfit(bloxverse_qr_c4, rday1_c4, 1, full = True)
fit_icomarks = np.polyfit(icomarks_c4, rday1_c4, 1, full = True)
bloxverse_yr_error = np.sum((np.polyval(np.polyfit(bloxverse_yr_c4, rday1_c4, 1), bloxverse_yr_c4) - rday1_c4)**2)
bloxverse_sa_error = np.sum((np.polyval(np.polyfit(bloxverse_sa_c4, rday1_c4, 1), bloxverse_sa_c4) - rday1_c4)**2)
bloxverse_qr_error = np.sum((np.polyval(np.polyfit(bloxverse_qr_c4, rday1_c4, 1), bloxverse_qr_c4) - rday1_c4)**2)
icomarks_error = np.sum((np.polyval(np.polyfit(icomarks_c4, rday1_c4, 1), icomarks_c4) - rday1_c4)**2)
print('Bloxverse/Full Linear Fit Error: ',round(bloxverse_yr_error,3))
print('Bloxverse/Semiannual Linear Fit Error: ',round(bloxverse_sa_error,3))
print('Bloxverse/Quarterly Linear Fit Error: ',round(bloxverse_qr_error,3))
print('ICO Rating Risk Linear Fit Error: ',round(icomarks_error,3))

###5. BLOXVERSE VERSUS ICOBENCH SCORE: DAY 1 RETURNS
print('----------------------------------------------------------------')
print('BLOXVERSE VS. ICOBENCH: DAY 1 RETURNS')
print('----------------------------------------------------------------')

#First find indices for which ICORATING HYPE entries are not equal to N/A
icobench = np.asarray(icobench)
indices2 = np.argwhere(icobench != 'N/A')

indices = []
bloxverse_yr_c5 = []
bloxverse_sa_c5 = []
bloxverse_qr_c5 = []
icobench_c5 = []
rday1_c5 = []

for i in range(0,len(indices2)):
    indices.append(i)
    icobench_c5.append(i)
    bloxverse_yr_c5.append(i)
    bloxverse_sa_c5.append(i)
    bloxverse_qr_c5.append(i)

    rday1_c5.append(i)
    
    indices[i] = indices2[i][0]
    icobench_c5[i] = round(eval(icobench[indices[i]]),2)
    bloxverse_yr_c5[i] = bloxverse_yr[indices[i]]
    bloxverse_sa_c5[i] = bloxverse_sa[indices[i]]
    bloxverse_qr_c5[i] = bloxverse_qr[indices[i]]

    rday1_c5[i] = return_day1[indices[i]]

#Calculate Kendall's tau for each correlation with day 1 return.
#Method with better correlation wins

tau_bloxverse_yr, p_value_bloxverse_yr = stats.kendalltau(bloxverse_yr_c5, rday1_c5)
tau_bloxverse_sa, p_value_bloxverse_sa = stats.kendalltau(bloxverse_sa_c5, rday1_c5)
tau_bloxverse_qr, p_value_bloxverse_qr = stats.kendalltau(bloxverse_qr_c5, rday1_c5)
tau_icobench, p_value_icobench = stats.kendalltau(icobench_c5, rday1_c5)
print('Bloxverse/Full Score Kendall Tau: ',round(tau_bloxverse_yr,3))
print('Bloxverse/Semiannual Score Kendall Tau: ',round(tau_bloxverse_sa,3))
print('Bloxverse/Quarterly Score Kendall Tau: ',round(tau_bloxverse_qr,3))
print('ICO Rating Risk Score Kendall Tau: ',round(tau_icobench,3))

#Calculate Linear Fit for all Methods and Compute Fit Error
fit_bloxverse_yr = np.polyfit(bloxverse_yr_c5, rday1_c5, 1, full = True)
fit_bloxverse_sa = np.polyfit(bloxverse_sa_c5, rday1_c5, 1, full = True)
fit_bloxverse_qr = np.polyfit(bloxverse_qr_c5, rday1_c5, 1, full = True)
fit_icobench = np.polyfit(icobench_c5, rday1_c5, 1, full = True)
bloxverse_yr_error = np.sum((np.polyval(np.polyfit(bloxverse_yr_c5, rday1_c5, 1), bloxverse_yr_c5) - rday1_c5)**2)
bloxverse_sa_error = np.sum((np.polyval(np.polyfit(bloxverse_sa_c5, rday1_c5, 1), bloxverse_sa_c5) - rday1_c5)**2)
bloxverse_qr_error = np.sum((np.polyval(np.polyfit(bloxverse_qr_c5, rday1_c5, 1), bloxverse_qr_c5) - rday1_c5)**2)
icobench_error = np.sum((np.polyval(np.polyfit(icobench_c5, rday1_c5, 1), icobench_c5) - rday1_c5)**2)
print('Bloxverse/Full Linear Fit Error: ',round(bloxverse_yr_error,3))
print('Bloxverse/Semiannual Linear Fit Error: ',round(bloxverse_sa_error,3))
print('Bloxverse/Quarterly Linear Fit Error: ',round(bloxverse_qr_error,3))
print('ICO Rating Risk Linear Fit Error: ',round(icobench_error,3))


####################################################################################################################
####################################################################################################################
####################################################################################################################
####################################################################################################################
####################################################################################################################


###1. BLOXVERSE VERSUS ICORATING HYPE SCORE: DAY 1 VOLUME
print('----------------------------------------------------------------')
print('BLOXVERSE VS. ICORATING HYPE: DAY 1 VOLUME')
print('----------------------------------------------------------------')

#First find indices for which ICORATING HYPE entries are not equal to N/A
icorating_hype = np.asarray(icorating_hype)
indices2 = np.argwhere(icorating_hype != 'N/A')

indices = []
bloxverse_yr_c1 = []
bloxverse_sa_c1 = []
bloxverse_qr_c1 = []
icorating_hype_c1 = []
volday1_c1 = []

for i in range(0,len(indices2)):
    indices.append(i)
    icorating_hype_c1.append(i)
    bloxverse_yr_c1.append(i)
    bloxverse_sa_c1.append(i)
    bloxverse_qr_c1.append(i)

    volday1_c1.append(i)
    
    indices[i] = indices2[i][0]
    icorating_hype_c1[i] = round(eval(icorating_hype[indices[i]]),2)
    bloxverse_yr_c1[i] = bloxverse_yr[indices[i]]
    bloxverse_sa_c1[i] = bloxverse_sa[indices[i]]
    bloxverse_qr_c1[i] = bloxverse_qr[indices[i]]

    volday1_c1[i] = volume_day1[indices[i]]

#Calculate Kendall's tau for each correlation with day 1 return.
#Method with better correlation wins

tau_bloxverse_yr, p_value_bloxverse_yr = stats.kendalltau(bloxverse_yr_c1, volday1_c1)
tau_bloxverse_sa, p_value_bloxverse_sa = stats.kendalltau(bloxverse_sa_c1, volday1_c1)
tau_bloxverse_qr, p_value_bloxverse_qr = stats.kendalltau(bloxverse_qr_c1, volday1_c1)
tau_icorating_hype, p_value_icorating_hype = stats.kendalltau(icorating_hype_c1, volday1_c1)
print('Bloxverse/Full Score Kendall Tau: ',round(tau_bloxverse_yr,3))
print('Bloxverse/Semiannual Score Kendall Tau: ',round(tau_bloxverse_sa,3))
print('Bloxverse/Quarterly Score Kendall Tau: ',round(tau_bloxverse_qr,3))
print('ICO Rating Hype Score Kendall Tau: ',round(tau_icorating_hype,3))

#Calculate Linear Fit for all Methods and Compute Fit Error
fit_bloxverse_yr = np.polyfit(bloxverse_yr_c1, volday1_c1, 1, full = True)
fit_bloxverse_sa = np.polyfit(bloxverse_sa_c1, volday1_c1, 1, full = True)
fit_bloxverse_qr = np.polyfit(bloxverse_qr_c1, volday1_c1, 1, full = True)
fit_icorating_hype = np.polyfit(icorating_hype_c1, volday1_c1, 1, full = True)
bloxverse_yr_error = np.sum((np.polyval(np.polyfit(bloxverse_yr_c1, volday1_c1, 1), bloxverse_yr_c1) - volday1_c1)**2)
bloxverse_sa_error = np.sum((np.polyval(np.polyfit(bloxverse_sa_c1, volday1_c1, 1), bloxverse_sa_c1) - volday1_c1)**2)
bloxverse_qr_error = np.sum((np.polyval(np.polyfit(bloxverse_qr_c1, volday1_c1, 1), bloxverse_qr_c1) - volday1_c1)**2)
icorating_hype_error = np.sum((np.polyval(np.polyfit(icorating_hype_c1, volday1_c1, 1), icorating_hype_c1) - volday1_c1)**2)
print('Bloxverse/Full Linear Fit Error: ',round(bloxverse_yr_error,3))
print('Bloxverse/Semiannual Linear Fit Error: ',round(bloxverse_sa_error,3))
print('Bloxverse/Quarterly Linear Fit Error: ',round(bloxverse_qr_error,3))
print('ICO Rating Hype Linear Fit Error: ',round(icorating_hype_error,3))

###2. BLOXVERSE VERSUS ICORATING RISK SCORE: DAY 1 VOLUME
print('----------------------------------------------------------------')
print('BLOXVERSE VS. ICORATING RISK: DAY 1 VOLUME')
print('----------------------------------------------------------------')

#First find indices for which ICORATING HYPE entries are not equal to N/A
icorating_risk = np.asarray(icorating_risk)
indices2 = np.argwhere(icorating_risk != 'N/A')

indices = []
bloxverse_yr_c2 = []
bloxverse_sa_c2 = []
bloxverse_qr_c2 = []
icorating_risk_c2 = []
volday1_c2 = []

for i in range(0,len(indices2)):
    indices.append(i)
    icorating_risk_c2.append(i)
    bloxverse_yr_c2.append(i)
    bloxverse_sa_c2.append(i)
    bloxverse_qr_c2.append(i)

    volday1_c2.append(i)
    
    indices[i] = indices2[i][0]
    icorating_risk_c2[i] = round(eval(icorating_risk[indices[i]]),2)
    bloxverse_yr_c2[i] = bloxverse_yr[indices[i]]
    bloxverse_sa_c2[i] = bloxverse_sa[indices[i]]
    bloxverse_qr_c2[i] = bloxverse_qr[indices[i]]

    volday1_c2[i] = volume_day1[indices[i]]

#Calculate Kendall's tau for each correlation with day 1 return.
#Method with better correlation wins

tau_bloxverse_yr, p_value_bloxverse_yr = stats.kendalltau(bloxverse_yr_c2, volday1_c2)
tau_bloxverse_sa, p_value_bloxverse_sa = stats.kendalltau(bloxverse_sa_c2, volday1_c2)
tau_bloxverse_qr, p_value_bloxverse_qr = stats.kendalltau(bloxverse_qr_c2, volday1_c2)
tau_icorating_risk, p_value_icorating_risk = stats.kendalltau(icorating_risk_c2, volday1_c2)
print('Bloxverse/Full Score Kendall Tau: ',round(tau_bloxverse_yr,3))
print('Bloxverse/Semiannual Score Kendall Tau: ',round(tau_bloxverse_sa,3))
print('Bloxverse/Quarterly Score Kendall Tau: ',round(tau_bloxverse_qr,3))
print('ICO Rating Risk Score Kendall Tau: ',round(tau_icorating_risk,3))

#Calculate Linear Fit for all Methods and Compute Fit Error
fit_bloxverse_yr = np.polyfit(bloxverse_yr_c2, volday1_c2, 1, full = True)
fit_bloxverse_sa = np.polyfit(bloxverse_sa_c2, volday1_c2, 1, full = True)
fit_bloxverse_qr = np.polyfit(bloxverse_qr_c2, volday1_c2, 1, full = True)
fit_icorating_risk = np.polyfit(icorating_risk_c2, volday1_c2, 1, full = True)
bloxverse_yr_error = np.sum((np.polyval(np.polyfit(bloxverse_yr_c2, volday1_c2, 1), bloxverse_yr_c2) - volday1_c2)**2)
bloxverse_sa_error = np.sum((np.polyval(np.polyfit(bloxverse_sa_c2, volday1_c2, 1), bloxverse_sa_c2) - volday1_c2)**2)
bloxverse_qr_error = np.sum((np.polyval(np.polyfit(bloxverse_qr_c2, volday1_c2, 1), bloxverse_qr_c2) - volday1_c2)**2)
icorating_risk_error = np.sum((np.polyval(np.polyfit(icorating_risk_c2, volday1_c2, 1), icorating_risk_c2) - volday1_c2)**2)
print('Bloxverse/Full Linear Fit Error: ',round(bloxverse_yr_error,3))
print('Bloxverse/Semiannual Linear Fit Error: ',round(bloxverse_sa_error,3))
print('Bloxverse/Quarterly Linear Fit Error: ',round(bloxverse_qr_error,3))
print('ICO Rating Risk Linear Fit Error: ',round(icorating_risk_error,3))

###3. BLOXVERSE VERSUS ICOBAZAAR SCORE: DAY 1 VOLUME
print('----------------------------------------------------------------')
print('BLOXVERSE VS. ICOBAZAAR: DAY 1 VOLUME')
print('----------------------------------------------------------------')

#First find indices for which ICORATING HYPE entries are not equal to N/A
icobazaar = np.asarray(icobazaar)
indices2 = np.argwhere(icobazaar != 'N/A')

indices = []
bloxverse_yr_c3 = []
bloxverse_sa_c3 = []
bloxverse_qr_c3 = []
icobazaar_c3 = []
volday1_c3 = []

for i in range(0,len(indices2)):
    indices.append(i)
    icobazaar_c3.append(i)
    bloxverse_yr_c3.append(i)
    bloxverse_sa_c3.append(i)
    bloxverse_qr_c3.append(i)

    volday1_c3.append(i)
    
    indices[i] = indices2[i][0]
    icobazaar_c3[i] = round(eval(icobazaar[indices[i]]),2)
    bloxverse_yr_c3[i] = bloxverse_yr[indices[i]]
    bloxverse_sa_c3[i] = bloxverse_sa[indices[i]]
    bloxverse_qr_c3[i] = bloxverse_qr[indices[i]]

    volday1_c3[i] = volume_day1[indices[i]]

#Calculate Kendall's tau for each correlation with day 1 return.
#Method with better correlation wins

tau_bloxverse_yr, p_value_bloxverse_yr = stats.kendalltau(bloxverse_yr_c3, volday1_c3)
tau_bloxverse_sa, p_value_bloxverse_sa = stats.kendalltau(bloxverse_sa_c3, volday1_c3)
tau_bloxverse_qr, p_value_bloxverse_qr = stats.kendalltau(bloxverse_qr_c3, volday1_c3)
tau_icobazaar, p_value_icobazaar = stats.kendalltau(icobazaar_c3, volday1_c3)
print('Bloxverse/Full Score Kendall Tau: ',round(tau_bloxverse_yr,3))
print('Bloxverse/Semiannual Score Kendall Tau: ',round(tau_bloxverse_sa,3))
print('Bloxverse/Quarterly Score Kendall Tau: ',round(tau_bloxverse_qr,3))
print('ICO Rating Risk Score Kendall Tau: ',round(tau_icobazaar,3))

#Calculate Linear Fit for all Methods and Compute Fit Error
fit_bloxverse_yr = np.polyfit(bloxverse_yr_c3, volday1_c3, 1, full = True)
fit_bloxverse_sa = np.polyfit(bloxverse_sa_c3, volday1_c3, 1, full = True)
fit_bloxverse_qr = np.polyfit(bloxverse_qr_c3, volday1_c3, 1, full = True)
fit_icobazaar = np.polyfit(icobazaar_c3, volday1_c3, 1, full = True)
bloxverse_yr_error = np.sum((np.polyval(np.polyfit(bloxverse_yr_c3, volday1_c3, 1), bloxverse_yr_c3) - volday1_c3)**2)
bloxverse_sa_error = np.sum((np.polyval(np.polyfit(bloxverse_sa_c3, volday1_c3, 1), bloxverse_sa_c3) - volday1_c3)**2)
bloxverse_qr_error = np.sum((np.polyval(np.polyfit(bloxverse_qr_c3, volday1_c3, 1), bloxverse_qr_c3) - volday1_c3)**2)
icobazaar_error = np.sum((np.polyval(np.polyfit(icobazaar_c3, volday1_c3, 1), icobazaar_c3) - volday1_c3)**2)
print('Bloxverse/Full Linear Fit Error: ',round(bloxverse_yr_error,3))
print('Bloxverse/Semiannual Linear Fit Error: ',round(bloxverse_sa_error,3))
print('Bloxverse/Quarterly Linear Fit Error: ',round(bloxverse_qr_error,3))
print('ICO Rating Risk Linear Fit Error: ',round(icobazaar_error,3))

###4. BLOXVERSE VERSUS ICOMARKS SCORE: DAY 1 VOLUME
print('----------------------------------------------------------------')
print('BLOXVERSE VS. ICOMARKS: DAY 1 VOLUME')
print('----------------------------------------------------------------')

#First find indices for which ICORATING HYPE entries are not equal to N/A
icomarks = np.asarray(icomarks)
indices2 = np.argwhere(icomarks != 'N/A')

indices = []
bloxverse_yr_c4 = []
bloxverse_sa_c4 = []
bloxverse_qr_c4 = []
icomarks_c4 = []
volday1_c4 = []

for i in range(0,len(indices2)):
    indices.append(i)
    icomarks_c4.append(i)
    bloxverse_yr_c4.append(i)
    bloxverse_sa_c4.append(i)
    bloxverse_qr_c4.append(i)

    volday1_c4.append(i)
    
    indices[i] = indices2[i][0]
    icomarks_c4[i] = round(eval(icomarks[indices[i]]),2)
    bloxverse_yr_c4[i] = bloxverse_yr[indices[i]]
    bloxverse_sa_c4[i] = bloxverse_sa[indices[i]]
    bloxverse_qr_c4[i] = bloxverse_qr[indices[i]]

    volday1_c4[i] = volume_day1[indices[i]]

#Calculate Kendall's tau for each correlation with day 1 return.
#Method with better correlation wins

tau_bloxverse_yr, p_value_bloxverse_yr = stats.kendalltau(bloxverse_yr_c4, volday1_c4)
tau_bloxverse_sa, p_value_bloxverse_sa = stats.kendalltau(bloxverse_sa_c4, volday1_c4)
tau_bloxverse_qr, p_value_bloxverse_qr = stats.kendalltau(bloxverse_qr_c4, volday1_c4)
tau_icomarks, p_value_icomarks = stats.kendalltau(icomarks_c4, volday1_c4)
print('Bloxverse/Full Score Kendall Tau: ',round(tau_bloxverse_yr,3))
print('Bloxverse/Semiannual Score Kendall Tau: ',round(tau_bloxverse_sa,3))
print('Bloxverse/Quarterly Score Kendall Tau: ',round(tau_bloxverse_qr,3))
print('ICO Rating Risk Score Kendall Tau: ',round(tau_icomarks,3))

#Calculate Linear Fit for all Methods and Compute Fit Error
fit_bloxverse_yr = np.polyfit(bloxverse_yr_c4, volday1_c4, 1, full = True)
fit_bloxverse_sa = np.polyfit(bloxverse_sa_c4, volday1_c4, 1, full = True)
fit_bloxverse_qr = np.polyfit(bloxverse_qr_c4, volday1_c4, 1, full = True)
fit_icomarks = np.polyfit(icomarks_c4, volday1_c4, 1, full = True)
bloxverse_yr_error = np.sum((np.polyval(np.polyfit(bloxverse_yr_c4, volday1_c4, 1), bloxverse_yr_c4) - volday1_c4)**2)
bloxverse_sa_error = np.sum((np.polyval(np.polyfit(bloxverse_sa_c4, volday1_c4, 1), bloxverse_sa_c4) - volday1_c4)**2)
bloxverse_qr_error = np.sum((np.polyval(np.polyfit(bloxverse_qr_c4, volday1_c4, 1), bloxverse_qr_c4) - volday1_c4)**2)
icomarks_error = np.sum((np.polyval(np.polyfit(icomarks_c4, volday1_c4, 1), icomarks_c4) - volday1_c4)**2)
print('Bloxverse/Full Linear Fit Error: ',round(bloxverse_yr_error,3))
print('Bloxverse/Semiannual Linear Fit Error: ',round(bloxverse_sa_error,3))
print('Bloxverse/Quarterly Linear Fit Error: ',round(bloxverse_qr_error,3))
print('ICO Rating Risk Linear Fit Error: ',round(icomarks_error,3))

###5. BLOXVERSE VERSUS ICOBENCH SCORE: DAY 1 VOLUME
print('----------------------------------------------------------------')
print('BLOXVERSE VS. ICOBENCH: DAY 1 VOLUME')
print('----------------------------------------------------------------')

#First find indices for which ICORATING HYPE entries are not equal to N/A
icobench = np.asarray(icobench)
indices2 = np.argwhere(icobench != 'N/A')

indices = []
bloxverse_yr_c5 = []
bloxverse_sa_c5 = []
bloxverse_qr_c5 = []
icobench_c5 = []
volday1_c5 = []

for i in range(0,len(indices2)):
    indices.append(i)
    icobench_c5.append(i)
    bloxverse_yr_c5.append(i)
    bloxverse_sa_c5.append(i)
    bloxverse_qr_c5.append(i)

    volday1_c5.append(i)
    
    indices[i] = indices2[i][0]
    icobench_c5[i] = round(eval(icobench[indices[i]]),2)
    bloxverse_yr_c5[i] = bloxverse_yr[indices[i]]
    bloxverse_sa_c5[i] = bloxverse_sa[indices[i]]
    bloxverse_qr_c5[i] = bloxverse_qr[indices[i]]

    volday1_c5[i] = volume_day1[indices[i]]

#Calculate Kendall's tau for each correlation with day 1 return.
#Method with better correlation wins

tau_bloxverse_yr, p_value_bloxverse_yr = stats.kendalltau(bloxverse_yr_c5, volday1_c5)
tau_bloxverse_sa, p_value_bloxverse_sa = stats.kendalltau(bloxverse_sa_c5, volday1_c5)
tau_bloxverse_qr, p_value_bloxverse_qr = stats.kendalltau(bloxverse_qr_c5, volday1_c5)
tau_icobench, p_value_icobench = stats.kendalltau(icobench_c5, volday1_c5)
print('Bloxverse/Full Score Kendall Tau: ',round(tau_bloxverse_yr,3))
print('Bloxverse/Semiannual Score Kendall Tau: ',round(tau_bloxverse_sa,3))
print('Bloxverse/Quarterly Score Kendall Tau: ',round(tau_bloxverse_qr,3))
print('ICO Rating Risk Score Kendall Tau: ',round(tau_icobench,3))

#Calculate Linear Fit for all Methods and Compute Fit Error
fit_bloxverse_yr = np.polyfit(bloxverse_yr_c5, volday1_c5, 1, full = True)
fit_bloxverse_sa = np.polyfit(bloxverse_sa_c5, volday1_c5, 1, full = True)
fit_bloxverse_qr = np.polyfit(bloxverse_qr_c5, volday1_c5, 1, full = True)
fit_icobench = np.polyfit(icobench_c5, volday1_c5, 1, full = True)
bloxverse_yr_error = np.sum((np.polyval(np.polyfit(bloxverse_yr_c5, volday1_c5, 1), bloxverse_yr_c5) - volday1_c5)**2)
bloxverse_sa_error = np.sum((np.polyval(np.polyfit(bloxverse_sa_c5, volday1_c5, 1), bloxverse_sa_c5) - volday1_c5)**2)
bloxverse_qr_error = np.sum((np.polyval(np.polyfit(bloxverse_qr_c5, volday1_c5, 1), bloxverse_qr_c5) - volday1_c5)**2)
icobench_error = np.sum((np.polyval(np.polyfit(icobench_c5, volday1_c5, 1), icobench_c5) - volday1_c5)**2)
print('Bloxverse/Full Linear Fit Error: ',round(bloxverse_yr_error,3))
print('Bloxverse/Semiannual Linear Fit Error: ',round(bloxverse_sa_error,3))
print('Bloxverse/Quarterly Linear Fit Error: ',round(bloxverse_qr_error,3))
print('ICO Rating Risk Linear Fit Error: ',round(icobench_error,3))

####################################################################################################################
####################################################################################################################
####################################################################################################################
####################################################################################################################
####################################################################################################################


###1. BLOXVERSE VERSUS ICORATING HYPE SCORE: ANNUALIZED SHARPE RATIO
print('----------------------------------------------------------------')
print('BLOXVERSE VS. ICORATING HYPE: ANNUALIZED SHARPE RATIO')
print('----------------------------------------------------------------')

#First find indices for which ICORATING HYPE entries are not equal to N/A
icorating_hype = np.asarray(icorating_hype)
indices2 = np.argwhere(icorating_hype != 'N/A')

indices = []
bloxverse_yr_c1 = []
bloxverse_sa_c1 = []
bloxverse_qr_c1 = []
icorating_hype_c1 = []
shrp_c1 = []

for i in range(0,len(indices2)):
    indices.append(i)
    icorating_hype_c1.append(i)
    bloxverse_yr_c1.append(i)
    bloxverse_sa_c1.append(i)
    bloxverse_qr_c1.append(i)

    shrp_c1.append(i)
    
    indices[i] = indices2[i][0]
    icorating_hype_c1[i] = round(eval(icorating_hype[indices[i]]),2)
    bloxverse_yr_c1[i] = bloxverse_yr[indices[i]]
    bloxverse_sa_c1[i] = bloxverse_sa[indices[i]]
    bloxverse_qr_c1[i] = bloxverse_qr[indices[i]]

    shrp_c1[i] = sharpe_annual[indices[i]]

#Calculate Kendall's tau for each correlation with day 1 return.
#Method with better correlation wins

tau_bloxverse_yr, p_value_bloxverse_yr = stats.kendalltau(bloxverse_yr_c1, shrp_c1)
tau_bloxverse_sa, p_value_bloxverse_sa = stats.kendalltau(bloxverse_sa_c1, shrp_c1)
tau_bloxverse_qr, p_value_bloxverse_qr = stats.kendalltau(bloxverse_qr_c1, shrp_c1)
tau_icorating_hype, p_value_icorating_hype = stats.kendalltau(icorating_hype_c1, shrp_c1)
print('Bloxverse/Full Score Kendall Tau: ',round(tau_bloxverse_yr,3))
print('Bloxverse/Semiannual Score Kendall Tau: ',round(tau_bloxverse_sa,3))
print('Bloxverse/Quarterly Score Kendall Tau: ',round(tau_bloxverse_qr,3))
print('ICO Rating Hype Score Kendall Tau: ',round(tau_icorating_hype,3))

#Calculate Linear Fit for all Methods and Compute Fit Error
fit_bloxverse_yr = np.polyfit(bloxverse_yr_c1, shrp_c1, 1, full = True)
fit_bloxverse_sa = np.polyfit(bloxverse_sa_c1, shrp_c1, 1, full = True)
fit_bloxverse_qr = np.polyfit(bloxverse_qr_c1, shrp_c1, 1, full = True)
fit_icorating_hype = np.polyfit(icorating_hype_c1, shrp_c1, 1, full = True)
bloxverse_yr_error = np.sum((np.polyval(np.polyfit(bloxverse_yr_c1, shrp_c1, 1), bloxverse_yr_c1) - shrp_c1)**2)
bloxverse_sa_error = np.sum((np.polyval(np.polyfit(bloxverse_sa_c1, shrp_c1, 1), bloxverse_sa_c1) - shrp_c1)**2)
bloxverse_qr_error = np.sum((np.polyval(np.polyfit(bloxverse_qr_c1, shrp_c1, 1), bloxverse_qr_c1) - shrp_c1)**2)
icorating_hype_error = np.sum((np.polyval(np.polyfit(icorating_hype_c1, shrp_c1, 1), icorating_hype_c1) - shrp_c1)**2)
print('Bloxverse/Full Linear Fit Error: ',round(bloxverse_yr_error,3))
print('Bloxverse/Semiannual Linear Fit Error: ',round(bloxverse_sa_error,3))
print('Bloxverse/Quarterly Linear Fit Error: ',round(bloxverse_qr_error,3))
print('ICO Rating Hype Linear Fit Error: ',round(icorating_hype_error,3))

###2. BLOXVERSE VERSUS ICORATING RISK SCORE: ANNUALIZED SHARPE RATIO
print('----------------------------------------------------------------')
print('BLOXVERSE VS. ICORATING RISK: ANNUALIZED SHARPE RATIO')
print('----------------------------------------------------------------')

#First find indices for which ICORATING HYPE entries are not equal to N/A
icorating_risk = np.asarray(icorating_risk)
indices2 = np.argwhere(icorating_risk != 'N/A')

indices = []
bloxverse_yr_c2 = []
bloxverse_sa_c2 = []
bloxverse_qr_c2 = []
icorating_risk_c2 = []
shrp_c2 = []

for i in range(0,len(indices2)):
    indices.append(i)
    icorating_risk_c2.append(i)
    bloxverse_yr_c2.append(i)
    bloxverse_sa_c2.append(i)
    bloxverse_qr_c2.append(i)

    shrp_c2.append(i)
    
    indices[i] = indices2[i][0]
    icorating_risk_c2[i] = round(eval(icorating_risk[indices[i]]),2)
    bloxverse_yr_c2[i] = bloxverse_yr[indices[i]]
    bloxverse_sa_c2[i] = bloxverse_sa[indices[i]]
    bloxverse_qr_c2[i] = bloxverse_qr[indices[i]]

    shrp_c2[i] = sharpe_annual[indices[i]]

#Calculate Kendall's tau for each correlation with day 1 return.
#Method with better correlation wins

tau_bloxverse_yr, p_value_bloxverse_yr = stats.kendalltau(bloxverse_yr_c2, shrp_c2)
tau_bloxverse_sa, p_value_bloxverse_sa = stats.kendalltau(bloxverse_sa_c2, shrp_c2)
tau_bloxverse_qr, p_value_bloxverse_qr = stats.kendalltau(bloxverse_qr_c2, shrp_c2)
tau_icorating_risk, p_value_icorating_risk = stats.kendalltau(icorating_risk_c2, shrp_c2)
print('Bloxverse/Full Score Kendall Tau: ',round(tau_bloxverse_yr,3))
print('Bloxverse/Semiannual Score Kendall Tau: ',round(tau_bloxverse_sa,3))
print('Bloxverse/Quarterly Score Kendall Tau: ',round(tau_bloxverse_qr,3))
print('ICO Rating Risk Score Kendall Tau: ',round(tau_icorating_risk,3))

#Calculate Linear Fit for all Methods and Compute Fit Error
fit_bloxverse_yr = np.polyfit(bloxverse_yr_c2, shrp_c2, 1, full = True)
fit_bloxverse_sa = np.polyfit(bloxverse_sa_c2, shrp_c2, 1, full = True)
fit_bloxverse_qr = np.polyfit(bloxverse_qr_c2, shrp_c2, 1, full = True)
fit_icorating_risk = np.polyfit(icorating_risk_c2, shrp_c2, 1, full = True)
bloxverse_yr_error = np.sum((np.polyval(np.polyfit(bloxverse_yr_c2, shrp_c2, 1), bloxverse_yr_c2) - shrp_c2)**2)
bloxverse_sa_error = np.sum((np.polyval(np.polyfit(bloxverse_sa_c2, shrp_c2, 1), bloxverse_sa_c2) - shrp_c2)**2)
bloxverse_qr_error = np.sum((np.polyval(np.polyfit(bloxverse_qr_c2, shrp_c2, 1), bloxverse_qr_c2) - shrp_c2)**2)
icorating_risk_error = np.sum((np.polyval(np.polyfit(icorating_risk_c2, shrp_c2, 1), icorating_risk_c2) - shrp_c2)**2)
print('Bloxverse/Full Linear Fit Error: ',round(bloxverse_yr_error,3))
print('Bloxverse/Semiannual Linear Fit Error: ',round(bloxverse_sa_error,3))
print('Bloxverse/Quarterly Linear Fit Error: ',round(bloxverse_qr_error,3))
print('ICO Rating Risk Linear Fit Error: ',round(icorating_risk_error,3))

###3. BLOXVERSE VERSUS ICOBAZAAR SCORE: ANNUALIZED SHARPE RATIO
print('----------------------------------------------------------------')
print('BLOXVERSE VS. ICOBAZAAR: ANNUALIZED SHARPE RATIO')
print('----------------------------------------------------------------')

#First find indices for which ICORATING HYPE entries are not equal to N/A
icobazaar = np.asarray(icobazaar)
indices2 = np.argwhere(icobazaar != 'N/A')

indices = []
bloxverse_yr_c3 = []
bloxverse_sa_c3 = []
bloxverse_qr_c3 = []
icobazaar_c3 = []
shrp_c3 = []

for i in range(0,len(indices2)):
    indices.append(i)
    icobazaar_c3.append(i)
    bloxverse_yr_c3.append(i)
    bloxverse_sa_c3.append(i)
    bloxverse_qr_c3.append(i)

    shrp_c3.append(i)
    
    indices[i] = indices2[i][0]
    icobazaar_c3[i] = round(eval(icobazaar[indices[i]]),2)
    bloxverse_yr_c3[i] = bloxverse_yr[indices[i]]
    bloxverse_sa_c3[i] = bloxverse_sa[indices[i]]
    bloxverse_qr_c3[i] = bloxverse_qr[indices[i]]

    shrp_c3[i] = sharpe_annual[indices[i]]

#Calculate Kendall's tau for each correlation with day 1 return.
#Method with better correlation wins

tau_bloxverse_yr, p_value_bloxverse_yr = stats.kendalltau(bloxverse_yr_c3, shrp_c3)
tau_bloxverse_sa, p_value_bloxverse_sa = stats.kendalltau(bloxverse_sa_c3, shrp_c3)
tau_bloxverse_qr, p_value_bloxverse_qr = stats.kendalltau(bloxverse_qr_c3, shrp_c3)
tau_icobazaar, p_value_icobazaar = stats.kendalltau(icobazaar_c3, shrp_c3)
print('Bloxverse/Full Score Kendall Tau: ',round(tau_bloxverse_yr,3))
print('Bloxverse/Semiannual Score Kendall Tau: ',round(tau_bloxverse_sa,3))
print('Bloxverse/Quarterly Score Kendall Tau: ',round(tau_bloxverse_qr,3))
print('ICO Rating Risk Score Kendall Tau: ',round(tau_icobazaar,3))

#Calculate Linear Fit for all Methods and Compute Fit Error
fit_bloxverse_yr = np.polyfit(bloxverse_yr_c3, shrp_c3, 1, full = True)
fit_bloxverse_sa = np.polyfit(bloxverse_sa_c3, shrp_c3, 1, full = True)
fit_bloxverse_qr = np.polyfit(bloxverse_qr_c3, shrp_c3, 1, full = True)
fit_icobazaar = np.polyfit(icobazaar_c3, shrp_c3, 1, full = True)
bloxverse_yr_error = np.sum((np.polyval(np.polyfit(bloxverse_yr_c3, shrp_c3, 1), bloxverse_yr_c3) - shrp_c3)**2)
bloxverse_sa_error = np.sum((np.polyval(np.polyfit(bloxverse_sa_c3, shrp_c3, 1), bloxverse_sa_c3) - shrp_c3)**2)
bloxverse_qr_error = np.sum((np.polyval(np.polyfit(bloxverse_qr_c3, shrp_c3, 1), bloxverse_qr_c3) - shrp_c3)**2)
icobazaar_error = np.sum((np.polyval(np.polyfit(icobazaar_c3, shrp_c3, 1), icobazaar_c3) - shrp_c3)**2)
print('Bloxverse/Full Linear Fit Error: ',round(bloxverse_yr_error,3))
print('Bloxverse/Semiannual Linear Fit Error: ',round(bloxverse_sa_error,3))
print('Bloxverse/Quarterly Linear Fit Error: ',round(bloxverse_qr_error,3))
print('ICO Rating Risk Linear Fit Error: ',round(icobazaar_error,3))

###4. BLOXVERSE VERSUS ICOMARKS SCORE: ANNUALIZED SHARPE RATIO
print('----------------------------------------------------------------')
print('BLOXVERSE VS. ICOMARKS: ANNUALIZED SHARPE RATIO')
print('----------------------------------------------------------------')

#First find indices for which ICORATING HYPE entries are not equal to N/A
icomarks = np.asarray(icomarks)
indices2 = np.argwhere(icomarks != 'N/A')

indices = []
bloxverse_yr_c4 = []
bloxverse_sa_c4 = []
bloxverse_qr_c4 = []
icomarks_c4 = []
shrp_c4 = []

for i in range(0,len(indices2)):
    indices.append(i)
    icomarks_c4.append(i)
    bloxverse_yr_c4.append(i)
    bloxverse_sa_c4.append(i)
    bloxverse_qr_c4.append(i)

    shrp_c4.append(i)
    
    indices[i] = indices2[i][0]
    icomarks_c4[i] = round(eval(icomarks[indices[i]]),2)
    bloxverse_yr_c4[i] = bloxverse_yr[indices[i]]
    bloxverse_sa_c4[i] = bloxverse_sa[indices[i]]
    bloxverse_qr_c4[i] = bloxverse_qr[indices[i]]

    shrp_c4[i] = sharpe_annual[indices[i]]

#Calculate Kendall's tau for each correlation with day 1 return.
#Method with better correlation wins

tau_bloxverse_yr, p_value_bloxverse_yr = stats.kendalltau(bloxverse_yr_c4, shrp_c4)
tau_bloxverse_sa, p_value_bloxverse_sa = stats.kendalltau(bloxverse_sa_c4, shrp_c4)
tau_bloxverse_qr, p_value_bloxverse_qr = stats.kendalltau(bloxverse_qr_c4, shrp_c4)
tau_icomarks, p_value_icomarks = stats.kendalltau(icomarks_c4, shrp_c4)
print('Bloxverse/Full Score Kendall Tau: ',round(tau_bloxverse_yr,3))
print('Bloxverse/Semiannual Score Kendall Tau: ',round(tau_bloxverse_sa,3))
print('Bloxverse/Quarterly Score Kendall Tau: ',round(tau_bloxverse_qr,3))
print('ICO Rating Risk Score Kendall Tau: ',round(tau_icomarks,3))

#Calculate Linear Fit for all Methods and Compute Fit Error
fit_bloxverse_yr = np.polyfit(bloxverse_yr_c4, shrp_c4, 1, full = True)
fit_bloxverse_sa = np.polyfit(bloxverse_sa_c4, shrp_c4, 1, full = True)
fit_bloxverse_qr = np.polyfit(bloxverse_qr_c4, shrp_c4, 1, full = True)
fit_icomarks = np.polyfit(icomarks_c4, shrp_c4, 1, full = True)
bloxverse_yr_error = np.sum((np.polyval(np.polyfit(bloxverse_yr_c4, shrp_c4, 1), bloxverse_yr_c4) - shrp_c4)**2)
bloxverse_sa_error = np.sum((np.polyval(np.polyfit(bloxverse_sa_c4, shrp_c4, 1), bloxverse_sa_c4) - shrp_c4)**2)
bloxverse_qr_error = np.sum((np.polyval(np.polyfit(bloxverse_qr_c4, shrp_c4, 1), bloxverse_qr_c4) - shrp_c4)**2)
icomarks_error = np.sum((np.polyval(np.polyfit(icomarks_c4, shrp_c4, 1), icomarks_c4) - shrp_c4)**2)
print('Bloxverse/Full Linear Fit Error: ',round(bloxverse_yr_error,3))
print('Bloxverse/Semiannual Linear Fit Error: ',round(bloxverse_sa_error,3))
print('Bloxverse/Quarterly Linear Fit Error: ',round(bloxverse_qr_error,3))
print('ICO Rating Risk Linear Fit Error: ',round(icomarks_error,3))

###5. BLOXVERSE VERSUS ICOBENCH SCORE: ANNUALIZED SHARPE RATIO
print('----------------------------------------------------------------')
print('BLOXVERSE VS. ICOBENCH: ANNUALIZED SHARPE RATIO')
print('----------------------------------------------------------------')

#First find indices for which ICORATING HYPE entries are not equal to N/A
icobench = np.asarray(icobench)
indices2 = np.argwhere(icobench != 'N/A')

indices = []
bloxverse_yr_c5 = []
bloxverse_sa_c5 = []
bloxverse_qr_c5 = []
icobench_c5 = []
shrp_c5 = []

for i in range(0,len(indices2)):
    indices.append(i)
    icobench_c5.append(i)
    bloxverse_yr_c5.append(i)
    bloxverse_sa_c5.append(i)
    bloxverse_qr_c5.append(i)

    shrp_c5.append(i)
    
    indices[i] = indices2[i][0]
    icobench_c5[i] = round(eval(icobench[indices[i]]),2)
    bloxverse_yr_c5[i] = bloxverse_yr[indices[i]]
    bloxverse_sa_c5[i] = bloxverse_sa[indices[i]]
    bloxverse_qr_c5[i] = bloxverse_qr[indices[i]]

    shrp_c5[i] = sharpe_annual[indices[i]]

#Calculate Kendall's tau for each correlation with day 1 return.
#Method with better correlation wins

tau_bloxverse_yr, p_value_bloxverse_yr = stats.kendalltau(bloxverse_yr_c5, shrp_c5)
tau_bloxverse_sa, p_value_bloxverse_sa = stats.kendalltau(bloxverse_sa_c5, shrp_c5)
tau_bloxverse_qr, p_value_bloxverse_qr = stats.kendalltau(bloxverse_qr_c5, shrp_c5)
tau_icobench, p_value_icobench = stats.kendalltau(icobench_c5, shrp_c5)
print('Bloxverse/Full Score Kendall Tau: ',round(tau_bloxverse_yr,3))
print('Bloxverse/Semiannual Score Kendall Tau: ',round(tau_bloxverse_sa,3))
print('Bloxverse/Quarterly Score Kendall Tau: ',round(tau_bloxverse_qr,3))
print('ICO Rating Risk Score Kendall Tau: ',round(tau_icobench,3))

#Calculate Linear Fit for all Methods and Compute Fit Error
fit_bloxverse_yr = np.polyfit(bloxverse_yr_c5, shrp_c5, 1, full = True)
fit_bloxverse_sa = np.polyfit(bloxverse_sa_c5, shrp_c5, 1, full = True)
fit_bloxverse_qr = np.polyfit(bloxverse_qr_c5, shrp_c5, 1, full = True)
fit_icobench = np.polyfit(icobench_c5, shrp_c5, 1, full = True)
bloxverse_yr_error = np.sum((np.polyval(np.polyfit(bloxverse_yr_c5, shrp_c5, 1), bloxverse_yr_c5) - shrp_c5)**2)
bloxverse_sa_error = np.sum((np.polyval(np.polyfit(bloxverse_sa_c5, shrp_c5, 1), bloxverse_sa_c5) - shrp_c5)**2)
bloxverse_qr_error = np.sum((np.polyval(np.polyfit(bloxverse_qr_c5, shrp_c5, 1), bloxverse_qr_c5) - shrp_c5)**2)
icobench_error = np.sum((np.polyval(np.polyfit(icobench_c5, shrp_c5, 1), icobench_c5) - shrp_c5)**2)
print('Bloxverse/Full Linear Fit Error: ',round(bloxverse_yr_error,3))
print('Bloxverse/Semiannual Linear Fit Error: ',round(bloxverse_sa_error,3))
print('Bloxverse/Quarterly Linear Fit Error: ',round(bloxverse_qr_error,3))
print('ICO Rating Risk Linear Fit Error: ',round(icobench_error,3))

