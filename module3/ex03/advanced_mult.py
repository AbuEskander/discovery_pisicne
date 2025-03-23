#!/usr/bin/python3

counter = 0
sec = 0

while counter <= 10:
    print(f"Table of {counter}: :",end="") 
    while sec <= 10:
        print(f"{counter * sec} ",end="")
        sec+=1
    print("")
    sec = 0
    counter +=1
        
