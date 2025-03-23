#!/usr/bin/python3

def greetings(st=None):
    print("Hello, ",end="")
    if not st:
        print("noble stranger")
    elif isinstance(st,str):
        print(st)
    else:
        print("It was not a name")

greetings('Alexandra')
greetings('Wil')
greetings()
greetings(42)
