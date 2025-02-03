# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 16:05:02 2025

@author: Bhushan
"""

s = input("enter any string please")
print("the entered string is",s)

c = input("enter the required character which you want to remove")
res = ''
for i in s:
    if i == c:
        continue
    else:
        res = res + i;
        
print(f"the string after removal of character==>{c} is==>{res}")

        