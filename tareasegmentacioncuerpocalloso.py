# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 23:00:27 2024

@author: faust
"""


import numpy as np
import matplotlib.pyplot as plt

mat = plt.imread('img77.png')
ss=mat.shape

img=mat[:,:,0]
imgN=np.zeros((ss[0],ss[1]))

del1 = 25
i0 =900
j0 =850
ref=mat[i0-del1:i0+del1, j0-del1:j0+del1,0]
media=np.mean(ref)
desv=np.std(ref)
li=media-(3*desv)
ls=media+(3*desv)

#filtrando imagen
for i in range(ss[0]):
    for j in range (ss[1]):
        if img [i,j] >= li and img[i,j]<=ls:
            imgN[i,j]=1
            
imgF=np.copy(imgN) 
           
#limpiando imagen

i=0
j=0

for i in range(ss[0]):
    for j in range (ss[1]):
        if imgN[i,j]==1:
            if imgN[i,j-25]==0 and imgN[i,j+25]==0:
                imgF[i,j]=0
            if imgN[i-5,j]==0 and imgN[i+5,j]==0:
                imgF[i,j]=0
              
            
                
                
                
plt.figure()
plt.imshow(imgN ,cmap = "gray")
plt.figure()
plt.imshow(imgF,cmap = "gray")
plt.show()
