# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 18:28:36 2025

@author: Bhushan
"""

import pandas as pd
import numpy as np

#mostly methods that one use in Pandas are Capital case

print()
print("creation of series")
ds1 = pd.Series([1,2,3,4,5,6,7,8,9,10])
ds2 = pd.Series([10,20,30,40,50,60,70])

print(f"Printing the series===>'ds1' as =====>{ds1}")
print(f"Printing the series===>'ds2' as =====>{ds2}")

print()
print("Printing the type of Series")

print(f"The type of 'ds1' series====>{type(ds1)}")
print(f"The type if 'ds2' series====>{type(ds2)}")

print()
print("Indexing Use")
print(f"ds1 series before==>{ds1}")
print("replacing the value at index 0 for Series ds1 with value 2")
ds1[0] = 2
print(f"ds1 series after==>{ds1}")

print("The Series ds2 before replacing==>{ds2}")
print("Replacing the value at index 1 for series ds2 with value 22")
ds2[1] = 22
print(f"ds2 series after replacing===>{ds2}")

print()

print("label indexing concept")
print("here labels a,b,c,d,e and f are used as indexes instead of numbers i.e. 0,1,2,.....")
ds3 = pd.Series([100,200,300,400,500,np.nan],index=list('abcdef'))
print(f"the Series with label indexing ===>{ds3}")

print()
print("printing values at indexes using labels")
print(f"printing value at index===>'a' is ===> {ds3['a']}")
print(f"printing value at index===>'f' is ===> {ds3['f']}")

print()
print("replacing the indexing values i.e. labels with old values")
print(f"previous indexing values==>{ds3} ")

ds3.index = list('pqrstu')

print(f"the values after replacing the index labels ")
print(f"current indexing values===>{ds3}")

print()
print()
print("slicing examples")
print("printing the values from index 'r' to 'u' as")
print(f"Series ds3===>{ds3['s':'u']}")

print()
print()
print("printing Series after removal of value at perticular label index ")

print(f"Previous Series==>{ds3}")
print()
print(f"the series after removal ==>{ds3.drop('t')}")



















