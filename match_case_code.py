# -*- coding: utf-8 -*-
"""
Created on Wed Jan 15 18:03:03 2025

@author: Bhushan
"""

print('1:addition')
print('2:substraction')
print('3:multiplication')
print('4:division')

a=int(input('enter your choice'))
b=int(input('enter first number'))
c=int(input('enter second number'))
match a:
    case 1:
        print('the addition is',b+c)
    case 2:
        print('the substraction is',b-c)
    case 3:
        print('the multiplication is',b*c)
    case 4:
        if c!=0:
           print('the division is',b/c)
        else:
           print('could not divide')
    case default:
        print('invalid choice')