# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 21:30:28 2025

@author: Bhushan
"""

import matplotlib.pyplot as plt
import numpy as np

print("Marker Example ===>'X'")

xpoints = np.array([2,3,4,5,6,7])
ypoints = np.array([2,3,4,5,6,7])

plt.plot(xpoints,ypoints,marker = 'X')

plt.show()

