# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 09:23:35 2025

@author: Bhushan
"""

import numpy as np

arr = np.array([2,3,4,5,6,7])

print("the original array",arr)

x = arr.copy()
y = arr.view()

print()

x[0] = 10

print("copy function example")
print("changes made to copy will not impact the original one")
print("copy function will create separate array")
print("the original array",arr)
print("the copy array",x)


print()
y[2] = 90

print("view fucntion example")
print("changes made to view will impact original one")
print("the original array",arr)
print("the view array",y)

print()


arr[4] = 50
print("changes made to original will impact the view but not in the copy as below")
print("the original array",arr)
print("copy array",x)
print("view array",y)