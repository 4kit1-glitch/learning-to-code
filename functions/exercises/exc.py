# Program ccomputes the hypotenuse of a right angle triangle

import math

def hypot(base, hieght):
    sqbase = base**2
    sqhieght= hieght**2
    sum = sqbase + sqhieght
    hypotenuse = math.sqrt(sum)
    return hypotenuse

def is_between(x, y, z):
    if x < y < z:
        return True
    elif z < y < x:
        return True
    else:
        return False
    
