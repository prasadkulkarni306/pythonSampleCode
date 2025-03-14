# -*- coding: utf-8 -*-
"""
Created on Fri Mar 14 08:05:06 2025

@author: Bhushan
"""

import oracledb as o
import pandas as pd

conn = o.connect(user = 'soe',password = 'soe',dsn = '192.168.1.100:1522/SAI')

print("Connection successful")

cursor = conn.cursor()

cursor.execute("select c.CUSTOMER_ID,c.CUST_FIRST_NAME,c.CUST_LAST_NAME,c.CREDIT_LIMIT,c.CUST_EMAIL,c.DOB,o.ORDER_ID,o.ORDER_STATUS,o.DELIVERY_TYPE from customers c,orders o where c.customer_id=o.customer_id and rownum<50000")

res = cursor.fetchall()

print("The rows are :")

for row in res:
    print("The rows are:",row)
    
df = pd.DataFrame(res)
df.to_excel("custOrderMap.xlsx") 
print("exported completed")   
    
cursor.close()
conn.close()

    

