# -*- coding: utf-8 -*-
"""
Created on Tue Jan 21 17:58:06 2025

@author: Bhushan
"""

sum = 0
num = int(input("please enter any number"))

while num >= 0:
    if num%2 != 0:
        sum = sum + num
        print(f"Hey,find the odd number-->{num} and addition till now is-->{sum}")
    else:
        print(f"the current number-->{num} is even one and we are skipping")
    num = num - 1    
        
print(f"the addition of all odd numbers between 1 and {num} is ===> {sum}")  

      