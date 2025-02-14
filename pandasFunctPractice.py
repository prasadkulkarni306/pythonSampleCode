# -*- coding: utf-8 -*-
"""
Created on Fri Feb 14 16:17:24 2025

@author: Bhushan
"""

import pandas as pd
import numpy as np

ds2 = pd.Series([10,20,30,40,50,60,np.nan,np.nan],index = list('abcdefgh'))

print()
print("Printing Series",ds2)
print()

print()
print('Mean Value :',ds2.mean())
print()

print()
print("Sum :",ds2.sum())
print()

print()
print("Minimum Value :",ds2.min())
print()

print()
print("Maximum Value :",ds2.max())
print()

print()
print("Mode(Most Frequent Elements) :",ds2.mode())
print()

print()
print("Count Elements",ds2.count())
print()

print()
print("is null",ds2.isnull())
print()

print()
print("is null values counting",ds2.isnull().sum())
print()



