import csv
from csv import *

#columnTitles_complete = "coin,start,end,duration,age,region,industry,team,raised,hardcap,success,price,telegram,N_google_news,N_twitter,N_daily_views,N_daily_time,hype,risk,bazaar-rate,ret_ico_to_day_one,vol_day1,sharpe_1,sharpe_3,sharpe_yr,sharpe_yr2,beta_btc,beta_top10,alpha_btc,alpha_top10\n"

with open("outdata/ico_data_rate_cluster.csv") as f2:
    reader = csv.reader(f2)
    target_data = [r2 for r2 in reader]

with open('outdata/ico_data_social.csv', 'w') as csvfile_b:
    #csvfile_b.write(columnTitles_complete)
    writer=csv.writer(csvfile_b, delimiter=',')

    for i in range(0,len(target_data)):
        if ('N/A' not in target_data[i][10]) and ('N/A' not in target_data[i][12]) and ('N/A' not in target_data[i][14]) and ('N/A' not in target_data[i][15]) and ('N/A' not in target_data[i][16]):
            all_data = [target_data[i][0],target_data[i][1],target_data[i][2],target_data[i][3],target_data[i][4],target_data[i][5],target_data[i][6],target_data[i][7],target_data[i][8],target_data[i][9],target_data[i][10],target_data[i][11],target_data[i][12],target_data[i][13],target_data[i][14],target_data[i][15],target_data[i][16],target_data[i][17],target_data[i][18],target_data[i][19],target_data[i][20],target_data[i][21],target_data[i][22],target_data[i][23],target_data[i][24],target_data[i][25],target_data[i][26],target_data[i][27],target_data[i][28],target_data[i][29]]
            writer.writerow(all_data)
