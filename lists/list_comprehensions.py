"""
Learning list comprehensions


"""
import math

numbers = [1, 2, 3, 4, 4, 5, 6, 7, 8]   # can contain duplicates
fruits = ["banana", "apple", "carrot"]
new_list = []

for x in numbers:
    if x % 2 == 0:
        new_list.append(x)

even_numbers = [x for x in numbers if x % 2 == 0]
sqrt_list = [math.sqrt(x) for x in numbers if x > 0]
shopped = [fruit if fruit in "apple" else "orange" for fruit in fruits]

print(shopped)
