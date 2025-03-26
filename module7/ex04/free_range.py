#!/usr/bin/python3

import sys

if len(sys.argv) != 3:
    print("none")
    exit(1)

try:
    first_val, second_val = int(sys.argv[1]), int(sys.argv[2])
except ValueError:
    print("none")
    exit(1)

if first_val < second_val:
    arr = list(range(first_val,second_val))
else:
    arr = list(range(second_val, first_val))
print(arr)
