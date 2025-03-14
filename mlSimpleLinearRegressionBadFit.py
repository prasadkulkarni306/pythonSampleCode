# -*- coding: utf-8 -*-
"""
Created on Fri Mar 14 22:25:51 2025

@author: Bhushan
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats as s

x = [89,43,36,36,95,10,66,34,38,20,26,29,48,64,6,5,36,66,72,40]
y = [21,46,3,35,67,95,53,72,58,10,26,34,90,33,38,20,56,2,47,15]


slope, intercept, r, p, std_err = s.linregress(x,y)

print("The coefficient of corelation is",r)

#Here the coeffient of corelation is 0.013 which means that data set is not suitable for 
#linear regression


def myfunc(x):
    return slope*x + intercept

mymodel = list(map(myfunc,x))

plt.scatter(x,y)
plt.plot(x,mymodel)
plt.show()


 
 