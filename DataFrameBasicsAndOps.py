# -*- coding: utf-8 -*-
"""
Created on Fri Feb 14 18:01:09 2025

@author: Bhushan
"""

import pandas as pd

#definition of DataFrame
df1 = pd.DataFrame({'name':['amol','raj','vishal','rajesh','suraj','amit'],
                    'sal':[500,600,700,800,900,400]
    },
                   index = list('abcdef')
                   
    )

print("Printing the dataframe values")
print(df1)

print()
print("Use of 'dtypes' to get the column names with data types")

print(df1.dtypes)
print()

print("Use of 'info()' for dataframe")
print(df1.info())
print()


print("Use of 'head()' and 'tail()' functions")
print("By default head()-->Displays first 5  and tail()--->Displays last 5 records")
print("----head()----")
print(df1.head())

print()
print("----tail()----")
print(df1.tail())
print()


print("to display 3 records only with head() and tail() functions")
print()

print("---head(3)---")
print(df1.head(3))

print()
print("---tail(3)---")
print(df1.tail(3))

print()

print("to read a specific column ==>")
print(df1['sal'])
print()

print("Use of 'loc' and 'iloc' functions ")
print("loc====>for label based")
print("iloc====>for index based")
print("to read specific row value with column condition===>")
print(df1.loc['d','sal'])

print()
print("adding columns")
print("adding column HRA as")
df1['hra']=[100,110,112,113,120,132]

print("printing dataframe after adding column")
print(df1)

print()
print("printing row with two column values as")
print(df1.loc['d',['sal','hra']])

print()
print("adding column example i.e. DA")
df1['da'] = 20
print("printing dataframe after adding column da as :-->")
print(df1)


print()
print("use of describe function")

print(df1.describe())

print()
print("use of describe function for perticular column")
print(df1.sal.describe())

print()


print("Rename the column ")
df1.rename(columns = {'name':'emp_name','sal':"emp_sal"},inplace=True)
print("dataframe after column rename is as ===>")
print(df1)

print()
print("renameing index value as")
df1.rename(index = {'a':'A'},inplace=True)
print("printing dataframe after renaming index value 'a' with 'A'")
print(df1)

print()
print("add column gross_sal as")
df1['gross_sal'] = df1['emp_sal']+df1['hra']+df1['da']

print("printing dataframe after addition of gross salary column as ===>")
print(df1)


print()
print("display bonus based on condition")

df1['bonus'] = df1['gross_sal'].apply(lambda x:100 if x>800 else 50)

print(df1)


print()
print("exporting the data to excel sheet")
print(".xlsx extension")
df1.to_excel('employee.xlsx')
print("done exporting ")

print(".csv extension")
df1.to_csv('stud.csv')
print("done exporting ")



