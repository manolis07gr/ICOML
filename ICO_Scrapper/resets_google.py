import csv
import numpy as np
from numpy import *

#This program replaces the NA contents of the ico_data_full.csv file with the contents produced by the re-run of the partial py file

with open("outdata/ico_data_full3.csv") as f1:
    reader1 = csv.reader(f1)
    data1 = [r for r in reader1]
    
with open("outdata/ico_data_full_final_hype.csv") as f1b:
    reader1b = csv.reader(f1b)
    data1b = [r for r in reader1b]       

with open("outdata/ico_google_new.csv") as f2:
    reader2 = csv.reader(f2)
    data2 = [r for r in reader2]

with open('outdata/ico_data_full_final_b.csv', 'w') as csvfile_b:
    writer=csv.writer(csvfile_b, delimiter=',')

    for i in range(0,np.shape(data1)[0]):
        all_data = [data1[i][0],data1[i][1],data1[i][2],data1[i][3],data1[i][4],data1[i][5],data1[i][6],data1[i][7],data1[i][8],data1[i][9],data1[i][10],data1[i][11],data1[i][12],data2[i][1],data1[i][14],data1[i][15],data1[i][16],data1[i][17],data1[i][18],data1[i][19],data1[i][20],data1[i][21],data1[i][22],data1[i][23],data1[i][24]]
        writer.writerow(all_data)


with open('outdata/ico_data_full_final_hype_b.csv', 'w') as csvfile_c:
    writer=csv.writer(csvfile_c, delimiter=',')

    for i in range(0,np.shape(data1)[0]):
        #print data1[i][0],data1[i][1],data1[i][2],data1[i][3],data1[i][4],data1[i][5],data1[i][6],data1[i][7],data1[i][8],data1[i][9],data1[i][10],data1[i][11],data1[i][12],data2[i][1],data1[i][14],data1b[i][15],data1[i][16],data1[i][17],data1[i][18],data1[i][19],data1[i][20],data1[i][21],data1[i][22],data1[i][23],data1[i][24]
        all_data2 = [data1[i][0],data1[i][1],data1[i][2],data1[i][3],data1[i][4],data1[i][5],data1[i][6],data1[i][7],data1[i][8],data1[i][9],data1[i][10],data1[i][11],data1[i][12],data2[i][1],data1[i][14],data1b[i][15],data1[i][16],data1[i][17],data1[i][18],data1[i][19],data1[i][20],data1[i][21],data1[i][22],data1[i][23],data1[i][24]]
        writer.writerow(all_data2)
