#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 18 10:31:22 2022

@author: anaritapena
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sklearn.metrics

total_budgets_list = np.logspace(-1, 1, 20)
ntree=10
variables=['3','5','6','7','8','9','10','11','12','13','14']

test = pd.read_csv('/Users/anaritapena/Smooth_Random_Trees/Smooth_Random_Trees/test.csv')
y=pd.DataFrame(test['0'])

for var in variables:
    perf=pd.DataFrame(columns=['Budget','Accuracy','ROC'])
    
    for total_budget in total_budgets_list:
        y_pred=pd.read_csv('/Users/anaritapena/Smooth_Random_Trees/Smooth_Random_Trees/testing_'+str(var)+'v/'+str(ntree)+'_trees/y_pred_full_budget_'+str(total_budget)+'.csv')
        acc=sklearn.metrics.accuracy_score(y, y_pred['0'])
        roc=sklearn.metrics.roc_auc_score(y,y_pred['0'])
        perf = perf.append({'Budget': total_budget,'Accuracy':acc,'ROC':roc}, ignore_index=True)
    
    plt.figure(str(var)+' Variables') 
    # plt.plot(perf['Budget'],perf['Accuracy'],'--',label='Accuracy')
    # plt.scatter(perf['Budget'],perf['Accuracy'],s=20)   
    plt.plot(perf['Budget'],perf['ROC'],'--',color='orange',label='ROC')
    plt.scatter(perf['Budget'],perf['ROC'],color='orange',s=20)
    plt.axis([0,10,0.4,1])
    plt.xlabel("Privacy Loss")
    plt.legend()
    plt.show()