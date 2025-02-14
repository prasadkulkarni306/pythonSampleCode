# -*- coding: utf-8 -*-
"""
Created on Fri Feb 14 16:49:28 2025

@author: Bhushan
"""

import pandas as pd
import numpy as np

print("Describe Function :")
ds1 = pd.Series([10,20,30,40,50,60,1,3,4,2,6,9,10])

print(ds1.describe())

print()
print("Describe Function :")
ds2 = pd.Series([1,6,2,5,7,3,1,5,7,9,5])

print()
print(ds2.describe())

ds1.sort_values(ascending=False,inplace=True,kind='mergesort')
print("printing before",ds1)
print()
print("printing after")
print(ds1)

ds2.sort_values(ascending=True,inplace=True,kind='mergesort')
print()
print("printing before",ds2)
print()
print("printing after",ds2)