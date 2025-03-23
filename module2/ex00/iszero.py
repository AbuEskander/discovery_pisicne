#!/usr/bin/python3
try:
    number = int(input("Enter a number: "))
except ValueError:
    print("Input is not an integer")
    exit(0)
except KeyboardInterrupt:
    print("CTRL + C is pressed ")
    exit(1)
except EOFError:
    print("EOF Error ")
    exit(1)

if number == 0:
    print("This number is equal to zero")
else:
    print("This number is not equal to zero")
