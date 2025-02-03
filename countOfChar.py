# -*- coding: utf-8 -*-
"""
Created on Thu Jan 23 18:41:21 2025

@author: Bhushan
"""

s = input("Please enter the string")
print(f"The entered string is-->{s}")

c = input("enter the character you want to find it's occurance")
count = 0
flag = 0
for t in s:
    if t == c:
        count = count + 1
        print(f"Hey,the given character found in string-->{count}")
        flag = 1

if flag == 1:
    print(f"the given character-->{c} is present in the string-->{s} total-->{count} times")        
else:
    print(f"Sorry,the given character is not present in the string")        