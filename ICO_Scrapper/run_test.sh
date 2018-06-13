python rescan1.py >> nan_coins.txt
python scrap_icos_main_partial1.py
python replaces_nans1.py
python rescan2.py >> nan_coins2.txt
python scrap_icos_main_partial2.py
python replaces_nans2.py

cp outdata/ico_data_full3.csv outdata/ico_data_full_final.csv
python resets_hype.py
python resets_google.py
cp outdata/ico_data_full_final_b.csv outdata/ico_data_full_final.csv
cp outdata/ico_data_full_final_hype_b.csv outdata/ico_data_full_final_hype.csv
python uniform_set_extract.py

#FINAL PRODUCTS: outdata/ico_data_full_final.csv, outdata/ico_data_full_final_hype.csv
# and outdata/ico_data_full_final_hype_uniform.csv
#USE Google open browser tabs to replace new N/A google news results with values
