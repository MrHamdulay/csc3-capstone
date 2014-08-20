print("Welcome to the 30 Second Rule Expert")
print("------------------------------------")
print("Answer the following questions by selecting from among the options.")
a=input("Did anyone see you? (yes/no)\n")
if a=="yes":
    b=input("Was it a boss/lover/parent? (yes/no)\n")
    if b=="no":
        print("Decision: Eat it.")
    if b=="yes":
        c=input("Was it expensive? (yes/no)\n")
        if c=="no":
            d=input("Is it chocolate? (yes/no)\n")
            if d=="yes":
                print("Decision: Eat it.")
            if d=="no":
                print("Decision: Don't eat it.")
        if c=="yes":
            e=input("Can you cut off the part that touched the floor? (yes/no)\n")
            if e=="yes":
                print("Decision: Eat it.")
            if e=="no":
                print("Decision: Your call.")
if a=="no":
    f=input("Was it sticky? (yes/no)\n")
    if f=="no":
        g=input("Is it an Emausaurus? (yes/no)\n")
        if g=="yes":
            h=input("Are you a Megalosaurus? (yes/no)\n")
            if h=="yes":
                print("Decision: Eat it.")
            if h=="no":
                print("Decision: Don't eat it.")
        if g=="no":
            i=input("Did the cat lick it? (yes/no)\n")
            if i=="yes":
                j=input("Is your cat healthy? (yes/no)\n")
                if j=="yes":
                    print("Decision: Eat it.")
                if j=="no":
                    print("Decision: Your call.")
            if i=="no":
                print("Decision: Eat it.")
    if f=="yes":
        k=input("Is it a raw steak? (yes/no)\n")
        if k=="no":
            i=input("Did the cat lick it? (yes/no)\n")
            if i=="yes":
                j=input("Is your cat healthy? (yes/no)\n")
                if j=="yes":
                    print("Decision: Eat it.")
                if j=="no":
                        print("Decision: Your call.")
            if i=="no":
                        print("Decision: Eat it.")
        if k=="yes":
            l=input("Are you a puma? (yes/no)\n")
            if l=="yes":
                print("Decision: Eat it.")
            if l=="no":
                    print("Decision: Don't eat it.")