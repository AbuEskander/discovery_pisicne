#!/usr/bin/python3

try:
    number = int(input("ENter a number less than 25: "))
except ValueError:
    print("Input is not an integer")
    exit(1)
except KeyboardInterrupt:
    print("CTRL + C pressed")
    exit(1)
except EOFError:
    print("EOF error")
    exit(1)

if number > 25:
    print("Error")
    exit(1)

while number <= 25:
    print(f"Inside the loop, my variable is {number}")
    number+=1

