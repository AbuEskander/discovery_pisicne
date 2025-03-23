#!/usr/bin/python3

import sys 

if len(sys.argv) != 2:
    print("none")
    exit(1)

count = sys.argv[1].count("z")

if count == 0:
    print("none")
    exit(1)
while count:
    print("z",end="")
    count -=1
print("")
