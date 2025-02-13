# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 18:02:09 2025

@author: Bhushan
"""

import numpy as np

array1 = np.array([1,2,3])

array2 = np.array([4,5,6])

array3 = np.array([-1,-2,-3])

angles = np.array([0,np.pi/2,np.pi])

array4 = np.array([1,10,100])

##############################################
print()
print("first Array",array1)
print("Second Array",array2)
print("addition:",array1 + array2)

###############################################
print()
print("first Array",array1)
print("second array",array2)
print("substraction:", array1 - array2)

###############################################
print()
print("first array",array1)
print("second array",array2)
print("multiplication:",array1 * array2)

###############################################
print()
print("first Array",array1)
print("second array",array2)
print("Dvision:",array1 / array2)

###############################################

print()
print("first Array",array1)
print("second array",array2)
print("modulus",array1 % array2)
print("modulus using np.mod:",np.mod(array1,array2))
###############################################

print()
print("third array",array3)
print("absoulute value :",np.abs(array3))
###############################################

print()
print("Sine :Trigonometric function")
print("Source Array",angles)
print("Sine",np.sin(angles))

###############################################
print()
print("Cosine Trigonometric function")
print("Source Array",angles)
print("cosine",np.cos(angles))

###############################################

print()
print("tangent :Trigonometric Function")
print("source Array:",angles)
print("tangent",np.tan(angles))

###############################################

print()
print("logarithmic Function:")
print("source array",array4)
print("Natural Log:",np.log(array4))

###############################################

print()
print("Logarithmic Function:")
print("Soruce Array",array4)
print("Base 10 Log:",np.log10(array4))

###############################################

print()
print("agrgregate function")
print("Sum:",np.mean(array1))

print("mean:",np.mean(array1))

print("Product:",np.prod(array1))

###############################################






