# -*- coding: utf-8 -*-
"""
Created on Sat Feb 22 22:46:03 2025

@author: Bhushan
"""

import oracledb as o
import pandas as pd

connection = o.connect(user = 'soe',password = 'soe',dsn = '192.168.1.100:1522/SAI')

print("connection success")

print("connection is",connection)

cursor = connection.cursor()

cursor.execute("select * from products")

res = cursor.fetchall()

df = pd.DataFrame(res)

df.to_excel("products.xlsx")

print("export completed")

cursor.close()