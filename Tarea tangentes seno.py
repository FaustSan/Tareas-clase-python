# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 16:58:43 2024

@author: faust
"""

import matplotlib.pyplot as plt
import math


del1=.1
xx=0
x=[]; y=[]; y2=[]

while xx<2*math.pi:
    x.append(xx)
    y.append(math.sin(xx))
    
    xx=xx+del1
    


start = math.pi/4
step = math.pi / 2

while start < 2*math.pi:
    
    x0=start
    y0=math.sin(start)
    m=math.cos(start)
    x1=(start)-0.5
    x2=(start)+0.5
    
    y1=m*(x1-x0)+y0
    y2= m*(x2-x0)+y0
    
    start=start+step
    
    px=[x1,x2]
    py=[y1,y2]
    
    plt.plot(px,py) 
    
    
plt.plot(x,y)
plt.show()

