print("Welcome to the 30 Second Rule Expert")
print("------------------------------------")
print("Answer the following questions by selecting from among the options.")

x="Decision: Eat it."
y="Decision: Don't eat it."
z="Decision: Your call."

if input("Did anyone see you? (yes/no)\n") == "yes":
    if input("Was it a boss/lover/parent? (yes/no)\n") == "no":
        print(x)
    elif input("Was it expensive? (yes/no)\n") == "yes":
        if input("Can you cut off the part that touched the floor? (yes/no)\n") == "no":
            print(z)
        else:
            print(x)
    elif input("Is it chocolate? (yes/no)\n") == "yes":
        print(x)
    else:
        print(y)
elif input("Was it sticky? (yes/no)\n") == "yes":
    if input("Is it a raw steak? (yes/no)\n") =="yes":
        if input("Are you a puma? (yes/no)\n") == "no":
            print(y)
        else:
            print(x)
    elif input("Did the cat lick it? (yes/no)\n") == "no":
        print(x)
    elif input("Is your cat healthy? (yes/no)\n") == "no":
        print(z)
    else:
        print(x)
elif input("Is it an Emausaurus? (yes/no)\n") == "no":
    if input("Did the cat lick it? (yes/no)\n") == "no":
        print(x)
    elif input("Is your cat healthy? (yes/no)\n") == "no":
        print(z)
    else:
        print(x)
elif input("Are you a Megalosaurus? (yes/no)\n") == "no":
    print(y)
else:
    print(x)