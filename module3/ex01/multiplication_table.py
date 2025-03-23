#!/usr/bin/python3

UPTO = 10

try:
    number = int(input("Enter a number to show it's multiplication table: "))
except ValueError:
    print("Input is not an integer")
    exit(1)
except KeyboardInterrupt:
    print("CTRL + C is pressed")
    exit(1)
except EOFError:
    print("EOF error")
    exit(1)
    
counter = 0

while counter < UPTO:
    print(f"{counter} x {number} = {counter * number}")
    counter += 1

