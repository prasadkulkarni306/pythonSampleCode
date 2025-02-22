# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 17:43:37 2025

@author: Bhushan
"""
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd

print("scatter plots")

print("Old Cars --->Max Speed")

#Day1
x = [2,3,4,5,6]
y = [100,70,80,65,55]

plt.scatter(x, y)
plt.show()

#Day2
x = [2,3,4,5,6]
y = [90,75,50,80,55]

plt.scatter(x, y)
plt.show()

plt.xlabel("old cars(in years)")
plt.ylabel("max speed")
plt.legend(['Day1','Day2'])
plt.scatter(x,y)
plt.show()