# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 05:24:09 2025

@author: Bhushan
"""

import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([10,40,45,70,80])
ypoints = np.array([1,4,89,2,10])

print("the linestype dashdot example")

plt.plot(xpoints,ypoints,linestyle = 'dashdot',color='red')

plt.show()
