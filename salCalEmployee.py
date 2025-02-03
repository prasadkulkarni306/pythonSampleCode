# -*- coding: utf-8 -*-
"""
Created on Fri Jan 31 16:04:18 2025

@author: Bhushan
"""

class employee:
    __sid = None
    __sname = None
    __bsal = None
    __gsal = 0
    
    def __init__(self,sid,sname,bsal,gsal):
        self.__sid = sid
        self.__sname = sname
        self.__bsal = bsal
        self.__gsal = gsal
        
    def dispInfo(self,sid,sname,bsal,gsal):
        print(f"employee ID==>{self.__sid}")
        print(f"employeename==>{self.__sname}")
        print(f"employee basic salary==>{self.__bsal}")
        print(f"employee gross salary==>{self.__gsal}")
        
    def calGSal(self,sid,sname,bsal,gsal):
        self.__gsal=self.__bsal*0.4+self.__bsal*0.2+self.__bsal*0.12+self.__bsal
        return self.__gsal


e1=employee(1,"Prasad",40000,0)
result=e1.calGSal(1,"Prasad",40000,0)
e1.dispInfo(1,"Prasad",40000,result)    