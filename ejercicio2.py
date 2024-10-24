# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 16:39:31 2024

@author: faust
"""

import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

datos=pd.read_csv('Datos')

conteo=datos['Sexo'].value_counts()

print(datos.describe())

print(conteo)

plt.figure()
plt.title('Histograma Pesos')
plt.hist(datos['Pesos'], bins=25, alpha=0.5,label='Country',edgecolor = "black")
plt.show()


plt.figure()
plt.title('Histograma Edad')
plt.hist(datos['Edad'], bins=25, alpha=1,label='Country',edgecolor = "black")
plt.show()

res1=stats.shapiro(datos['Edad'])
res2=stats.shapiro(datos['Pesos'])

print('La prueba de Shapiro para Edad es', res1.statistic)
print('La prueba de Shapiro para Pesos es', res2.statistic)