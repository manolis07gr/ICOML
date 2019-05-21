import csv
from csv import *
from numpy import *
import numpy as np
import sys
from matplotlib import pyplot as plt
import matplotlib.cm as cm
import datetime as dt
from datetime import datetime

#Define quarter start/end dates from 2016 through 2019
[y2016_q1_s,y2016_q1_e,y2016_q2_s,y2016_q2_e,y2016_q3_s,y2016_q3_e,y2016_q4_s,y2016_q4_e] = ['01Jan2016','31Mar2016','01Apr2016','30Jun2016','01Jul2016','30Sep2016','01Oct2016','31Dec2016']

[y2016_q1_s_o,y2016_q1_e_o,y2016_q2_s_o,y2016_q2_e_o,y2016_q3_s_o,y2016_q3_e_o,y2016_q4_s_o,y2016_q4_e_o] = [datetime.strptime(y2016_q1_s, '%d%b%Y'),datetime.strptime(y2016_q1_e, '%d%b%Y'),datetime.strptime(y2016_q2_s, '%d%b%Y'),datetime.strptime(y2016_q2_e, '%d%b%Y'),datetime.strptime(y2016_q3_s, '%d%b%Y'),datetime.strptime(y2016_q3_e, '%d%b%Y'),datetime.strptime(y2016_q4_s, '%d%b%Y'),datetime.strptime(y2016_q4_e, '%d%b%Y')]

y2016 = np.asarray([y2016_q1_s_o,y2016_q1_e_o,y2016_q2_s_o,y2016_q2_e_o,y2016_q3_s_o,y2016_q3_e_o,y2016_q4_s_o,y2016_q4_e_o])

[y2017_q1_s,y2017_q1_e,y2017_q2_s,y2017_q2_e,y2017_q3_s,y2017_q3_e,y2017_q4_s,y2017_q4_e] = ['01Jan2017','31Mar2017','01Apr2017','30Jun2017','01Jul2017','30Sep2017','01Oct2017','31Dec2017']

[y2017_q1_s_o,y2017_q1_e_o,y2017_q2_s_o,y2017_q2_e_o,y2017_q3_s_o,y2017_q3_e_o,y2017_q4_s_o,y2017_q4_e_o] = [datetime.strptime(y2017_q1_s, '%d%b%Y'),datetime.strptime(y2017_q1_e, '%d%b%Y'),datetime.strptime(y2017_q2_s, '%d%b%Y'),datetime.strptime(y2017_q2_e, '%d%b%Y'),datetime.strptime(y2017_q3_s, '%d%b%Y'),datetime.strptime(y2017_q3_e, '%d%b%Y'),datetime.strptime(y2017_q4_s, '%d%b%Y'),datetime.strptime(y2017_q4_e, '%d%b%Y')]

y2017 = np.asarray([y2017_q1_s_o,y2017_q1_e_o,y2017_q2_s_o,y2017_q2_e_o,y2017_q3_s_o,y2017_q3_e_o,y2017_q4_s_o,y2017_q4_e_o])

[y2018_q1_s,y2018_q1_e,y2018_q2_s,y2018_q2_e,y2018_q3_s,y2018_q3_e,y2018_q4_s,y2018_q4_e] = ['01Jan2018','31Mar2018','01Apr2018','30Jun2018','01Jul2018','30Sep2018','01Oct2018','31Dec2018']

[y2018_q1_s_o,y2018_q1_e_o,y2018_q2_s_o,y2018_q2_e_o,y2018_q3_s_o,y2018_q3_e_o,y2018_q4_s_o,y2018_q4_e_o] = [datetime.strptime(y2018_q1_s, '%d%b%Y'),datetime.strptime(y2018_q1_e, '%d%b%Y'),datetime.strptime(y2018_q2_s, '%d%b%Y'),datetime.strptime(y2018_q2_e, '%d%b%Y'),datetime.strptime(y2018_q3_s, '%d%b%Y'),datetime.strptime(y2018_q3_e, '%d%b%Y'),datetime.strptime(y2018_q4_s, '%d%b%Y'),datetime.strptime(y2018_q4_e, '%d%b%Y')]

y2018 = np.asarray([y2018_q1_s_o,y2018_q1_e_o,y2018_q2_s_o,y2018_q2_e_o,y2018_q3_s_o,y2018_q3_e_o,y2018_q4_s_o,y2018_q4_e_o])

[y2019_q1_s,y2019_q1_e,y2019_q2_s,y2019_q2_e,y2019_q3_s,y2019_q3_e,y2019_q4_s,y2019_q4_e] = ['01Jan2019','31Mar2019','01Apr2019','30Jun2019','01Jul2019','30Sep2019','01Oct2019','31Dec2019']

[y2019_q1_s_o,y2019_q1_e_o,y2019_q2_s_o,y2019_q2_e_o,y2019_q3_s_o,y2019_q3_e_o,y2019_q4_s_o,y2019_q4_e_o] = [datetime.strptime(y2019_q1_s, '%d%b%Y'),datetime.strptime(y2019_q1_e, '%d%b%Y'),datetime.strptime(y2019_q2_s, '%d%b%Y'),datetime.strptime(y2019_q2_e, '%d%b%Y'),datetime.strptime(y2019_q3_s, '%d%b%Y'),datetime.strptime(y2019_q3_e, '%d%b%Y'),datetime.strptime(y2019_q4_s, '%d%b%Y'),datetime.strptime(y2019_q4_e, '%d%b%Y')]

y2019 = np.asarray([y2019_q1_s_o,y2019_q1_e_o,y2019_q2_s_o,y2019_q2_e_o,y2019_q3_s_o,y2019_q3_e_o,y2019_q4_s_o,y2019_q4_e_o])

######

with open("outdata/ico_data_reduced.csv") as f:
            reader = csv.reader(f)
            data = [r for r in reader]

ico_q = []
ico_q_s = []
k = -1

for m in range(0,len(data)):
    k = k + 1
    
    ico_q.append(k)
    ico_q_s.append(k)
    
    if m == 0:
        a = 'ICO Quarter #'
        b = 'ICO Quarter'
        ico_year = 'ICO year'

    if m != 0:
        ico_end = data[m][2].replace(" ","")
        ico_end_o = datetime.strptime(ico_end, '%d%b%Y')
        ico_year = ico_end_o.year

        if ico_year == 2016:
            quarters = y2016
            for i in range(0,len(quarters)-1):
                if quarters[i] <= ico_end_o < quarters[i+1]:
                    q_start = quarters[i]
                    q_start_index = i
                    q_end = quarters[i+1]
                    q_end_index = i+1

            if (q_start_index) == 0:
                a =1
                b ='2016 Q1'
            if (q_start_index) == 2:
                a =2
                b ='2016 Q2'
            if (q_start_index) == 4:
                q =3
                b ='2016 Q3'
            if (q_start_index) == 6:
                a =4
                b ='2016 Q4'

        if ico_year == 2017:
            quarters = y2017
            for i in range(0,len(quarters)-1):
                if quarters[i] <= ico_end_o < quarters[i+1]:
                    q_start = quarters[i]
                    q_start_index = i
                    q_end = quarters[i+1]
                    q_end_index = i+1

            if (q_start_index) == 0:
                a =5
                b ='2017 Q1'
            if (q_start_index) == 2:
                a =6
                b ='2017 Q2'
            if (q_start_index) == 4:
                q =7
                b ='2017 Q3'
            if (q_start_index) == 6:
                a =8
                b ='2017 Q4'
    
        if ico_year == 2018:
            quarters = y2018
            for i in range(0,len(quarters)-1):
                if quarters[i] <= ico_end_o < quarters[i+1]:
                    q_start = quarters[i]
                    q_start_index = i
                    q_end = quarters[i+1]
                    q_end_index = i+1

            if (q_start_index) == 0:
                a = 9
                b ='2018 Q1'
            if (q_start_index) == 2:
                a =10
                b ='2018 Q2'
            if (q_start_index) == 4:
                q =11
                b ='2018 Q3'
            if (q_start_index) == 6:
                a =12
                b ='2018 Q4'

        if ico_year == 2019:
            quarters = y2019
            for i in range(0,len(quarters)-1):
                if quarters[i] <= ico_end_o < quarters[i+1]:
                    q_start = quarters[i]
                    q_start_index = i
                    q_end = quarters[i+1]
                    q_end_index = i+1

            if (q_start_index) == 0:
                a =13
                b ='2019 Q1'
            if (q_start_index) == 2:
                a =14
                b ='2019 Q2'
            if (q_start_index) == 4:
                q =15
                b ='2019 Q3'
            if (q_start_index) == 6:
                a =16
                b ='2019 Q4'              

    ico_q[k] = a
    ico_q_s[k] = b

    #print(m,ico_year,ico_q[k],ico_q_s[k])
    
