# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 18:30:00 2025

@author: Bhushan
"""

import numpy as np

print("creation of 1D array using NP")

arr1 = np.array([1,2,3,4,5])
arr2 = np.array([6,7,8,9,10])
print()
print(f"Array arr1===>{arr1}")
print()
print(f"Array arr2==>{arr2}")


print("to find out the total number of elements using shape function")
print(f"Total elements ===>{arr1.shape} in array===>{arr1} ")

print()
print("dimention of array i.e. 1D or 2D")
print(f"the dimension==>{arr1.ndim} of array===>{arr1}")
print(f"the dimention=={arr1.ndim} of array===>{arr2}")

print()
print("finding type of array")
print(f"the type ===>{type(arr1)} of array ===>{arr1}")
print(f"the type ===>{type(arr2)} of array ====>{arr2}")

print()
print("Assigning a value at specific index")
print(f"initial value ===>{arr1[0]} in array==>{arr1}")
arr1[0] = 10
print(f"after value===>{arr1[0]} in array==>{arr1}")


print()
print("Assigning values at different indexes")
print(f"initial array===>{arr1}")
arr1[[1,2,3]]=[20,30,40]
print(f"array after assignment===>{arr1}")


print()
print("printing values at indexes specific range")
print(f"initial array==>{arr1}")
print(f"values at indexes i.e. from 1 to 4 are===>{arr1[1:4]}")


print()
print("printing values between given range with step 2 i.e. at odd indexes")
print(f"Initial Array===>{arr1}")
print(f"values are even indexes==>{arr1[1:5:2]} in array===>{arr1}")


print()
print("Create float type array with size 10 and intialize it to 0")
arr_zero = np.zeros(10)
print(f"The array with floating datatype===>{arr_zero}")

print()
print("create integer type array with size 10 and initlize it to 1")
arr_one = np.ones(10,dtype="int")
print(f"the array with integer datatype===>{arr_one}")


print()
print("converting 1D to 2D array")
aa = np.arange(1,13)
print(f"the 1D array===>{aa}")


print()
print("converting 1D Array to 2D Array")
print()
res = aa.reshape(6,2)
print(f"the the 2D array==>{res}")
res = aa.reshape(2,6)
print(f"converting 1D array to 2D Array==>{res}") 
res = aa.reshape(4,3)
print(f"converting 1D array to 2D array==>{res}")
res = aa.reshape(3,4)
print(f"converting 1D to 2D array==>{res}")


print()
print("To generate arrray with random values between the range")
#1==start value 10==end value 6==total elements of array
arr = np.random.randint(1,10,6)
print(f"The resultant array is==>{arr}")

print()
arr1 = np.random.randint(20,100,10)
print(f"the resultant array is===>{arr1}")

print()

print("to generate array with random values with float datatype between given range")
arr1 = np.random.uniform(1,5,4)
print(f"the resultant array is===>{arr1}")

print()
print("generating the 2D array within random range given with integer datatype")
arr2 = np.random.randint(1,20,(5,2))
print(f"the resultant array ==>{arr2}")

print()
print("generating 2D array within random range with datatype float ")
arr2 = np.random.uniform(1,30,(4,6))
print(f"the resultant array is===>{arr2}")


print()




