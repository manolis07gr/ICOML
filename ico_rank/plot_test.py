import numpy as np
from numpy import *
import csv
from matplotlib import pyplot as plt


with open("ico_data_complete.csv") as f:
            reader = csv.reader(f)
            data = [r for r in reader]
	    
data = np.asarray(data)

indices, = np.where(data[:,10] != 'N/A')
indices = np.delete(indices,0)

duration = []
success = []

duration = [eval(data[i][4]) for i in indices]
success = [eval(data[i][10]) for i in indices]

fig, ax = plt.subplots()
plt.xlabel('age')
plt.ylabel('success')
ax.scatter(duration, success, c='k')
plt.show()
