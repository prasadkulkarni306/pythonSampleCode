# -*- coding: utf-8 -*-
"""
Created on Thu Jan 23 18:12:36 2025

@author: Bhushan
"""

s=input("enter the string")
count = 0

for t in s:
    print(t)
    if (t == 'a' or t == 'A')  or  (t == 'e' or t == 'E') or (t == 'i' or t == 'I') or (t == 'o' or t == 'O') or (t == 'u' or t == 'U'):
          count = count + 1
    
      

print(f"the total count of vowels is -->{count}")        