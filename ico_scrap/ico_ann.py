import csv
from csv import *
from numpy import *
import numpy as np
import sys
from matplotlib import pyplot as plt
import matplotlib.cm as cm
from region_category import func_region
from industry_category import func_industry
from scrap_icos_main_func import ico_data_collector
from top10_returns import func_top10
from bitcoin_returns import func_btc
import pandas as pd

#First we determine what is the best combination of 5 features so
#that the size of the dataset is maximized

with open("outdata/ico_data_reduced.csv") as f:
    reader = csv.reader(f)
    data = [r for r in reader]

data = np.asarray(data)

feature1= 'price'     # 1194
feature2= 'hardcap'   # 1133
feature3= 'telegram'  # 924
feature4 = 'N_daily_views' # 875
feature5 = 'N_daily_time' # 875
feature6 = 'region' # 1006
feature7 = 'team' # 1080
feature8 = 'N_twitter' # 1000
feature9 = 'industry' # 730
feature10 = 'age'

var = 'success'

feature_set = [feature1, feature2, feature3, feature4, feature5, feature6, feature7, feature8, feature9, feature10, var]

ind_feature = []
k = - 1
for feature in feature_set:
    k = k + 1
    ind_feature.append(k)
    ind_feature[k] = np.where(data[0,:]==feature)[0][0]


columnTitles = "name,age,price,hardcap,social,daily_views,daily_time,success\n"

with open('outdata/ico_ann_data.csv', 'w') as csvfile:
    csvfile.write(columnTitles)
    writer=csv.writer(csvfile, delimiter=',')    

    num_data = 0
    complete_dataset = []
    m = -1
    for i in range(1,len(data)):
        if (data[i,ind_feature[10]] not in ['N/A','other','12']):
            success = eval(data[i,ind_feature[10]])
            name = data[i,0]

            """
            if 0.0 <= success < 0.25:
                success = int(4)
            if 0.25 <= success < 0.5:
                success = int(3)
            if 0.5 <= success < 0.75:
                success = int(2)
            if 0.75 <= success <= 1.0:
                success = int(1)
            """
            
            if 0.0 <= success < 0.5:
                success = int(0)
            if 0.5 <= success <= 1.0:
                success = int(1)
                

            if (data[i,ind_feature[2]] not in ['N/A','other','12']) or (data[i,ind_feature[7]] not in ['N/A','other','12']):
                social = data[i,ind_feature[2]]
            if (data[i,ind_feature[2]] in ['N/A','other','12']) and (data[i,ind_feature[7]] not in ['N/A','other','12']):
                social = data[i,ind_feature[7]]
            if (data[i,ind_feature[2]] not in ['N/A','other','12']) and (data[i,ind_feature[7]] in ['N/A','other','12']):
                social = data[i,ind_feature[2]]
            if (data[i,ind_feature[2]] in ['N/A','other','12']) and (data[i,ind_feature[7]] in ['N/A','other','12']):
                social = 'N/A'

            if (data[i,ind_feature[0]] not in ['N/A','other','12']) and (data[i,ind_feature[1]] not in ['N/A','other','12']) and (social not in ['N/A','other','12']) and (data[i,ind_feature[3]] not in ['N/A','other','12']) and (data[i,ind_feature[4]] not in ['N/A','other','12']) and (data[i,ind_feature[9]] not in ['N/A','other','12']):
                m = m + 1
            
                price = eval(data[i,ind_feature[0]])
                hardcap = eval(data[i,ind_feature[1]])
                daily_views = eval(data[i,ind_feature[3]])
                daily_time = eval(data[i,ind_feature[4]])
                age = abs(eval(data[i,ind_feature[9]]))
                social = eval(social)
            
                complete_dataset.append(m)
                complete_dataset[m] = [age,price,hardcap,social,daily_views,daily_time,success]
                writer.writerow([name,age,price,hardcap,social,daily_views,daily_time,success])  


