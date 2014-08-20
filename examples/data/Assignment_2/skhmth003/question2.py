print("Welcome to the 30 Second Rule Expert")
print("------------------------------------")
print("Answer the following questions by selecting from among the options.")
x=input("Did anyone see you? (yes/no)\n")
if x=="no":
    a=input("Was it sticky? (yes/no)\n")
    if a=="no":
        b=input("Is it an Emausaurus? (yes/no)\n")
        if b=="yes":
            c=input("Are you a Megalosaurus? (yes/no)\n")
            if c=="yes":
                print("Decision: Eat it.")
            else:
                print("Decision: Don't eat it.")  
        else:
            d=input("Did the cat lick it? (yes/no)\n")
            if d=="yes":
                e=input("Is your cat healthy? (yes/no)\n")
                if e== "no":
                    print("Decision: Your call.")
                else:
                    print("Decision: Eat it.")
            else:
                print("Decision: Eat it.")             
    else:
        b=input("Is it a raw steak? (yes/no)\n")
        if b=="yes":
            c=input("Are you a puma? (yes/no)\n")
            if c=="yes":
                print("Decision: Eat it.")
            else:
                print("Decision: Don't eat it.")
        else:
            d=input("Did the cat lick it? (yes/no)\n")
            if d=="no":
                print("Decision: Eat it.") 
            else:
                e=input("Is your cat healthy? (yes/no)\n")
                if e=="yes":
                    print("Decision: Eat it.")
                else:
                    print("Decision: Your call.")
#This is where the yes starts
else:
    b=input("Was it a boss/lover/parent? (yes/no)\n")
    if b=="yes":
        b=input("Was it expensive? (yes/no)\n")
        if b=="yes":
            c=input("Can you cut off the part that touched the floor? (yes/no)\n")
            if c=="yes":
                print("Decision: Eat it.")
            else:
                print("Decision: Your call.")
        else:
            d=input("Is it chocolate? (yes/no)\n")
            if d=="yes":
                print("Decision: Eat it.")
            else:
                print("Decision: Don't eat it.")
    else:
            print("Decision: Eat it.")
            