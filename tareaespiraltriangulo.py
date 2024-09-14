# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 22:10:31 2024

@author: faust
"""

import matplotlib.pyplot as plt
import math

#Triángulo inicial
ax=[0,1]
ay=[0,0]
plt.plot(ax,ay)

bx=[1,1]
by=[0,1]
plt.plot(bx,by)

cx=[0,1]
cy=[0,1]
plt.plot(cx,cy)

x1=1 
y1=1 


for i in range(16):
    x0=0
    y0=0
    
    
    mA=(y1-y0)/(x1-x0)
    mB=-(1/mA)  
    
    deltx= 1/(math.sqrt(1+(mB**2)))
    delty=mB*deltx
    
    if i < 5:
    
        x2=x1-deltx
        y2=y1-delty
        
    else:
        x2=x1+deltx
        y2=y1+delty
        
    Ax=[x0,x1]
    Ay=[y0,y1]
    plt.plot(Ax,Ay)
    
    Bx=[x1,x2]
    By=[y1,y2]
    plt.plot(Bx,By)
    
    x1=x2
    y1=y2
    
