
try:
    first_name = input("Hey BOI, what is your name :  ")
    last_name = input("What about your last name ;):  ")
except EOFError:
    print("EOF error boi")
    exit(0)
whole_name = f"{first_name.strip()} {last_name.strip()}"

print(whole_name.strip())
