# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 17:42:58 2025

@author: Bhushan
"""

import numpy as np

arr = np.array([1,2,3,np.nan,5,np.nan])

print(arr)

print()
nan_ele = np.isnan(arr)   
print(nan_ele)

print()

arr2 = np.linspace(1,20,8)

print(arr2)

#creation of identity matrix
ide = np.identity(4)
print(ide)

######################################################
print()
arr3 = np.array([56,23,78,12,67])
print(arr3)

print(arr3.argmax())
print(arr3.argmin())
print()

######################################################

print()
print(np.max(arr3))

#======================================================

print(np.argsort(arr3))

######################################################
print()
arr4 = np.array([[15,21,30],[14,50,16]])
print(arr4)

print()
print(arr4.argmax(axis=0))

print(arr4.argmax(axis=1))


print("###############################################")

print(arr4)
print()
print(np.argsort(arr4,axis=0))
print(np.argsort(arr4,axis=1))

