import math
from jupyturtle import make_turtle , forward, left
 
def polyline(n , lenght , angle):
    make_turtle
    for i in range(n):
        forward(lenght)
        left(angle)

def polygon(n , lenght):
    angle = 360 / n
    polyline(n , lenght , angle)

def arc(radius , angle):
    arc_lenght = (2*math.pi*radius) *angle / 360
    n = 30
    lenght = arc_lenght / n #actual lenght of the line 
    step_angle = 360 / n
    polyline(n,lenght , step_angle)

def circle(radius):
    arc(radius , 360)

