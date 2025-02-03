# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 17:09:58 2025

@author: Bhushan
"""

class Employee:
    #data members
    __empname = None
    __empid = None
    __dept = None
    
    def accept(self,empid,empname,dept):
        self.__empid = empid
        self.__empname = empname
        self.__dept = dept
        
    def display(self):
        print(f"firstname==>{self.__empname} || employee ID==>{self.__empid} || Department ==>{self.__dept}")      
        
emp1=Employee()
emp2=Employee()


emp1.accept(1,"Prasad","IT")
emp1.display()

emp2.accept(2,"Sayali","BDS")
emp2.display()
       