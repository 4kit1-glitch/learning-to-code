# program draws a regular polygon

import math
from jupyturtle import make_turtle , forward , left

def polygon(sides , lenght):

    make_turtle(delay=0.02)
    angle = 360/sides   ### calculations for angles
    
    for i in range(sides):
        forward(lenght)
        left(angle)

def circle(radius):

    circumfrence = 2*math.pi*radius #calculation of perimeter of circle
    n = 30      #30 sided small lines
    lenght = circumfrence/n

    polygon(sides = n , lenght = lenght)


circle(10)