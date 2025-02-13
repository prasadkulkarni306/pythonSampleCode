# -*- coding: utf-8 -*-
"""
Created on Mon Feb  3 18:05:15 2025

@author: Bhushan
"""

from abc import ABC,abstractmethod

class shape(ABC):
    @abstractmethod
    def area(self):
        pass
    
class circle(shape):
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        self.result=3.14*self.radius*self.radius
        print(f"the area od circle is==>{self.result}")


class triangle(shape):
     def __init__(self,length,breadth):
         self.length=length
         self.breadth=breadth
     def area(self):
         self.res=self.length*self.breadth
         print(f"the area of triangle is==>{self.res}")
 


c1=circle()
c1.area(5) 
        
t1=triangle()
t1.area(1,3)