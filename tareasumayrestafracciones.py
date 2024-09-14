# -*- coding: utf-8 -*-
"""
Created on Wed Aug 14 16:47:13 2024

@author: faust
"""
suma=0
for i in range(2,101,2) :
    suma= suma + (1/(i-1)) - (1/i)
    print (suma)
    print (i)
    
    
    
# b='11111111'
# c= len(b)-1
# suma =0

# for s in b:
#     n=int (s)
#     suma= suma + (n)*(2**c)
#     c=c-1
    
# print(suma)