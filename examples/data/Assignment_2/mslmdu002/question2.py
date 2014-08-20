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
        if c=="yes":
            d=input("Can you cut off the part that touched the floor? (yes/no)\n")
            if d=="yes":
                print("Decision: Eat it.")
            if d=="no":
                print("Decision: Your call.")
        if c=="no":
            e=input("Is it chocolate? (yes/no)\n")
            if e=="yes":
                print("Decision: Eat it.")
            if e=="no":
                print("Decision: Don't eat it.")
if a=="no":
    f=input("Was it sticky? (yes/no)\n")
    if f=="yes":
        g=input("Is it a raw steak? (yes/no)\n")
        if g=="yes":
            h=input("Are you a puma? (yes/no)\n")
            if h=="no":
                print("Decision: Don't eat it.")
            if h=="yes":
                print("Decision: Eat it.")
        if g=="no":
            w=input("Did the cat lick it? (yes/no)\n")
            if w=="no":
                print("Decision: Eat it.")
            if w=="yes":
                p=input("Is your cat healthy? (yes/no)\n")
                if p=="no":
                    print("Decision: Your call.")
                if p=="yes":
                    print("Decision: Eat it.")
    if f=="no":
        o=input("Is it an Emausaurus? (yes/no)\n")
        if o=="no":
            q=input("Did the cat lick it? (yes/no)\n")
            if q=="no":
                print("Decision: Eat it.")
            if q=="yes":
                s=input("Is your cat healthy? (yes/no)\n")
                if s=="no":
                    print("Decision: Your call.")
                if s=="yes":
                    print("Decision: Eat it.")
        if o=="yes":
           v=input("Are you a Megalosaurus? (yes/no)\n")
           if v=="no":
               print("Decision: Don't eat it.")
           if v=="yes":
               print("Decision: Eat it.")