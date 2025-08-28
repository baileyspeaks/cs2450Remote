import random

print("Hello. I am going to try and guess your age")
name = input("What is your name? ")
x = False
while x == False:
    age = random.randint(15, 30)
    yesorno = input(f"Are you {age} years old? y or n? ")
    if yesorno == "y":
        print(f" {name} is {age} years old")
        x = True
        quit
    elif yesorno == "n":
        print("Rats")
        
    else:
        yesorno = input(f"Please enter y or n")