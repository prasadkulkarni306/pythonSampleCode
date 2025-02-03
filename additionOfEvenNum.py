# -*- coding: utf-8 -*-
"""
Created on Tue Jan 21 17:33:27 2025

@author: Bhushan
"""
sum = 0
num = int(input("enter the number "))
print(f"the entered number is--->{num}")

i = 0
while i <= num:
    i=i+1
    if i%2 != 0:
        continue
    else:
        sum = sum + i
        print(f"the even number found is -->{i} and sum till now is-->{sum}")
     

print(f"the addition of all even numbers between 1 and {num} is--->{sum}") 

       
