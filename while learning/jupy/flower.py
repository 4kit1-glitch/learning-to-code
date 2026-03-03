from jupyturtle import make_turtle , forward , left
import math

def polyline(n , lenght , angle):
    make_turtle
    for i in range(n):
        forward(lenght)
        left(angle)

def arc(radius , angle):
    arc_lenght = (2*math.pi*radius) *angle / 360
    n = 30
    lenght = arc_lenght / n #actual lenght of the line 
    step_angle = 360 / n
    polyline(n,lenght , step_angle)


def flower(n):
    for i in range(n):
        arc(10 , 43)

flower(5)
