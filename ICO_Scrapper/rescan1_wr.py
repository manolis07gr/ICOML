import csv
import numpy as np
from numpy import *

#This code produces a list of token names that returned NAN values from the first coinmarketcap run

with open("outdata/ico_data_full_wr.csv") as f1:
    reader1 = csv.reader(f1)
    data1 = [r for r in reader1]

for i in range(1,np.shape(data1)[0]):
    if data1[i][18] == 'N/A':
        print data1[i][0]
