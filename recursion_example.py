# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 17:48:45 2025

@author: Bhushan
"""



def addNumber(num):
     
    j=num%10
    i=num//10
    num=i
    if j==0:
        return 0
    else:
        return j + addNumber(i)
        
    
n=int(input("enter the number"))    
result=addNumber(n)  
print(f"addition is-->{result}")  