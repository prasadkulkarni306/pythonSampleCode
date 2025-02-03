# -*- coding: utf-8 -*-
"""
Created on Thu Jan 23 17:55:58 2025

@author: Bhushan
"""

s = input("enter the string")
print(f"the entered string -->{s}")
i = 0
le = 0
count = 0

 
while i < len(s):
    t = s[i]
    if t == 'a' or t == 'e' or t == 'o' or t == 'u' or t == 'i':
        count = count + 1
    i = i + 1        
       
        
print(f"count --> {count}")