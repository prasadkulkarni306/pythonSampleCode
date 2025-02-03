# -*- coding: utf-8 -*-
"""
Created on Mon Jan 20 05:11:57 2025

@author: Bhushan
"""

sal=float(input("enter the basic salary of employee"))
print("you have entered the basic salary",sal)

hra=sal*40/100;
da=sal*20/100;
pf=sal*12/100;
pt=200;

g_sal=(sal+hra+da)-(pf+pt)

print("the hra is",hra)
print("the da is",da)
print("the pf is",pf)
print("the professional tax is",pt)
print("the gross salary is",g_sal)




