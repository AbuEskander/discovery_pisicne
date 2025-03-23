#!/usr/bin/python3

UPTO = 10

number = int(input("Enter a number to show it's multiplication table: "))

counter = 0

while counter < UPTO:
    print(f"{counter} x {number} = {counter * number}")
    counter += 1

