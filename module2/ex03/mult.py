#!/usr/bin/python3
try:
    first_int = int(input("Enter first value: "))
    second_int = int(input("Enter second value: "))
except ValueError:
    print("Input is not integer")
    exit(1)
except KeyboardInterrupt:
    print("CTRL + C pressed")
    exit(1)
except EOFError:
    print("EOF error ")
    exit(1)

mult = first_int * second_int

if mult > 0:
    print("The result is postive")
elif mult < 0:
    print("The result is negative")
else:
    print("The result is zero")

print(f"The result of: {first_int} x {second_int} = {mult}")
