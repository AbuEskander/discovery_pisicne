#!/usr/bin/python3

import sys

if len(sys.argv) == 1:
    print("none")
    exit(1)

def downcase_it(st:str)-> str:
    return st.lower()

for item in sys.argv[1:]:
    print(downcase_it(item))
