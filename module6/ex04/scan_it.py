#!/usr/bin/python3

import sys

if len(sys.argv) != 3:
    print("none")
    exit(1)

st = sys.argv[2].count(sys.argv[1])

if st == 0:
    print("none")
else:
    print(st)
