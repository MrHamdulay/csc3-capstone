print("Welcome to the 30 Second Rule Expert")
print("------------------------------------")
print("Answer the following questions by selecting from among the options.")
a=input("Did anyone see you? (yes/no)""\n")
if a=="yes":
    b=input("Was it a boss/lover/parent? (yes/no)""\n")
    if b=="yes":
        c=input("Was it expensive? (yes/no)""\n")
    if b=="no":
        c=print("Decision: Eat it.")
    if c=="yes":
        d=input("Can you cut off the part that touched the floor? (yes/no)""\n")
        if d=="yes":
            e=print("Decision: Eat it.")
        if d=="no":
            e=print("Decision: Your call.")
    if c=="no":
        d=input("Is it chocolate? (yes/no)""\n")
        if d=="no":
            e=print("Decision: Don't eat it.")
        if d=="yes":
                e=print("Decision: Eat it.")
if a=="no":
    b=input("Was it sticky? (yes/no)""\n")
    if b=="no":
        c=input("Is it an Emausaurus? (yes/no)""\n")
        if c=="yes":
            d=input("Are you a Megalosaurus? (yes/no)""\n")
            if d=="yes":
                e=print("Decision: Eat it.")
            if d=="no":
                e=print("Decision: Don't eat it.")
        if c=="no":
            d=input("Did the cat lick it? (yes/no)""\n")
            if d=="yes":
                e=input("Is your cat healthy? (yes/no)""\n")
                if e=="yes":
                    f=print("Decision: Eat it.")
                if e=="no":
                    f=print("Decision: Your call.")
            if d=="no":
                e=print("Decision: Eat it.")
    if b=="yes":
        c=input("Is it a raw steak? (yes/no)""\n")
        if c=="no":
            d=input("Did the cat lick it? (yes/no)""\n")
            if d=="yes":
                e=input("Is your cat healthy? (yes/no)""\n")
                if e=="yes":
                    f=print("Decision: Eat it.")
                if e=="no":
                    f=print("Decision: Your call.")
            if d=="no":
                e=print("Decision: Eat it.")
        if c=="yes":
            d=input("Are you a puma? (yes/no)""\n")
            if d=="yes":
                e=print("Decision: Eat it.")
            if d=="no":
                e=print("Decision: Don't eat it.")