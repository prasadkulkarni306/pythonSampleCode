# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 16:05:00 2025

@author: Bhushan
"""
n = int(input("enter the value for numerator"))

d = int(input("enter the number to divide i.e. denominator"))

try:
    res = n/d

except ZeroDivisionError:
    print("can't divide by zero")
    
except ValueError:
    print("enter a valid number")

else:
    print(f"Result is==>{res}")

finally:
   print("Execution Complete")        

