#!/usr/bin/python3

def array_of_names(arr:dict)->list:
    li = []
    for key,value in arr.items():
        li.append(f"{key.capitalize()} {value.capitalize()}")
    return li

persons = {
"jean": "valjean",
"grace": "hopper",
"xavier": "niel",
"fifi": "brindacier"
}

print(array_of_names(persons))
