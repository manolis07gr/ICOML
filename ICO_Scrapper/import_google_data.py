import csv
import numpy as np
from numpy import *

with open("outdata/ico_data_full.csv") as f1:
    reader1 = csv.reader(f1)
    data1 = [r for r in reader1]

with open("outdata2/ico_data_full_final.csv") as f2:
#with open("ico_google_new.csv") as f2:
    reader2 = csv.reader(f2)
    data2 = [r for r in reader2]

with open('outdata/ico_google_new.csv', 'w') as csvfile_b:
    writer=csv.writer(csvfile_b, delimiter=',')

    for i in range(0,np.shape(data1)[0]):
        col2 = 'N/A'
        for j in range(0,np.shape(data2)[0]):
            #if data2[j][0].replace(' ','-') == data1[i][0]:
            if data2[j][0] == data1[i][0]:
                col2 = data2[j][13]
	        	#col2 = data2[j][1]

        writer.writerow([data1[i][0],col2])

