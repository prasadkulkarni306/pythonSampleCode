# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 18:38:30 2025

@author: Bhushan
"""

import matplotlib.pyplot as plt

x = ['Rohan','Raj','Suraj','Tej']
y = [67,89,77,73]

plt.bar(x,y,width=0.4,color='red')

plt.xlabel('Student Name')

plt.ylabel("Student Marks")

plt.title("Student Report")

plt.show()