#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 30 09:48:41 2026

@author: aimmee
"""

family = {
    "father": {
        "name": "kengah alfed",
        "hobby": "driving"
    },
    "mother": {
        "name": "kengah gladys",
        "age": 41,
        "hobby": "singing"
    }
}

age1 = family["father"].get("age", "age not-specified")

# from keys method

keys = ["name", "class"]
values = ["kit", 2]

my_dict = dict.fromkeys(keys)


car = {
    "model": "toyota",
    "version": "runx",
}

car.setdefault("color", "black")
colour = car.popitem()
print(car)

car.update({"owner": "nax"})
print(car)