#ICO Country/Region counts initilization
[q1_na,q1_rs,q1_as,q1_uk,q1_eu,q1_sw,q1_th,q1_jk,q1_au,q1_sa,q1_af] = [0,0,0,0,0,0,0,0,0,0,0]
[q2_na,q2_rs,q2_as,q2_uk,q2_eu,q2_sw,q2_th,q2_jk,q2_au,q2_sa,q2_af] = [0,0,0,0,0,0,0,0,0,0,0]
[q3_na,q3_rs,q3_as,q3_uk,q3_eu,q3_sw,q3_th,q3_jk,q3_au,q3_sa,q3_af] = [0,0,0,0,0,0,0,0,0,0,0]
[q4_na,q4_rs,q4_as,q4_uk,q4_eu,q4_sw,q4_th,q4_jk,q4_au,q4_sa,q4_af] = [0,0,0,0,0,0,0,0,0,0,0]
[q5_na,q5_rs,q5_as,q5_uk,q5_eu,q5_sw,q5_th,q5_jk,q5_au,q5_sa,q5_af] = [0,0,0,0,0,0,0,0,0,0,0]
[q6_na,q6_rs,q6_as,q6_uk,q6_eu,q6_sw,q6_th,q6_jk,q6_au,q6_sa,q6_af] = [0,0,0,0,0,0,0,0,0,0,0]
[q7_na,q7_rs,q7_as,q7_uk,q7_eu,q7_sw,q7_th,q7_jk,q7_au,q7_sa,q7_af] = [0,0,0,0,0,0,0,0,0,0,0]
[q8_na,q8_rs,q8_as,q8_uk,q8_eu,q8_sw,q8_th,q8_jk,q8_au,q8_sa,q8_af] = [0,0,0,0,0,0,0,0,0,0,0]
[q9_na,q9_rs,q9_as,q9_uk,q9_eu,q9_sw,q9_th,q9_jk,q9_au,q9_sa,q9_af] = [0,0,0,0,0,0,0,0,0,0,0]
[q10_na,q10_rs,q10_as,q10_uk,q10_eu,q10_sw,q10_th,q10_jk,q10_au,q10_sa,q10_af] = [0,0,0,0,0,0,0,0,0,0,0]
[q11_na,q11_rs,q11_as,q11_uk,q11_eu,q11_sw,q11_th,q11_jk,q11_au,q11_sa,q11_af] = [0,0,0,0,0,0,0,0,0,0,0]
[q12_na,q12_rs,q12_as,q12_uk,q12_eu,q12_sw,q12_th,q12_jk,q12_au,q12_sa,q12_af] = [0,0,0,0,0,0,0,0,0,0,0]
[q13_na,q13_rs,q13_as,q13_uk,q13_eu,q13_sw,q13_th,q13_jk,q13_au,q13_sa,q13_af] = [0,0,0,0,0,0,0,0,0,0,0]
[q14_na,q14_rs,q14_as,q14_uk,q14_eu,q14_sw,q14_th,q14_jk,q14_au,q14_sa,q14_af] = [0,0,0,0,0,0,0,0,0,0,0]
[q15_na,q15_rs,q15_as,q15_uk,q15_eu,q15_sw,q15_th,q15_jk,q15_au,q15_sa,q15_af] = [0,0,0,0,0,0,0,0,0,0,0]
[q16_na,q16_rs,q16_as,q16_uk,q16_eu,q16_sw,q16_th,q16_jk,q16_au,q16_sa,q16_af] = [0,0,0,0,0,0,0,0,0,0,0]
#ICO Industry counts initilization
[q1_fin,q1_blk,q1_re,q1_ss,q1_ent,q1_gam,q1_gmb,q1_eco,q1_sas,q1_trs,q1_law,q1_ins,q1_tel,q1_ener] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0]
[q2_fin,q2_blk,q2_re,q2_ss,q2_ent,q2_gam,q2_gmb,q2_eco,q2_sas,q2_trs,q2_law,q2_ins,q2_tel,q2_ener] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0]
[q3_fin,q3_blk,q3_re,q3_ss,q3_ent,q3_gam,q3_gmb,q3_eco,q3_sas,q3_trs,q3_law,q3_ins,q3_tel,q3_ener] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0]
[q4_fin,q4_blk,q4_re,q4_ss,q4_ent,q4_gam,q4_gmb,q4_eco,q4_sas,q4_trs,q4_law,q4_ins,q4_tel,q4_ener] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0]
[q5_fin,q5_blk,q5_re,q5_ss,q5_ent,q5_gam,q5_gmb,q5_eco,q5_sas,q5_trs,q5_law,q5_ins,q5_tel,q5_ener] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0]
[q6_fin,q6_blk,q6_re,q6_ss,q6_ent,q6_gam,q6_gmb,q6_eco,q6_sas,q6_trs,q6_law,q6_ins,q6_tel,q6_ener] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0]
[q7_fin,q7_blk,q7_re,q7_ss,q7_ent,q7_gam,q7_gmb,q7_eco,q7_sas,q7_trs,q7_law,q7_ins,q7_tel,q7_ener] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0]
[q8_fin,q8_blk,q8_re,q8_ss,q8_ent,q8_gam,q8_gmb,q8_eco,q8_sas,q8_trs,q8_law,q8_ins,q8_tel,q8_ener] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0]
[q9_fin,q9_blk,q9_re,q9_ss,q9_ent,q9_gam,q9_gmb,q9_eco,q9_sas,q9_trs,q9_law,q9_ins,q9_tel,q9_ener] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0]
[q10_fin,q10_blk,q10_re,q10_ss,q10_ent,q10_gam,q10_gmb,q10_eco,q10_sas,q10_trs,q10_law,q10_ins,q10_tel,q10_ener] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0]
[q11_fin,q11_blk,q11_re,q11_ss,q11_ent,q11_gam,q11_gmb,q11_eco,q11_sas,q11_trs,q11_law,q11_ins,q11_tel,q11_ener] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0]
[q12_fin,q12_blk,q12_re,q12_ss,q12_ent,q12_gam,q12_gmb,q12_eco,q12_sas,q12_trs,q12_law,q12_ins,q12_tel,q12_ener] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0]
[q13_fin,q13_blk,q13_re,q13_ss,q13_ent,q13_gam,q13_gmb,q13_eco,q13_sas,q13_trs,q13_law,q13_ins,q13_tel,q13_ener] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0]
[q14_fin,q14_blk,q14_re,q14_ss,q14_ent,q14_gam,q14_gmb,q14_eco,q14_sas,q14_trs,q14_law,q14_ins,q14_tel,q14_ener] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0]
[q15_fin,q15_blk,q15_re,q15_ss,q15_ent,q15_gam,q15_gmb,q15_eco,q15_sas,q15_trs,q15_law,q15_ins,q15_tel,q15_ener] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0]
[q16_fin,q16_blk,q16_re,q16_ss,q16_ent,q16_gam,q16_gmb,q16_eco,q16_sas,q16_trs,q16_law,q16_ins,q16_tel,q16_ener] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0]
#ICO daily views and indices per Quarter
[i1,i2,i3,i4,i5,i6,i7,i8,i9,i10,i11,i12,i13,i14,i15,i16] = [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]
[dv1,dv2,dv3,dv4,dv5,dv6,dv7,dv8,dv9,dv10,dv11,dv12,dv13,dv14,dv15,dv16] = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
#ICO Day 1 Return indices per Quarter
[j1,j2,j3,j4,j5,j6,j7,j8,j9,j10,j11,j12,j13,j14,j15,j16] = [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]
[ret1,ret2,ret3,ret4,ret5,ret6,ret7,ret8,ret9,ret10,ret11,ret12,ret13,ret14,ret15,ret16] = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
#ICO Annualized Sharpe Ratio indices per Quarter
[g1,g2,g3,g4,g5,g6,g7,g8,g9,g10,g11,g12,g13,g14,g15,g16] = [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]
[srp1,srp2,srp3,srp4,srp5,srp6,srp7,srp8,srp9,srp10,srp11,srp12,srp13,srp14,srp15,srp16] = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
#ICO Day 1 Volume indices per Quarter
[o1,o2,o3,o4,o5,o6,o7,o8,o9,o10,o11,o12,o13,o14,o15,o16] = [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]
[vol1,vol2,vol3,vol4,vol5,vol6,vol7,vol8,vol9,vol10,vol11,vol12,vol13,vol14,vol15,vol16] = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
#ICO token price arrays and indices per Quarter
[l1,l2,l3,l4,l5,l6,l7,l8,l9,l10,l11,l12,l13,l14,l15,l16] = [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]
[pr1,pr2,pr3,pr4,pr5,pr6,pr7,pr8,pr9,pr10,pr11,pr12,pr13,pr14,pr15,pr16] = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
#Twitter arrays and indices per Quarter
[k1,k2,k3,k4,k5,k6,k7,k8,k9,k10,k11,k12,k13,k14,k15,k16] = [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]
[tw1,tw2,tw3,tw4,tw5,tw6,tw7,tw8,tw9,tw10,tw11,tw12,tw13,tw14,tw15,tw16] = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
#Telegram arrays and indices per Quarter
[m1,m2,m3,m4,m5,m6,m7,m8,m9,m10,m11,m12,m13,m14,m15,m16] = [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]
[tg1,tg2,tg3,tg4,tg5,tg6,tg7,tg8,tg9,tg10,tg11,tg12,tg13,tg14,tg15,tg16] = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
#Successful ICOs per Quarter
[s1,s2,s3,s4,s5,s6,s7,s8,s9,s10,s11,s12,s13,s14,s15,s16] = [0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.]
#Number of ICOs per Quarter
[q1n,q2n,q3n,q4n,q5n,q6n,q7n,q8n,q9n,q10n,q11n,q12n,q13n,q14n,q15n,q16n] = [0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.]
#Cumulative funds raised by ICOs per Quarter
[cum_funds_1,cum_funds_2,cum_funds_3,cum_funds_4,cum_funds_5,cum_funds_6,cum_funds_7,cum_funds_8,cum_funds_9,cum_funds_10,cum_funds_11,cum_funds_12,cum_funds_13,cum_funds_14,cum_funds_15,cum_funds_16] = [0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.]
for i in range(1,len(data)):
    if ico_q[i] == 1:
        q1n = q1n + 1
    if ico_q[i] == 2:
        q2n = q2n + 1
    if ico_q[i] == 3:
        q3n = q3n + 1
    if ico_q[i] == 4:
        q4n = q4n + 1
    if ico_q[i] == 5:
        q5n = q5n + 1
    if ico_q[i] == 6:
        q6n = q6n + 1
    if ico_q[i] == 7:
        q7n = q7n + 1
    if ico_q[i] == 8:
        q8n = q8n + 1
    if ico_q[i] == 9:
        q9n = q9n + 1
    if ico_q[i] == 10:
        q10n = q10n + 1
    if ico_q[i] == 11:
        q11n = q11n + 1
    if ico_q[i] == 12:
        q12n = q12n + 1
    if ico_q[i] == 13:
        q13n = q13n + 1
    if ico_q[i] == 14:
        q14n = q14n + 1
    if ico_q[i] == 15:
        q15n = q15n + 1
    if ico_q[i] == 16:
        q16n = q16n + 1
    
    #Based on funds raised
    if data[i][8] != 'N/A':
        if ico_q[i] == 1:
            cum_funds_1 = cum_funds_1 + eval(data[i][8])
        if ico_q[i] == 2:
            cum_funds_2 = cum_funds_2 + eval(data[i][8])
        if ico_q[i] == 3:
            cum_funds_3 = cum_funds_3 + eval(data[i][8])
        if ico_q[i] == 4:
            cum_funds_4 = cum_funds_4 + eval(data[i][8])
        if ico_q[i] == 5:
            cum_funds_5 = cum_funds_5 + eval(data[i][8])
        if ico_q[i] == 6:
            cum_funds_6 = cum_funds_6 + eval(data[i][8])
        if ico_q[i] == 7:
            cum_funds_7 = cum_funds_7 + eval(data[i][8])
        if ico_q[i] == 8:
            cum_funds_8 = cum_funds_8 + eval(data[i][8])
        if ico_q[i] == 9:
            cum_funds_9 = cum_funds_9 + eval(data[i][8])
        if ico_q[i] == 10:
            cum_funds_10 = cum_funds_10 + eval(data[i][8])
        if ico_q[i] == 11:
            cum_funds_11 = cum_funds_11 + eval(data[i][8])
        if ico_q[i] == 12:
            cum_funds_12 = cum_funds_12 + eval(data[i][8])
        if ico_q[i] == 13:
            cum_funds_13 = cum_funds_13 + eval(data[i][8])
        if ico_q[i] == 14:
            cum_funds_14 = cum_funds_14 + eval(data[i][8])
        if ico_q[i] == 15:
            cum_funds_15 = cum_funds_15 + eval(data[i][8])
        if ico_q[i] == 16:
            cum_funds_16 = cum_funds_16 + eval(data[i][8])

    #Based on success
    if data[i][10] != 'N/A' and eval(data[i][10]) >= 0.9:
        if ico_q[i] == 1:
            s1 = s1 + 1
        if ico_q[i] == 2:
            s2 = s2 + 1
        if ico_q[i] == 3:
            s3 = s3 + 1
        if ico_q[i] == 4:
            s4 = s4 + 1
        if ico_q[i] == 5:
            s5 = s5 + 1
        if ico_q[i] == 6:
            s6 = s6 + 1
        if ico_q[i] == 7:
            s7 = s7 + 1
        if ico_q[i] == 8:
            s8 = s8 + 1
        if ico_q[i] == 9:
            s9 = s9 + 1
        if ico_q[i] == 10:
            s10 = s10 + 1
        if ico_q[i] == 11:
            s11 = s11 + 1
        if ico_q[i] == 12:
            s12 = s12 + 1
        if ico_q[i] == 13:
            s13 = s13 + 1
        if ico_q[i] == 14:
            s14 = s14 + 1
        if ico_q[i] == 15:
            s15 = s15 + 1
        if ico_q[i] == 16:
            s16 = s16 + 1

    #Based on Telegram Following
    if data[i][12] != 'N/A':
        if ico_q[i] == 1:
            m1 = m1 + 1
            tg1.append(m1)
            tg1[m1] = eval(data[i][12])
        if ico_q[i] == 2:
            m2 = m2 + 1
            tg2.append(m2)
            tg2[m2] = eval(data[i][12])
        if ico_q[i] == 3:
            m3 = m3 + 1
            tg3.append(m3)
            tg3[m3] = eval(data[i][12])
        if ico_q[i] == 4:
            m4 = m4 + 1
            tg4.append(m4)
            tg4[m4] = eval(data[i][12])
        if ico_q[i] == 5:
            m5 = m5 + 1
            tg5.append(m5)
            tg5[m5] = eval(data[i][12])
        if ico_q[i] == 6:
            m6 = m6 + 1
            tg6.append(m6)
            tg6[m6] = eval(data[i][12])
        if ico_q[i] == 7:
            m7 = m7 + 1
            tg7.append(m7)
            tg7[m7] = eval(data[i][12])
        if ico_q[i] == 8:
            m8 = m8 + 1
            tg8.append(m8)
            tg8[m8] = eval(data[i][12])
        if ico_q[i] == 9:
            m9 = m9 + 1
            tg9.append(m9)
            tg9[m9] = eval(data[i][12])
        if ico_q[i] == 10:
            m10 = m10 + 1
            tg10.append(m10)
            tg10[m10] = eval(data[i][12])
        if ico_q[i] == 11:
            m11 = m11 + 1
            tg11.append(m11)
            tg11[m11] = eval(data[i][12])
        if ico_q[i] == 12:
            m12 = m12 + 1
            tg12.append(m12)
            tg12[m12] = eval(data[i][12])
        if ico_q[i] == 13:
            m13 = m13 + 1
            tg13.append(m13)
            tg13[m13] = eval(data[i][12])
        if ico_q[i] == 14:
            m14 = m14 + 1
            tg14.append(m14)
            tg14[m14] = eval(data[i][12])
        if ico_q[i] == 15:
            m15 = m15 + 1
            tg15.append(m15)
            tg15[m15] = eval(data[i][12])
        if ico_q[i] == 16:
            m16 = m16 + 1
            tg16.append(m16)
            tg16[m16] = eval(data[i][12])

    #Based on Twitter Following
    if data[i][14] != 'N/A':
        if ico_q[i] == 1:
            k1 = k1 + 1
            tw1.append(k1)
            tw1[k1] = eval(data[i][14])
        if ico_q[i] == 2:
            k2 = k2 + 1
            tw2.append(k2)
            tw2[k2] = eval(data[i][14])
        if ico_q[i] == 3:
            k3 = k3 + 1
            tw3.append(k3)
            tw3[k3] = eval(data[i][14])
        if ico_q[i] == 4:
            k4 = k4 + 1
            tw4.append(k4)
            tw4[k4] = eval(data[i][14])
        if ico_q[i] == 5:
            k5 = k5 + 1
            tw5.append(k5)
            tw5[k5] = eval(data[i][14])
        if ico_q[i] == 6:
            k6 = k6 + 1
            tw6.append(k6)
            tw6[k6] = eval(data[i][14])
        if ico_q[i] == 7:
            k7 = k7 + 1
            tw7.append(k7)
            tw7[k7] = eval(data[i][14])
        if ico_q[i] == 8:
            k8 = k8 + 1
            tw8.append(k8)
            tw8[k8] = eval(data[i][14])
        if ico_q[i] == 9:
            k9 = k9 + 1
            tw9.append(k9)
            tw9[k9] = eval(data[i][14])
        if ico_q[i] == 10:
            k10 = k10 + 1
            tw10.append(k10)
            tw10[k10] = eval(data[i][14])
        if ico_q[i] == 11:
            k11 = k11 + 1
            tw11.append(k11)
            tw11[k11] = eval(data[i][14])
        if ico_q[i] == 12:
            k12 = k12 + 1
            tw12.append(k12)
            tw12[k12] = eval(data[i][14])
        if ico_q[i] == 13:
            k13 = k13 + 1
            tw13.append(k13)
            tw13[k13] = eval(data[i][14])
        if ico_q[i] == 14:
            k14 = k14 + 1
            tw14.append(k14)
            tw14[k14] = eval(data[i][14])
        if ico_q[i] == 15:
            k15 = k15 + 1
            tw15.append(k15)
            tw15[k15] = eval(data[i][14])
        if ico_q[i] == 16:
            k16 = k16 + 1
            tw16.append(k16)
            tw16[k16] = eval(data[i][14])

    #Based on ICO Price
    if data[i][11] != 'N/A':
        if ico_q[i] == 1:
            l1 = l1 + 1
            pr1.append(l1)
            pr1[l1] = eval(data[i][11])
        if ico_q[i] == 2:
            l2 = l2 + 1
            pr2.append(l2)
            pr2[l2] = eval(data[i][11])
        if ico_q[i] == 3:
            l3 = l3 + 1
            pr3.append(l3)
            pr3[l3] = eval(data[i][11])
        if ico_q[i] == 4:
            l4 = l4 + 1
            pr4.append(l4)
            pr4[l4] = eval(data[i][11])
        if ico_q[i] == 5:
            l5 = l5 + 1
            pr5.append(l5)
            pr5[l5] = eval(data[i][11])
        if ico_q[i] == 6:
            l6 = l6 + 1
            pr6.append(l6)
            pr6[l6] = eval(data[i][11])
        if ico_q[i] == 7:
            l7 = l7 + 1
            pr7.append(l7)
            pr7[l7] = eval(data[i][11])
        if ico_q[i] == 8:
            l8 = l8 + 1
            pr8.append(l8)
            pr8[l8] = eval(data[i][11])
        if ico_q[i] == 9:
            l9 = l9 + 1
            pr9.append(l9)
            pr9[l9] = eval(data[i][11])
        if ico_q[i] == 10:
            l10 = l10 + 1
            pr10.append(l10)
            pr10[l10] = eval(data[i][11])
        if ico_q[i] == 11:
            l11 = l11 + 1
            pr11.append(l11)
            pr11[l11] = eval(data[i][11])
        if ico_q[i] == 12:
            l12 = l12 + 1
            pr12.append(l12)
            pr12[l12] = eval(data[i][11])
        if ico_q[i] == 13:
            l13 = l13 + 1
            pr13.append(l13)
            pr13[l13] = eval(data[i][11])
        if ico_q[i] == 14:
            l14 = l14 + 1
            pr14.append(l14)
            pr14[l14] = eval(data[i][11])
        if ico_q[i] == 15:
            l15 = l15 + 1
            pr15.append(l15)
            pr15[l15] = eval(data[i][11])
        if ico_q[i] == 16:
            l16 = l16 + 1
            pr16.append(l16)
            pr16[l16] = eval(data[i][11])

    #Based on ICO Industry
    if data[i][6] != 'other' and data[i][8] != 'N/A':
        if ico_q[i] == 1:
            if data[i][6] == 'fintech':
                q1_fin = q1_fin + eval(data[i][8])
            if data[i][6] == 'blockchain':
                q1_blk = q1_blk + eval(data[i][8])
            if data[i][6] == 'real_estate':
                q1_re = q1_re + eval(data[i][8])
            if data[i][6] == 'social_service':
                q1_ss = q1_ss + eval(data[i][8])
            if data[i][6] == 'entertainment':
                q1_ent = q1_ent + eval(data[i][8])
            if data[i][6] == 'gaming':
                q1_gam = q1_gam + eval(data[i][8])
            if data[i][6] == 'gambling':
                q1_gmb = q1_gmb + eval(data[i][8])
            if data[i][6] == 'ecommerce':
                q1_eco = q1_eco + eval(data[i][8])
            if data[i][6] == 'saas':
                q1_sas = q1_sas + eval(data[i][8])
            if data[i][6] == 'transportation':
                q1_trs = q1_trs + eval(data[i][8])
            if data[i][6] == 'law':
                q1_law = q1_law + eval(data[i][8])
            if data[i][6] == 'insurances':
                q1_ins = q1_ins + eval(data[i][8])
            if data[i][6] == 'telecom':
                q1_tel = q1_tel + eval(data[i][8])
            if data[i][6] == 'energy':
                q1_ener = q1_ener + eval(data[i][8])

        if ico_q[i] == 2:
            if data[i][6] == 'fintech':
                q2_fin = q2_fin + eval(data[i][8])
            if data[i][6] == 'blockchain':
                q2_blk = q2_blk + eval(data[i][8])
            if data[i][6] == 'real_estate':
                q2_re = q2_re + eval(data[i][8])
            if data[i][6] == 'social_service':
                q2_ss = q2_ss + eval(data[i][8])
            if data[i][6] == 'entertainment':
                q2_ent = q2_ent + eval(data[i][8])
            if data[i][6] == 'gaming':
                q2_gam = q2_gam + eval(data[i][8])
            if data[i][6] == 'gambling':
                q2_gmb = q2_gmb + eval(data[i][8])
            if data[i][6] == 'ecommerce':
                q2_eco = q2_eco + eval(data[i][8])
            if data[i][6] == 'saas':
                q2_sas = q2_sas + eval(data[i][8])
            if data[i][6] == 'transportation':
                q2_trs = q2_trs + eval(data[i][8])
            if data[i][6] == 'law':
                q2_law = q2_law + eval(data[i][8])
            if data[i][6] == 'insurances':
                q2_ins = q2_ins + eval(data[i][8])
            if data[i][6] == 'telecom':
                q2_tel = q2_tel + eval(data[i][8])
            if data[i][6] == 'energy':
                q2_ener = q2_ener + eval(data[i][8])

        if ico_q[i] == 3:
            if data[i][6] == 'fintech':
                q3_fin = q3_fin + eval(data[i][8])
            if data[i][6] == 'blockchain':
                q3_blk = q3_blk + eval(data[i][8])
            if data[i][6] == 'real_estate':
                q3_re = q3_re + eval(data[i][8])
            if data[i][6] == 'social_service':
                q3_ss = q3_ss + eval(data[i][8])
            if data[i][6] == 'entertainment':
                q3_ent = q3_ent + eval(data[i][8])
            if data[i][6] == 'gaming':
                q3_gam = q3_gam + eval(data[i][8])
            if data[i][6] == 'gambling':
                q3_gmb = q3_gmb + eval(data[i][8])
            if data[i][6] == 'ecommerce':
                q3_eco = q3_eco + eval(data[i][8])
            if data[i][6] == 'saas':
                q3_sas = q3_sas + eval(data[i][8])
            if data[i][6] == 'transportation':
                q3_trs = q3_trs + eval(data[i][8])
            if data[i][6] == 'law':
                q3_law = q3_law + eval(data[i][8])
            if data[i][6] == 'insurances':
                q3_ins = q3_ins + eval(data[i][8])
            if data[i][6] == 'telecom':
                q3_tel = q3_tel + eval(data[i][8])
            if data[i][6] == 'energy':
                q3_ener = q3_ener + eval(data[i][8])

        if ico_q[i] == 4:
            if data[i][6] == 'fintech':
                q4_fin = q4_fin + eval(data[i][8])
            if data[i][6] == 'blockchain':
                q4_blk = q4_blk + eval(data[i][8])
            if data[i][6] == 'real_estate':
                q4_re = q4_re + eval(data[i][8])
            if data[i][6] == 'social_service':
                q4_ss = q4_ss + eval(data[i][8])
            if data[i][6] == 'entertainment':
                q4_ent = q4_ent + eval(data[i][8])
            if data[i][6] == 'gaming':
                q4_gam = q4_gam + eval(data[i][8])
            if data[i][6] == 'gambling':
                q4_gmb = q4_gmb + eval(data[i][8])
            if data[i][6] == 'ecommerce':
                q4_eco = q4_eco + eval(data[i][8])
            if data[i][6] == 'saas':
                q4_sas = q4_sas + eval(data[i][8])
            if data[i][6] == 'transportation':
                q4_trs = q4_trs + eval(data[i][8])
            if data[i][6] == 'law':
                q4_law = q4_law + eval(data[i][8])
            if data[i][6] == 'insurances':
                q4_ins = q4_ins + eval(data[i][8])
            if data[i][6] == 'telecom':
                q4_tel = q4_tel + eval(data[i][8])
            if data[i][6] == 'energy':
                q4_ener = q4_ener + eval(data[i][8])

        if ico_q[i] == 5:
            if data[i][6] == 'fintech':
                q5_fin = q5_fin + eval(data[i][8])
            if data[i][6] == 'blockchain':
                q5_blk = q5_blk + eval(data[i][8])
            if data[i][6] == 'real_estate':
                q5_re = q5_re + eval(data[i][8])
            if data[i][6] == 'social_service':
                q5_ss = q5_ss + eval(data[i][8])
            if data[i][6] == 'entertainment':
                q5_ent = q5_ent + eval(data[i][8])
            if data[i][6] == 'gaming':
                q5_gam = q5_gam + eval(data[i][8])
            if data[i][6] == 'gambling':
                q5_gmb = q5_gmb + eval(data[i][8])
            if data[i][6] == 'ecommerce':
                q5_eco = q5_eco + eval(data[i][8])
            if data[i][6] == 'saas':
                q5_sas = q5_sas + eval(data[i][8])
            if data[i][6] == 'transportation':
                q5_trs = q5_trs + eval(data[i][8])
            if data[i][6] == 'law':
                q5_law = q5_law + eval(data[i][8])
            if data[i][6] == 'insurances':
                q5_ins = q5_ins + eval(data[i][8])
            if data[i][6] == 'telecom':
                q5_tel = q5_tel + eval(data[i][8])
            if data[i][6] == 'energy':
                q5_ener = q5_ener + eval(data[i][8])

        if ico_q[i] == 6:
            if data[i][6] == 'fintech':
                q6_fin = q6_fin + eval(data[i][8])
            if data[i][6] == 'blockchain':
                q6_blk = q6_blk + eval(data[i][8])
            if data[i][6] == 'real_estate':
                q6_re = q6_re + eval(data[i][8])
            if data[i][6] == 'social_service':
                q6_ss = q6_ss + eval(data[i][8])
            if data[i][6] == 'entertainment':
                q6_ent = q6_ent + eval(data[i][8])
            if data[i][6] == 'gaming':
                q6_gam = q6_gam + eval(data[i][8])
            if data[i][6] == 'gambling':
                q6_gmb = q6_gmb + eval(data[i][8])
            if data[i][6] == 'ecommerce':
                q6_eco = q6_eco + eval(data[i][8])
            if data[i][6] == 'saas':
                q6_sas = q6_sas + eval(data[i][8])
            if data[i][6] == 'transportation':
                q6_trs = q6_trs + eval(data[i][8])
            if data[i][6] == 'law':
                q6_law = q6_law + eval(data[i][8])
            if data[i][6] == 'insurances':
                q6_ins = q6_ins + eval(data[i][8])
            if data[i][6] == 'telecom':
                q6_tel = q6_tel + eval(data[i][8])
            if data[i][6] == 'energy':
                q6_ener = q6_ener + eval(data[i][8])
		
        if ico_q[i] == 7:
            if data[i][6] == 'fintech':
                q7_fin = q7_fin + eval(data[i][8])
            if data[i][6] == 'blockchain':
                q7_blk = q7_blk + eval(data[i][8])
            if data[i][6] == 'real_estate':
                q7_re = q7_re + eval(data[i][8])
            if data[i][6] == 'social_service':
                q7_ss = q7_ss + eval(data[i][8])
            if data[i][6] == 'entertainment':
                q7_ent = q7_ent + eval(data[i][8])
            if data[i][6] == 'gaming':
                q7_gam = q7_gam + eval(data[i][8])
            if data[i][6] == 'gambling':
                q7_gmb = q7_gmb + eval(data[i][8])
            if data[i][6] == 'ecommerce':
                q7_eco = q7_eco + eval(data[i][8])
            if data[i][6] == 'saas':
                q7_sas = q7_sas + eval(data[i][8])
            if data[i][6] == 'transportation':
                q7_trs = q7_trs + eval(data[i][8])
            if data[i][6] == 'law':
                q7_law = q7_law + eval(data[i][8])
            if data[i][6] == 'insurances':
                q7_ins = q7_ins + eval(data[i][8])
            if data[i][6] == 'telecom':
                q7_tel = q7_tel + eval(data[i][8])
            if data[i][6] == 'energy':
                q7_ener = q7_ener + eval(data[i][8])
		
        if ico_q[i] == 8:
            if data[i][6] == 'fintech':
                q8_fin = q8_fin + eval(data[i][8])
            if data[i][6] == 'blockchain':
                q8_blk = q8_blk + eval(data[i][8])
            if data[i][6] == 'real_estate':
                q8_re = q8_re + eval(data[i][8])
            if data[i][6] == 'social_service':
                q8_ss = q8_ss + eval(data[i][8])
            if data[i][6] == 'entertainment':
                q8_ent = q8_ent + eval(data[i][8])
            if data[i][6] == 'gaming':
                q8_gam = q8_gam + eval(data[i][8])
            if data[i][6] == 'gambling':
                q8_gmb = q8_gmb + eval(data[i][8])
            if data[i][6] == 'ecommerce':
                q8_eco = q8_eco + eval(data[i][8])
            if data[i][6] == 'saas':
                q8_sas = q8_sas + eval(data[i][8])
            if data[i][6] == 'transportation':
                q8_trs = q8_trs + eval(data[i][8])
            if data[i][6] == 'law':
                q8_law = q8_law + eval(data[i][8])
            if data[i][6] == 'insurances':
                q8_ins = q8_ins + eval(data[i][8])
            if data[i][6] == 'telecom':
                q8_tel = q8_tel + eval(data[i][8])
            if data[i][6] == 'energy':
                q8_ener = q8_ener + eval(data[i][8])
		
		
        if ico_q[i] == 9:
            if data[i][6] == 'fintech':
                q9_fin = q9_fin + eval(data[i][8])
            if data[i][6] == 'blockchain':
                q9_blk = q9_blk + eval(data[i][8])
            if data[i][6] == 'real_estate':
                q9_re = q9_re + eval(data[i][8])
            if data[i][6] == 'social_service':
                q9_ss = q9_ss + eval(data[i][8])
            if data[i][6] == 'entertainment':
                q9_ent = q9_ent + eval(data[i][8])
            if data[i][6] == 'gaming':
                q9_gam = q9_gam + eval(data[i][8])
            if data[i][6] == 'gambling':
                q9_gmb = q9_gmb + eval(data[i][8])
            if data[i][6] == 'ecommerce':
                q9_eco = q9_eco + eval(data[i][8])
            if data[i][6] == 'saas':
                q9_sas = q9_sas + eval(data[i][8])
            if data[i][6] == 'transportation':
                q9_trs = q9_trs + eval(data[i][8])
            if data[i][6] == 'law':
                q9_law = q9_law + eval(data[i][8])
            if data[i][6] == 'insurances':
                q9_ins = q9_ins + eval(data[i][8])
            if data[i][6] == 'telecom':
                q9_tel = q9_tel + eval(data[i][8])
            if data[i][6] == 'energy':
                q9_ener = q9_ener + eval(data[i][8])
		
		
        if ico_q[i] == 10:
            if data[i][6] == 'fintech':
                q10_fin = q10_fin + eval(data[i][8])
            if data[i][6] == 'blockchain':
                q10_blk = q10_blk + eval(data[i][8])
            if data[i][6] == 'real_estate':
                q10_re = q10_re + eval(data[i][8])
            if data[i][6] == 'social_service':
                q10_ss = q10_ss + eval(data[i][8])
            if data[i][6] == 'entertainment':
                q10_ent = q10_ent + eval(data[i][8])
            if data[i][6] == 'gaming':
                q10_gam = q10_gam + eval(data[i][8])
            if data[i][6] == 'gambling':
                q10_gmb = q10_gmb + eval(data[i][8])
            if data[i][6] == 'ecommerce':
                q10_eco = q10_eco + eval(data[i][8])
            if data[i][6] == 'saas':
                q10_sas = q10_sas + eval(data[i][8])
            if data[i][6] == 'transportation':
                q10_trs = q10_trs + eval(data[i][8])
            if data[i][6] == 'law':
                q10_law = q10_law + eval(data[i][8])
            if data[i][6] == 'insurances':
                q10_ins = q10_ins + eval(data[i][8])
            if data[i][6] == 'telecom':
                q10_tel = q10_tel + eval(data[i][8])
            if data[i][6] == 'energy':
                q10_ener = q10_ener + eval(data[i][8])
		
        if ico_q[i] == 11:
            if data[i][6] == 'fintech':
                q11_fin = q11_fin + eval(data[i][8])
            if data[i][6] == 'blockchain':
                q11_blk = q11_blk + eval(data[i][8])
            if data[i][6] == 'real_estate':
                q11_re = q11_re + eval(data[i][8])
            if data[i][6] == 'social_service':
                q11_ss = q11_ss + eval(data[i][8])
            if data[i][6] == 'entertainment':
                q11_ent = q11_ent + eval(data[i][8])
            if data[i][6] == 'gaming':
                q11_gam = q11_gam + eval(data[i][8])
            if data[i][6] == 'gambling':
                q11_gmb = q11_gmb + eval(data[i][8])
            if data[i][6] == 'ecommerce':
                q11_eco = q11_eco + eval(data[i][8])
            if data[i][6] == 'saas':
                q11_sas = q11_sas + eval(data[i][8])
            if data[i][6] == 'transportation':
                q11_trs = q11_trs + eval(data[i][8])
            if data[i][6] == 'law':
                q11_law = q11_law + eval(data[i][8])
            if data[i][6] == 'insurances':
                q11_ins = q11_ins + eval(data[i][8])
            if data[i][6] == 'telecom':
                q11_tel = q11_tel + eval(data[i][8])
            if data[i][6] == 'energy':
                q11_ener = q11_ener + eval(data[i][8])
		
        if ico_q[i] == 12:
            if data[i][6] == 'fintech':
                q12_fin = q12_fin + eval(data[i][8])
            if data[i][6] == 'blockchain':
                q12_blk = q12_blk + eval(data[i][8])
            if data[i][6] == 'real_estate':
                q12_re = q12_re + eval(data[i][8])
            if data[i][6] == 'social_service':
                q12_ss = q12_ss + eval(data[i][8])
            if data[i][6] == 'entertainment':
                q12_ent = q12_ent + eval(data[i][8])
            if data[i][6] == 'gaming':
                q12_gam = q12_gam + eval(data[i][8])
            if data[i][6] == 'gambling':
                q12_gmb = q12_gmb + eval(data[i][8])
            if data[i][6] == 'ecommerce':
                q12_eco = q12_eco + eval(data[i][8])
            if data[i][6] == 'saas':
                q12_sas = q12_sas + eval(data[i][8])
            if data[i][6] == 'transportation':
                q12_trs = q12_trs + eval(data[i][8])
            if data[i][6] == 'law':
                q12_law = q12_law + eval(data[i][8])
            if data[i][6] == 'insurances':
                q12_ins = q12_ins + eval(data[i][8])
            if data[i][6] == 'telecom':
                q12_tel = q12_tel + eval(data[i][8])
            if data[i][6] == 'energy':
                q12_ener = q12_ener + eval(data[i][8])

        if ico_q[i] == 13:
            if data[i][6] == 'fintech':
                q13_fin = q13_fin + eval(data[i][8])
            if data[i][6] == 'blockchain':
                q13_blk = q13_blk + eval(data[i][8])
            if data[i][6] == 'real_estate':
                q13_re = q13_re + eval(data[i][8])
            if data[i][6] == 'social_service':
                q13_ss = q13_ss + eval(data[i][8])
            if data[i][6] == 'entertainment':
                q13_ent = q13_ent + eval(data[i][8])
            if data[i][6] == 'gaming':
                q13_gam = q13_gam + eval(data[i][8])
            if data[i][6] == 'gambling':
                q13_gmb = q13_gmb + eval(data[i][8])
            if data[i][6] == 'ecommerce':
                q13_eco = q13_eco + eval(data[i][8])
            if data[i][6] == 'saas':
                q13_sas = q13_sas + eval(data[i][8])
            if data[i][6] == 'transportation':
                q13_trs = q13_trs + eval(data[i][8])
            if data[i][6] == 'law':
                q13_law = q13_law + eval(data[i][8])
            if data[i][6] == 'insurances':
                q13_ins = q13_ins + eval(data[i][8])
            if data[i][6] == 'telecom':
                q13_tel = q13_tel + eval(data[i][8])
            if data[i][6] == 'energy':
                q13_ener = q13_ener + eval(data[i][8])
		
        if ico_q[i] == 14:
            if data[i][6] == 'fintech':
                q14_fin = q14_fin + eval(data[i][8])
            if data[i][6] == 'blockchain':
                q14_blk = q14_blk + eval(data[i][8])
            if data[i][6] == 'real_estate':
                q14_re = q14_re + eval(data[i][8])
            if data[i][6] == 'social_service':
                q14_ss = q14_ss + eval(data[i][8])
            if data[i][6] == 'entertainment':
                q14_ent = q14_ent + eval(data[i][8])
            if data[i][6] == 'gaming':
                q14_gam = q14_gam + eval(data[i][8])
            if data[i][6] == 'gambling':
                q14_gmb = q14_gmb + eval(data[i][8])
            if data[i][6] == 'ecommerce':
                q14_eco = q14_eco + eval(data[i][8])
            if data[i][6] == 'saas':
                q14_sas = q14_sas + eval(data[i][8])
            if data[i][6] == 'transportation':
                q14_trs = q14_trs + eval(data[i][8])
            if data[i][6] == 'law':
                q14_law = q14_law + eval(data[i][8])
            if data[i][6] == 'insurances':
                q14_ins = q14_ins + eval(data[i][8])
            if data[i][6] == 'telecom':
                q14_tel = q14_tel + eval(data[i][8])
            if data[i][6] == 'energy':
                q14_ener = q14_ener + eval(data[i][8])
		
        if ico_q[i] == 15:
            if data[i][6] == 'fintech':
                q15_fin = q15_fin + eval(data[i][8])
            if data[i][6] == 'blockchain':
                q15_blk = q15_blk + eval(data[i][8])
            if data[i][6] == 'real_estate':
                q15_re = q15_re + eval(data[i][8])
            if data[i][6] == 'social_service':
                q15_ss = q15_ss + eval(data[i][8])
            if data[i][6] == 'entertainment':
                q15_ent = q15_ent + eval(data[i][8])
            if data[i][6] == 'gaming':
                q15_gam = q15_gam + eval(data[i][8])
            if data[i][6] == 'gambling':
                q15_gmb = q15_gmb + eval(data[i][8])
            if data[i][6] == 'ecommerce':
                q15_eco = q15_eco + eval(data[i][8])
            if data[i][6] == 'saas':
                q15_sas = q15_sas + eval(data[i][8])
            if data[i][6] == 'transportation':
                q15_trs = q15_trs + eval(data[i][8])
            if data[i][6] == 'law':
                q15_law = q15_law + eval(data[i][8])
            if data[i][6] == 'insurances':
                q15_ins = q15_ins + eval(data[i][8])
            if data[i][6] == 'telecom':
                q15_tel = q15_tel + eval(data[i][8])
            if data[i][6] == 'energy':
                q15_ener = q15_ener + eval(data[i][8])
		
        if ico_q[i] == 16:
            if data[i][6] == 'fintech':
                q16_fin = q16_fin + eval(data[i][8])
            if data[i][6] == 'blockchain':
                q16_blk = q16_blk + eval(data[i][8])
            if data[i][6] == 'real_estate':
                q16_re = q16_re + eval(data[i][8])
            if data[i][6] == 'social_service':
                q16_ss = q16_ss + eval(data[i][8])
            if data[i][6] == 'entertainment':
                q16_ent = q16_ent + eval(data[i][8])
            if data[i][6] == 'gaming':
                q16_gam = q16_gam + eval(data[i][8])
            if data[i][6] == 'gambling':
                q16_gmb = q16_gmb + eval(data[i][8])
            if data[i][6] == 'ecommerce':
                q16_eco = q16_eco + eval(data[i][8])
            if data[i][6] == 'saas':
                q16_sas = q16_sas + eval(data[i][8])
            if data[i][6] == 'transportation':
                q16_trs = q16_trs + eval(data[i][8])
            if data[i][6] == 'law':
                q16_law = q16_law + eval(data[i][8])
            if data[i][6] == 'insurances':
                q16_ins = q16_ins + eval(data[i][8])
            if data[i][6] == 'telecom':
                q16_tel = q16_tel + eval(data[i][8])
            if data[i][6] == 'energy':
                q16_ener = q16_ener + eval(data[i][8])

