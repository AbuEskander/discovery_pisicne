#!/usr/bin/python3


try:
    check = input("What you gotta say ")
    while True:
        if check == "STOP":
            exit(1)
        check = input("I got that! Anything else? : ")
except KeyboardInterrupt:
    print("CTRL + C is pressed")
except EOFError:
    print("EOFError")

