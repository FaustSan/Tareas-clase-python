# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 16:02:30 2024

@author: faust
"""

import pandas as pd
import numpy as np

pref1='Juan'
pref2='María'

nombres=[]
sexo=[]
pesos=[]
edad=[]

for i in range (37):
    if i <20:
        nombres.append(pref1+str(i+1))
        sexo.append('H')
    else: 
        nombres.append(pref2+str(i-19))
        sexo.append('M')
        
datos=pd.DataFrame({'Nombres':nombres})

pesosH=np.round(np.random.normal(60,7,20))
pesosM=np.round(np.random.normal(55,5,17))
pesos= np.concatenate((pesosH,pesosM))

edad=np.round(np.random.uniform(40,60,37))

datos['Edad']=edad

datos['Sexo']=sexo

datos['Pesos']=pesos


print(datos)

datos.to_csv('Datos')