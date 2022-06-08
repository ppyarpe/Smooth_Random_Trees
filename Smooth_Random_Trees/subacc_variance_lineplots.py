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
test = pd.read_csv('/Users/anaritapena/Smooth_Random_Trees/Smooth_Random_Trees/Synthetic Datasets/test.csv',index_col=False)

test.columns=['default','gender','salary']
#['actual','age','wrkcls','fnlwgt','edu','edu_num','mart_sts','occup','rel','race','gender','cap_gain','cap_loss','hours','native']
y_actual=pd.DataFrame(test['default'])

total_budgets_list = np.logspace(-1, 1, 20)

covar_list=['default','gender','salary']
#['age','wrkcls','fnlwgt','edu','edu_num','mart_sts','occup','rel','race','gender','cap_gain','cap_loss','hours','native']
#['actual']

#['fnlwgt']
#['age','wrkcls','fnlwgt','edu','edu_num','mart_sts','occup','rel','race','gender','cap_gain','cap_loss','hours','native']

#y_pred=pd.read_csv('testing_14v/10_trees/y_pred_budget_7.847599703514611_10_iter.csv')
y_pred_1=pd.read_csv('/Users/anaritapena/Smooth_Random_Trees/Smooth_Random_Trees/Synthetic Datasets/y_pred_budget_0.42813323987193935_10_iter_10_trees.csv')
y_pred_2=pd.read_csv('/Users/anaritapena/Smooth_Random_Trees/Smooth_Random_Trees/Synthetic Datasets/y_pred_budget_7.847599703514611_10_iter_10_trees.csv')
y_pred_3=pd.read_csv('/Users/anaritapena/Smooth_Random_Trees/Smooth_Random_Trees/Synthetic Datasets/y_pred_total_NP_10_iter_10_trees.csv')




for covar in covar_list:


    rw_all_1=pd.DataFrame()
    for i in y_pred_1.columns:
        a_1=pd.DataFrame(y_pred_1[str(i)])
        y_actual.columns=[str(i)]
        rw_1=1-abs(a_1.subtract(y_actual))
        rw_all_1=pd.concat([rw_all_1, rw_1], axis=1)
    
    y_actual.columns=['actual']

    accu_1=pd.DataFrame((rw_all_1['0']+rw_all_1['0.1']+rw_all_1['0.2']+rw_all_1['0.3']+rw_all_1['0.4']+rw_all_1['0.5']+rw_all_1['0.6']+rw_all_1['0.7']+rw_all_1['0.8']+rw_all_1['0.9'])/10)
    accu_1.columns=['acc_1']
    test_acc=pd.concat([test,accu_1],axis=1)
    
    
    
    rw_all_2=pd.DataFrame()
    for j in y_pred_2.columns:
       a_2=pd.DataFrame(y_pred_2[str(j)])
       y_actual.columns=[str(j)]
       rw_2=1-abs(a_2.subtract(y_actual))
       rw_all_2=pd.concat([rw_all_2, rw_2], axis=1)
   
    y_actual.columns=['actual']

    accu_2=pd.DataFrame((rw_all_2['0']+rw_all_2['0.1']+rw_all_2['0.2']+rw_all_2['0.3']+rw_all_2['0.4']+rw_all_2['0.5']+rw_all_2['0.6']+rw_all_2['0.7']+rw_all_2['0.8']+rw_all_2['0.9'])/10)
    accu_2.columns=['acc_2']
    test_acc=pd.concat([test_acc,accu_2],axis=1)
   
    rw_all_3=pd.DataFrame()
    for i in y_pred_3.columns:
        a_3=pd.DataFrame(y_pred_3[str(i)])
        y_actual.columns=[str(i)]
        rw_3=1-abs(a_3.subtract(y_actual))
        rw_all_3=pd.concat([rw_all_3, rw_3], axis=1)
    
    y_actual.columns=['actual']

    accu_3=pd.DataFrame((rw_all_3['0']+rw_all_3['0.1']+rw_all_3['0.2']+rw_all_3['0.3']+rw_all_3['0.4']+rw_all_3['0.5']+rw_all_3['0.6']+rw_all_3['0.7']+rw_all_3['0.8']+rw_all_3['0.9'])/10)
    accu_3.columns=['acc_3']
    test_acc=pd.concat([test_acc,accu_3],axis=1)
    
    
