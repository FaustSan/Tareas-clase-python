# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 16:06:19 2024

@author: faust
"""

import numpy as np
import matplotlib.pyplot as plt

img=np.ones((256,256))
ss=img.shape

img[:10, :] = 0  # Marco superior
img[-10:, :] = 0  # Marco inferior
img[:, :10] = 0  # Marco izquierdo
img[:, -10:] = 0  # Marco derecho

i=10
j=10
for i in range(ss[0]-10):
    for j in range (ss[1]-10):
        if i==j:
            img[i-5:i+5,j]=0
            
for i in range(10, ss[0]-10):
    j=ss[1]-i-1
    img[i-5:i+5, j] = 0
    
    
plt.figure()
plt.imshow(img,cmap = "gray")