#!/usr/bin/python3

number = int(input("ENter a number less than 25: "))

if number > 25:
    print("Error")
    exit(1)

while number <= 25:
    print(f"Inside the loop, my variable is {number}")
    number+=1

