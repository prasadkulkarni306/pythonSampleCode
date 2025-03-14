# -*- coding: utf-8 -*-
"""
Created on Fri Mar 14 16:33:03 2025

@author: Bhushan
"""

import numpy as np
import matplotlib.pyplot as plt

#this will generate the random databset
x = np.random.uniform(0,50,500)

#this will create the histogram 
plt.hist(x,10)

plt.show()
