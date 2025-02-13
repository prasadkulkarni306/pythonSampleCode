# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 16:36:38 2025

@author: Bhushan
"""

list1 = ["20","30","40","50","Rajesh","Umesh","10"]

print("---MENU---")
print("1:find length of List")
print("2:print all elements of List")
print("3:Sorting the elements")
ch = int(input("enter your choice"))

match ch:
    case 1:
        res = len(list1)
        print("the length is",res)
    case 2:
        i = 0 
        while(i < len(list1)):
            print(f"the value at index==>{i} is value==>{list1[i]}")
            i =i + 1
    case 3:
        print("the list before sorting",list1)
        list1.sort()
        print("The list after sorting",list1)
        
    case default:
        print("Invalid Choice")
        
        
        
        