# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 18:40:49 2025

@author: Bhushan
"""

class studentInfo():
    #members
    __sid = None
    __sname = None
    __sdept = None
    
    #constructor
    def __init__(self,sid,name,dept):
        self.__sid = sid
        self.__sname = name
        self.__sdept = dept

    #methods    
    def infoDisplay(self):
        print(f"student ID==>{self.__sid}")
        print(f"stduent Name==>{self.__sname}")
        print(f"student Department==>{self.__sdept}")
        
    def infoAccept(self,sid,name,dept):
        self.__sid = sid
        self.__sname = name
        self.__sdept = dept
        

s1 = studentInfo(1,"TOM","IT")
print("the initial values are as below:-->")
s1.infoDisplay() 
print()
print()
print("Values accepted through end users as below:-->")
s1.infoAccept(333, "Rajesh", "HR")
s1.infoDisplay()      