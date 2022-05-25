#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 10 09:09:37 2022

@author: anaritapena
"""
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os
import seaborn as sns
import statistics
import sklearn.metrics

#train = pd.read_csv('train.csv',index_col=False)
test = pd.read_csv('test.csv',index_col=False)
test.columns=['actual','age','wrkcls','fnlwgt','edu','edu_num','mart_sts','occup','rel','race','gender','cap_gain','cap_loss','hours','native']
y_actual=pd.DataFrame(test['actual'])

total_budgets_list = np.logspace(-1, 1, 20)

covar_list=['age','wrkcls','fnlwgt','edu','edu_num','mart_sts','occup','rel','race','gender','cap_gain','cap_loss','hours','native']
#['fnlwgt']
#['age','wrkcls','fnlwgt','edu','edu_num','mart_sts','occup','rel','race','gender','cap_gain','cap_loss','hours','native']

#y_pred=pd.read_csv('testing_14v/10_trees/y_pred_budget_7.847599703514611_10_iter.csv')
y_pred=pd.read_csv('/Users/anaritapena/Smooth_Random_Trees/Smooth_Random_Trees/testing_14v/10_trees/y_pred_budget_0.42813323987193935_10_iter.csv')
#y_pred=pd.read_csv('testing_14v/10_trees/y_pred_total_NP_10_iter.csv')




for covar in covar_list:


    rw_all=pd.DataFrame()
    for i in y_pred.columns:
        a=pd.DataFrame(y_pred[str(i)])
        y_actual.columns=[str(i)]
        rw=1-abs(a.subtract(y_actual))
        rw_all=pd.concat([rw_all, rw], axis=1)
    
    y_actual.columns=['actual']

    accu=pd.DataFrame((rw_all['0']+rw_all['0.1']+rw_all['0.2']+rw_all['0.3']+rw_all['0.4']+rw_all['0.5']+rw_all['0.6']+rw_all['0.7']+rw_all['0.8']+rw_all['0.9'])/10)
    accu.columns=['acc']
    test_acc=pd.concat([test,accu],axis=1)
    test_acc['age'] = pd.cut(test_acc['age'], bins=range(17,100,10), labels=[f'{l}-{l+10}' for l in range(17,90,10)])
    test_acc['hours'] = pd.cut(test_acc['hours'], bins=range(0,100,10), labels=[f'{l}-{l+10}' for l in range(0,90,10)])
    #test_acc['fnlwgt'] = pd.cut(test_acc['fnlwgt'], bins=range(10000,1500000,10000), labels=[f'{l}-{l+10000}' for l in range(10000,140000,10000)])
#ax = sns.countplot(x="age", data=test_acc)
    # plt.figure(figsize=(10,14))
    # sns.histplot(x=str(covar), data=test_acc,hue='acc',multiple="stack")
    # plt.title('Priv Loss=0.428')
    # plt.xticks(rotation=90)
    # plt.tight_layout()
    # plt.savefig('testing_14v/10_trees/hist_plot_10_iter_'+str(covar)+'_0.428.png')

    # plt.figure(figsize=(10,14))
    # sns.barplot(x=str(covar), y="acc", data=test_acc,)
    # plt.title('Priv Loss=0.428')
    # plt.xticks(rotation=90)
    # plt.tight_layout()
    # plt.savefig('testing_14v/10_trees/subacc_plot_10_iter_'+str(covar)+'_0.428.png')

    plt.figure(figsize=(15, 8))
    ax = sns.histplot(x=str(covar), data=test_acc)
    ax.yaxis.set_major_formatter(PercentFormatter(1))

    ax2 = ax.twinx()
    #sns.lineplot(x=x_, y=y_2, data=data2, marker='o', color='crimson', lw=3, ax=ax2)

    plt.show()

sns.pairplot(data=test_acc, hue="acc",diag_kind="hist")
