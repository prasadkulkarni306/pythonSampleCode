# -*- coding: utf-8 -*-
"""
Created on Fri Feb 14 15:44:54 2025

@author: Bhushan
"""

import numpy as np
import pandas as pd

#methods used in Padas are capital case
ds1 = pd.Series([11,12,13,14,15])

ds2 = pd.Series([1,2,3,4,5])
print()
print("printing datatype of Series",type(ds1),type(ds2))

#index Support

print()
print("Series before value replacing",ds1)
ds1[0] = 30
print("Series after replacing",ds1)
print()


#use of label indexing
print()
print("printing elements with label indexing")
ds1 = pd.Series([10,20,30,40,50,np.NAN],index=list('abcdef'))
print()

ds2 = pd.Series([1,2,3,4,5,5,6,np.nan],index = list("pqrstuvw"))
print("printing elements with label indexing")
print(ds1)
print()

#indexing with numbers
#ds1[1] = 40
#print("element after replacing",ds1[1])
print()

#indexing with label
ds1['a'] = 70
print("Element after replacing",ds1['a'])
print()


#replacing label indexes 
print()
print("printing before replacing label indexes")
print(ds2)
ds2.index = list('zxcvbnmk')
print("printing after replacing label indexes")
print(ds2)

#printing values with index label range
print()
print("printing elements with range index label x to m")
print("elements",ds2['x':'m'])
print()


#droping the element and generating new series
print()
print("droping element position 'm' and generating new Series")

print("priting before dropping",ds2)
print("count before",len(ds2))
ds4 = ds2.drop('m')
print("printing Series elements after dropping",ds4)
print("count after",len(ds4))


#inplace will do the change in the original series 
print("Original Series",ds2)
print("Droping the value with inplace=True")
ds2.drop('k',inplace=True)

print(ds2)









