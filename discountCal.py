# -*- coding: utf-8 -*-
"""
Created on Fri Jan 31 16:27:16 2025

@author: Bhushan
"""

class product:
    __code = None
    __name = None
    __price = None
    __disc = None
    
    
    def __init__(self,code,name,price):
        self.__code = code
        self.__name = name
        self.__price = price
        
    
    def display(self):
        print(f"Product Code ==>{self.__code}")
        print(f"Product Name ==>{self.__name}")
        print(f"Product Price==>{self.__price}")
        print(f"product discount==>{self.__disc}")
           
    def disCal(self): 
         if self.__price > 2000:
             self.__disc=self.__price*0.2
             
         elif self.__price >= 1000 and self.__price <= 2000:
             self.__disc=self.__price*0.15           
         else:
             print("No Discount on this price")
             self.__disc = 0
         self.__price = self.__price - self.__disc    
     
            
p=product(1,"Prasad",1000)
d=p.disCal()
p.display()

            
    
