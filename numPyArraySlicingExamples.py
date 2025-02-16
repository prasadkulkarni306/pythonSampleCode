# -*- coding: utf-8 -*-
"""
Created on Sat Feb 15 15:05:07 2025

@author: Bhushan
"""

import numpy as np

arr1 = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])

print("array slicing")

print("printing array elements within index range 1 to 5")
print(arr1[1:5])

print("printing array elements starting from 1 to end")
print(arr1[1:])

print("printing array elements starting from 0th index upto 5 i.e. 4 as it skips the last one")
print(arr1[:5])


print("printing array elements from 1 to 14th (skiping last one) in step 2")
print(arr1[1:14:2])

print("printing array elements from 1st to 13th index (skipping last one) in step 3")
print(arr1[1:13:3])

print("printing array elements from -3 to -1 i.e. -ve indexing starts from last with index -1 ")
print(arr1[-3:-1])

print("printing array elements from -10 to -2 i.e. -ve indexing")
print(arr1[-10:-2])

print("printing array elements from -10 to -1 with step 3")
print(arr1[-10:-1:2])

print("skipping the first and last index")
print(arr1[-5:])

print(arr1[-5::2])

print(arr1[:-5])

print(arr1[:-5:2])
print("skipping both indexes i.e. start and end with steps in -ve value")
print(arr1[::-3])

print("skipping both indexes i.e. start and end with steps in +ve value ")
print(arr1[::3])