# -*- coding: utf-8 -*-
"""
Created on Fri Feb 14 15:34:03 2025

@author: Bhushan
"""

print("Python Collections(Arrays)")
print("There are four collection datatypes in python programming language")
print("1:List is ordered/changable/allow duplicates")
print("2:Tuple is ordered/unchangable/allows duplicates")
print("3:Set")
print("4:dictionary")

print("TIP : when choosing a collection type out of LIST/TUPLE/SET/DICTIONARY, it is useful to understand their properties")

print("List items are index and it starts with 0")
print("negative indexing starts from the end i.e. with -1")

print()

mylist = ["Banana","Cherry","Apple","Bannana"]

print()
print(f"the list is==>{mylist}")
print()

i = 0
while (i < len(mylist)):
  print(f"the element at index==>{i} is ==>{mylist[i]}")
  i = i + 1

print()
print(f"the list is==>{mylist}")
print()

print(f"the element at index -4 is==>{mylist[-4]}")
print(f"the element at index -3 is==>{mylist[-3]}")
print(f"the element at index -2 is==>{mylist[-2]}")
print(f"the element at index -1 is==>{mylist[-1]}")



