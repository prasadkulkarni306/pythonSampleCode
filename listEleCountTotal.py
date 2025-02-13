# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


o = 0
j = 0
list1 = [61,61,61,61,62,63,64]




for i in list1:
    while j < len(list1):
        if list1[j] == i:
           o = o + 1    
        j = j + 1
print(f"counter={o} and element==>{i} ")    
o = 0
j = 0               


