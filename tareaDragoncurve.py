# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 21:42:51 2024

@author: faust
"""

import  turtle 

s='F'
R1= 'F+G'
R2= 'F-G'
angle = 90

for i in range (10):
    ss=''
    for m in s:
        if m == 'F':
            ss=ss+R1
        elif m== 'G':
            ss=ss+R2
        else :
            ss=ss+m
    s=ss
    

    
for d in  s:
    if (d == 'F') or (d=='G'):
        turtle.forward(10)
    
    elif d == '+':
        turtle.left(angle)
    else :
        turtle.right(angle)
        
        
