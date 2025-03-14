# -*- coding: utf-8 -*-
"""
Created on Fri Mar 14 16:05:46 2025

@author: Bhushan
"""

#Percentile
#Below is the array of ages of every person living on street

import numpy as np

ages = [10,11,45,65,33,22,56,78,89,99,11,17,27,87,89,34,23,48,29,78,75,76,49]

#numpy has percentile method for finding specified percentile

x = np.percentile(ages,56)

print("ages",x)

ages = [5,31,43,48,50,41,7,11,15,39,80,82,32,2,8,6,25,36,27,61,31]

x = np.percentile(ages, 90)

print(x)