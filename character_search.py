# -*- coding: utf-8 -*-
"""
Created on Thu Jan 23 18:28:30 2025

@author: Bhushan
"""

s=input("enter any string")
print(f"you have enterted-->{s}")
flag = 0
c=input("enter the character you want to search in a given string")
for t in s:
    if t == c:
        print(f"the given character-->{c} is present in the string-->{s}")
        flag = 1
        break
    
if flag == 0:
    print(f"The given character-->{c} is not present in the string-->{s}")    
        
     
        
        