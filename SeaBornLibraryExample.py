# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 17:54:01 2025

@author: Bhushan
"""

from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

print("different datasources 'tips','iris',''titanic")

print("We will use tips datasource to load the data")

df = sns.load_dataset('tips')

print(df)

sns.relplot(x = 'total_bill',y = 'tip',data = df)

plt.show()

sns.relplot(x = 'total_bill',y = 'tip',hue ='sex', data = df)

plt.show()

sns.relplot(x = 'total_bill',y = 'tip',hue = 'sex',style = 'time',data = df)

plt.show()

sns.relplot(x = 'total_bill',y='tip',hue = 'sex',style = 'time',size = 'size',data = df)

plt.show()

sns.relplot(x = 'total_bill',y = 'tip',hue = 'sex',style = 'time',size = 'size',col = 'time', data = df)

plt.show()