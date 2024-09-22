# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 15:45:19 2024

@author: faust
"""
import numpy as np
import matplotlib.pyplot as plt

# Valores de t para las primeras dos ecuaciones
t = np.linspace(0, 24 * np.pi, 1000)

# Primera ecuación
x1 = np.sin(t) * np.exp(np.cos(t) - 2 * np.cos(4 * t) - np.sin(t / 12)**5)
y1 = np.cos(t) * np.exp(np.cos(t) - 2 * np.cos(4 * t) - np.sin(t / 12)**5)

# Graficar la primera ecuación

plt.plot(x1, y1)

plt.show()

# Segunda ecuación
x2 = np.cos(t) * np.exp(np.cos(t) - 2 * np.cos(4 * t) - np.sin(t / 12)**5)
y2 = np.sin(t) * np.exp(np.cos(t) - 2 * np.cos(4 * t) - np.sin(t / 12)**5)

# Graficar la segunda ecuación
plt.plot(x2, y2)
plt.show()

# Valores de theta para la tercera ecuación
theta = np.linspace(0, 24 * np.pi, 1000)

# Tercera ecuación
r = np.exp(np.sin(theta)) - 2 * np.cos(4 * theta) + np.sin((2 * theta - np.pi) / 24)**5

# Convertir a coordenadas cartesianas
x3 = r * np.cos(theta)
y3 = r * np.sin(theta)

# Graficar la tercera ecuación
#plt.figure()
plt.plot(x3, y3)

plt.show()

