# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 16:25:56 2024

@author: faust
"""

import numpy as np
import matplotlib.pyplot as plt

# Cargar la imagen
img = plt.imread('img81.jpg')

# Si es una imagen en color, seleccionar un canal (por ejemplo, el canal rojo)
# Si es una imagen en escala de grises, esto no es necesario
mat = img[:,:,0]

# Aplanar la matriz para convertirla en un array 1D
x = mat.flatten()

# Calcular el histograma con 256 bins (para cubrir los valores de intensidad de 0 a 255)
histo, bins = np.histogram(x, bins=256, range=(0, 200))

# Graficar el histograma
plt.figure()
plt.plot(bins[:-1], histo)  # Excluir el último bin, que es el borde superior
plt.title('Histograma de intensidades')
plt.xlabel('Intensidad de píxeles')
plt.ylabel('Frecuencia')
plt.show()


