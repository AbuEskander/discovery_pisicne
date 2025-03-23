#!/usr/bin/python3





def famous_births(arr:dict):
    res = sorted(arr.items(), key=lambda x: x[1]['date_of_birth'])
    for value in res:
        print(f'{value[1]["name"]} is a great scienteist born in {value[1]["date_of_birth"]}')

women_scientists = {
"ada": { "name": "Ada Lovelace", "date_of_birth": "1815" },
"cecilia": { "name": "Cecila Payne", "date_of_birth": "1900" },
"lise": { "name": "Lise Meitner", "date_of_birth": "1878" },
"grace": { "name": "Grace Hopper", "date_of_birth": "1906" }
}
famous_births(women_scientists)
