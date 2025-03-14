# -*- coding: utf-8 -*-
"""
Created on Sat Feb 22 22:03:56 2025

@author: Bhushan
"""

import getpass as g
import oracledb as o
import pandas as pd

pwd = g.getpass("enter password")

connection = o.connect(user = 'sample',password = pwd,dsn = '192.168.1.100:1521/source1')

print("success")

print(connection)

cursor = connection.cursor();

cursor.execute("select * from test")

res = cursor.fetchall()


print(res)



df = pd.DataFrame(res)
print(df)

df.to_excel("sample.xlsx")

print("exported successfully")

print("query exexcuted successfully")

cursor.close()
 
connection.close()