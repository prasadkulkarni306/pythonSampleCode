# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 06:01:31 2025

@author: Bhushan
"""

import numpy as np

print("generate the 2D array within range with integer datatype")
arr = np.random.randint(1,10,(4,3))
print(f"the resultant array is===>{arr}")

print()
print("the sum function example==>")
s = np.sum(arr)
print(f"the array is==>{arr}")
print(f"the sum is===>{s}")


print()
arr = np.random.randint(20,30,(3,5))
print(f"the resultant array is===>{arr}")
s = np.sum(arr)
print(f"the sum is===>{s}")


print()
arr = np.random.randint(1,10,(4,10))
print(f"the resultant array is===>{arr}")
s = np.sum(arr,axis=0)
print(f"the sum is(vertical)==>{s}")

s = np.sum(arr,axis=1)
print(f"the sum is(Horizontal)==>{s}")


print()
print("the maximum value is")
arr = np.random.randint(1,100,(10,10))
print(f"the resultant array i===>{arr}")
s = np.max(arr)
print(f"the maximum value is===>{s}")

print()
print("The max value vartically")
arr = np.random.randint(20,40,(20,20))
print(f"the resultant array is===>{arr}")
v = np.max(arr,axis=0)
print(f"the maximums value vertically is===>{v}")

h = np.max(arr,axis=1)
print(f"the maximum value horizontally is==>{h}")





