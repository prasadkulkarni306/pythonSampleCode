# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 18:42:34 2025

@author: Bhushan
"""

import matplotlib.pyplot as plt

name = ['Rohan','Raj','Suraj','Tej']
maths = [67,89,60,69]
eng = [90,67,89,36]

plt.bar(name,maths,width = 0.4,color = 'red')
plt.bar(name,maths,bottom = eng,width = 0.4)
plt.legend(['maths','eng'])
plt.xlabel('Stduent Name')
plt.ylabel('Marks')
plt.title('Report')

plt.show()