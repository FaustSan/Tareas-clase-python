# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 21:15:15 2024

@author: faust
"""

import  turtle 

s='A'
R1= 'B-A-B'
R2= 'A+B+A'
angle = 60

for i in range (6):
    ss=''
    for m in s:
        if m == 'A':
            ss=ss+R1
        elif m== 'B':
            ss=ss+R2
        else :
            ss=ss+m
    s=ss
    

    
for d in  s:
    if (d == 'A') or (d=='B'):
        turtle.forward(10)
    
    elif d == '+':
        turtle.left(angle)
    else :
        turtle.right(angle)