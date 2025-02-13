# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 18:14:48 2025

@author: Bhushan
"""

import numpy as np

#declare the array

arr1 = np.array([1,2,3,4,5])

print(arr1)

arr2 = np.array((1,2,3,4,5))

print(arr2)

#print number of elements

print(arr1.shape)
print(arr2.shape)

#dimension of array

print(arr1.ndim)
print(arr2.ndim)

#type of array

print(type(arr1))
print(type(arr2))

#value assignment
print(arr1)
arr1[0] = 10
print(arr1)

#multiple assignments

print(arr1)
arr1[[1,2,3]] = [30,40,50]
print(arr1)

#printing array elements in range
print()
print(arr1)
print(arr1[1:4])


print()
print(arr1)
print(arr1[1:5:2])


#initialise array with zero with size as 10,bydefault datatype is float
print()
arr3=np.zeros(10)
print(arr3)

#initialise array with zero with size 10 and datatype integer
print()
arr3=np.zeros(10,dtype="int")
print(arr3)


#initialise array with one with size as 10,by default datatype is float
print()
arr3=np.ones(10)
print(arr3)

#initialise array with one with size 10, and datatype is integer

print()
arr3=np.ones(10,dtype="int") 
print(arr3)


#use of arange function
print()
arr3=np.arange(0,11,2)
print(arr3)


print()
arr3=np.arange(10,30,3)
print(arr3)