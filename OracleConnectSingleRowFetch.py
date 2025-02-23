# -*- coding: utf-8 -*-
"""
Created on Sun Feb 23 15:57:18 2025

@author: Bhushan
"""

import oracledb as o
import pandas as pd

con = o.connect(user = 'soe',password = 'soe',dsn = '192.168.1.100:1522/SAI')

print("connection success")

cursor = con.cursor()

cursor.execute("select * from customers")


#fetching single row 
res = cursor.fetchone()

for row in res:
    print(row)
    
cursor.close()   