import csv
import numpy as np
from numpy import *

#This program replaces the NA contents of the ico_data_full.csv file with the contents produced by the re-run of the partial py file
    
with open("outdata/ico_data_full_final_hype.csv") as f1:
    reader1 = csv.reader(f1)
    data1 = [r for r in reader1]       

with open('outdata/ico_data_full_final_hype_uniform.csv', 'w') as csvfile_b:
    writer=csv.writer(csvfile_b, delimiter=',')

    for i in range(0,np.shape(data1)[0]):
        if 'N/A' not in data1[i][:]:
            all_data = [data1[i][0],data1[i][1],data1[i][2],data1[i][3],data1[i][4],data1[i][5],data1[i][6],data1[i][7],data1[i][8],data1[i][9],data1[i][10],data1[i][11],data1[i][12],data1[i][13],data1[i][14],data1[i][15],data1[i][16],data1[i][17],data1[i][18],data1[i][19],data1[i][20],data1[i][21],data1[i][22],data1[i][23],data1[i][24],data1[i][25]]
            writer.writerow(all_data)
