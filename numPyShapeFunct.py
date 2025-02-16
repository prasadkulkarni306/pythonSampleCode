# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 09:51:43 2025

@author: Bhushan
"""

import numpy as np

arr = np.array([1,2,3,4,4])
arr1 = np.array([[1,2,3,4],[10,20,30,40]])

print("The Shape function examples")

print()
print("the array arr elements",arr)
print("The arr===>",arr.shape)
print()
print("the array arr1 elements",arr1)
print("The arr1===>",arr1.shape)

print()
arr2 = np.array([10,20,30,40],ndmin=5)
print("The Array is",arr2)
print("Array ndmin===>",arr2.shape)