#######
#######

    #Based on ICO Country
    if data[i][5] != '12' and data[i][8] != 'N/A':
        if ico_q[i] == 1:
            if data[i][5] == '1':
                q1_na = q1_na + eval(data[i][8])
            if data[i][5] == '2':
                q1_rs = q1_rs + eval(data[i][8])
            if data[i][5] == '3':
                q1_as = q1_as + eval(data[i][8])
            if data[i][5] == '4':
                q1_uk = q1_uk + eval(data[i][8])
            if data[i][5] == '5':
                q1_eu = q1_eu + eval(data[i][8])
            if data[i][5] == '6':
                q1_sw = q1_sw + eval(data[i][8])
            if data[i][5] == '7':
                q1_th = q1_th + eval(data[i][8])
            if data[i][5] == '8':
                q1_jk = q1_jk + eval(data[i][8])
            if data[i][5] == '9':
                q1_au = q1_au + eval(data[i][8])
            if data[i][5] == '10':
                q1_sa = q1_sa + eval(data[i][8])
            if data[i][5] == '11':
                q1_af = q1_af + eval(data[i][8])

        if ico_q[i] == 2:
            if data[i][5] == '1':
                q2_na = q2_na + eval(data[i][8])
            if data[i][5] == '2':
                q2_rs = q2_rs + eval(data[i][8])
            if data[i][5] == '3':
                q2_as = q2_as + eval(data[i][8])
            if data[i][5] == '4':
                q2_uk = q2_uk + eval(data[i][8])
            if data[i][5] == '5':
                q2_eu = q2_eu + eval(data[i][8])
            if data[i][5] == '6':
                q2_sw = q2_sw + eval(data[i][8])
            if data[i][5] == '7':
                q2_th = q2_th + eval(data[i][8])
            if data[i][5] == '8':
                q2_jk = q2_jk + eval(data[i][8])
            if data[i][5] == '9':
                q2_au = q2_au + eval(data[i][8])
            if data[i][5] == '10':
                q2_sa = q2_sa + eval(data[i][8])
            if data[i][5] == '11':
                q2_af = q2_af + eval(data[i][8])

        if ico_q[i] == 3:
            if data[i][5] == '1':
                q3_na = q3_na + eval(data[i][8])
            if data[i][5] == '2':
                q3_rs = q3_rs + eval(data[i][8])
            if data[i][5] == '3':
                q3_as = q3_as + eval(data[i][8])
            if data[i][5] == '4':
                q3_uk = q3_uk + eval(data[i][8])
            if data[i][5] == '5':
                q3_eu = q3_eu + eval(data[i][8])
            if data[i][5] == '6':
                q3_sw = q3_sw + eval(data[i][8])
            if data[i][5] == '7':
                q3_th = q3_th + eval(data[i][8])
            if data[i][5] == '8':
                q3_jk = q3_jk + eval(data[i][8])
            if data[i][5] == '9':
                q3_au = q3_au + eval(data[i][8])
            if data[i][5] == '10':
                q3_sa = q3_sa + eval(data[i][8])
            if data[i][5] == '11':
                q3_af = q3_af + eval(data[i][8])

        if ico_q[i] == 4:
            if data[i][5] == '1':
                q4_na = q4_na + eval(data[i][8])
            if data[i][5] == '2':
                q4_rs = q4_rs + eval(data[i][8])
            if data[i][5] == '3':
                q4_as = q4_as + eval(data[i][8])
            if data[i][5] == '4':
                q4_uk = q4_uk + eval(data[i][8])
            if data[i][5] == '5':
                q4_eu = q4_eu + eval(data[i][8])
            if data[i][5] == '6':
                q4_sw = q4_sw + eval(data[i][8])
            if data[i][5] == '7':
                q4_th = q4_th + eval(data[i][8])
            if data[i][5] == '8':
                q4_jk = q4_jk + eval(data[i][8])
            if data[i][5] == '9':
                q4_au = q4_au + eval(data[i][8])
            if data[i][5] == '10':
                q4_sa = q4_sa + eval(data[i][8])
            if data[i][5] == '11':
                q4_af = q4_af + eval(data[i][8])

        if ico_q[i] == 5:
            if data[i][5] == '1':
                q5_na = q5_na + eval(data[i][8])
            if data[i][5] == '2':
                q5_rs = q5_rs + eval(data[i][8])
            if data[i][5] == '3':
                q5_as = q5_as + eval(data[i][8])
            if data[i][5] == '4':
                q5_uk = q5_uk + eval(data[i][8])
            if data[i][5] == '5':
                q5_eu = q5_eu + eval(data[i][8])
            if data[i][5] == '6':
                q5_sw = q5_sw + eval(data[i][8])
            if data[i][5] == '7':
                q5_th = q5_th + eval(data[i][8])
            if data[i][5] == '8':
                q5_jk = q5_jk + eval(data[i][8])
            if data[i][5] == '9':
                q5_au = q5_au + eval(data[i][8])
            if data[i][5] == '10':
                q5_sa = q5_sa + eval(data[i][8])
            if data[i][5] == '11':
                q5_af = q5_af + eval(data[i][8])

        if ico_q[i] == 6:
            if data[i][5] == '1':
                q6_na = q6_na + eval(data[i][8])
            if data[i][5] == '2':
                q6_rs = q6_rs + eval(data[i][8])
            if data[i][5] == '3':
                q6_as = q6_as + eval(data[i][8])
            if data[i][5] == '4':
                q6_uk = q6_uk + eval(data[i][8])
            if data[i][5] == '5':
                q6_eu = q6_eu + eval(data[i][8])
            if data[i][5] == '6':
                q6_sw = q6_sw + eval(data[i][8])
            if data[i][5] == '7':
                q6_th = q6_th + eval(data[i][8])
            if data[i][5] == '8':
                q6_jk = q6_jk + eval(data[i][8])
            if data[i][5] == '9':
                q6_au = q6_au + eval(data[i][8])
            if data[i][5] == '10':
                q6_sa = q6_sa + eval(data[i][8])
            if data[i][5] == '11':
                q6_af = q6_af + eval(data[i][8])
		
        if ico_q[i] == 7:
            if data[i][5] == '1':
                q7_na = q7_na + eval(data[i][8])
            if data[i][5] == '2':
                q7_rs = q7_rs + eval(data[i][8])
            if data[i][5] == '3':
                q7_as = q7_as + eval(data[i][8])
            if data[i][5] == '4':
                q7_uk = q7_uk + eval(data[i][8])
            if data[i][5] == '5':
                q7_eu = q7_eu + eval(data[i][8])
            if data[i][5] == '6':
                q7_sw = q7_sw + eval(data[i][8])
            if data[i][5] == '7':
                q7_th = q7_th + eval(data[i][8])
            if data[i][5] == '8':
                q7_jk = q7_jk + eval(data[i][8])
            if data[i][5] == '9':
                q7_au = q7_au + eval(data[i][8])
            if data[i][5] == '10':
                q7_sa = q7_sa + eval(data[i][8])
            if data[i][5] == '11':
                q7_af = q7_af + eval(data[i][8])
		
        if ico_q[i] == 8:
            if data[i][5] == '1':
                q8_na = q8_na + eval(data[i][8])
            if data[i][5] == '2':
                q8_rs = q8_rs + eval(data[i][8])
            if data[i][5] == '3':
                q8_as = q8_as + eval(data[i][8])
            if data[i][5] == '4':
                q8_uk = q8_uk + eval(data[i][8])
            if data[i][5] == '5':
                q8_eu = q8_eu + eval(data[i][8])
            if data[i][5] == '6':
                q8_sw = q8_sw + eval(data[i][8])
            if data[i][5] == '7':
                q8_th = q8_th + eval(data[i][8])
            if data[i][5] == '8':
                q8_jk = q8_jk + eval(data[i][8])
            if data[i][5] == '9':
                q8_au = q8_au + eval(data[i][8])
            if data[i][5] == '10':
                q8_sa = q8_sa + eval(data[i][8])
            if data[i][5] == '11':
                q8_af = q8_af + eval(data[i][8])
		
		
        if ico_q[i] == 9:
            if data[i][5] == '1':
                q9_na = q9_na + eval(data[i][8])
            if data[i][5] == '2':
                q9_rs = q9_rs + eval(data[i][8])
            if data[i][5] == '3':
                q9_as = q9_as + eval(data[i][8])
            if data[i][5] == '4':
                q9_uk = q9_uk + eval(data[i][8])
            if data[i][5] == '5':
                q9_eu = q9_eu + eval(data[i][8])
            if data[i][5] == '6':
                q9_sw = q9_sw + eval(data[i][8])
            if data[i][5] == '7':
                q9_th = q9_th + eval(data[i][8])
            if data[i][5] == '8':
                q9_jk = q9_jk + eval(data[i][8])
            if data[i][5] == '9':
                q9_au = q9_au + eval(data[i][8])
            if data[i][5] == '10':
                q9_sa = q9_sa + eval(data[i][8])
            if data[i][5] == '11':
                q9_af = q9_af + eval(data[i][8])
		
		
        if ico_q[i] == 10:
            if data[i][5] == '1':
                q10_na = q10_na + eval(data[i][8])
            if data[i][5] == '2':
                q10_rs = q10_rs + eval(data[i][8])
            if data[i][5] == '3':
                q10_as = q10_as + eval(data[i][8])
            if data[i][5] == '4':
                q10_uk = q10_uk + eval(data[i][8])
            if data[i][5] == '5':
                q10_eu = q10_eu + eval(data[i][8])
            if data[i][5] == '6':
                q10_sw = q10_sw + eval(data[i][8])
            if data[i][5] == '7':
                q10_th = q10_th + eval(data[i][8])
            if data[i][5] == '8':
                q10_jk = q10_jk + eval(data[i][8])
            if data[i][5] == '9':
                q10_au = q10_au + eval(data[i][8])
            if data[i][5] == '10':
                q10_sa = q10_sa + eval(data[i][8])
            if data[i][5] == '11':
                q10_af = q10_af + eval(data[i][8])
		
        if ico_q[i] == 11:
            if data[i][5] == '1':
                q11_na = q11_na + eval(data[i][8])
            if data[i][5] == '2':
                q11_rs = q11_rs + eval(data[i][8])
            if data[i][5] == '3':
                q11_as = q11_as + eval(data[i][8])
            if data[i][5] == '4':
                q11_uk = q11_uk + eval(data[i][8])
            if data[i][5] == '5':
                q11_eu = q11_eu + eval(data[i][8])
            if data[i][5] == '6':
                q11_sw = q11_sw + eval(data[i][8])
            if data[i][5] == '7':
                q11_th = q11_th + eval(data[i][8])
            if data[i][5] == '8':
                q11_jk = q11_jk + eval(data[i][8])
            if data[i][5] == '9':
                q11_au = q11_au + eval(data[i][8])
            if data[i][5] == '10':
                q11_sa = q11_sa + eval(data[i][8])
            if data[i][5] == '11':
                q11_af = q11_af + eval(data[i][8])
		
        if ico_q[i] == 12:
            if data[i][5] == '1':
                q12_na = q12_na + eval(data[i][8])
            if data[i][5] == '2':
                q12_rs = q12_rs + eval(data[i][8])
            if data[i][5] == '3':
                q12_as = q12_as + eval(data[i][8])
            if data[i][5] == '4':
                q12_uk = q12_uk + eval(data[i][8])
            if data[i][5] == '5':
                q12_eu = q12_eu + eval(data[i][8])
            if data[i][5] == '6':
                q12_sw = q12_sw + eval(data[i][8])
            if data[i][5] == '7':
                q12_th = q12_th + eval(data[i][8])
            if data[i][5] == '8':
                q12_jk = q12_jk + eval(data[i][8])
            if data[i][5] == '9':
                q12_au = q12_au + eval(data[i][8])
            if data[i][5] == '10':
                q12_sa = q12_sa + eval(data[i][8])
            if data[i][5] == '11':
                q12_af = q12_af + eval(data[i][8])

        if ico_q[i] == 13:
            if data[i][5] == '1':
                q13_na = q13_na + eval(data[i][8])
            if data[i][5] == '2':
                q13_rs = q13_rs + eval(data[i][8])
            if data[i][5] == '3':
                q13_as = q13_as + eval(data[i][8])
            if data[i][5] == '4':
                q13_uk = q13_uk + eval(data[i][8])
            if data[i][5] == '5':
                q13_eu = q13_eu + eval(data[i][8])
            if data[i][5] == '6':
                q13_sw = q13_sw + eval(data[i][8])
            if data[i][5] == '7':
                q13_th = q13_th + eval(data[i][8])
            if data[i][5] == '8':
                q13_jk = q13_jk + eval(data[i][8])
            if data[i][5] == '9':
                q13_au = q13_au + eval(data[i][8])
            if data[i][5] == '10':
                q13_sa = q13_sa + eval(data[i][8])
            if data[i][5] == '11':
                q13_af = q13_af + eval(data[i][8])
		
        if ico_q[i] == 14:
            if data[i][5] == '1':
                q14_na = q14_na + eval(data[i][8])
            if data[i][5] == '2':
                q14_rs = q14_rs + eval(data[i][8])
            if data[i][5] == '3':
                q14_as = q14_as + eval(data[i][8])
            if data[i][5] == '4':
                q14_uk = q14_uk + eval(data[i][8])
            if data[i][5] == '5':
                q14_eu = q14_eu + eval(data[i][8])
            if data[i][5] == '6':
                q14_sw = q14_sw + eval(data[i][8])
            if data[i][5] == '7':
                q14_th = q14_th + eval(data[i][8])
            if data[i][5] == '8':
                q14_jk = q14_jk + eval(data[i][8])
            if data[i][5] == '9':
                q14_au = q14_au + eval(data[i][8])
            if data[i][5] == '10':
                q14_sa = q14_sa + eval(data[i][8])
            if data[i][5] == '11':
                q14_af = q14_af + eval(data[i][8])
		
        if ico_q[i] == 15:
            if data[i][5] == '1':
                q15_na = q15_na + eval(data[i][8])
            if data[i][5] == '2':
                q15_rs = q15_rs + eval(data[i][8])
            if data[i][5] == '3':
                q15_as = q15_as + eval(data[i][8])
            if data[i][5] == '4':
                q15_uk = q15_uk + eval(data[i][8])
            if data[i][5] == '5':
                q15_eu = q15_eu + eval(data[i][8])
            if data[i][5] == '6':
                q15_sw = q15_sw + eval(data[i][8])
            if data[i][5] == '7':
                q15_th = q15_th + eval(data[i][8])
            if data[i][5] == '8':
                q15_jk = q15_jk + eval(data[i][8])
            if data[i][5] == '9':
                q15_au = q15_au + eval(data[i][8])
            if data[i][5] == '10':
                q15_sa = q15_sa + eval(data[i][8])
            if data[i][5] == '11':
                q15_af = q15_af + eval(data[i][8])
		
        if ico_q[i] == 16:
            if data[i][5] == '1':
                q16_na = q16_na + eval(data[i][8])
            if data[i][5] == '2':
                q16_rs = q16_rs + eval(data[i][8])
            if data[i][5] == '3':
                q16_as = q16_as + eval(data[i][8])
            if data[i][5] == '4':
                q16_uk = q16_uk + eval(data[i][8])
            if data[i][5] == '5':
                q16_eu = q16_eu + eval(data[i][8])
            if data[i][5] == '6':
                q16_sw = q16_sw + eval(data[i][8])
            if data[i][5] == '7':
                q16_th = q16_th + eval(data[i][8])
            if data[i][5] == '8':
                q16_jk = q16_jk + eval(data[i][8])
            if data[i][5] == '9':
                q16_au = q16_au + eval(data[i][8])
            if data[i][5] == '10':
                q16_sa = q16_sa + eval(data[i][8])
            if data[i][5] == '11':
                q16_af = q16_af + eval(data[i][8])

    #Based on ICO daily time spent on website (Alexa)
    if data[i][16] != 'N/A':
        if ico_q[i] == 1:
            i1 = i1 + 1
            dv1.append(i1)
            dv1[i1] = eval(data[i][16])
        if ico_q[i] == 2:
            i2 = i2 + 1
            dv2.append(i2)
            dv2[i2] = eval(data[i][16])
        if ico_q[i] == 3:
            i3 = i3 + 1
            dv3.append(i3)
            dv3[i3] = eval(data[i][16])
        if ico_q[i] == 4:
            i4 = i4 + 1
            dv4.append(i4)
            dv4[i4] = eval(data[i][16])
        if ico_q[i] == 5:
            i5 = i5 + 1
            dv5.append(i5)
            dv5[i5] = eval(data[i][16])
        if ico_q[i] == 6:
            i6 = i6 + 1
            dv6.append(i6)
            dv6[i6] = eval(data[i][16])
        if ico_q[i] == 7:
            i7 = i7 + 1
            dv7.append(i7)
            dv7[i7] = eval(data[i][16])
        if ico_q[i] == 8:
            i8 = i8 + 1
            dv8.append(i8)
            dv8[i8] = eval(data[i][16])
        if ico_q[i] == 9:
            i9 = i9 + 1
            dv9.append(i9)
            dv9[i9] = eval(data[i][16])
        if ico_q[i] == 10:
            i10 = i10 + 1
            dv10.append(i10)
            dv10[i10] = eval(data[i][16])
        if ico_q[i] == 11:
            i11 = i11 + 1
            dv11.append(i11)
            dv11[i11] = eval(data[i][16])
        if ico_q[i] == 12:
            i12 = i12 + 1
            dv12.append(i12)
            dv12[i12] = eval(data[i][16])
        if ico_q[i] == 13:
            i13 = i13 + 1
            dv13.append(i13)
            dv13[i13] = eval(data[i][16])
        if ico_q[i] == 14:
            i14 = i14 + 1
            dv14.append(i14)
            dv14[i14] = eval(data[i][16])
        if ico_q[i] == 15:
            i15 = i15 + 1
            dv15.append(i15)
            dv15[i15] = eval(data[i][16])
        if ico_q[i] == 16:
            i16 = i16 + 1
            dv16.append(i16)
            dv16[i16] = eval(data[i][16])

    #Based on Day 1 return upon exchange listing
    if data[i][20] != 'N/A':
        if ico_q[i] == 1:
            j1 = j1 + 1
            ret1.append(j1)
            ret1[j1] = eval(data[i][20])
        if ico_q[i] == 2:
            j2 = j2 + 1
            ret2.append(j2)
            ret2[j2] = eval(data[i][20])
        if ico_q[i] == 3:
            j3 = j3 + 1
            ret3.append(j3)
            ret3[j3] = eval(data[i][20])
        if ico_q[i] == 4:
            j4 = j4 + 1
            ret4.append(j4)
            ret4[j4] = eval(data[i][20])
        if ico_q[i] == 5:
            j5 = j5 + 1
            ret5.append(j5)
            ret5[j5] = eval(data[i][20])
        if ico_q[i] == 6:
            j6 = j6 + 1
            ret6.append(j6)
            ret6[j6] = eval(data[i][20])
        if ico_q[i] == 7:
            j7 = j7 + 1
            ret7.append(j7)
            ret7[j7] = eval(data[i][20])
        if ico_q[i] == 8:
            j8 = j8 + 1
            ret8.append(j8)
            ret8[j8] = eval(data[i][20])
        if ico_q[i] == 9:
            j9 = j9 + 1
            ret9.append(j9)
            ret9[j9] = eval(data[i][20])
        if ico_q[i] == 10:
            j10 = j10 + 1
            ret10.append(j10)
            ret10[j10] = eval(data[i][20])
        if ico_q[i] == 11:
            j11 = j11 + 1
            ret11.append(j11)
            ret11[j11] = eval(data[i][20])
        if ico_q[i] == 12:
            j12 = j12 + 1
            ret12.append(j12)
            ret12[j12] = eval(data[i][20])
        if ico_q[i] == 13:
            j13 = j13 + 1
            ret13.append(j13)
            ret13[j13] = eval(data[i][20])
        if ico_q[i] == 14:
            j14 = j14 + 1
            ret14.append(j14)
            ret14[j14] = eval(data[i][20])
        if ico_q[i] == 15:
            j15 = j15 + 1
            ret15.append(j15)
            ret15[j15] = eval(data[i][20])
        if ico_q[i] == 16:
            j16 = j16 + 1
            ret16.append(j16)
            ret16[j16] = eval(data[i][20])

    #Based on Day 1 volume upon exchange listing
    if data[i][21] != 'N/A':
        if ico_q[i] == 1:
            o1 = o1 + 1
            vol1.append(o1)
            vol1[o1] = eval(data[i][21])
        if ico_q[i] == 2:
            o2 = o2 + 1
            vol2.append(o2)
            vol2[o2] = eval(data[i][21])
        if ico_q[i] == 3:
            o3 = o3 + 1
            vol3.append(o3)
            vol3[o3] = eval(data[i][21])
        if ico_q[i] == 4:
            o4 = o4 + 1
            vol4.append(o4)
            vol4[o4] = eval(data[i][21])
        if ico_q[i] == 5:
            o5 = o5 + 1
            vol5.append(o5)
            vol5[o5] = eval(data[i][21])
        if ico_q[i] == 6:
            o6 = o6 + 1
            vol6.append(o6)
            vol6[o6] = eval(data[i][21])
        if ico_q[i] == 7:
            o7 = o7 + 1
            vol7.append(o7)
            vol7[o7] = eval(data[i][21])
        if ico_q[i] == 8:
            o8 = o8 + 1
            vol8.append(o8)
            vol8[o8] = eval(data[i][21])
        if ico_q[i] == 9:
            o9 = o9 + 1
            vol9.append(o9)
            vol9[o9] = eval(data[i][21])
        if ico_q[i] == 10:
            o10 = o10 + 1
            vol10.append(o10)
            vol10[o10] = eval(data[i][21])
        if ico_q[i] == 11:
            o11 = o11 + 1
            vol11.append(o11)
            vol11[o11] = eval(data[i][21])
        if ico_q[i] == 12:
            o12 = o12 + 1
            vol12.append(o12)
            vol12[o12] = eval(data[i][21])
        if ico_q[i] == 13:
            o13 = o13 + 1
            vol13.append(o13)
            vol13[o13] = eval(data[i][21])
        if ico_q[i] == 14:
            o14 = o14 + 1
            vol14.append(o14)
            vol14[o14] = eval(data[i][21])
        if ico_q[i] == 15:
            o15 = o15 + 1
            vol15.append(o15)
            vol15[o15] = eval(data[i][21])
        if ico_q[i] == 16:
            o16 = o16 + 1
            vol16.append(o16)
            vol16[o16] = eval(data[i][21])

    #Based on annualized Sharpe ratio
    if data[i][25] != 'N/A':
        if ico_q[i] == 1:
            g1 = g1 + 1
            srp1.append(g1)
            srp1[g1] = eval(data[i][25])
        if ico_q[i] == 2:
            g2 = g2 + 1
            srp2.append(g2)
            srp2[g2] = eval(data[i][25])
        if ico_q[i] == 3:
            g3 = g3 + 1
            srp3.append(g3)
            srp3[g3] = eval(data[i][25])
        if ico_q[i] == 4:
            g4 = g4 + 1
            srp4.append(g4)
            srp4[g4] = eval(data[i][25])
        if ico_q[i] == 5:
            g5 = g5 + 1
            srp5.append(g5)
            srp5[g5] = eval(data[i][25])
        if ico_q[i] == 6:
            g6 = g6 + 1
            srp6.append(g6)
            srp6[g6] = eval(data[i][25])
        if ico_q[i] == 7:
            g7 = g7 + 1
            srp7.append(g7)
            srp7[g7] = eval(data[i][25])
        if ico_q[i] == 8:
            g8 = g8 + 1
            srp8.append(g8)
            srp8[g8] = eval(data[i][25])
        if ico_q[i] == 9:
            g9 = g9 + 1
            srp9.append(g9)
            srp9[g9] = eval(data[i][25])
        if ico_q[i] == 10:
            g10 = g10 + 1
            srp10.append(g10)
            srp10[g10] = eval(data[i][25])
        if ico_q[i] == 11:
            g11 = g11 + 1
            srp11.append(g11)
            srp11[g11] = eval(data[i][25])
        if ico_q[i] == 12:
            g12 = g12 + 1
            srp12.append(g12)
            srp12[g12] = eval(data[i][25])
        if ico_q[i] == 13:
            g13 = g13 + 1
            srp13.append(g13)
            srp13[g13] = eval(data[i][25])
        if ico_q[i] == 14:
            g14 = g14 + 1
            srp14.append(g14)
            srp14[g14] = eval(data[i][25])
        if ico_q[i] == 15:
            g15 = g15 + 1
            srp15.append(g15)
            srp15[g15] = eval(data[i][25])
        if ico_q[i] == 16:
            g16 = g16 + 1
            srp16.append(g16)
            srp16[g16] = eval(data[i][25])

