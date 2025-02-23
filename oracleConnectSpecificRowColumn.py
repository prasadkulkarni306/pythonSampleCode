# -*- coding: utf-8 -*-
"""
Created on Sun Feb 23 16:33:16 2025

@author: Bhushan
"""

import oracledb as o
import pandas as pd

conn = o.connect(user = 'soe',password = 'soe',dsn = '192.168.1.100:1522/SAI')

print("conneection csuccessfully done")

cursor = conn.cursor()

cursor.execute("select street_name,country,town from addresses")
               
res = cursor.fetchmany(numRows = 5) 

print("The datatype is",type(res))



print("printing all rows and columns")
for row in res:
    print(row)
    
print()    

print("printing only first row i.e. Street Name")
for row in res:
    print(row[0])
    
print()    

print("printing specific row nd column")
print(res[0][1])
print(res[2][1])
print()

cursor.close()
conn.close()    