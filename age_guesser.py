import random

print("Hello. I am going to try and guess your age")
name = input("What is your name? ")

low = 1
high = 100
x = False

while x == False:
    age = random.randint(low, high)
    yesorno = input(f"Are you {age} years old? y or n? ").lower()
    if yesorno == "y":
        print(f" {name} is {age} years old")
        x = True
    elif yesorno == "n":
        print("Rats")
        oldoryoung = input(f"Older or Younger? ").lower()
        if oldoryoung == "older":
            low = age + 1
        elif oldoryoung == "younger":
            high = age - 1
        else:
            print("Please enter 'Older' or 'Younger'")
         
    else:
        print("Please enter y or n")