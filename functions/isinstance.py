# testing the is instance function

def factorial(n):
    if not isinstance(n, int) or n < 0:
        print("factorial only defined for positive intergers")
        return -1
    elif n == 0:
        return 1
    else:
        return n*factorial(n - 1)

print(factorial(-2))