#Set quarters with zero ICOs to unity to avoid ZeroDivisionErrors in success rates
qs = [q1n,q2n,q3n,q4n,q5n,q6n,q7n,q8n,q9n,q10n,q11n,q12n,q13n,q14n,q15n,q16n]
for i in range(0,len(qs)):
    if qs[i] == 0:
        qs[i] = 1.0

############################################################
###ICO FUNDING STATS (Q+Y)
############################################################
    
quarter_index = ['2016 Q1','2016 Q2','2016 Q3','2016 Q4','2017 Q1','2017 Q2','2017 Q3','2017 Q4','2018 Q1','2018 Q2','2018 Q3','2018 Q4','2019 Q1','2019 Q2','2019 Q3','2019 Q4']
cum_funds = [cum_funds_1,cum_funds_2,cum_funds_3,cum_funds_4,cum_funds_5,cum_funds_6,cum_funds_7,cum_funds_8,cum_funds_9,cum_funds_10,cum_funds_11,cum_funds_12,cum_funds_13,cum_funds_14,cum_funds_15,cum_funds_16]
cum_funds = [x / 1000000000. for x in cum_funds]
#Cut off 2019
quarter_index_b = quarter_index[:-4]
cum_funds_b = cum_funds[:-4]

year_index = ['2016','2017','2018','2019']
cum_annual = [cum_funds_1+cum_funds_2+cum_funds_3+cum_funds_4,cum_funds_5+cum_funds_6+cum_funds_7+cum_funds_8,cum_funds_9+cum_funds_10+cum_funds_11+cum_funds_12,cum_funds_13+cum_funds_14+cum_funds_15+cum_funds_16]
cum_annual = [x / 1000000000. for x in cum_annual]
#Cut off 2019
year_index_b = year_index[:-1]
cum_annual_b = cum_annual[:-1]

