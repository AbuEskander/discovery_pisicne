#!/usr/bin/python3

def find_the_readheads(arr:dict)->list:
    li = []
    for key,value in arr.items():
        if value == "red":
            li.append(key)
    return li



dupont_family = {
"florian": "red",
"marie": "blond",
"virginie": "brunette",
"david": "red",
"franck": "red"
}

print(find_the_readheads(dupont_family))
