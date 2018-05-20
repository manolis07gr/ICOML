import csv
import numpy as np
from numpy import *

with open("outdata/ico_data_reduced_wratings.csv") as f:
    reader = csv.reader(f)
    data = [r for r in reader]

with open('outdata/ico_data_reduced_wr_noNA.csv', 'w') as csvfile_b:
    writer=csv.writer(csvfile_b, delimiter=',')
    

    for i in range(0,np.shape(data)[0]):
        if (data[i][1] != 'N/A') and (data[i][15] != 'N/A'):
            if (data[i][17] == 'N/A'):
                (data[i][17],data[i][18],data[i][19],data[i][20],data[i][21],data[i][22],data[i][23],data[i][24],data[i][25],data[i][26]) = (-1.0,0.0,-100.,-100.,-100.,-100,-100.,-100.,-100.,-100.)
            writer.writerow([data[i][0],data[i][1],data[i][2],data[i][3],data[i][4],data[i][5],data[i][6],data[i][7],data[i][8],data[i][9],data[i][10],data[i][11],data[i][12],data[i][13],data[i][14],data[i][15],data[i][16],data[i][17],data[i][18],data[i][19],data[i][20],data[i][21],data[i][22],data[i][23],data[i][24],data[i][25],data[i][26]])
            continue

