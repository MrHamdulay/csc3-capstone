print("Welcome to the 30 Second Rule Expert\n------------------------------------")
print("Answer the following questions by selecting from among the options.")
x = input("Did anyone see you? (yes/no)\n")
if x=="yes":
    y = input("Was it a boss/lover/parent? (yes/no)\n")
    if y=="yes":
        z = input("Was it expensive? (yes/no)\n")
        if z=="yes":
            r = input("Can you cut off the part that touched the floor? (yes/no)\n")
            if r=="yes":
                print("Decision: Eat it.")
            else:
                print("Decision: Your call.")
        else:
            t=input("Is it chocolate? (yes/no)\n")
            if t=="yes":
                print("Decision: Eat it.")
            else:
                print("Decision: Don't eat it.")
    else:
        print("Decision: Eat it.")
else:
    y=input("Was it sticky? (yes/no)\n")
    if y=="yes":
        z=input("Is it a raw steak? (yes/no)\n")
        if z=="yes":
            r=input("Are you a puma? (yes/no)\n")
            if r=="yes":
                print("Decision: Eat it.")
            else:
                print("Decision: Don't eat it.")
        else:
            f=input("Did the cat lick it? (yes/no)\n")
            if f=="yes":
                q=input("Is your cat healthy? (yes/no)\n")
                if q=="yes":
                    print("Decision: Eat it.")
                else:
                    print("Decision: Your call.")
    else:
        g=input("Is it an Emausaurus? (yes/no)\n")
        if g=="yes":
            h=input("Are you a Megalosaurus? (yes/no)\n")
            if h=="yes":
                print("Decision: Eat it.")
            else:
                print("Decision: Don't eat it.")
        else:
            f=input("Did the cat lick it? (yes/no)\n")
            if f=="yes":
                q=input("Is your cat healthy? (yes/no)\n")
                if q=="yes":
                    print("Decision: Eat it.")
                else:
                    print("Decision: Your call.")
            else:
                print("Decision: Eat it.")