print('The cumulative funds raised by ICOs since 2016 total:', round(sum(cum_annual_b),2),'Billion USD')

objects = quarter_index_b
y_pos = np.arange(len(objects))
performance = cum_funds_b

objects2 = year_index_b
y_pos2 = np.arange(len(objects2))
performance2 = cum_annual_b

fig = plt.figure(figsize=(18, 9))

plt.subplot(1, 2, 1)
plt.bar(y_pos, performance, align='center', alpha=0.5, color = 'b')
plt.xticks(y_pos, objects, size = '12', weight = 'bold')
plt.yticks(size = '12', weight = 'bold')
plt.ylabel('Funds Raised [Billions of USD]',fontweight="bold",fontsize=12)
plt.xticks(rotation=60)
plt.title('Quarterly ICO Funding',fontweight="bold",fontsize=15)

plt.subplot(1, 2, 2)
plt.bar(y_pos2, performance2, align='center', alpha=0.5, color = 'r')
plt.xticks(y_pos2, objects2, size = '12', weight = 'bold')
plt.yticks(size = '12', weight = 'bold')
plt.ylabel('Funds Raised [Billions of USD]',fontweight="bold",fontsize=12)
plt.xticks(rotation=60)
plt.title('Annual ICO Funding',fontweight="bold",fontsize=15)

plt.show()
############################################################
###ICO SUCCESS STATS (Q+Y)
############################################################

