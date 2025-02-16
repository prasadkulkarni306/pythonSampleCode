# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 08:56:02 2025

@author: Bhushan
"""

import numpy as np

print("converting the array from integer to boolean")

arr = np.array([1,2,3,4,5,6,7,10])

print()
print("the array is==>",arr)
print("the datatype is==>",arr.dtype)


print()
print("the datatype conversion")
arrnew = arr.astype(bool)

print("The new arr is==>",arrnew)
print("the datatype is==>",arrnew.dtype)

