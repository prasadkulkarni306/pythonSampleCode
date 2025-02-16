# -*- coding: utf-8 -*-
"""
Created on Sat Feb 15 10:45:46 2025

@author: Bhushan
"""

print("The indexing in Array in Numpy Starts at 0 and first element is at Zero index")

import numpy as np
arr1 = np.array([1,2,3,4,5,6,7,8,9])
print()
print("the 1-D Array is",arr1)

print("printing first element in 1-D array")
print("The first element of array i.e. at 0th index is",arr1[0])
print("The second element of an array is i.e. at 1st index",arr1[1])
print()


print("The addition of 1st and 5th element in 1-D array ==>")
print("The addition is",arr1[0]+arr1[4])
print()


arr2 = np.array([[1,2,3,4,5],[1,2,3,4,5]])
print("the 2-D Array is",arr2)
print()
print("printing the elements of 2-D array")
print("the element at 1st row and fifth element is",arr2[1,4])
print()


print("accessing 3-D Array")
arr3 = np.array([[[1,2,3,4],[5,6,7,8]],[[9,10,11,12],[13,14,15,16]]])
print(f"the element at ",arr3[0,1,2])


