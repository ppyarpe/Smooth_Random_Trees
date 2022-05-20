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





for var in variables:
    path1='/Users/anaritapena/Smooth_Random_Trees/Smooth_Random_Trees/testing_'+str(var)+'v/10_trees/performance_metrics_10.0_10_iter.csv'
    perf_over=pd.read_csv(path1)
    
    path2='/Users/anaritapena/Smooth_Random_Trees/Smooth_Random_Trees/testing_'+str(var)+'v/10_trees/performance_metrics_NP_10_iter.csv'
    perf_np_over=pd.read_csv(path2)
    perf_np_over=perf_np_over.T
       
    plt.figure(str(var)+' Variables-Acc') 
    plt.plot(perf_over['Budget'],perf_over['Accuracy'],'--',label='Accuracy')
    plt.scatter(perf_over['Budget'],perf_over['Accuracy'],s=20)
    plt.axhline(y = perf_np_over.iat[1,0], color = 'grey', linestyle = 'dashed')
    plt.axis([0,10,0.72,0.86])
    plt.xlabel("Privacy Loss")
    plt.legend()
    plt.show()
    plt.savefig('/Users/anaritapena/Smooth_Random_Trees/Smooth_Random_Trees/testing_'+str(var)+'v/'+str(ntree)+'_trees/acc_plot_10_iter.png')
    
    plt.figure(str(var)+' Variables-ROC')   
    plt.plot(perf_over['Budget'],perf_over['ROC'],'--',color='orange',label='ROC')
    plt.scatter(perf_over['Budget'],perf_over['ROC'],color='orange',s=20)
    plt.axhline(y = perf_np_over.iat[1,1], color = 'grey', linestyle = 'dashed')
    plt.axis([0,10,0.5,0.75])
    plt.xlabel("Privacy Loss")
    plt.legend()
    plt.show()
    plt.savefig('/Users/anaritapena/Smooth_Random_Trees/Smooth_Random_Trees/testing_'+str(var)+'v/'+str(ntree)+'_trees/roc_plot_10_iter.png')