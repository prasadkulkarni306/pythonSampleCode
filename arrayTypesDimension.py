# -*- coding: utf-8 -*-
"""
Created on Sat Feb 15 10:20:19 2025

@author: Bhushan
"""

import numpy as np

print("0-D Array with value 98")
print("0-D arrays or Scalars are the elements in an array.Each value in an array is 0-D Array")
arr1 = np.array(98)

print("====0-D Array=====")
print(arr1)
print("The Type is ",type(arr1))

print()

print("===1-D Array=====")
print("An array that has 0-D Arrays as its elements is called 1-D Array")
arr2 = np.array([10,20,30,40,50,60])
print(arr2)
print("The array type is",type(arr2))

print()


print("===2-D Array====")
print("An array that has 1-D arrays as its elements is called as 2-D Array")
arr3 = np.array([[1,2,3,4],[4,3,2,1]])
print(arr3)
print("The array type is",type(arr3))

print()

print("===3-D Array====")
print("An array that has 2-D Arrays or Matrices as its elements is called 3-D Array")
arr4 = np.array([[[1,2,3,4],[1,2,3,4]],[[1,2,3,4],[2,3,4,5]]])
print(arr4)

print("The array type is",type(arr4))

print()