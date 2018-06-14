import csv
import numpy as np
from numpy import *

#This program replaces the NA contents of the ico_data_full.csv file with the contents produced by the re-run of the partial py file

with open("outdata/ico_data_full2.csv") as f1:
    reader1 = csv.reader(f1)
    data1 = [r for r in reader1]
    
with open("outdata/ico_data_full_wr2.csv") as f2:
    reader2 = csv.reader(f2)
    data2 = [r for r in reader2]

with open("outdata/ico_google_new.csv") as f3:
    reader3 = csv.reader(f3)
    data3 = [r for r in reader3]

with open('outdata/ico_data_full3.csv', 'w') as csvfile_b:
    writer=csv.writer(csvfile_b, delimiter=',')
    
    for i in range(0,np.shape(data1)[0]):
        all_data = [data1[i][0],data1[i][1],data1[i][2],data1[i][3],data1[i][4],data1[i][5],data1[i][6],data1[i][7],data1[i][8],data1[i][9],data1[i][10],data1[i][11],data1[i][12],data3[i][1],data1[i][14],data1[i][15],data1[i][16],data1[i][17],data1[i][18],data1[i][19],data1[i][20],data1[i][21],data1[i][22],data1[i][23],data1[i][24]]
                
        writer.writerow(all_data)

with open('outdata/ico_data_full_wr3.csv', 'w') as csvfile_c:
    writer=csv.writer(csvfile_c, delimiter=',')
    
    for i in range(0,np.shape(data2)[0]):
        all_data2 = [data2[i][0],data2[i][1],data2[i][2],data2[i][3],data2[i][4],data2[i][5],data2[i][6],data2[i][7],data2[i][8],data2[i][9],data2[i][10],data2[i][11],data2[i][12],data3[i][1],data2[i][14],data2[i][15],data2[i][16],data2[i][17],data2[i][18],data2[i][19],data2[i][20],data2[i][21],data2[i][22],data2[i][23],data2[i][24],data2[i][25]]
                
        writer.writerow(all_data2)
