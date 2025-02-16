# -*- coding: utf-8 -*-
"""
Created on Sat Feb 15 10:35:13 2025

@author: Bhushan
"""

import numpy as np

print("Printing dimesions of array")

arr1 = np.array(97)
arr2 = np.array([1,2,3,4,5])
arr3 = np.array([[1,2,3,4],[1,2,3,4]])
arr4 = np.array([[[1,2,3],[1,2,3]],[[1,2,3],[1,2,3]]])


print()
print("printing elements af array ")
print("0-D array",arr1)
print()
print("1-D array",arr2)
print()
print("2-D array",arr3)
print()
print("3-D array",arr4)
print()


print("printing the dimensions")
print("0-D array dimesnion==>",arr1.ndim)
print("1-D array dimension==>",arr2.ndim)
print("2-D Array dimension==>",arr3.ndim)
print("3-D array dimension==>",arr4.ndim)


print()
print("creating multi dimension array")

arr5 = np.array([1,2,3,4,5],ndmin=10)

print("the array is",arr5)

print("the dimension of array 5 is",arr5.ndim)

