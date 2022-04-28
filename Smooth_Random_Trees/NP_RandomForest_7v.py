#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 19 11:13:09 2022

@author: anaritapena
"""
import pandas as pd    
import sklearn.metrics
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import MinMaxScaler
from sklearn.ensemble import RandomForestClassifier

train = pd.read_csv('train.csv',index_col=False)
train = train.drop(columns=['2','3','12','9','10','14','13'])      
#train = train.values.tolist()

test = pd.read_csv('test.csv',index_col=False)
test = test.drop(columns=['2','3','12','9','10','14','13'])   
#test = test.values.tolist()

x_train=train.drop(columns='0')
y_train=train['0']

x_test=test.drop(columns='0')
y_test=test['0']


#One-hot enconding

enc = OneHotEncoder(handle_unknown='ignore')
enc.fit(x_train)
x_train=enc.transform(x_train).toarray()

#enc_test = OneHotEncoder(handle_unknown='ignore')
#enc_test.fit(x_test)

n_trees=50

#No loop
x_test=enc.transform(x_test).toarray()

# model = RandomForestClassifier(n_estimators=n_trees)
# model.fit(x_train, y_train)
# # make a single prediction
# #row = [[-8.52381793,5.24451077,-12.14967704,-2.92949242,0.99314133,0.67326595,-0.38657932,1.27955683,-0.60712621,3.20807316,0.60504151,-1.38706415,8.92444588,-7.43027595,-2.33653219,1.10358169,0.21547782,1.05057966,0.6975331,0.26076035]]
# y_pred = model.predict(x_test)
# output_path='testing_3v/'+str(ntree)+'_trees/y_pred_full_budget_'+str(total_budget)+'.csv'
# y_pred.to_csv(output_path)

# acc=sklearn.metrics.accuracy_score(y_test, y_pred)
# roc=sklearn.metrics.roc_auc_score(y_test,y_pred)


perf=pd.DataFrame(columns=['Accuracy','ROC'])



    
model = RandomForestClassifier(n_estimators=n_trees)
model.fit(x_train, y_train)
y_pred = model.predict(x_test)

output_path='NP_RandomForest/testing_7v/'+str(n_trees)+'_trees/y_pred.csv'
pd.DataFrame(y_pred).to_csv(output_path, index=None)
        
acc=sklearn.metrics.accuracy_score(y_test, y_pred)
roc=sklearn.metrics.roc_auc_score(y_test,y_pred)
perf = perf.append({'Accuracy':acc,'ROC':roc}, ignore_index=True)

perfy=pd.DataFrame(perf)  
perfy.to_csv('NP_RandomForest/testing_7v/'+str(n_trees)+'_trees/performance_metrics.csv',index=None)
    

