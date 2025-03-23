#!/usr/bin/python3

age = input("Please tell me your age: ")

if not age:
    print ("you didn't enter a number")
    exit(1)
age = int(age)
counter = 1

while counter <= 3:
    print(f"In {counter * 10} years, you'll be {age + counter * 10} years old ")
    counter +=1
