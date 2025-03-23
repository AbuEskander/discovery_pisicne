#!/usr/bin/python3

import sys

if len(sys.argv) != 2:
    print("none")
    exit(1)

st = input("What was the parameter? ")

if st == sys.argv[1]:
    print("Good job")
else:
    print("Nope, sorry..")
