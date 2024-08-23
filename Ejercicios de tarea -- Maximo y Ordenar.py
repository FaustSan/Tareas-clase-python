# -*- coding: utf-8 -*-
"""
Created on Thu Aug 22 09:48:35 2024

@author: faust
"""

"""" Encontrar el número mayor """

a=[1,7,4,2,1,5,4,6,2]
nm=a[0]

for i in  range(len(a)):
    if (nm < a[i]):
        nm = a[i]



print ('el numero mayor del arreglo es ', nm)



""" Ordenar de mayor a menor """

c=len(a)

for b in  range(len(a)): 
    for j in range (0,c-b-1):
         x=a[j]
         y=a[j+1]
         if x>y:
             a[j]=y
             a[j+1]=x
        
        
        
print ("la lista ordenada es ", a)