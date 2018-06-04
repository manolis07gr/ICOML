import csv
import numpy as np
from numpy import *

#This program replaces the NA contents of the ico_data_full.csv file with the contents produced by the re-run of the partial py file

with open("outdata/ico_data_full2_wr.csv") as f1:
    reader1 = csv.reader(f1)
    data1 = [r for r in reader1]

with open("outdata/ico_data_reduced_nans2_wr.csv") as f2:
    reader2 = csv.reader(f2)
    data2 = [r for r in reader2]

with open('outdata/ico_data_full3_wr.csv', 'w') as csvfile_b:
    writer=csv.writer(csvfile_b, delimiter=',')

    for i in range(0,np.shape(data1)[0]):
        all_data = [data1[i][0],data1[i][1],data1[i][2],data1[i][3],data1[i][4],data1[i][5],data1[i][6],data1[i][7],data1[i][8],data1[i][9],data1[i][10],data1[i][11],data1[i][12],data1[i][13],data1[i][14],data1[i][15],data1[i][16],data1[i][17],data1[i][18],data1[i][19],data1[i][20],data1[i][21],data1[i][22],data1[i][23],data1[i][24]]
        for j in range(0,np.shape(data2)[0]):
                if data2[j][0].replace('-',' ') == data1[i][0]:
                        all_data = [data2[j][0],data2[j][1],data2[j][2],data2[j][3],data2[j][4],data2[j][5],data2[j][6],data2[j][7],data2[j][8],data2[j][9],data2[j][10],data2[j][11],data2[j][12],data2[j][13],data2[j][14],data2[j][15],data2[j][16],data2[j][17],data2[j][18],data2[j][19],data2[j][20],data2[j][21],data2[j][22],data2[j][23],data1[j][24]]

        writer.writerow(all_data)

