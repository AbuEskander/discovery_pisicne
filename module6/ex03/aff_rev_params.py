#!/usr/bin/python3

import sys

if len(sys.argv) < 3:
    print("none")
    exit(1)

for item in sys.argv[:0:-1]:
    print(item)
