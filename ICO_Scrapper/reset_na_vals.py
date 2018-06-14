import csv
import numpy as np
from numpy import *

#This program replaces the NA contents of the ico_data_full.csv file with the contents produced by the re-run of the partial py file

with open("outdata/ico_data_reduced_nans_rerun.csv") as f1:
    reader1 = csv.reader(f1)
    data1 = [r for r in reader1]
    
with open("outdata/ico_data_reduced_wratings_nans_rerun.csv") as f2:
    reader2 = csv.reader(f2)
    data2 = [r for r in reader2]       

with open("outdata/ico_data_full_nodup.csv") as f3:
    reader3 = csv.reader(f3)
    data3 = [r for r in reader3]

with open("outdata/ico_data_full_wr_nodup.csv") as f4:
    reader4 = csv.reader(f4)
    data4 = [r for r in reader4]   

with open('outdata/ico_data_full_nodup2.csv', 'w') as csvfile_b:
    writer=csv.writer(csvfile_b, delimiter=',')
    
    for i in range(0,np.shape(data3)[0]):
        all_data = [data3[i][0],data3[i][1],data3[i][2],data3[i][3],data3[i][4],data3[i][5],data3[i][6],data3[i][7],data3[i][8],data3[i][9],data3[i][10],data3[i][11],data3[i][12],data3[i][13],data3[i][14],data3[i][15],data3[i][16],data3[i][17],data3[i][18],data3[i][19],data3[i][20],data3[i][21],data3[i][22],data3[i][23],data3[i][24]]
        for j in range(0,np.shape(data1)[0]):
            if data3[i][0] == data1[j][0]:
                all_data = [data1[j][0],data1[j][1],data1[j][2],data1[j][3],data1[j][4],data1[j][5],data1[j][6],data1[j][7],data1[j][8],data1[j][9],data1[j][10],data1[j][11],data1[j][12],data1[j][13],data1[j][14],data1[j][15],data1[j][16],data1[j][17],data1[j][18],data1[j][19],data1[j][20],data1[j][21],data1[j][22],data1[j][23],data1[j][24]]
                
        writer.writerow(all_data)

with open('outdata/ico_data_full_wr_nodup2.csv', 'w') as csvfile_c:
    writer=csv.writer(csvfile_c, delimiter=',')
    
    for i in range(0,np.shape(data4)[0]):
        all_data2 = [data4[i][0],data4[i][1],data4[i][2],data4[i][3],data4[i][4],data4[i][5],data4[i][6],data4[i][7],data4[i][8],data4[i][9],data4[i][10],data4[i][11],data4[i][12],data4[i][13],data4[i][14],data4[i][15],data4[i][17],data4[i][18],data4[i][19],data4[i][20],data4[i][21],data4[i][22],data4[i][23],data4[i][24],data4[i][25],data4[i][26]]
        for j in range(0,np.shape(data2)[0]):
            if data3[i][0] == data2[j][0]:
                all_data2 = [data2[j][0],data2[j][1],data2[j][2],data2[j][3],data2[j][4],data2[j][5],data2[j][6],data2[j][7],data2[j][8],data2[j][9],data2[j][10],data2[j][11],data2[j][12],data2[j][13],data2[j][14],data2[j][15],data2[j][17],data2[j][18],data2[j][19],data2[j][20],data2[j][21],data2[j][22],data2[j][23],data2[j][24],data2[j][25],data2[j][26]]
                
        writer.writerow(all_data2)