success_rate = [round((s1/qs[0])*100,2),round((s2/qs[1])*100,2),round((s3/qs[2])*100,2),round((s4/qs[3])*100,2),round((s5/qs[4])*100,2),round((s6/qs[5])*100,2),round((s7/qs[6])*100,2),round((s8/qs[7])*100,2),round((s9/qs[8])*100,2),round((s10/qs[9])*100,2),round((s11/qs[10])*100,2),round((s12/qs[11])*100,2),round((s13/qs[12])*100,2),round((s14/qs[13])*100,2),round((s15/qs[14])*100,2),round((s16/qs[15])*100,2)]
#Cut off 2019
success_rate_b = success_rate[:-4]

success_annual = [round(((s1+s2+s3+s4)/(q1n+q2n+q3n+q4n))*100,2),round(((s5+s6+s7+s8)/(q5n+q6n+q7n+q8n))*100,2),round(((s9+s10+s11+s12)/(q9n+q10n+q11n+q12n))*100,2),round(((s13+s14+s15+s16)/(q13n+q14n+q15n+q16n))*100,2)]
#Cut off 2019
success_annual_b = success_annual[:-1]

objects = quarter_index_b
y_pos = np.arange(len(objects))
performance = success_rate_b

objects2 = year_index_b
y_pos2 = np.arange(len(objects2))
performance2 = success_annual_b

fig = plt.figure(figsize=(18, 9))

plt.subplot(1, 2, 1)
plt.bar(y_pos, performance, align='center', alpha=0.5, color = 'b')
plt.xticks(y_pos, objects, size = '12', weight = 'bold')
plt.yticks(size = '12', weight = 'bold')
plt.ylabel('Percentage of Successful ICOs',fontweight="bold",fontsize=12)
plt.xticks(rotation=60)
plt.title('Quarterly ICO Success Rates',fontweight="bold",fontsize=15)

plt.subplot(1, 2, 2)
plt.bar(y_pos2, performance2, align='center', alpha=0.5, color = 'r')
plt.xticks(y_pos2, objects2, size = '12', weight = 'bold')
plt.yticks(size = '12', weight = 'bold')
plt.ylabel('Percentage of Successful ICOs',fontweight="bold",fontsize=12)
plt.xticks(rotation=60)
plt.title('Annual ICO Success Rates',fontweight="bold",fontsize=15)

plt.show()

############################################################
###ICO TELEGRAM FOLLOWING STATS (Q+Y)
############################################################
for i in range(1,16):
    a = vars()['tg'+str(i)]
    if len(a) == 0:
        a.append(0.0)
    
tg_medians = [np.median(tg1),np.median(tg2),np.median(tg3),np.median(tg4),np.median(tg5),np.median(tg6),np.median(tg7),np.median(tg8),np.median(tg9),np.median(tg10),np.median(tg11),np.median(tg12),np.median(tg13),np.median(tg14),np.median(tg15),np.median(tg16)]
#Cut off 2019
tg_medians_b = tg_medians[:-4]

tg_annual = [np.median(np.concatenate((tg1,tg2,tg3,tg4))),np.median(np.concatenate((tg5,tg6,tg7,tg8))),np.median(np.concatenate((tg9,tg10,tg11,tg12))),np.median(np.concatenate((tg13,tg14,tg15,tg16)))]
#Cut off 2019
tg_annual_b = tg_annual[:-1]

objects = quarter_index_b
y_pos = np.arange(len(objects))
performance = tg_medians_b

objects2 = year_index_b
y_pos2 = np.arange(len(objects2))
performance2 = tg_annual_b

fig = plt.figure(figsize=(18, 9))

plt.subplot(1, 2, 1)
plt.bar(y_pos, performance, align='center', alpha=0.5, color = 'b')
plt.xticks(y_pos, objects, size = '12', weight = 'bold')
plt.yticks(size = '12', weight = 'bold')
plt.ylabel('ICO Median Telegram Following',fontweight="bold",fontsize=12)
plt.xticks(rotation=60)
plt.title('Quarterly ICO Median Telegram Following',fontweight="bold",fontsize=15)

plt.subplot(1, 2, 2)
plt.bar(y_pos2, performance2, align='center', alpha=0.5, color = 'r')
plt.xticks(y_pos2, objects2, size = '12', weight = 'bold')
plt.yticks(size = '12', weight = 'bold')
plt.ylabel('ICO Median Telegram Following',fontweight="bold",fontsize=12)
plt.xticks(rotation=60)
plt.title('Annual ICO Median Telegram Following',fontweight="bold",fontsize=15)

plt.show()

############################################################
###ICO TWITTER FOLLOWING STATS (Q+Y)
############################################################
for i in range(1,16):
    b = vars()['tw'+str(i)]
    if len(b) == 0:
        b.append(0.0)
    
tw_medians = [np.median(tw1),np.median(tw2),np.median(tw3),np.median(tw4),np.median(tw5),np.median(tw6),np.median(tw7),np.median(tw8),np.median(tw9),np.median(tw10),np.median(tw11),np.median(tw12),np.median(tw13),np.median(tw14),np.median(tw15),np.median(tw16)]
#Cut off 2019
tw_medians_b = tw_medians[:-4]

tw_annual = [np.median(np.concatenate((tw1,tw2,tw3,tw4))),np.median(np.concatenate((tw5,tw6,tw7,tw8))),np.median(np.concatenate((tw9,tw10,tw11,tw12))),np.median(np.concatenate((tw13,tw14,tw15,tw16)))]
#Cut off 2019
tw_annual_b = tw_annual[:-1]

objects = quarter_index_b
y_pos = np.arange(len(objects))
performance = tw_medians_b

objects2 = year_index_b
y_pos2 = np.arange(len(objects2))
performance2 = tw_annual_b

fig = plt.figure(figsize=(18, 9))

plt.subplot(1, 2, 1)
plt.bar(y_pos, performance, align='center', alpha=0.5, color = 'b')
plt.xticks(y_pos, objects, size = '12', weight = 'bold')
plt.yticks(size = '12', weight = 'bold')
plt.ylabel('ICO Median Twitter Following',fontweight="bold",fontsize=12)
plt.xticks(rotation=60)
plt.title('Quarterly ICO Median Twitter Following',fontweight="bold",fontsize=15)

plt.subplot(1, 2, 2)
plt.bar(y_pos2, performance2, align='center', alpha=0.5, color = 'r')
plt.xticks(y_pos2, objects2, size = '12', weight = 'bold')
plt.yticks(size = '12', weight = 'bold')
plt.ylabel('ICO Median Twitter Following',fontweight="bold",fontsize=12)
plt.xticks(rotation=60)
plt.title('Annual ICO Median Twitter Following',fontweight="bold",fontsize=15)

plt.show()

############################################################
###ICO TOKEN PRICE STATS (Q+Y)
############################################################
for i in range(1,16):
    b = vars()['pr'+str(i)]
    if len(b) == 0:
        b.append(0.0)
    
pr_medians = [np.median(pr1),np.median(pr2),np.median(pr3),np.median(pr4),np.median(pr5),np.median(pr6),np.median(pr7),np.median(pr8),np.median(pr9),np.median(pr10),np.median(pr11),np.median(pr12),np.median(pr13),np.median(pr14),np.median(pr15),np.median(pr16)]
#Cut off 2019
pr_medians_b = pr_medians[:-4]

pr_annual = [np.median(np.concatenate((pr1,pr2,pr3,pr4))),np.median(np.concatenate((pr5,pr6,pr7,pr8))),np.median(np.concatenate((pr9,pr10,pr11,pr12))),np.median(np.concatenate((pr13,pr14,pr15,pr16)))]
#Cut off 2019
pr_annual_b = pr_annual[:-1]

objects = quarter_index_b
y_pos = np.arange(len(objects))
performance = pr_medians_b

objects2 = year_index_b
y_pos2 = np.arange(len(objects2))
performance2 = pr_annual_b

fig = plt.figure(figsize=(18, 9))

plt.subplot(1, 2, 1)
plt.bar(y_pos, performance, align='center', alpha=0.5, color = 'b')
plt.xticks(y_pos, objects, size = '12', weight = 'bold')
plt.yticks(size = '12', weight = 'bold')
plt.ylabel('ICO Median Token Price [USD]',fontweight="bold",fontsize=12)
plt.xticks(rotation=60)
plt.title('Quarterly ICO Median Token Price',fontweight="bold",fontsize=15)

plt.subplot(1, 2, 2)
plt.bar(y_pos2, performance2, align='center', alpha=0.5, color = 'r')
plt.xticks(y_pos2, objects2, size = '12', weight = 'bold')
plt.yticks(size = '12', weight = 'bold')
plt.ylabel('ICO Median Token Price [USD]',fontweight="bold",fontsize=12)
plt.xticks(rotation=60)
plt.title('Annual ICO Median Token Price',fontweight="bold",fontsize=15)

plt.show()

############################################################
###ICO ALEXA DAILY VIEWING TIME STATS (Q+Y)
############################################################
for i in range(1,16):
    b = vars()['dv'+str(i)]
    if len(b) == 0:
        b.append(0.0)
    
dv_medians = [np.median(dv1),np.median(dv2),np.median(dv3),np.median(dv4),np.median(dv5),np.median(dv6),np.median(dv7),np.median(dv8),np.median(dv9),np.median(dv10),np.median(dv11),np.median(dv12),np.median(dv13),np.median(dv14),np.median(dv15),np.median(dv16)]
#Cut off 2019
dv_medians_b = dv_medians[:-4]

dv_annual = [np.median(np.concatenate((dv1,dv2,dv3,dv4))),np.median(np.concatenate((dv5,dv6,dv7,dv8))),np.median(np.concatenate((dv9,dv10,dv11,dv12))),np.median(np.concatenate((dv13,dv14,dv15,dv16)))]
#Cut off 2019
dv_annual_b = dv_annual[:-1]

objects = quarter_index_b
y_pos = np.arange(len(objects))
performance = dv_medians_b

objects2 = year_index_b
y_pos2 = np.arange(len(objects2))
performance2 = dv_annual_b

fig = plt.figure(figsize=(18, 9))

plt.subplot(1, 2, 1)
plt.bar(y_pos, performance, align='center', alpha=0.5, color = 'b')
plt.xticks(y_pos, objects, size = '12', weight = 'bold')
plt.yticks(size = '12', weight = 'bold')
plt.ylabel('ICO Median Daily Website Visit Duration [sec]',fontweight="bold",fontsize=12)
plt.xticks(rotation=60)
plt.title('Quarterly ICO Median Daily Website Visit Duration',fontweight="bold",fontsize=15)

plt.subplot(1, 2, 2)
plt.bar(y_pos2, performance2, align='center', alpha=0.5, color = 'r')
plt.xticks(y_pos2, objects2, size = '12', weight = 'bold')
plt.yticks(size = '12', weight = 'bold')
plt.ylabel('ICO Median Daily Website Visit Duration [sec]',fontweight="bold",fontsize=12)
plt.xticks(rotation=60)
plt.title('Annual ICO Median Daily Website Visit Duration',fontweight="bold",fontsize=15)

plt.show()

############################################################
###ICO DAY 1 RETURNS STATS (Q+Y)
############################################################
for i in range(1,16):
    b = vars()['ret'+str(i)]
    if len(b) == 0:
        b.append(0.0)
    
ret_means = [np.mean(ret1),np.mean(ret2),np.mean(ret3),np.mean(ret4),np.mean(ret5),np.mean(ret6),np.mean(ret7),np.mean(ret8),np.mean(ret9),np.mean(ret10),np.mean(ret11),np.mean(ret12),np.mean(ret13),np.mean(ret14),np.mean(ret15),np.mean(ret16)]
#Cut off 2019
ret_means_b = ret_means[:-4]

ret_annual = [np.mean(np.concatenate((ret1,ret2,ret3,ret4))),np.mean(np.concatenate((ret5,ret6,ret7,ret8))),np.mean(np.concatenate((ret9,ret10,ret11,ret12))),np.mean(np.concatenate((ret13,ret14,ret15,ret16)))]
#Cut off 2019
ret_annual_b = ret_annual[:-1]

objects = quarter_index_b
y_pos = np.arange(len(objects))
performance = ret_means_b

objects2 = year_index_b
y_pos2 = np.arange(len(objects2))
performance2 = ret_annual_b

fig = plt.figure(figsize=(18, 9))

plt.subplot(1, 2, 1)
plt.bar(y_pos, performance, align='center', alpha=0.5, color = 'b')
plt.xticks(y_pos, objects, size = '12', weight = 'bold')
plt.yticks(size = '12', weight = 'bold')
plt.ylabel('ICO Mean Day 1 Return',fontweight="bold",fontsize=12)
plt.xticks(rotation=60)
plt.title('Quarterly ICO Mean Day 1 Return upon Listing',fontweight="bold",fontsize=15)

plt.subplot(1, 2, 2)
plt.bar(y_pos2, performance2, align='center', alpha=0.5, color = 'r')
plt.xticks(y_pos2, objects2, size = '12', weight = 'bold')
plt.yticks(size = '12', weight = 'bold')
plt.ylabel('ICO Mean Day 1 Return',fontweight="bold",fontsize=12)
plt.xticks(rotation=60)
plt.title('Annual ICO Mean Day 1 Return upon Listing',fontweight="bold",fontsize=15)

plt.show()

############################################################
###ICO VOLUME 1 RETURNS STATS (Q+Y)
############################################################
for i in range(1,16):
    b = vars()['vol'+str(i)]
    if len(b) == 0:
        b.append(0.0)
    
vol_means = [np.mean(vol1),np.mean(vol2),np.mean(vol3),np.mean(vol4),np.mean(vol5),np.mean(vol6),np.mean(vol7),np.mean(vol8),np.mean(vol9),np.mean(vol10),np.mean(vol11),np.mean(vol12),np.mean(vol13),np.mean(vol14),np.mean(vol15),np.mean(vol16)]
#Cut off 2019
vol_means_b = vol_means[:-4]

vol_annual = [np.mean(np.concatenate((vol1,vol2,vol3,vol4))),np.mean(np.concatenate((vol5,vol6,vol7,vol8))),np.mean(np.concatenate((vol9,vol10,vol11,vol12))),np.mean(np.concatenate((vol13,vol14,vol15,vol16)))]
#Cut off 2019
vol_annual_b = vol_annual[:-1]

objects = quarter_index_b
y_pos = np.arange(len(objects))
performance = vol_means_b

objects2 = year_index_b
y_pos2 = np.arange(len(objects2))
performance2 = vol_annual_b

fig = plt.figure(figsize=(18, 9))

plt.subplot(1, 2, 1)
plt.bar(y_pos, performance, align='center', alpha=0.5, color = 'b')
plt.xticks(y_pos, objects, size = '12', weight = 'bold')
plt.yticks(size = '12', weight = 'bold')
plt.ylabel('ICO Mean Day 1 Volume [USD]',fontweight="bold",fontsize=12)
plt.xticks(rotation=60)
plt.title('Quarterly ICO Mean Day 1 Volume upon Listing',fontweight="bold",fontsize=15)

plt.subplot(1, 2, 2)
plt.bar(y_pos2, performance2, align='center', alpha=0.5, color = 'r')
plt.xticks(y_pos2, objects2, size = '12', weight = 'bold')
plt.yticks(size = '12', weight = 'bold')
plt.ylabel('ICO Mean Day 1 Volume [USD]',fontweight="bold",fontsize=12)
plt.xticks(rotation=60)
plt.title('Annual ICO Mean Day 1 Volume upon Listing',fontweight="bold",fontsize=15)

plt.show()

############################################################
###ICO ANNUALIZED SHARPE RATIO STATS (Q+Y)
############################################################
for i in range(1,16):
    b = vars()['srp'+str(i)]
    if len(b) == 0:
        b.append(0.0)
    
srp_means = [np.mean(srp1),np.mean(srp2),np.mean(srp3),np.mean(srp4),np.mean(srp5),np.mean(srp6),np.mean(srp7),np.mean(srp8),np.mean(srp9),np.mean(srp10),np.mean(srp11),np.mean(srp12),np.mean(srp13),np.mean(srp14),np.mean(srp15),np.mean(srp16)]
#Cut off 2019
srp_means_b = srp_means[:-4]

