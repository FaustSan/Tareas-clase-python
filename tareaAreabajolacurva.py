# -*- coding: utf-8 -*-
"""
Created on Wed Aug 14 17:20:48 2024

@author: faust
"""



delta=(4-1)/100
suma = delta*(1**2)
for i in range (1,101):
    suma=suma + (((1 + (delta*i))**2)  * delta )
    print (suma)
    print (i)