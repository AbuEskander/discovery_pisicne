#!/usr/bin/python3

import sys

if len(sys.argv) == 1:
    print("none")

for item in sys.argv[1:]:
    if not item.endswith("ism"):
        print(item + "ism")