srp_annual = [np.mean(np.concatenate((srp1,srp2,srp3,srp4))),np.mean(np.concatenate((srp5,srp6,srp7,srp8))),np.mean(np.concatenate((srp9,srp10,srp11,srp12))),np.mean(np.concatenate((srp13,srp14,srp15,srp16)))]
#Cut off 2019
srp_annual_b = srp_annual[:-1]

objects = quarter_index_b
y_pos = np.arange(len(objects))
performance = srp_means_b

objects2 = year_index_b
y_pos2 = np.arange(len(objects2))
performance2 = srp_annual_b

fig = plt.figure(figsize=(18, 9))

plt.subplot(1, 2, 1)
plt.bar(y_pos, performance, align='center', alpha=0.5, color = 'b')
plt.xticks(y_pos, objects, size = '12', weight = 'bold')
plt.yticks(size = '12', weight = 'bold')
plt.ylabel('ICO Mean Annualized Sharpe Ratio',fontweight="bold",fontsize=12)
plt.xticks(rotation=60)
plt.title('Quarterly ICO Mean Annualized Sharpe Ratio',fontweight="bold",fontsize=15)

plt.subplot(1, 2, 2)
plt.bar(y_pos2, performance2, align='center', alpha=0.5, color = 'r')
plt.xticks(y_pos2, objects2, size = '12', weight = 'bold')
plt.yticks(size = '12', weight = 'bold')
plt.ylabel('ICO Mean Annualized Sharpe Ratio',fontweight="bold",fontsize=12)
plt.xticks(rotation=60)
plt.title('Annual ICO Mean Annualized Sharpe Ratio',fontweight="bold",fontsize=15)

plt.show()

############################################################
###ICO INDUSTRY STATS (Q+Y)
############################################################
#Fintech
ind_fin = [q1_fin,q2_fin,q3_fin,q4_fin,q5_fin,q6_fin,q7_fin,q8_fin,q9_fin,q10_fin,q11_fin,q12_fin,q13_fin,q14_fin,q15_fin,q16_fin]
ind_fin = [x / 1000000. for x in ind_fin]
#Cut off 2019
ind_fin_b = ind_fin[:-4]

ind_fin_annual = [(q1_fin+q2_fin+q3_fin+q4_fin),(q5_fin+q6_fin+q7_fin+q8_fin),(q9_fin+q10_fin+q11_fin+q12_fin),(q13_fin+q14_fin+q15_fin+q16_fin)]
ind_fin_annual = [x / 1000000. for x in ind_fin_annual]
#Cut off 2019
ind_fin_annual_b = ind_fin_annual[:-1]

#Blockchain
ind_blk = [q1_blk,q2_blk,q3_blk,q4_blk,q5_blk,q6_blk,q7_blk,q8_blk,q9_blk,q10_blk,q11_blk,q12_blk,q13_blk,q14_blk,q15_blk,q16_blk]
ind_blk = [x / 1000000. for x in ind_blk]
#Cut off 2019
ind_blk_b = ind_blk[:-4]

ind_blk_annual = [(q1_blk+q2_blk+q3_blk+q4_blk),(q5_blk+q6_blk+q7_blk+q8_blk),(q9_blk+q10_blk+q11_blk+q12_blk),(q13_blk+q14_blk+q15_blk+q16_blk)]
ind_blk_annual = [x / 1000000. for x in ind_blk_annual]
#Cut off 2019
ind_blk_annual_b = ind_blk_annual[:-1]

#Real Estate
ind_re = [q1_re,q2_re,q3_re,q4_re,q5_re,q6_re,q7_re,q8_re,q9_re,q10_re,q11_re,q12_re,q13_re,q14_re,q15_re,q16_re]
ind_re = [x / 1000000. for x in ind_re]
#Cut off 2019
ind_re_b = ind_re[:-4]

ind_re_annual = [(q1_re+q2_re+q3_re+q4_re),(q5_re+q6_re+q7_re+q8_re),(q9_re+q10_re+q11_re+q12_re),(q13_re+q14_re+q15_re+q16_re)]
ind_re_annual = [x / 1000000. for x in ind_re_annual]
#Cut off 2019
ind_re_annual_b = ind_re_annual[:-1]

#Social Service
ind_ss = [q1_ss,q2_ss,q3_ss,q4_ss,q5_ss,q6_ss,q7_ss,q8_ss,q9_ss,q10_ss,q11_ss,q12_ss,q13_ss,q14_ss,q15_ss,q16_ss]
ind_ss = [x / 1000000. for x in ind_ss]
#Cut off 2019
ind_ss_b = ind_ss[:-4]

ind_ss_annual = [(q1_ss+q2_ss+q3_ss+q4_ss),(q5_ss+q6_ss+q7_ss+q8_ss),(q9_ss+q10_ss+q11_ss+q12_ss),(q13_ss+q14_ss+q15_ss+q16_ss)]
ind_ss_annual = [x / 1000000. for x in ind_ss_annual]
#Cut off 2019
ind_ss_annual_b = ind_ss_annual[:-1]

#Entertainment
ind_ent = [q1_ent,q2_ent,q3_ent,q4_ent,q5_ent,q6_ent,q7_ent,q8_ent,q9_ent,q10_ent,q11_ent,q12_ent,q13_ent,q14_ent,q15_ent,q16_ent]
ind_ent = [x / 1000000. for x in ind_ent]
#Cut off 2019
ind_ent_b = ind_ent[:-4]

ind_ent_annual = [(q1_ent+q2_ent+q3_ent+q4_ent),(q5_ent+q6_ent+q7_ent+q8_ent),(q9_ent+q10_ent+q11_ent+q12_ent),(q13_ent+q14_ent+q15_ent+q16_ent)]
ind_ent_annual = [x / 1000000. for x in ind_ent_annual]
#Cut off 2019
ind_ent_annual_b = ind_ent_annual[:-1]

#Gaming
ind_gam = [q1_gam,q2_gam,q3_gam,q4_gam,q5_gam,q6_gam,q7_gam,q8_gam,q9_gam,q10_gam,q11_gam,q12_gam,q13_gam,q14_gam,q15_gam,q16_gam]
ind_gam = [x / 1000000. for x in ind_gam]
#Cut off 2019
ind_gam_b = ind_gam[:-4]

ind_gam_annual = [(q1_gam+q2_gam+q3_gam+q4_gam),(q5_gam+q6_gam+q7_gam+q8_gam),(q9_gam+q10_gam+q11_gam+q12_gam),(q13_gam+q14_gam+q15_gam+q16_gam)]
ind_gam_annual = [x / 1000000. for x in ind_gam_annual]
#Cut off 2019
ind_gam_annual_b = ind_gam_annual[:-1]

#Gambling
ind_gmb = [q1_gmb,q2_gmb,q3_gmb,q4_gmb,q5_gmb,q6_gmb,q7_gmb,q8_gmb,q9_gmb,q10_gmb,q11_gmb,q12_gmb,q13_gmb,q14_gmb,q15_gmb,q16_gmb]
ind_gmb = [x / 1000000. for x in ind_gmb]
#Cut off 2019
ind_gmb_b = ind_gmb[:-4]

ind_gmb_annual = [(q1_gmb+q2_gmb+q3_gmb+q4_gmb),(q5_gmb+q6_gmb+q7_gmb+q8_gmb),(q9_gmb+q10_gmb+q11_gmb+q12_gmb),(q13_gmb+q14_gmb+q15_gmb+q16_gmb)]
ind_gmb_annual = [x / 1000000. for x in ind_gmb_annual]
#Cut off 2019
ind_gmb_annual_b = ind_gmb_annual[:-1]

#E-Commerce
ind_eco = [q1_eco,q2_eco,q3_eco,q4_eco,q5_eco,q6_eco,q7_eco,q8_eco,q9_eco,q10_eco,q11_eco,q12_eco,q13_eco,q14_eco,q15_eco,q16_eco]
ind_eco = [x / 1000000. for x in ind_eco]
#Cut off 2019
ind_eco_b = ind_eco[:-4]

ind_eco_annual = [(q1_eco+q2_eco+q3_eco+q4_eco),(q5_eco+q6_eco+q7_eco+q8_eco),(q9_eco+q10_eco+q11_eco+q12_eco),(q13_eco+q14_eco+q15_eco+q16_eco)]
ind_eco_annual = [x / 1000000. for x in ind_eco_annual]
#Cut off 2019
ind_eco_annual_b = ind_eco_annual[:-1]

#SaaS
ind_sas = [q1_sas,q2_sas,q3_sas,q4_sas,q5_sas,q6_sas,q7_sas,q8_sas,q9_sas,q10_sas,q11_sas,q12_sas,q13_sas,q14_sas,q15_sas,q16_sas]
ind_sas = [x / 1000000. for x in ind_sas]
#Cut off 2019
ind_sas_b = ind_sas[:-4]

ind_sas_annual = [(q1_sas+q2_sas+q3_sas+q4_sas),(q5_sas+q6_sas+q7_sas+q8_sas),(q9_sas+q10_sas+q11_sas+q12_sas),(q13_sas+q14_sas+q15_sas+q16_sas)]
ind_sas_annual = [x / 1000000. for x in ind_sas_annual]
#Cut off 2019
ind_sas_annual_b = ind_sas_annual[:-1]

#Transportation
ind_trs = [q1_trs,q2_trs,q3_trs,q4_trs,q5_trs,q6_trs,q7_trs,q8_trs,q9_trs,q10_trs,q11_trs,q12_trs,q13_trs,q14_trs,q15_trs,q16_trs]
ind_trs = [x / 1000000. for x in ind_trs]
#Cut off 2019
ind_trs_b = ind_trs[:-4]

ind_trs_annual = [(q1_trs+q2_trs+q3_trs+q4_trs),(q5_trs+q6_trs+q7_trs+q8_trs),(q9_trs+q10_trs+q11_trs+q12_trs),(q13_trs+q14_trs+q15_trs+q16_trs)]
ind_trs_annual = [x / 1000000. for x in ind_trs_annual]
#Cut off 2019
ind_trs_annual_b = ind_trs_annual[:-1]

#Law
ind_law = [q1_law,q2_law,q3_law,q4_law,q5_law,q6_law,q7_law,q8_law,q9_law,q10_law,q11_law,q12_law,q13_law,q14_law,q15_law,q16_law]
ind_law = [x / 1000000. for x in ind_law]
#Cut off 2019
ind_law_b = ind_law[:-4]

ind_law_annual = [(q1_law+q2_law+q3_law+q4_law),(q5_law+q6_law+q7_law+q8_law),(q9_law+q10_law+q11_law+q12_law),(q13_law+q14_law+q15_law+q16_law)]
ind_law_annual = [x / 1000000. for x in ind_law_annual]
#Cut off 2019
ind_law_annual_b = ind_law_annual[:-1]

#Insurances
ind_ins = [q1_ins,q2_ins,q3_ins,q4_ins,q5_ins,q6_ins,q7_ins,q8_ins,q9_ins,q10_ins,q11_ins,q12_ins,q13_ins,q14_ins,q15_ins,q16_ins]
ind_ins = [x / 1000000. for x in ind_ins]
#Cut off 2019
ind_ins_b = ind_ins[:-4]

ind_ins_annual = [(q1_ins+q2_ins+q3_ins+q4_ins),(q5_ins+q6_ins+q7_ins+q8_ins),(q9_ins+q10_ins+q11_ins+q12_ins),(q13_ins+q14_ins+q15_ins+q16_ins)]
ind_ins_annual = [x / 1000000. for x in ind_ins_annual]
#Cut off 2019
ind_ins_annual_b = ind_ins_annual[:-1]

#Telecom
ind_tel = [q1_tel,q2_tel,q3_tel,q4_tel,q5_tel,q6_tel,q7_tel,q8_tel,q9_tel,q10_tel,q11_tel,q12_tel,q13_tel,q14_tel,q15_tel,q16_tel]
ind_tel = [x / 1000000. for x in ind_tel]
#Cut off 2019
ind_tel_b = ind_tel[:-4]

ind_tel_annual = [(q1_tel+q2_tel+q3_tel+q4_tel),(q5_tel+q6_tel+q7_tel+q8_tel),(q9_tel+q10_tel+q11_tel+q12_tel),(q13_tel+q14_tel+q15_tel+q16_tel)]
ind_tel_annual = [x / 1000000. for x in ind_tel_annual]
#Cut off 2019
ind_tel_annual_b = ind_tel_annual[:-1]

#Energy
ind_ener = [q1_ener,q2_ener,q3_ener,q4_ener,q5_ener,q6_ener,q7_ener,q8_ener,q9_ener,q10_ener,q11_ener,q12_ener,q13_ener,q14_ener,q15_ener,q16_ener]
ind_ener = [x / 1000000. for x in ind_ener]
#Cut off 2019
ind_ener_b = ind_ener[:-4]

ind_ener_annual = [(q1_ener+q2_ener+q3_ener+q4_ener),(q5_ener+q6_ener+q7_ener+q8_ener),(q9_ener+q10_ener+q11_ener+q12_ener),(q13_ener+q14_ener+q15_ener+q16_ener)]
ind_ener_annual = [x / 1000000. for x in ind_ener_annual]
#Cut off 2019
ind_ener_annual_b = ind_ener_annual[:-1]

fig = plt.figure(figsize=(19, 9))

plt.subplot(1, 2, 1)
plt.plot(quarter_index_b,ind_fin_b, color='blue', label = 'Fintech')
plt.plot(quarter_index_b,ind_blk_b, color='red', label = 'Blockchain')
plt.plot(quarter_index_b,ind_re_b, color='green', label = 'Real Estate')
plt.plot(quarter_index_b,ind_ss_b, color='orange', label = 'Social Services')
plt.plot(quarter_index_b,ind_ent_b, color='cyan', label = 'Entertainment')
plt.plot(quarter_index_b,ind_gam_b, color='magenta', label = 'Gaming')
plt.plot(quarter_index_b,ind_gmb_b, color='black', label = 'Gambling')
plt.plot(quarter_index_b,ind_eco_b, color='yellow', label = 'E-Commerce')
plt.plot(quarter_index_b,ind_sas_b, color='darkgray', label = 'SaaS')
plt.plot(quarter_index_b,ind_trs_b, color='indianred', label = 'Transportation')
plt.plot(quarter_index_b,ind_law_b, color='lightgreen', label = 'Legal')
plt.plot(quarter_index_b,ind_ins_b, color='y', label = 'Insurance')
plt.plot(quarter_index_b,ind_tel_b, color='pink', label = 'Telecommunications')
plt.plot(quarter_index_b,ind_ener_b, color='purple', label = 'Energy')
plt.ylabel('Funds Raised [millions of USD]',fontweight="bold",fontsize=12)
plt.xticks(rotation=60)
plt.xticks(size = '12', weight = 'bold')
plt.yticks(size = '12', weight = 'bold')
plt.title('Quarterly Funds Raised by Industry Category',fontweight="bold",fontsize=15)
plt.legend()

plt.subplot(1, 2, 2)
plt.plot(year_index_b,ind_fin_annual_b, color='blue', label = 'Fintech')
plt.plot(year_index_b,ind_blk_annual_b, color='red', label = 'Blockchain')
plt.plot(year_index_b,ind_re_annual_b, color='green', label = 'Real Estate')
plt.plot(year_index_b,ind_ss_annual_b, color='orange', label = 'Social Services')
plt.plot(year_index_b,ind_ent_annual_b, color='cyan', label = 'Entertainment')
plt.plot(year_index_b,ind_gam_annual_b, color='magenta', label = 'Gaming')
plt.plot(year_index_b,ind_gmb_annual_b, color='black', label = 'Gambling')
plt.plot(year_index_b,ind_eco_annual_b, color='yellow', label = 'E-Commerce')
plt.plot(year_index_b,ind_sas_annual_b, color='darkgray', label = 'SaaS')
plt.plot(year_index_b,ind_trs_annual_b, color='indianred', label = 'Transportation')
plt.plot(year_index_b,ind_law_annual_b, color='lightgreen', label = 'Legal')
plt.plot(year_index_b,ind_ins_annual_b, color='y', label = 'Insurance')
plt.plot(year_index_b,ind_tel_annual_b, color='pink', label = 'Telecommunications')
plt.plot(year_index_b,ind_ener_annual_b, color='purple', label = 'Energy')
plt.ylabel('Funds Raised [millions of USD]',fontweight="bold",fontsize=12)
plt.xticks(rotation=60)
plt.xticks(size = '12', weight = 'bold')
plt.yticks(size = '12', weight = 'bold')
plt.title('Annual Funds Raised by Industry Category',fontweight="bold",fontsize=15)
plt.legend()

