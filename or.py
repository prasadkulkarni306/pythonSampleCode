# -*- coding: utf-8 -*-
"""
Created on Sun Feb 23 16:06:28 2025

@author: Bhushan
"""

import oracledb as o
import pandas as pd

conn = o.connect(user = 'soe',password = 'soe',dsn = '192.168.1.100:1522/SAI')

cursor = conn.cursor()

cursor.execute("select * from products")

print("printing specific number of rows i.e. three(3)")
res = cursor.fetchmany(numRows = 3)

for row in res:
    print(row)
    print()
    
df = pd.DataFrame(res) 

print(df) 
print()  

cursor.close()
conn.close()
