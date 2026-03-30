#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 29 16:18:40 2026

@author: aimmee
"""

store_returns = {
    0: 0,
    1: 1
}


def fibonacci(num):
    if num in store_returns:
        return store_returns[num]

    result = fibonacci(num - 1) + fibonacci(num - 2)
    store_returns[num] = result
    return result


fib = fibonacci(4)

print(store_returns)
print(fib)
