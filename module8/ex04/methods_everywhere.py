#!/usr/bin/python3

import sys

if len(sys.argv) == 1:
    print("none")
    exit(1)

def shrink(st:str)-> str:
    return st[0:8]
def enlarge(st:str)-> str:
    return st.ljust(8,"Z")
for item in sys.argv[1:]:
    if len(item) == 8:
        print(item)
    elif len(item) < 8:
        print(enlarge(item))
    else:
        print(shrink(item))