import pandas as pd
icos = pd.read_csv('outdata/ico_ann_data.csv')

X = icos.drop('success',axis=1).drop('name',axis=1)
y = icos['success']

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y)

from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
scaler.fit(X_train)
X_train = scaler.transform(X_train)
X_train2 = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

from sklearn.neural_network import MLPClassifier
#mlp = MLPClassifier(hidden_layer_sizes=(13,13,13),max_iter=500)
mlp = MLPClassifier(hidden_layer_sizes=(6,6,6),max_iter=1000)
mlp.fit(X_train,y_train)
predictions = mlp.predict(X_test)

from sklearn.metrics import classification_report,confusion_matrix

##########################################################################################################
##########################################################################################################
##########################################################################################################
#Prediction for input ICO
#OPTIONS: region,industry,team,raised,hardcap,price,telegram,N_google_news,N_twitter,hype,risk,bazaar-rate
#raised goes for completed ICOs not for in-progress or planned ICOs

#TEST INPUT
#user_input = ['182.0',   '0.50000',  ' 50000000.0',    '1693',          '1.4',       '100.0']

ICO_name = input("Enter ICO Name: \n")
ICO_name = ICO_name.replace(" ","")
ICO_token = input("Enter ICO token Name: \n")

bitcoin = func_btc()
top10s = func_top10()
ico_data = ico_data_collector([ICO_name,ICO_token,ICO_name],bitcoin,top10s)[1]
#revert to verbose region variable
if ico_data[5] == 1:
    reg = 'usa'
if ico_data[5] == 2:
    reg = 'russia'
if ico_data[5] == 3:
    reg = 'china'
if ico_data[5] == 4:
    reg = 'uk'
if ico_data[5] == 5:
    reg = 'estonia'
if ico_data[5] == 6:
    reg = 'switzerland'
if ico_data[5] == 7:
    reg = 'singapore'
if ico_data[5] == 8:
    reg = 'japan'
if ico_data[5] == 9:
    reg = 'australia'
if ico_data[5] == 10:
    reg = 'brazil'
if ico_data[5] == 11:
    reg = 'south africa'
if ico_data[5] == 12:
    reg = 'mongolia'

user_input = []
user_input.append(reg)
user_input.append(ico_data[4])
user_input.append(ico_data[6])
user_input.append(ico_data[7])
user_input.append(ico_data[9])
user_input.append(ico_data[11])
user_input.append(ico_data[12])
user_input.append(ico_data[13])
user_input.append(ico_data[14])
user_input.append(ico_data[15])
user_input.append(ico_data[16])

features_vec = ['region','age','industry','team','hardcap','price','telegram','N_google_news','N_twitter','N_daily_views','N_daily_time']

for i in range(0,len(user_input)):
    if user_input[i] != 'N/A':
        user_input[i] = str(user_input[i])
    if user_input[i] == 'N/A':
        user_input[i] = input("Enter ICO feature: "+features_vec[i]+"\n")

print('Feature list: region,age,industry,team,hardcap,price,telegram,N_google_news,N_twitter,N_daily_views,N_daily_time')
print('The following features were found for the',ICO_name,' ICO:', user_input)

if (user_input[6] not in ['N/A','other','12']) or (user_input[8] not in ['N/A','other','12']):
    social_in = eval(data[i,ind_feature[6]])
if (user_input[6] in ['N/A','other','12']) and (user_input[8] not in ['N/A','other','12']):
    social_in = eval(data[i,ind_feature[8]])
if (user_input[6] not in ['N/A','other','12']) and (user_input[8] in ['N/A','other','12']):
    social_in = eval(data[i,ind_feature[6]])
if (user_input[6] in ['N/A','other','12']) and (user_input[8] in ['N/A','other','12']):
    social_in = 'N/A'

print(confusion_matrix(y_test,predictions))
print(classification_report(y_test,predictions))

