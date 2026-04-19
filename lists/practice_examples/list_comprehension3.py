#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  9 22:08:09 2026

@author: aimmee
"""

from timeit import timeit

age = 22

message = "eligible" if age >= 18 else "ineligible"  # Tenary conditions

for i in range(3):
    print(i)

else:
    print("met a 0")


while (age <= 30):
    print(age)
    age += 1
else:
    print("success")


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 13, 15, 17]


def is_prime(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i*i == 0:
            return False
    return True


func_time = timeit("is_prime", "from __main__ import is_prime")

print(func_time)

prime_numbers = [i for i in numbers if is_prime(i)]
print(prime_numbers)
