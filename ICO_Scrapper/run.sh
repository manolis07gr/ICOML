#First run main program producing 'full','reduced' and 'reduced_w_ratings' outputs
python scrap_icos_main_full.py
###python scrap_icos_main.py

#Secondly run program that removes data that lack date/duration ICO information and replace N/A from coinmarketcap
#with appropriate values for sharpe, beta, alpha, day 1 return and day 1 volume.
python reduce_na.py

#Finally attach icodesk start date, end date, duration and age for ICO data not available on coinmarketcap
#for failed ICOs
python coindesk_na.py
cat outdata/coindesk_na_data.csv >> outdata/ico_data_reduced_noNA.csv
mv outdata/ico_data_reduced_noNA.csv outdata/ico_data_full.csv

#Repeat second and third steps for 'wratings' category
python reduce_na_wratings.py
cat outdata/coindesk_na_wr_data.csv >> outdata/ico_data_reduced_wr_noNA.csv
mv outdata/ico_data_reduced_wr_noNa.csv outdata/ico_data_full_wr.csv

#in the end need to run google_search.py to add Google news data
#this is because Google restricts search bots to 50 searches an hour per IP
#python google_news.py
