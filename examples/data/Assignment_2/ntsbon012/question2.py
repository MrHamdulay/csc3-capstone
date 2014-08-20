#Ntshangase Bongiwe
#You dropped your food on the floor.....

print("Welcome to the 30 Second Rule Expert")
print("------------------------------------")
print("Answer the following questions by selecting from among the options.")
a=input("Did anyone see you? (yes/no)\n")
if a=="yes":
    a=input("Was it a boss/lover/parent? (yes/no)\n")
    if a=="yes":
        a=input("Was it expensive? (yes/no)\n")
        if a=="yes":
            a=input("Can you cut off the part that touched the floor? (yes/no)\n")
            if a=="yes":
                print("Decision: Eat it.")
            else:          
                print("Decision: Your call.")
        else:
            a=input("Is it chocolate? (yes/no)\n")
            if a=="yes":
                print("Decision: Eat it.")
            else:
                print("Decision: Don't eat it.")
    else:
        print("Decision: Eat it.")                
else:
    a=input("Was it sticky? (yes/no)\n")
    if a=="yes":
        a=input("Is it a raw steak? (yes/no)\n")
        if a=="yes":
            b=input("Are you a puma? (yes/no)\n")
            if b=="yes":
                print("Decision: Eat it.")
            else:
                print("Decision: Don't eat it.")
        else:
            a=input("Did the cat lick it? (yes/no)\n")
            if a=="yes":
                a=input("Is your cat healthy? (yes/no)\n")
                if a=="yes":
                    print("Decision: Eat it.")
                else:
                    print("Decision: Your call.")
            else:
                print("Decision: Eat it.")
    else:
        a=input("Is it an Emausaurus? (yes/no)\n")
        if a=="yes":
            a=input("Are you a Megalosaurus? (yes/no)\n")
            if a=="yes":
                print("Decision: Eat it.")
            else:
                print("Decision: Don't eat it.")
        else:
            a=input("Did the cat lick it? (yes/no)\n")
            if a=="yes":
                a=input("Is your cat healthy? (yes/no)\n")
                if a=="yes":
                    print("Decision: Eat it.")
                else:
                    print("Decision: Your call.")   
            else:
                print("Decision: Eat it.")