# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 21:24:01 2025

@author: Bhushan
"""

import matplotlib.pyplot as plt
import numpy as np

print("Marker Examples===> '*' ")

xpoints = np.array([1,2,3,4,5,6])
ypoints = np.array([1,2,3,4,5,6])

plt.plot(xpoints,ypoints,marker = '*')
plt.show()