try:
#Age, Price, Hardcap, Social, Daily Views, Daily Time
    X_in = [abs(eval(user_input[1])),   eval(user_input[5]), eval(user_input[4]), social_in, eval(user_input[9]), eval(user_input[10])]
    X_in = (np.asarray(X_in)).reshape(1, -1)
    print('ANN USING SKLEARN')
    print('FOR THE INPUT ICO FEATURES, THE PREDICTED SUCCESS CATEGORY IS: ',mlp.predict(X_in)[0])
    print('0 MEANS SUCCESS < 50%. 1 MEANS SUCCESS > 50%')
except:
    print('ANN USING SKLEARN')
    print('THE INPUT DATA FOR THIS ICO IS INCOMPLETE. CLASSIFICATION ABORTED.')


### METHOD 2:
# Importing the dataset
dataset = pd.read_csv('outdata/ico_ann_data.csv')
X = dataset.iloc[:, 1:7].values
y = dataset.iloc[:, 7].values

# Encoding categorical data
#from sklearn.preprocessing import LabelEncoder, OneHotEncoder
#labelencoder_X_1 = LabelEncoder()
#X[:, 1] = labelencoder_X_1.fit_transform(X[:, 1])
#labelencoder_X_2 = LabelEncoder()
#X[:, 2] = labelencoder_X_2.fit_transform(X[:, 2])
#onehotencoder = OneHotEncoder(categorical_features = [1])
#X = onehotencoder.fit_transform(X).toarray()
#X = X[:, 1:]

# Splitting the dataset into the Training set and Test set
#from sklearn.model_selection import train_test_split
from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)

# Feature Scaling
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

# Part 2 - Now let's make the ANN!

# Importing the Keras libraries and packages
import keras
import tensorflow
from keras.models import Sequential
from keras.layers import Dense

# Initialising the ANN
classifier = Sequential()

# Adding the input layer and the first hidden layer
classifier.add(Dense(units = 12, kernel_initializer = 'uniform', activation = 'relu', input_dim = 6))

# Adding the second hidden layer
classifier.add(Dense(units = 12, kernel_initializer = 'uniform', activation = 'relu'))

# Adding the third hidden layer
classifier.add(Dense(units = 12, kernel_initializer = 'uniform', activation = 'relu'))

# Adding the output layer
classifier.add(Dense(units = 1, kernel_initializer = 'uniform', activation = 'sigmoid'))

# Compiling the ANN
classifier.compile(optimizer = 'adam', loss = 'binary_crossentropy', metrics = ['accuracy'])

# Fitting the ANN to the Training set
classifier.fit(X_train, y_train, batch_size = 20, epochs = 1000)
#classifier.fit(X_train, y_train, batch_size = 10, epochs = 100)

# Part 3 - Making predictions and evaluating the model

# Predicting the Test set results
y_pred = classifier.predict(X_test)
y_pred = (y_pred > 0.5)

# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix

# Making the Confusion Matrix and the Classification Report
cm = confusion_matrix(y_test, y_pred)
cr = classification_report(y_test,y_pred)
print(cm)
print(cr)

try:
#Age, Price, Hardcap, Social, Daily Views, Daily Time
    X_in = [abs(eval(user_input[1])),   eval(user_input[5]), eval(user_input[4]), social_in, eval(user_input[9]), eval(user_input[10])]
    X_in = (np.asarray(X_in)).reshape(1, -1)
    print('ANN USING KERAS')
    print('FOR THE INPUT ICO FEATURES, THE PREDICTED SUCCESS CATEGORY IS: ',classifier.predict(X_in)[0][0])
    print('0 MEANS SUCCESS < 50%. 1 MEANS SUCCESS > 50%')
except:
    print('ANN USING KERAS')
    print('THE INPUT DATA FOR THIS ICO IS INCOMPLETE. CLASSIFICATION ABORTED.')
