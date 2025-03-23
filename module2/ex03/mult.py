#!/usr/bin/python3

first_int = int(input("Enter first value: "))
second_int = int(input("Enter second value: "))

mult = first_int * second_int

if mult > 0:
    print("The result is postive")
elif mult < 0:
    print("The result is negative")
else:
    print("The result is zero")

print(f"The result of: {first_int} x {second_int} = {mult}")
