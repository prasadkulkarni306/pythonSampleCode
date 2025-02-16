# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 11:07:13 2025

@author: Bhushan
"""


import matplotlib.pyplot as plt
import numpy as np

print("Graph")
xpoints = np.array([1,2,3,4,5,6])
ypoints = np.array([1,2,3,4,5,6])

plt.plot(xpoints,ypoints)
plt.show()

print("this will create a graph with (0,0) to (0,250)")
xpoints = np.array([0,6])
ypoints = np.array([0,250])
plt.plot(xpoints,ypoints)
plt.show()