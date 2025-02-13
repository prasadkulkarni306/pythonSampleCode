# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 16:14:10 2025

@author: Bhushan
"""


try:
    n = int(input("enter any number to inverse"))

except ValueError:
    print("Invalid number")
else:
    print("the entered number is",n)
finally:
    print("the number accepted successfully")    


try:
    res = 1/n
except ZeroDivisionError:
   print("Can't divide by zero") 

else:
    print("the result is",res)
finally:
    print("the operation completed")    
    
    