#!/usr/bin/python3
import math

inp = input("Give me a number: ")

if not inp:
    print("No value enterd")
    exit(1)

fl = float(inp)
try:
    it = int(inp)
except ValueError:
    if fl == math.floor(fl):
        print("The number is integer")
    else:
        print("The number is float")
    exit(1)

print("The number is integer")


