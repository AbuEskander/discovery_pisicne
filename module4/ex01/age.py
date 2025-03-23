#!/usr/bin/python3


try:
    age = int(input("Please tell me your age: "))
    counter = 1

    while counter <= 3:
        print(f"In {counter * 10} years, you'll be {age + counter * 10} years old ")
        counter +=1
except ValueError:
    print("Input is not an integer")
except KeyboardInterrupt:
    print("CTRL + C is pressed")
except EOFError:
    print("Eof error ")
