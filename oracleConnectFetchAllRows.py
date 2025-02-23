# -*- coding: utf-8 -*-
"""
Created on Sun Feb 23 16:23:28 2025

@author: Bhushan
"""

import oracledb as o
import pandas as pd

conn = o.connect(user = 'soe',password = 'soe',dsn = '192.168.1.100:1522/SAI')

cursor = conn.cursor()

cursor.execute("select * from products")

print("fetching all rows")
res = cursor.fetchall()

for row in res:
    print(row)
  
df = pd.DataFrame(res) 

print(df) 

cursor.close() 
conn.close()

 
    