#!/usr/bin/python3
import math

try:
    inp = float(input("Give me a number: "))
    if inp.is_integer():
        print("The number is integer")
    else:
        print("The numeber is float")
except ValueError:
    print("Input is not a number")
except KeyboardInterrupt:
    print("CTRL + C")
except EOFError:
    print("EOF error")

