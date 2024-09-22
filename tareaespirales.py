# -*- coding: utf-8 -*-
"""
Created on Fri Sep 20 09:59:04 2024

@author: faust
"""

import numpy as np
import matplotlib.pyplot as plt



# Generar valores para theta (ángulo)
theta = np.linspace(0, 10 * np.pi, 1000)  # De 0 a 10π para varias vueltas


"""espiral de arquímedes---------------------------"""
a = 0  # Desplazamiento radial
b = 0.2  # Controla el espaciamiento entre los giros
r = a + b * theta
# Convertir a coordenadas cartesianas la espiral de arquímedes
x = r * np.cos(theta)
y = r * np.sin(theta)
plt.figure()
# Crear la gráfica
plt.plot(x, y)
# Ajustes de la gráfica
plt.title("Espiral de Arquímedes")
plt.axis('equal')  # Para mantener las proporciones entre los ejes


"""espiral de femat---------------------------"""
# Convertir a coordenadas cartesianas la espiral de femat
r2= theta**(1/2)
x2 = r2 * np.cos(theta)
y2 = r2 * np.sin(theta)
plt.figure()
plt.plot(x2,y2,color='red')
plt.title("Espiral de Femat")
plt.axis('equal')

"""espiral de hiperbólica---------------------------"""
theta2 = np.linspace(0.1, 10 * np.pi, 1000)
a2=1
r3=a2/theta2
x3 = r3 * np.cos(theta)
y3 = r3 * np.sin(theta)
plt.figure()
plt.plot(x3,y3,color='green')
plt.title("Espiral de hiperbólica")
plt.axis('equal')


"""espiral de logarítmica---------------------------"""
a3=0.1
b3=.2
r4 = a3 * np.exp(b3 * theta)# thetha despejada
x4=r4*np.cos(theta)
y4=r4*np.sin(theta)
plt.figure()
plt.plot(x4,y4,color='pink')
plt.title("Espiral de logarítmica")
plt.axis('equal')



plt.show()