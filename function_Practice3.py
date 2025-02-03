# -*- coding: utf-8 -*-
"""
Created on Mon Jan 20 18:27:47 2025

@author: Bhushan
"""

def stduInfo():
    fname=input("enter the first name")
    lname=input("enter the last name")
    m1=int(input("enter the marks for maths"))
    m2=int(input("enter the marks for science"))
    m3=int(input("enter the marks for english"))
    return fname,lname,m1,m2,m3

def stduRes(a,b,c,d,e):
    total=c+d+e
    per=float(total/3)
    return total,per

first,last,math,sci,eng=stduInfo()
t,p=stduRes(first,last,math,sci,eng)


print(f'the student{first}+{last} has scored total-->{t} and percentage-->{p}')



    