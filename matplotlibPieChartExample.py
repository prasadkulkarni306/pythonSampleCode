# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 18:00:57 2025

@author: Bhushan
"""

from matplotlib import pyplot as plt

expenses = ['Rent','PL','Other','Medical']
  
amount = [22000,10000,23000,5000]
  
plt.pie(amount,labels = expenses, autopct = '%0.2f%%')
  
plt.show()