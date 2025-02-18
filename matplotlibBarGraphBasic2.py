# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 18:48:23 2025

@author: Bhushan
"""

from matplotlib import pyplot as plt

name = ['Prasad','Abdul','Divyansh','Murali']

maths = [90,80,70,75]
sci = [80,50,69,89]
eng = [98,78,67,94]

bar1 = [0,2,4,6]
bar2 = [i+0.4 for i in bar1]
bar3 = [i+0.4 for i in bar2]

plt.bar(bar1,maths,width=0.4,label='Maths')
plt.bar(bar2,eng,width=0.4,label='english')
plt.bar(bar3,sci,width=0.4,label='sci')

plt.xticks(bar2,name)

plt.xlabel("Student Name")
plt.ylabel('Marks')
plt.title('Reports')
plt.legend(['Maths','Science','English'])

plt.show()