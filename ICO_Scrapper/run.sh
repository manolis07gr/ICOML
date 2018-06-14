#Copy outdata to outdata2 folder to use import_google_data.py to get google news
#N/A are the ones that will have to be done manually
rm -rf outdata2
cp -r outdata outdata2
rm outdata/*

#First run main program producing 'full','reduced' and 'reduced_w_ratings' outputs
python scrap_icos_main_full.py
###python scrap_icos_main.py to run for a single ICO

#Secondly run program that removes data that lack date/duration ICO information and replace N/A from coinmarketcap
#with appropriate values for sharpe, beta, alpha, day 1 return and day 1 volume.
python reduce_na.py
python reduce_na_wratings.py

#Finally attach icodesk start date, end date, duration and age for ICO data not available on coinmarketcap
#for failed ICOs
python coindesk_na.py

cat outdata/coindesk_na_data.csv >> outdata/ico_data_reduced_noNA.csv
mv outdata/ico_data_reduced_noNA.csv outdata/ico_data_full.csv
#Repeat second and third steps for 'wratings' category
cat outdata/coindesk_na_wr_data.csv >> outdata/ico_data_reduced_wr_noNA.csv
mv outdata/ico_data_reduced_wr_noNa.csv outdata/ico_data_full_wr.csv

#THAT IS MAIN PART OF THE RUN NOW WE NEED TO RE-INSTERT GOOG RESULTS AND CHECK COMPLETENESS
#PRODUCES: ico_data_full.csv and ico_data_full_wr.csv

#Remove Duplicates
awk -F',' '!seen[$1]++' outdata/ico_data_full.csv > outdata/ico_data_full_nodup.csv
awk -F',' '!seen[$1]++' outdata/ico_data_full_wr.csv > outdata/ico_data_full_wr_nodup.csv

python rescan.py > nan_coins.txt
python scrap_icos_main_partial.py
python reset_na_vals.py
python reset_na_vals2.py
cp outdata/ico_data_full_nodup3.csv outdata/ico_data_full2.csv
cp outdata/ico_data_full_wr_nodup3.csv outdata/ico_data_full_wr2.csv

#Import Google News data from previous run
python import_google_data.py
python reset_google_vals.py
cp outdata/ico_data_full3.csv outdata/ico_data_full_final.csv
cp outdata/ico_data_full_wr3.csv outdata/ico_data_full_final_hype.csv 
python uniform_set_extract.py

python google_nans.py
python open_google_news.py

#FINAL PRODUCTS: outdata/ico_data_full_final.csv, outdata/ico_data_full_final_hype.csv
# and outdata/ico_data_full_final_hype_uniform.csv
#USE Google open browser tabs to replace new N/A google news results with values
