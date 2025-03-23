#!/usr/bin/python3
import math

it = input("Give me a number: ")

try:
    it = int(it)
except ValueError:
    print(math.ceil(float(it)))
    exit(1)
print(it)
