import urllib2
import re
import numpy as np
from numpy import *

#Inputs: currency name, export to file option and today's date
###
currency = 'crypterium'   # name of cryptocurrency as in Coinmarketcap.com
export = True          # Export time-series data to file? If so exports data number, date, open price, high price, low price, close price
today = '20180327'      # Today's day or end date for the analysis/export of price data
###

#Downloading Coinmarketcap.com data
data = urllib2.urlopen('https://coinmarketcap.com/currencies/'+currency+'/historical-data/?start=20130428&end='+today)

i = -1
time_array = []
r1=[]
r2=[]

#Reading URL data and fixing alignment issues
for line in data: # files are iterable

	line = line.replace(" <td data-format-fiat data-format","<td data-format-fiat data-format")
	line = line.replace("  <td data-format-fiat data-format","<td data-format-fiat data-format")
	line = line.replace("   <td data-format-fiat data-format","<td data-format-fiat data-format")
	line = line.replace(" <td data-format-market-cap data-format-value","<td data-format-market-cap data-format-value")
	line = line.replace("  <td data-format-market-cap data-format-value","<td data-format-market-cap data-format-value")
	line = line.replace("   <td data-format-market-cap data-format-value","<td data-format-market-cap data-format-value")
	line = line.replace('">','0000000">')
	
	#print line

	if '<td class="text-left' in line:
		i = i + 1	
		time_array.append(i)
		time_array[i] = line[29:41]
		
		
	if ('<td data-format-fiat data-format') in line:  # Or whatever test is needed
		r1.append(line.split('\n'))
		#print line
		
	if ('<td data-format-market-cap data-format-value') in line:  # Or whatever test is needed
		line = line.replace(',','')
		r2.append(line.split('\n'))
		#print line
				
time_array = time_array[::-1]
timesteps = len(time_array)
data_size = 4
data_size2 = 2
	
### Structuring the prices array		
rr = []
for i in range(0,len(r1)):
	rr.append(i)
	rr[i] = r1[i][0][40:45]
	#print rr[i]
	
	
r = [0 for y in range(timesteps)] 

for i in range(0,timesteps):
	k_low = k_low = 4*i
	k_high = k_high = data_size+4*i
	for j in range(0,data_size):
		r[i] = rr[k_low:k_high]
		#print i,k_low,k_high,r[i]


for i in range(0,timesteps):
	for j in range(0,data_size):
		r[i][j] = round(eval(r[i][j]),2)

r = r[::-1]

### Structuring the Volume and Market Cap array
rr2 = []
for i in range(0,len(r2)):
	rr2.append(i)
	rr2[i] = r2[i][0][46:59]
	#print rr2[i]
	
	
r2 = [0 for y in range(timesteps)] 

for i in range(0,timesteps):
	j_low = j_low = 2*i
	j_high = j_high = data_size2+2*i
	for j in range(0,data_size2):
		r2[i] = rr2[j_low:j_high]
		#print i,j_low,j_high,r2[i]


for i in range(0,timesteps):
	for j in range(0,data_size2):
		if '>-<' in r2[i][j]:
			r2[i][j] = '0.00'
		r2[i][j] = round(eval(r2[i][j]),2)

r2 = r2[::-1]


#print time_array[8],r[8][:]
#Above print displays time (date) and open, high, low close values in USD
#Array r now contains the daily open, high, low and close values for the cryptocurrency for each time data point
#following code saves output to file
if export:
	with open('series_'+currency+'.dat','w') as f1:
		for i in range(0,len(time_array)):
			print >> f1, i,time_array[i],r[i][0],r[i][1],r[i][2],r[i][3],r2[i][0],r2[i][1]
		
		
		
		
		
		
		
