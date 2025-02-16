# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 08:37:05 2025

@author: Bhushan
"""

import numpy as np

print("creating datatype with defined datatype as")

arr = np.array([1,2,3,4])

print("the datatype is i.e. before==>",arr.dtype)
arr = np.array([1,2,3,4],dtype = 'S')
print("the datatype is i.e. after==>",arr.dtype)

print()

print("to define the size of datatype")
arr = np.array([1,2,3,4,5],dtype = 'S5')
print("the datatype is",arr.dtype)


print("The array integer with 4 bytes integer")
print()
arr = np.array([1,2,3,4,5],dtype = 'i4')

print(f"The datatype is ===>{arr.dtype}")