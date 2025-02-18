# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 18:32:21 2025

@author: Bhushan
"""

import matplotlib.pyplot as plt

x = [1,2,3,4]
y = [10,20,30,40]

plt.plot(x,y,'go:')

plt.xlabel('Points')
plt.ylabel('Marks')
plt.title("My Graph")

plt.show()

