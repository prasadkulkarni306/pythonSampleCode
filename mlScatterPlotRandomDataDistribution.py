# -*- coding: utf-8 -*-
"""
Created on Fri Mar 14 20:35:59 2025

@author: Bhushan
"""

import numpy as np
import matplotlib.pyplot as plt

#Random Data Distribution

#let's create two arrays with 1000 points with random data dsitribution

#The first array -->mean 5.0 / std. deviation 1.0 / number of points 500

x = np.random.normal(5.0,1.0,500)

#The second array :--> mean 10.0 /std. deviation 2.0 / number of points 500

y = np.random.normal(10.0,2.0,500)


plt.scatter(x,y)
plt.show()

