#Program to help you decide whether you should eat a dropped piece of food

print("Welcome to the 30 Second Rule Expert")
print("------------------------------------")
print("Answer the following questions by selecting from among the options.")

seen = input("Did anyone see you? (yes/no)\n")
if seen=="yes":
    bossLP=input("Was it a boss/lover/parent? (yes/no)\n")
    if bossLP=="yes":
        expensive=input("Was it expensive? (yes/no)\n")
        if expensive=="yes":
            cut=input("Can you cut off the part that touched the floor? (yes/no)\n")
            if cut=="yes":
                print("Decision: Eat it.")
            if cut=="no":
                print("Decision: Your call.")
        if expensive=="no":
            choc=input("Is it chocolate? (yes/no)\n")
            if choc=="yes":
                print("Decision: Eat it.")
            if choc=="no":
                print("Decision: Don't eat it.")
    if bossLP=="no":
        print("Decision: Eat it.")
if seen=="no":
    sticky=input("Was it sticky? (yes/no)\n")
    if sticky=="yes":
        steak=input("Is it a raw steak? (yes/no)\n")
        if steak=="yes":
            puma=input("Are you a puma? (yes/no)\n")
            if puma=="yes":
                print("Decision: Eat it.")
            if puma=="no":
                print("Decision: Don't eat it.")
        if steak=="no":
            cat=input("Did the cat lick it? (yes/no)\n")
            if cat=="yes":
                catHealth=input("Is your cat healthy? (yes/no)\n")
                if catHealth=="yes":
                    print("Decision: Eat it.")
                if catHealth=="no":
                    print("Decision: Your call.")
            if cat=="no":
                print("Decision: Eat it.")
    if sticky=="no":
        Emaus=input("Is it an Emausaurus? (yes/no)\n")
        if Emaus=="yes":
            Mega=input("Are you a Megalosaurus? (yes/no)\n")
            if Mega=="yes":
                print("Decision: Eat it.")
            if Mega=="no":
                print("Decision: Don't eat it.")
        if Emaus=="no":
            cat=input("Did the cat lick it? (yes/no)\n")
            if cat=="yes":
                catHealth=input("Is your cat healthy? (yes/no)\n")
                if catHealth=="yes":
                    print("Decision: Eat it.")
                if catHealth=="no":
                    print("Decision: Your call.")
            if cat=="no":
                print("Decision: Eat it.")

