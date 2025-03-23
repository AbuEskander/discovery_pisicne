#!/usr/bin/python3
try:
    st = input("Gimme a word: ") 
    print(st.upper())
except KeyboardInterrupt:
    print("CTRL + C is pressed")
except EOFError:
    print("EOF Error")
