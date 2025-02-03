# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 18:15:16 2025

@author: Bhushan
"""

class productInfo():
    #members
    __prodCode = None
    __prodName = None
    __prodPrice = None
    
    #functions
    def acceptInfo(self,code,name,price):
        self.__prodCode = code
        self.__prodName = name
        self.__prodPrice = price
        
    def displayInfo(self): 
        print(f"Product Code==>{self.__prodCode}")
        print(f"Product Name==>{self.__prodName}")
        print(f"Product Price==>{self.__prodPrice}")
        

prd1 = productInfo()
prd2 = productInfo()

prd1.acceptInfo(1, "Washing Powder", 34.12) 
prd2.acceptInfo(2, "Tooth Paste", 23)

prd1.displayInfo()
prd2.displayInfo()       
        