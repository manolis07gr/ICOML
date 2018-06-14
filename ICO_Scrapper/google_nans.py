import csv
import numpy as np
from numpy import *

#This code produces a list of token names that returned NAN values from the first coinmarketcap run

with open("outdata/ico_data_full_final.csv") as f1:
    reader1 = csv.reader(f1)
    data1 = [r for r in reader1]

with open('outdata/nan_google.csv', 'w') as csvfile_b:
    writer=csv.writer(csvfile_b, delimiter=',')

    for i in range(1,np.shape(data1)[0]):
        if data1[i][13] == 'N/A' and data1[i][2] != 'N/A':
            all_data = [data1[i][0],data1[i][1],data1[i][2]]
            writer.writerow(all_data)

