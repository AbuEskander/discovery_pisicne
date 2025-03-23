#!/usr/bin/python3

import sys

if len(sys.argv) == 1:
    print("none")
    exit(1)

print(f"Parameter : {len(sys.argv) - 1}")

for item in sys.argv[1:]:
    print(f"{item} : {len(item)}")
