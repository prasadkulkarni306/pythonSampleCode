# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 17:38:20 2025

@author: Bhushan
"""

class studentInfo():
    __sid = None
    __sname = None
    __sdept = None
    
    def setSid(self,sid):
        self.__sid = sid
        
    def getSid(self):
        return self.__sid
    
    def setSname(self,sname):
        self.__sname = sname
        
    def getSname(self):
        return self.__sname
    
    def setDept(self,sdept):
        self.__sdept=sdept
        
    def getDept(self):
        return self.__sdept

    def infoDisplay(self):
        print(f"Student ID is=={self.__sid}")
        print(f"Student Name is=={self.__sname}")
        print(f"Student Department ==>{self.__sdept}")
        
s1=studentInfo()
s1.setSid(1)
s1.setSname("Prasad")
s1.setDept("IT") 

print("Student Information with getters and setters")
print(s1.getSid(),s1.getSname(),s1.getDept()) 

print("Student Information with function")
s1.infoDisplay()
      