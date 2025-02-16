# -*- coding: utf-8 -*-
"""
Created on Sat Feb 15 09:39:20 2025

@author: Bhushan
"""

import numpy as np

#creating array and displaying the elements
print("creating array with numpy as")
arr1 = np.array([1,2,3,4,5,6])
print(arr1)
     

#checking numpy version
print("checking numpy version as")
print(np.__version__)     


#creating array and displaying the type 
print("creating array with numpy and displaying it's type")
arr1 = np.array([1,2,3,4,5,6,7,8])
print("The array elements are",arr1)
print("the type is",type(arr1))


#creating array and passing list and tuple as an arguments
print("creating array with numpy and passing list as argument")

#List as an argument
arr1 = np.array([1,2,3,4,5,6])
print("The array with list as an argument",arr1)

#tuple as an argument
arr2 = np.array((1,2,3,4,5,6))
print("The array with tuple as an argument",arr2)



