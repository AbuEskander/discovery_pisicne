#!/usr/bin/python3
import math

try:
    it = float(input("Give me a number: "))
    print(math.ceil(float(it)))
except KeyboardInterrupt:
    print("CTRL + C is pressed")
except ValueError:
    print("Input is not a number")
except EOFError:
    print("EOF error")
    
