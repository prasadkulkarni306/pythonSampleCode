# -*- coding: utf-8 -*-
"""
Created on Fri Feb 14 16:41:30 2025

@author: Bhushan
"""

import pandas as pd
import numpy as np

ds1 = pd.Series([1,2,3,4,5,6,7,8,np.NAN,np.nan])

print()
print("printing Series Elements",ds1)

print()
print("Use of dropna function:")
print("dropna function drop the NaN Values from Series")

print(ds1.dropna())

print()

print("dropna function with inplace=True")
print(ds1.dropna(inplace = True))

print("printing elements after dropna function after inplace=True")

print(ds1)


