# Program ccomputes the hypotenuse of a right angle triangle

import math

def hypot(base, hieght):
    sqbase = base**2
    sqhieght = hieght**2
    sum = sqbase+sqhieght
    hypotenuse = math.sqrt(sum)
    return hypotenuse

def is_between(x, y, z):
    if x < y < z:
        return True
    elif z < y < x:
        return True
    else:
        return False

def ackarman(m, n):
    if (m == 0):
        return n+1
    elif (m > 0 and n == 0):
       return ackarman(m-1, 1)
    elif (m > 0 and n > 0):
        return ackarman(m - 1, ackarman(m, n-1))

def gdc(x, y):
    if(y == 0):
        return x
    else:
        r = x % y
        return gdc(y, r)
    
print(gdc(15, 6))