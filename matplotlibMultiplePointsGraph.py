# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 13:49:37 2025

@author: Bhushan
"""

import matplotlib.pyplot as plt
import numpy as np


print("To draw a line from (1,3)==>(2,8)==>(6,1)==>(8,10)")

xpoints = np.array([1,2,6,8])
ypoints = np.array([3,8,1,10])

plt.plot(xpoints,ypoints)
plt.show()

print()
print("to draw a line from (1,1)==>(2,5)==>(6,7)==>(3,10)==>(5,5)")

xpoints = np.array([1,2,6,3,5])
ypoints = np.array([1,5,7,10,5])

print()
plt.plot(xpoints,ypoints)
plt.show()


print()
plt.plot(xpoints,ypoints,'o')
plt.show()