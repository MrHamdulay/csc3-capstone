e= "Decision: Eat it."
y="Decision: Don't eat it."
z="Decision: Your call."
print("Welcome to the 30 Second Rule Expert")
print("------------------------------------")
print("Answer the following questions by selecting from among the options.")
x=input("Did anyone see you? (yes/no)\n")
if x=="yes":
    x=input("Was it a boss/lover/parent? (yes/no)\n")
    if x=="yes":
        x=input("Was it expensive? (yes/no)\n")
        if x=="yes":
            x=input("Can you cut off the part that touched the floor? (yes/no)\n")
            if x=="yes":
                print(e)
            elif x=="no":
                print("Decision: Your call.")
        elif x=="no":
            x=input("Is it chocolate? (yes/no)\n")
            if x=="yes":
                print(e)
            elif x=="no":
                print(y)
    elif x=="no":
        print (e)
elif x=="no":
    x=input("Was it sticky? (yes/no)\n")
    if x=="yes":
        x=input("Is it a raw steak? (yes/no)\n")
        if x=="yes":
            x=input("Are you a puma? (yes/no)\n")
            if x=="yes":
                print(e)
            elif x=="no":
                print(y)
        elif x=="no":
            x=input("Did the cat lick it? (yes/no)\n")
            if x=="yes":
                x=input("Is your cat healthy? (yes/no)\n")
                if x=="yes":
                    print(e)
                if x=="no":
                    print(z)
            elif x=="no":
                print(e)
    elif x=="no":
        x=input("Is it an Emausaurus? (yes/no)\n")
        if x=="yes":
            x=input("Are you a Megalosaurus? (yes/no)\n")
            if x=="yes":
                print(e)
            elif x=="no":
                print(y)
        elif x=="no":
            x=input("Did the cat lick it? (yes/no)\n")
            if x=="yes":
                x=input("Is your cat healthy? (yes/no)\n")
                if x=="yes":
                    print(e)
                elif x=="no":
                    print(z)
            elif x=="no":
                print(e)
            