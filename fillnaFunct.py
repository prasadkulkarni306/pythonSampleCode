# -*- coding: utf-8 -*-
"""
Created on Fri Feb 14 16:29:59 2025

@author: Bhushan
"""

import pandas as pd
import numpy as np
#Replacing NaN with some default values

print("fillna Function")
print("Replacing a NaN Values with Some values using 'fillna' function")

ds1 = pd.Series([1,2,3,4,5,5,6,np.nan,np.nan])

print()
print("Series elements before i.e. with NAN values",ds1)
print()

ds1.fillna(1)

print()
print("Series elements after i.e. without NaN Values",ds1)
print()

print()
print("Fillna function with inplace=True")
ds1.fillna(2,inplace=True)
print(ds1)
print()

