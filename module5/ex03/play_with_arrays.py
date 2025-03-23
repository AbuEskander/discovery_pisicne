#!/usr/bin/python3

arr = [2,8,9,48,8,22,-12,2]
mod = []

for item in arr:
    if item > 5:
        mod.append(item + 2)

mod = set(mod)

print (arr)
print (mod)

