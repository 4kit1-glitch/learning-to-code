# computes  the factorial of a number

def factorial(num):
    if(num == 0):
        return 1
    else:
        recurse = factorial(num - 1)
        return num * recurse

print(factorial(5))