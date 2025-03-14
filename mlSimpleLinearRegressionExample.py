# -*- coding: utf-8 -*-
"""
Created on Fri Mar 14 20:55:21 2025

@author: Bhushan
"""

import matplotlib.pyplot as plt
import numpy as np
from scipy import stats as s

#X-axis represents the age of the car
#Y-axis represents the speed of the car

x = [5,7,8,7,2,17,2,9,4,11,12,9,6]
y = [99,86,87,88,111,86,103,87,94,78,77,85,86]


slope, intercept, r, p, std_err = s.linregress(x,y)

def myfunc(x):
    return slope * x + intercept

mymodel = list(map(myfunc,x))

#The coefficient of corelation ranges from -1 to 1,where 0 means no relationship
#and 1 (and -1) means 100% related

print("The relationship / the coeffient of corelation is r",r)


plt.scatter(x,y)
plt.plot(x,mymodel)
plt.show()

#to predict the speed of a car with 10 years age

speed = myfunc(10)

print("The speed of the car with age 10 years",speed)

