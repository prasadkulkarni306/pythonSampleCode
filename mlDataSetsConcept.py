# -*- coding: utf-8 -*-
"""
Created on Fri Mar 14 16:20:07 2025

@author: Bhushan
"""

#DataSets
#DataSets is a collection of data.It can be anything from an array to a complete database

#to create a bigger datasets,one can use numpy methods to create random datasets of any size

#creation of an array of 250 floats between 1.0 to 5.0 range

import numpy as np 

x = np.random.uniform(1.0,5.0,250)

print(x)

y = np.random.uniform(1,500,10000)

print(y)