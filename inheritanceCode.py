# -*- coding: utf-8 -*-
"""
Created on Fri Jan 31 17:31:39 2025

@author: Bhushan
"""

#__ Private
#_ protected
# no underscore public

class Employee:
    _id = None
    _name = None
    _basic = None
    _hra = None
    _da = None
    _pf = None
    _gross = None
    
    def __init__(self,id,name,basic):
        self._id = id
        self._name = name
        self._basic = basic
        
    def calculate(self):
        self._hra = self._basic*0.40
        self._da = self._basic*0.20
        self._pf = self._basic*0.12
        self._gross = (self._hra + self._da + self._basic) - self._pf
        
    def __str__(self):
        return f"employee data==>{self._name},{self._gross}"
    
    
class Manager(Employee):
    __travelling = None
    def __init__(self,id,name,basic,ta):
        super().__init__(id,name,basic)
        self.__travelling = ta
        
    def calculate(self):
         self._hra = self._basic*0.40
         self._da = self._basic*0.20
         self._pf = self._basic*0.12
         self._gross = (self._hra + self._da + self._basic + self.__travelling) - self._pf
         
    def __str__(self):
        return f"Manager Data==>{self._name},{self._gross}"
    
    
class CEO(Manager):
    __MAllow = None
    def __init__(self,id,name,basic,ta,ma):
        super().__init__(id,name,basic,ta)
        self.__MAllow = ma
        
    def calculate(self):
        self._hra = self._basic*0.40
        self._da = self._basic*0.20
        self._pf = self._basic*0.12
        self._gross = (self._hra + self._da + self._basic + self.__MAllow) - self._pf
        
    def __str__(self):
        return f"CEO's Data==>{self._name},{self._gross}"
        
        
        
        
            
  
    
e1=Employee(1,"Prasad",40000)    
e1.calculate()  
print(e1)  
    

m1=Manager(1,"Prasad",100000,20000)  
m1.calculate()
print(m1)

c1=CEO(1,"Prasad",400000,20000,50000)
c1.calculate()
print(c1)
      
        