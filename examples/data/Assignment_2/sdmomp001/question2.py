
print("Welcome to the 30 Second Rule Expert")
print("------------------------------------")
print("Answer the following questions by selecting from among the options.")
see=(input("Did anyone see you? (yes/no)\n"))
if see=="yes":
    was=(input("Was it a boss/lover/parent? (yes/no)\n"))
    if was=="no":
        print("Decision: Eat it.")
    elif was=="yes":
        expensive=(input("Was it expensive? (yes/no)\n"))
        if expensive=="no":
            choco=(input("Is it chocolate? (yes/no)\n"))
            if choco=="yes":
                print("Decision: Don't eat it.")
            elif choco=="no":
                print("Decision: Eat it.")
        elif expensive=="yes":
            cut=(input("Can you cut off the part that touched the floor? (yes/no)\n"))
            if cut=="no":
                print("Decision: Your call.")
            elif cut=="yes":
                print("Decision: Eat it.")
elif see=="no":
    sticky=(input("Was it sticky? (yes/no)\n"))
    if sticky=="yes":
        steak=(input("Is it a raw steak? (yes/no)\n"))
        if steak=="yes":
            puma=(input("Are you a puma? (yes/no)\n"))
            if puma=="yes":
                print("Decision: Eat it.")
            elif puma=="no":
                print("Decision: Don't eat it.")
        elif steak=="no":
            cat=(input("Did the cat lick it? (yes/no)\n"))
            if cat=="no":
                print("Decision: Eat it.")
                if cat=="yes":
                    healthy=(input("is your cat healthy? (yes/no)\n"))
                    if healthy=="no":
                        print("Decision: Eat it.")
                    elif healthy=="yes":
                        print("Decision: Eat it.")
    elif sticky=="no":
        Emausaurus=(input("Is it an Emausaurus? ( yes/no)\n"))
        if Emausaurus=="yes":
            Megalosaurus=(input("Are you a Megalosaurus? (yes/no)\n"))
            if Megalosaurus=="yes":
                print("Decision: Eat it.")
            elif Megalosaurus=="no":
                print("Decision: Don't eat it.")
        elif Emausaurus=="no":
            lick=(input("Did the cat lick it? (yes/no)\n"))
            if lick=="yes":
                health=(input("Is your cat healthy? (yes/no)\n"))
            elif lick=="no":
                print("Decision: Eat it.")
                if health=="yes":
                    print("Decision: Eat it.")
                elif health=="no":
                    print("Decision: Your call.")