#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 14:57:26 2026

@author: kit
"""

def evaluate_input():
    message = """enter the equation it should be simple
    not containing any exponential equations the value of the:
    if you need to use ^ use ** for now  
    """

    print(message)

    operator = ["+", "-", "/", "*", "**"]
    operands = []
    user_input = input("equation: ")
    input = user_input.split()