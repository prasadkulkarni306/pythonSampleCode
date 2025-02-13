# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 18:35:53 2025

@author: Bhushan
"""
###########################################################
t = (1,2,3,4,5,6,7)

print("the tuble of same datatype is ==>")
print(t)
print()
print()

###########################################################
print("the tuple of different datatype is ==>")
t = (1,"Prasad","Kulkarni",[1,34,1,45],(1,2,3,4,5,6,7,8,9),"M")
print(t)
print()
print()

###########################################################
print("the values at different indexes are ")
print(t[0])
print(t[1])
print(t[2])
print(t[3])
print(t[4])
print(t[5])

print()
print()
###########################################################

print("printing the values at indexes inside the tuple using loop")
i = 0
while i < len(t):
    print(f"the value at index==>{i} of tuple is ==>{t[i]}")         
    i = i + 1
    
print()    

###########################################################

print("printing elements at different indexes")
print(t[3][0])
print(t[3][1])
print(t[4][5])
print(t[5])

###########################################################

t = (1,2,3,4,5)

print("the elements in the tuple are ===>",t)

print("the datatype of t is==>",type(t))
t1 = list(t)
print("the datatype is now changed to list to add/append the value")
t1.append(6)

print("the changed datatype is ==>",type(t1))
print("the elements in the list are ===>",t)
print("changing the datatype again from list to tuple")

t=tuple(t1)

print("the tuple after adding element is",t)
print("the datatype of t is==>",type(t))

###########################################################




    
    