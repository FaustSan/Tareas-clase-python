# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 16:00:19 2024

@author: faust
"""
import turtle
import random

turtle.colormode(255)

turtle.up()
turtle.setx(200)
turtle.down()
turtle.left(90)
turtle.forward(200)
turtle.left(90)
turtle.forward(400)
turtle.left(90)
turtle.forward(400)
turtle.left(90)
turtle.forward(400)
turtle.left(90)
turtle.forward(200)


for i in range (100):
    radio= random.randint(10,20)
    
    x=random.randint(-180,180)
    y=random.randint(-180,180)
    
   
    r=random.randint(0, 255)
    g=random.randint(0, 255)
    b=random.randint(0, 255)
    
   
    turtle.color(r,g,b)
    turtle.up()
    turtle.setx(x)
    turtle.sety(y)
    turtle.down()
    turtle.circle(radio)
    
 