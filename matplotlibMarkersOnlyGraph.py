# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 13:41:58 2025

@author: Bhushan
"""

import matplotlib.pyplot as plt
import numpy as np

print("tp plot only markers,one can use shortcut string notation parameter 'o' i.e. rings")

print("to draw two points,first at==>(1,3) and second at==>(8,10)")

xpoints = np.array([1,8])
ypoints = np.array([3,10])

plt.plot(xpoints,ypoints,'o')

plt.show()

