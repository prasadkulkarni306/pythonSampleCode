# -*- coding: utf-8 -*-
"""
Created on Fri Mar 14 15:56:49 2025

@author: Bhushan
"""

#standard deviation
import numpy as np

#Standard Deviation
#Standard deviation is the number the describes how spread out the values are 
#A low value of std. deviation means most of the numbers are close to mean(Average) value
#A high value of std. deviation means values are spread out over wider range

arr = [89,87,88,87,88,89,86,83,82]

sdev = np.std(arr)

print("The standard deviation is",sdev)

#here the std. deviation is 2.36 means values are close to mean(average) value


arr = [12,111,56,78,99,11,47,98]

sdev = np.std(arr)

print("The standard deviation is",sdev)

#here the standard deviation is 36.48 means values are widely spread

