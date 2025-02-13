# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 15:59:04 2025

@author: Bhushan
"""

n = int(input("enter any number please"))

try:
    res = n/0 
except ZeroDivisionError:
    print("can't divide by zero")
        