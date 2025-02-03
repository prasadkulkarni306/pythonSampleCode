# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 18:06:40 2025

@author: Bhushan
"""

class student:
    #data members
    __rollNo = None
    __name = None
    __per = None
    
    #members
    def acceptData(self,rollNo,name,per):
        self.__rollNo = rollNo
        self.__name = name
        self.__per = per
        
    def displayData(self):
        print(f"the Roll Number is==>{self.__rollNo} Name is ==>{self.__name} Percentage=={self.__per}")
        
        
st1=student()
st2=student()

st1.acceptData(1, "Prasad", 60.34)
st2.acceptData(2,"Rajesh", 50.23) 

st1.displayData()
st2.displayData()
       