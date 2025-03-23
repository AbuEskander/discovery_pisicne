#!/usr/bin/python3

import sys

if len(sys.argv) != 2:
    print("none")
    exit(1)
try:
    st = input("What was the parameter? ")
except KeyboardInterrupt:
    print("CTRL + C")
    exit(1)
except EOFError:
    print("EOF Error ")
    exit(1)

if st == sys.argv[1]:
    print("Good job")
else:
    print("Nope, sorry..")