plt.show()

#Y-axis constrained to 500M without fintech and blockchain shown

fig = plt.figure(figsize=(19, 9))

plt.subplot(1, 2, 1)
#plt.plot(quarter_index_b,ind_fin_b, color='blue', label = 'Fintech')
#plt.plot(quarter_index_b,ind_blk_b, color='red', label = 'Blockchain')
plt.plot(quarter_index_b,ind_re_b, color='green', label = 'Real Estate')
plt.plot(quarter_index_b,ind_ss_b, color='orange', label = 'Social Services')
plt.plot(quarter_index_b,ind_ent_b, color='cyan', label = 'Entertainment')
plt.plot(quarter_index_b,ind_gam_b, color='magenta', label = 'Gaming')
plt.plot(quarter_index_b,ind_gmb_b, color='black', label = 'Gambling')
plt.plot(quarter_index_b,ind_eco_b, color='yellow', label = 'E-Commerce')
plt.plot(quarter_index_b,ind_sas_b, color='darkgray', label = 'SaaS')
plt.plot(quarter_index_b,ind_trs_b, color='indianred', label = 'Transportation')
plt.plot(quarter_index_b,ind_law_b, color='lightgreen', label = 'Legal')
plt.plot(quarter_index_b,ind_ins_b, color='y', label = 'Insurance')
plt.plot(quarter_index_b,ind_tel_b, color='pink', label = 'Telecommunications')
plt.plot(quarter_index_b,ind_ener_b, color='purple', label = 'Energy')
plt.ylabel('Funds Raised [millions of USD]',fontweight="bold",fontsize=12)
plt.xticks(rotation=60)
plt.xticks(size = '12', weight = 'bold')
plt.yticks(size = '12', weight = 'bold')
plt.title('Quarterly Funds Raised by Industry Category',fontweight="bold",fontsize=15)
plt.ylim([0.0,500.0])
plt.legend()

plt.subplot(1, 2, 2)
#plt.plot(year_index_b,ind_fin_annual_b, color='blue', label = 'Fintech')
#plt.plot(year_index_b,ind_blk_annual_b, color='red', label = 'Blockchain')
plt.plot(year_index_b,ind_re_annual_b, color='green', label = 'Real Estate')
plt.plot(year_index_b,ind_ss_annual_b, color='orange', label = 'Social Services')
plt.plot(year_index_b,ind_ent_annual_b, color='cyan', label = 'Entertainment')
plt.plot(year_index_b,ind_gam_annual_b, color='magenta', label = 'Gaming')
plt.plot(year_index_b,ind_gmb_annual_b, color='black', label = 'Gambling')
plt.plot(year_index_b,ind_eco_annual_b, color='yellow', label = 'E-Commerce')
plt.plot(year_index_b,ind_sas_annual_b, color='darkgray', label = 'SaaS')
plt.plot(year_index_b,ind_trs_annual_b, color='indianred', label = 'Transportation')
plt.plot(year_index_b,ind_law_annual_b, color='lightgreen', label = 'Legal')
plt.plot(year_index_b,ind_ins_annual_b, color='y', label = 'Insurance')
plt.plot(year_index_b,ind_tel_annual_b, color='pink', label = 'Telecommunications')
plt.plot(year_index_b,ind_ener_annual_b, color='purple', label = 'Energy')
plt.ylabel('Funds Raised [millions of USD]',fontweight="bold",fontsize=12)
plt.xticks(rotation=60)
plt.xticks(size = '12', weight = 'bold')
plt.yticks(size = '12', weight = 'bold')
plt.title('Annual Funds Raised by Industry Category',fontweight="bold",fontsize=15)
plt.ylim([0.0,500.0])
plt.legend()

plt.show()

############################################################
###ICO COUNTRY/ASGION STATS (Q+Y)
############################################################
#North America
ind_na = [q1_na,q2_na,q3_na,q4_na,q5_na,q6_na,q7_na,q8_na,q9_na,q10_na,q11_na,q12_na,q13_na,q14_na,q15_na,q16_na]
ind_na = [x / 1000000. for x in ind_na]
#Cut off 2019
ind_na_b = ind_na[:-4]

ind_na_annual = [(q1_na+q2_na+q3_na+q4_na),(q5_na+q6_na+q7_na+q8_na),(q9_na+q10_na+q11_na+q12_na),(q13_na+q14_na+q15_na+q16_na)]
ind_na_annual = [x / 1000000. for x in ind_na_annual]
#Cut off 2019
ind_na_annual_b = ind_na_annual[:-1]

#Russia
ind_rs = [q1_rs,q2_rs,q3_rs,q4_rs,q5_rs,q6_rs,q7_rs,q8_rs,q9_rs,q10_rs,q11_rs,q12_rs,q13_rs,q14_rs,q15_rs,q16_rs]
ind_rs = [x / 1000000. for x in ind_rs]
#Cut off 2019
ind_rs_b = ind_rs[:-4]

ind_rs_annual = [(q1_rs+q2_rs+q3_rs+q4_rs),(q5_rs+q6_rs+q7_rs+q8_rs),(q9_rs+q10_rs+q11_rs+q12_rs),(q13_rs+q14_rs+q15_rs+q16_rs)]
ind_rs_annual = [x / 1000000. for x in ind_rs_annual]
#Cut off 2019
ind_rs_annual_b = ind_rs_annual[:-1]

#Asia
ind_as = [q1_as,q2_as,q3_as,q4_as,q5_as,q6_as,q7_as,q8_as,q9_as,q10_as,q11_as,q12_as,q13_as,q14_as,q15_as,q16_as]
ind_as = [x / 1000000. for x in ind_as]
#Cut off 2019
ind_as_b = ind_as[:-4]

ind_as_annual = [(q1_as+q2_as+q3_as+q4_as),(q5_as+q6_as+q7_as+q8_as),(q9_as+q10_as+q11_as+q12_as),(q13_as+q14_as+q15_as+q16_as)]
ind_as_annual = [x / 1000000. for x in ind_as_annual]
#Cut off 2019
ind_as_annual_b = ind_as_annual[:-1]

#United Kingdom
ind_uk = [q1_uk,q2_uk,q3_uk,q4_uk,q5_uk,q6_uk,q7_uk,q8_uk,q9_uk,q10_uk,q11_uk,q12_uk,q13_uk,q14_uk,q15_uk,q16_uk]
ind_uk = [x / 1000000. for x in ind_uk]
#Cut off 2019
ind_uk_b = ind_uk[:-4]

ind_uk_annual = [(q1_uk+q2_uk+q3_uk+q4_uk),(q5_uk+q6_uk+q7_uk+q8_uk),(q9_uk+q10_uk+q11_uk+q12_uk),(q13_uk+q14_uk+q15_uk+q16_uk)]
ind_uk_annual = [x / 1000000. for x in ind_uk_annual]
#Cut off 2019
ind_uk_annual_b = ind_uk_annual[:-1]

#European Union
ind_eu = [q1_eu,q2_eu,q3_eu,q4_eu,q5_eu,q6_eu,q7_eu,q8_eu,q9_eu,q10_eu,q11_eu,q12_eu,q13_eu,q14_eu,q15_eu,q16_eu]
ind_eu = [x / 1000000. for x in ind_eu]
#Cut off 2019
ind_eu_b = ind_eu[:-4]

ind_eu_annual = [(q1_eu+q2_eu+q3_eu+q4_eu),(q5_eu+q6_eu+q7_eu+q8_eu),(q9_eu+q10_eu+q11_eu+q12_eu),(q13_eu+q14_eu+q15_eu+q16_eu)]
ind_eu_annual = [x / 1000000. for x in ind_eu_annual]
#Cut off 2019
ind_eu_annual_b = ind_eu_annual[:-1]

#Switzerland
ind_sw = [q1_sw,q2_sw,q3_sw,q4_sw,q5_sw,q6_sw,q7_sw,q8_sw,q9_sw,q10_sw,q11_sw,q12_sw,q13_sw,q14_sw,q15_sw,q16_sw]
ind_sw = [x / 1000000. for x in ind_sw]
#Cut off 2019
ind_sw_b = ind_sw[:-4]

ind_sw_annual = [(q1_sw+q2_sw+q3_sw+q4_sw),(q5_sw+q6_sw+q7_sw+q8_sw),(q9_sw+q10_sw+q11_sw+q12_sw),(q13_sw+q14_sw+q15_sw+q16_sw)]
ind_sw_annual = [x / 1000000. for x in ind_sw_annual]
#Cut off 2019
ind_sw_annual_b = ind_sw_annual[:-1]

#Tax Havens
ind_th = [q1_th,q2_th,q3_th,q4_th,q5_th,q6_th,q7_th,q8_th,q9_th,q10_th,q11_th,q12_th,q13_th,q14_th,q15_th,q16_th]
ind_th = [x / 1000000. for x in ind_th]
#Cut off 2019
ind_th_b = ind_th[:-4]

ind_th_annual = [(q1_th+q2_th+q3_th+q4_th),(q5_th+q6_th+q7_th+q8_th),(q9_th+q10_th+q11_th+q12_th),(q13_th+q14_th+q15_th+q16_th)]
ind_th_annual = [x / 1000000. for x in ind_th_annual]
#Cut off 2019
ind_th_annual_b = ind_th_annual[:-1]

#Japan/South Koasa
ind_jk = [q1_jk,q2_jk,q3_jk,q4_jk,q5_jk,q6_jk,q7_jk,q8_jk,q9_jk,q10_jk,q11_jk,q12_jk,q13_jk,q14_jk,q15_jk,q16_jk]
ind_jk = [x / 1000000. for x in ind_jk]
#Cut off 2019
ind_jk_b = ind_jk[:-4]

ind_jk_annual = [(q1_jk+q2_jk+q3_jk+q4_jk),(q5_jk+q6_jk+q7_jk+q8_jk),(q9_jk+q10_jk+q11_jk+q12_jk),(q13_jk+q14_jk+q15_jk+q16_jk)]
ind_jk_annual = [x / 1000000. for x in ind_jk_annual]
#Cut off 2019
ind_jk_annual_b = ind_jk_annual[:-1]

#Oceania
ind_au = [q1_au,q2_au,q3_au,q4_au,q5_au,q6_au,q7_au,q8_au,q9_au,q10_au,q11_au,q12_au,q13_au,q14_au,q15_au,q16_au]
ind_au = [x / 1000000. for x in ind_au]
#Cut off 2019
ind_au_b = ind_au[:-4]

ind_au_annual = [(q1_au+q2_au+q3_au+q4_au),(q5_au+q6_au+q7_au+q8_au),(q9_au+q10_au+q11_au+q12_au),(q13_au+q14_au+q15_au+q16_au)]
ind_au_annual = [x / 1000000. for x in ind_au_annual]
#Cut off 2019
ind_au_annual_b = ind_au_annual[:-1]

#South America
ind_sa = [q1_sa,q2_sa,q3_sa,q4_sa,q5_sa,q6_sa,q7_sa,q8_sa,q9_sa,q10_sa,q11_sa,q12_sa,q13_sa,q14_sa,q15_sa,q16_sa]
ind_sa = [x / 1000000. for x in ind_sa]
#Cut off 2019
ind_sa_b = ind_sa[:-4]

ind_sa_annual = [(q1_sa+q2_sa+q3_sa+q4_sa),(q5_sa+q6_sa+q7_sa+q8_sa),(q9_sa+q10_sa+q11_sa+q12_sa),(q13_sa+q14_sa+q15_sa+q16_sa)]
ind_sa_annual = [x / 1000000. for x in ind_sa_annual]
#Cut off 2019
ind_sa_annual_b = ind_sa_annual[:-1]

#Africa
ind_af = [q1_af,q2_af,q3_af,q4_af,q5_af,q6_af,q7_af,q8_af,q9_af,q10_af,q11_af,q12_af,q13_af,q14_af,q15_af,q16_af]
ind_af = [x / 1000000. for x in ind_af]
#Cut off 2019
ind_af_b = ind_af[:-4]

ind_af_annual = [(q1_af+q2_af+q3_af+q4_af),(q5_af+q6_af+q7_af+q8_af),(q9_af+q10_af+q11_af+q12_af),(q13_af+q14_af+q15_af+q16_af)]
ind_af_annual = [x / 1000000. for x in ind_af_annual]
#Cut off 2019
ind_af_annual_b = ind_af_annual[:-1]

fig = plt.figure(figsize=(19, 9))

plt.subplot(1, 2, 1)
plt.plot(quarter_index_b,ind_na_b, color='blue', label = 'USA')
plt.plot(quarter_index_b,ind_rs_b, color='red', label = 'Russia')
plt.plot(quarter_index_b,ind_as_b, color='green', label = 'China')
plt.plot(quarter_index_b,ind_uk_b, color='orange', label = 'UK')
plt.plot(quarter_index_b,ind_eu_b, color='cyan', label = 'EU')
plt.plot(quarter_index_b,ind_sw_b, color='magenta', label = 'Switzerland')
plt.plot(quarter_index_b,ind_th_b, color='black', label = 'Offshore')
plt.plot(quarter_index_b,ind_jk_b, color='yellow', label = 'Japan/S. Korea')
plt.plot(quarter_index_b,ind_au_b, color='darkgray', label = 'Oceania')
plt.plot(quarter_index_b,ind_sa_b, color='indianred', label = 'South America')
plt.plot(quarter_index_b,ind_af_b, color='lightgreen', label = 'Africa')
plt.ylabel('Funds Raised [millions of USD]',fontweight="bold",fontsize=12)
plt.xticks(rotation=60)
plt.xticks(size = '12', weight = 'bold')
plt.yticks(size = '12', weight = 'bold')
plt.title('Quarterly Funds Raised by Region',fontweight="bold",fontsize=15)
plt.legend()

plt.subplot(1, 2, 2)
plt.plot(year_index_b,ind_na_annual_b, color='blue', label = 'USA')
plt.plot(year_index_b,ind_rs_annual_b, color='red', label = 'Russia')
plt.plot(year_index_b,ind_as_annual_b, color='green', label = 'China')
plt.plot(year_index_b,ind_uk_annual_b, color='orange', label = 'UK')
plt.plot(year_index_b,ind_eu_annual_b, color='cyan', label = 'EU')
plt.plot(year_index_b,ind_sw_annual_b, color='magenta', label = 'Switzerland')
plt.plot(year_index_b,ind_th_annual_b, color='black', label = 'Offshore')
plt.plot(year_index_b,ind_jk_annual_b, color='yellow', label = 'Japan/S. Korea')
plt.plot(year_index_b,ind_au_annual_b, color='darkgray', label = 'Oceania')
plt.plot(year_index_b,ind_sa_annual_b, color='indianred', label = 'South America')
plt.plot(year_index_b,ind_af_annual_b, color='lightgreen', label = 'Africa')
plt.ylabel('Funds Raised [millions of USD]',fontweight="bold",fontsize=12)
plt.xticks(rotation=60)
plt.xticks(size = '12', weight = 'bold')
plt.yticks(size = '12', weight = 'bold')
plt.title('Annual Funds Raised by Region',fontweight="bold",fontsize=15)
plt.legend()

plt.show()

#Y-axis constrained to 500M without fintech and blockchain shown

fig = plt.figure()
