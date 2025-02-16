# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 08:48:02 2025

@author: Bhushan
"""

import numpy as np

print("Converting datatype of an existing arry")

print("Use astype() function to create copy and use dtype to specify datatype")

print("converting float to integer datatype")

arr = np.array([11.1,45.234,6.77])

arrnew = arr.astype('i')

print()
print("Before conversion",arr)
print()
print("after conversion",arrnew)


print()
print(f"the datatype before conversion arr==>{arr.dtype} and after conversion arrnew==>{arrnew.dtype}")


