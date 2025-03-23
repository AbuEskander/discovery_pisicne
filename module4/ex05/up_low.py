#!/usr/bin/python3

try:
    st = input("Enter string: ")
    print(st.swapcase())
except EOFError:
    print("EOF Error")
except KeyboardInterrupt:
    print("CTRL + C is pressed")
