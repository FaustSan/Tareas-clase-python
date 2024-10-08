# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 16:49:21 2024

@author: faust
"""

import numpy as np
import matplotlib.pyplot as plt

# Definir la función f(x) con manejo de singularidad en x = 0
def f(x):
    return np.where(x == 0, 0, x * np.sin(1 / x))

# Generar el rango de valores x
x_values = np.linspace(-2/np.pi, 2/np.pi, 256)

# Calcular los valores de f(x)
y_values = f(x_values)

# Normalizar y ajustar a la matriz 256x256
# Hacemos una transformación para que los valores de y estén en el rango [0, 255]
y_normalized = ((y_values - np.min(y_values)) / (np.max(y_values) - np.min(y_values)) * 255).astype(int)

# Crear una matriz de ceros de tamaño 256x256
matrix = np.zeros((256, 256))

# Dibujar la curva en la matriz
for i in range(len(x_values)):
    x_index = int((x_values[i] + 2/np.pi) / (4/np.pi) * 255)  # Escalar x para que esté en el rango [0, 255]
    y_index = 255 - y_normalized[i]  # Invertir para que (0,0) esté en la esquina inferior izquierda
    if 0 <= x_index < 256 and 0 <= y_index < 256:
        matrix[y_index, x_index] = 1  # Marcar el punto en la matriz

# Mostrar la matriz como una imagen
plt.imshow(matrix, cmap='gray', origin='lower')
plt.title('Curva de $f(x) = x \sin(1/x)$')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.colorbar(label='Intensidad')
plt.show()
