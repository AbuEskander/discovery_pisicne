#!/usr/bin/python3

f_value = input("Give me the first number: ")
s_value = input("Give me the second number: ")

print("Thank you")

if not f_value or not  s_value:
    print("One of the inputed values are not numbers")
    exit(1)
f_value = int(f_value)
s_value = int(s_value)

print(f"{f_value} + {s_value} = {f_value + s_value}")
print(f"{f_value} - {s_value} = {f_value - s_value}")
print(f"{f_value} / {s_value} = {f_value / s_value}")
print(f"{f_value} * {s_value} = {f_value * s_value}")

