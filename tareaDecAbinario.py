# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal.
"""


num = int(input("Introduce un número entero: "))
residuo= int()
dividendo=int()

resp=[]
dividendo=num

while dividendo >= 2 :
    residuo = dividendo % 2   
    resp.append(residuo)
    dividendo = int (dividendo/2)
    if dividendo < 2:
        resp.append(1)

arraybin= resp[::-1]

numero = int(''.join(map(str, arraybin)))


print ('El número '+ str(num) + ' en binario es: ' + str(numero))