# -*- coding: utf-8 -*-
"""
Created on Tue Jan 21 18:34:07 2025

@author: Bhushan
"""

num=int(input("enter the number"))
j=num
flag=0
count=0
while (flag==0):
 i=num%10
 j=num//10
 num=j
 count=count+1
 if j==0:
     flag=1
 print(f"i-->{i} and j-->{j}")
 
 print(f"the count is-->{count}")