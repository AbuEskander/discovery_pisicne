#!/usr/bin/python3

password = "Python is awesome"

try:
    check = input("Enter your password: ")
except KeyboardInterrupt:
    print("CTRL + C pressed")
    exit(0)
except EOFError:
    print("EOF error ")
    exit(0)

if password == check:
    print("ACCESS GRANTED")
else:
    print("ACCESS DENIED")

