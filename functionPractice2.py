# -*- coding: utf-8 -*-
"""
Created on Mon Jan 20 18:21:47 2025

@author: Bhushan
"""

def calcu(first_n,second_n):
    summ=first_n+second_n
    subb=first_n-second_n
    return summ,subb


f=int(input("enter the first number"))
s=int(input("enter the second number"))

res1,res2=calcu(f,s)    

print(f'the addition of {f} and {s} is==>{res1}')
print(f'the substraction of {f} and {s} is==>{res2}')
