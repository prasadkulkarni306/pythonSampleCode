# -*- coding: utf-8 -*-
"""
Created on Fri Mar 14 15:27:25 2025

@author: Bhushan
"""

import numpy as np
import scipy as stats

arr = [80,90,78,45,23,12,56,67,78,45,54,32,45,78,98,100]

#Mean
#The mean value is the average value.
#To calculate the mean, find the sum of all values, and divide the sum by the number of values:
    
mean = np.mean(arr)

print("The mean value is",mean)

#Median
#It is the value in the middle,after you have sorted all the values
#Sort all the numbers and then find the middle value

median = np.median(arr)

print("the median value is",median)


#mode
#mode is the value that appears most number of times

#mode = stats.mode(arr)

#print("The mode value is",mode)

    