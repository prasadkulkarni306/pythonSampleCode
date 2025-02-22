# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 18:13:19 2025

@author: Bhushan
"""
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

df = sns.load_dataset("tips")

print(df)

sns.jointplot(x = 'total_bill',y='tip',data=df )

plt.show()


# histogram + KDE (kernal density estimator)
# rug--> it will add lines at bottom that shows large 
# density


sns.distplot(df.total_bill,rug=True)

plt.show()

sns.displot(df.total_bill,rug=False)


plt.show()


# on x axis go with categories data
# on y axis go with numeric data


sns.barplot(x='sex',y='tip',data = df)

plt.show()


print(df.sex.value_counts())

print(df.time.value_counts())


sns.countplot(x='time',data = df)

plt.show()



sns.boxplot(x='sex',y = 'tip',data = df)

plt.show()


sns.kdeplot(df.tip)

plt.show()

sns.rugplot(df.total_bill)

plt.show()