#     test_acc['age'] = pd.cut(test_acc['age'], bins=range(17,100,10), labels=[f'{l}-{l+10}' for l in range(17,90,10)])
#     test_acc['hours'] = pd.cut(test_acc['hours'], bins=range(0,100,10), labels=[f'{l}-{l+10}' for l in range(0,90,10)])
#     test_acc['fnlwgt'] = pd.cut(test_acc['fnlwgt'], bins=range(10000,150000,10000), labels=[f'{l}-{l+10000}' for l in range(10000,140000,10000)])
#     test_acc['cap_gain'] = pd.cut(test_acc['cap_gain'], bins=range(0,100000,10000), labels=[f'{l}-{l+10000}' for l in range(0,90000,10000)])
#     test_acc['cap_loss'] = pd.cut(test_acc['cap_loss'], bins=range(0,5000,500), labels=[f'{l}-{l+10000}' for l in range(0,4500,500)])
# #ax = sns.countplot(x="age", data=test_acc)
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
    
    grouped_df = test_acc.groupby(str(covar))



    mean_df = grouped_df.mean()



    mean_df = mean_df.reset_index()


    #Option 1 of variance

    plt.figure(figsize=(15, 8))
    ax = sns.histplot(x=str(covar), data=test_acc,alpha=0.2,color='gray')
    plt.xticks(rotation=90)
    #ax.yaxis.set_major_formatter(PercentFormatter(1))

    ax2 = ax.twinx()
    #sns.boxplot(x=str(covar), y="acc_1",data=test_acc, palette="Set3")
    #ax2.set(ylim=(0, 1.05))
    sns.lineplot(x=str(covar), y='acc_1', data=test_acc, marker='o',palette="light:#5A9_r",ax=ax2,estimator="mean")
                 
                 #color='crimson', lw=2, ax=ax2)
    sns.lineplot(x=str(covar), y='acc_2', data=test_acc, marker='o', palette="light:#5A9_r",ax=ax2,estimator="mean")
                 #color='blue', lw=2, ax=ax2)
    sns.lineplot(x=str(covar), y='acc_3', data=test_acc, marker='o', palette="light:#5A9_r",ax=ax2,estimator='mean')
                 #color='orange', lw=2, ax=ax2)
    # sns.pointplot(x=str(covar), y='acc_1', data=test_acc, join=False,color='crimson',ax=ax2)
    # sns.pointplot(x=str(covar), y='acc_2', data=test_acc, join=False,color='blue',ax=ax2)
    # sns.pointplot(x=str(covar), y='acc_3', data=test_acc, join=False,color='orange',ax=ax2)
    ax2.legend(['DP=0.428', 'DP=7.848', 'NP-DP'])
    ax2.set(ylabel='Accuracy')
  
    plt.tight_layout()
    #plt.savefig('testing_14v/10_trees/plots/variance/lineplots/10_iter_'+str(covar)+'_line.png')
    
    # plt.figure(figsize=(15, 8))
    # ax = sns.histplot(x=str(covar), data=test_acc)
    # plt.xticks(rotation=90)
    # #ax.yaxis.set_major_formatter(PercentFormatter(1))

    # ax2 = ax.twinx()
    # #sns.boxplot(x=str(covar), y="acc_1",data=test_acc, palette="Set3")
    # ax2.set(ylim=(0, 1.05))
    # sns.lineplot(x=str(covar), y='acc_1', data=mean_df, marker='o', color='crimson', lw=2, ax=ax2)
    # sns.lineplot(x=str(covar), y='acc_2', data=mean_df, marker='o', color='blue', lw=2, ax=ax2,)
    # sns.lineplot(x=str(covar), y='acc_3', data=mean_df, marker='o', color='orange', lw=2, ax=ax2)
    # sns.pointplot(x=str(covar), y='acc_1', data=test_acc, join=False,color='crimson',ax=ax2,estimator=np.mean)
    # sns.pointplot(x=str(covar), y='acc_2', data=test_acc, join=False,color='blue',ax=ax2,estimator=np.mean)
    # sns.pointplot(x=str(covar), y='acc_3', data=test_acc, join=False,color='orange',ax=ax2,estimator=np.mean)
    # ax2.set(ylabel='Accuracy')
    # ax2.legend(['DP=0.428', 'DP=7.848', 'NP-DP'])
    # plt.tight_layout()

   
   # plt.savefig('testing_14v/10_trees/plots/subacc_plot_10_iter_'+str(covar)+'_vary_scale.png')
plt.figure()
sns.pairplot(data=test_acc, hue="acc_1",diag_kind="hist")

plt.figure()
sns.histplot(x='salary',data=test,hue='gender')
