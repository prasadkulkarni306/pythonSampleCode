# -*- coding: utf-8 -*-
"""
Created on Mon Jan 20 18:44:56 2025

@author: Bhushan
"""

def calc():
    f=int(input("enter the first number"))
    s=int(input("enter the second number"))
    display()
    ch=int(input("enter your choice"))
    return ch,f,s

def ops(ch,f,s):
    match ch:
        case 1:
            print("the addition is",f+s)
        case 2:
            print("the substraction is",f-s)
        case 3:
            print("the multiplication is",f*s)
        case 4:
            print("the division is",f/s)
        case default:
            print("invalid choice")
    
    
    
def display():
    print("MENU")
    print("1:addition")    
    print("2:subtraction")
    print("3:multiplication")
    print("4:division")
    
    
ch,f,s=calc() 
ops(ch,f,s)

 
  