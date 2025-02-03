# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 16:12:36 2025

@author: Bhushan
"""

f = input("enter the string to check for Palindrome")
print(f"the entered string is-->{f}")

r = ''
c = 0
for i in f:
    r = i + r
    c = c + 1
print(f"the reversed string is-->{r} and length is -->{c}")

flag = 0
i = 0
first = ' '
second = ' '
while i < len(f):
    first = f[i]
    second = r[i]
    print("the first",first)
    print("the second",second)
    if f[i] != r[i]:
            flag = 1
            break
    i = i + 1


    

if flag == 1:
   print(f"the entered string-->{f} is not palindrome")
else:
   print(f"the entered string-->{f} is palindrome")    
    
