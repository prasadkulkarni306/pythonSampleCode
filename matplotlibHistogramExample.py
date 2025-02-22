# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 17:55:37 2025

@author: Bhushan
"""

from matplotlib import pyplot as plt

data = [350,70,50,60,100,120,150,150,170,180,180,200,210,250,400,400,300,200,210]

plt.hist(data, ec = 'red', bins = [0,50,100,150,200,250,300,350,400,450])

plt.show()