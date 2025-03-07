# -*- coding: utf-8 -*-
"""
Created on Fri Mar  7 18:10:20 2025

@author: Bhushan
"""

import mysql.connector as sql

db_config = {
    'user':'root',
    'password':'root',
    'host':'localhost',
    'database':'sample'
        }

conn = sql.connect(**db_config)

cursor = conn.cursor()

def addEmp(id,name,salary,city):
    try:
        qry = "insert into employee1 values(%s,%s,%s,%s)"
        param = (id,name,salary,city)
        cursor.execute(qry,param)
        conn.commit()
        print("record inserted successfully")
    except Exception as e:
        print(e)
        
def displayEmp():
    try:
        qry = "select * from employee1"            
        cursor.execute(qry)
        res = cursor.fetchall()
        for data in res:
            print(data)
    except Exception as e:
        print(e)
        
def displayEmpWithID(id):
    try:
        qry = "select * from employee1 where id=%s"
        param =(id,)
        cursor.execute(qry,param)
        res = cursor.fetchone()
        for data in res:
            print(data)
    except Exception as e:
        print(e)
        
def updateEmp(id,name,salary,city):
    try:
        qry = "update employee1 set name=%s,salary=%s,city=%s where id=%s"
        param = (name,salary,city,id)
        cursor.execute(qry,param)
        conn.commit()
        print("record updated successfully")
    except Exception as e:
        print(e)                       
            
def deleteEmp(id):
    try:
        qry = "delete from employee1 where id=%s"
        param = (id,)
        cursor.execute(qry,param)
        conn.commit() 
        print("record delete successfully")            
    except Exception as e:
        print(e)        
        
        
        
addEmp(1,'Prasad',3444,'Pune')
displayEmp()
displayEmpWithID(1)
updateEmp(1, 'Sayali', 20000,'Solapur')
deleteEmp(1)




        