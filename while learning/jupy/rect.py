# code for the exercises in think python chapter 4

import math
from jupyturtle import make_turtle,penup,pendown,forward,left,right

make_turtle(delay=0.3,width=300,height=300)

def polyline(n , angle,lenght):
    for i in range(n):
        forward(lenght)
        left(angle)

def square(lenght):
    polyline(n = 4 , angle = 90 ,lenght  = lenght)

def rectangle(lenght, width):
    for i in range(2):
        polyline(n = 1 , angle=90 , lenght = lenght)
        polyline(n = 1 , angle = 90 , lenght = width)

def rhombus(side_lenght , internal_angle):
    linear_angle =  180 -  internal_angle   ### to draw a 180 degree line 
    for i in range(2):
        polyline(n=1 , angle = internal_angle , lenght = side_lenght)
        polyline(n = 1 , angle = linear_angle ,lenght= side_lenght)


