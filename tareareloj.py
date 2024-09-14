# -*- coding: utf-8 -*-
"""
Created on Thu Aug 22 11:12:07 2024

@author: faust
"""

import turtle
import time


"dibujando el reloj"
turtle.up()
turtle.sety(-100)
turtle.down()
turtle.circle(100)
turtle.up()
turtle.sety(0)
turtle.left(90)

"reloj, lo puse el cambio a 5 segundos , para que fuera más rápido"
intervalo=5
delta=60/intervalo
ang=360/delta
veces=int (60/intervalo)

for i in range(veces) :
    turtle.down()
    turtle.forward(90)
    turtle.pencolor("white")
    time.sleep(intervalo)
    turtle.backward(90)
    turtle.pencolor("black")
    turtle.right(ang)



