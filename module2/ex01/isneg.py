#!/usr/bin/python3
try:
    number = int(input("Enter a number: "))
except ValueError:
    print("Input is not an integer")
    exit(1)
except EOFError:
    print("EOF error")
    exit(1)
except KeyboardInterrupt:
    print("CTRL + C Pressed")
    exit(1)
if number < 0:
    print("This number is negative.")
elif number > 0:
    print("This number is positive.")
else:
    print("This number is both positive and negative.")
