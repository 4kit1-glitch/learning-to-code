#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 14:57:26 2026

@author: kit
"""

def evaluate_input():
    message = """enter the equation it should be simple not containing
    any exponential equations :   
    """
    operator = ["+", "-", "/", "*", "**"]
    user_input = input(f"{message}: ")
    
    for char in user_input.replace(" ", ""):
        if char in operator:
            