# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 17:37:17 2025

@author: Bhushan
"""

import pandas as pd
import numpy as np

print("reading data from excel file")


df = pd.read_csv("stud.csv")

print("sorting data")
print(df.sort_values(['emp_name']))

print()
print("Sorting with two columns")
print(df.sort_values(['emp_name','emp_sal'],ascending = [False,True]))


print()
print("using groupby ")

print(df.groupby('bonus')['emp_name'].count())



print()
print(df.groupby('bonus')['emp_sal'].min())
