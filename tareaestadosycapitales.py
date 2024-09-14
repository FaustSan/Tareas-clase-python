# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 08:33:19 2024

@author: faust
"""
import random

#definiendo lista
estados_y_capitales = {
    "Aguascalientes": "Aguascalientes",
    "Baja California": "Mexicali",
    "Baja California Sur": "La Paz",
    "Campeche": "San Francisco de Campeche",
    "Chiapas": "Tuxtla Gutiérrez",
    "Chihuahua": "Chihuahua",
    "Ciudad de México": "Ciudad de México",
    "Coahuila": "Saltillo",
    "Colima": "Colima",
    "Durango": "Victoria de Durango",
    "Guanajuato": "Guanajuato",
    "Guerrero": "Chilpancingo",
    "Hidalgo": "Pachuca",
    "Jalisco": "Guadalajara",
    "México": "Toluca",
    "Michoacán": "Morelia",
    "Morelos": "Cuernavaca",
    "Nayarit": "Tepic",
    "Nuevo León": "Monterrey",
    "Oaxaca": "Oaxaca de Juárez",
    "Puebla": "Puebla",
    "Querétaro": "Santiago de Querétaro",
    "Quintana Roo": "Chetumal",
    "San Luis Potosí": "San Luis Potosí",
    "Sinaloa": "Culiacán",
    "Sonora": "Hermosillo",
    "Tabasco": "Villahermosa",
    "Tamaulipas": "Ciudad Victoria",
    "Tlaxcala": "Tlaxcala",
    "Veracruz": "Xalapa",
    "Yucatán": "Mérida",
    "Zacatecas": "Zacatecas"
}



estados_lista = list(estados_y_capitales.keys())
capitales_lista=list(estados_y_capitales.values())

correctas=0
incorrectas=0

for i in range(5):
    estado_aleatorio = random.choice(estados_lista)
    print('\n¿Cuál es la capital del estado', estado_aleatorio)
    capital= estados_y_capitales[estado_aleatorio]
    
    #Buscando respuestas malas
    ri1=random.choice(capitales_lista)
    if ri1 == capital:
        ri1=random.choice(capitales_lista)
        
    ri2=random.choice(capitales_lista)
    if ri2 == capital:
        ri2=random.choice(capitales_lista)
        
    ri3=random.choice(capitales_lista)
    if ri3 == capital:
        ri3=random.choice(capitales_lista)
        
    respuestas=[capital,ri1,ri2,ri3]
    random.shuffle(respuestas)
        
    print("1.-",respuestas[0],"\n2.-",respuestas[1],"\n3.-",respuestas[2],"\n4.-",respuestas[3])
    r= int(input("Ingrese el número de la respuesta correcta:   "))

    if respuestas[r-1]==capital:
        print("\nrespuesta correcta")
        correctas=correctas+1
    else:
        print("\n3burro")    
        incorrectas=incorrectas+1
        
        

print("\nRespuestas correctas ", correctas)
   
        
   