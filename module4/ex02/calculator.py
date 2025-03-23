#!/usr/bin/python3
try:
    f_value = int(input("Give me the first number: "))
    s_value = int(input("Give me the second number: "))
    print("Thank you")
    print(f"{f_value} + {s_value} = {f_value + s_value}")
    print(f"{f_value} - {s_value} = {f_value - s_value}")
    print(f"{f_value} / {s_value} = {f_value / s_value}")
    print(f"{f_value} * {s_value} = {f_value * s_value}")
except ValueError:
    print("Input is not an integer")
except KeyboardInterrupt:
    print("CTRL + C is pressed")
except EOFError:
    print('EOF Error')
