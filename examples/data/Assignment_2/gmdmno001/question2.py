#You dropped a sweet
#User expected to type in "no" for a No and "yes" for a Yes. Nothing else
print("Welcome to the 30 Second Rule Expert")
print("------------------------------------")
print("Answer the following questions by selecting from among the options.")

sight=input("Did anyone see you? (yes/no)\n")
if sight=="no":
    sticky=input("Was it sticky? (yes/no)\n")
    if  sticky=="no":
        emausaurus=input("Is it an Emausaurus? (yes/no)\n")
        if emausaurus=="no":
            cat=input("Did the cat lick it? (yes/no)\n")
            if cat=="no":
                print("Decision: Eat it.")
            elif cat=="yes":
                cat_health=input("Is your cat healthy? (yes/no)\n")
                if cat_health=="no":
                    print("Decision: Your call.")
                elif cat_health=="yes":
                    print("Decision: Eat it.")
        elif emausaurus=="yes":
            megal=input("Are you a Megalosaurus? (yes/no)\n")
            if megal=="yes":
                print("Decision: Eat it.")
            elif megal=="no":
                print("Decision: Don't eat it.")
    elif sticky=="yes":
        raw=input("Is it a raw steak? (yes/no)\n")
        if raw=="no":
            cat=input("Did the cat lick it? (yes/no)\n")
            if cat=="no":
                print("Decision: Eat it.")
            elif cat=="yes":
                cat_health=input("Is your cat healthy? (yes/no)\n")
                if cat_health=="no":
                    print("Your call.")
                elif cat_health=="yes":
                    print("Decision: Eat it.")
        elif raw=="yes":
            puma=input("Are you a puma? (yes/no)\n")
            if puma=="yes":
                print("Decision: Eat it.")
            elif puma=="no":
                print("Decision: Don't eat it.")
elif sight=="yes":
    person=input("Was it a boss/lover/parent? (yes/no)\n")
    if person=="no":
        print("Decision: Eat it.")
    elif person=="yes":
        value=input("Was it expensive? (yes/no)\n")
        if value=="yes":
            cut_off=input("Can you cut off the part that touched the floor? (yes/no)\n")
            if cut_off=="no":
                print("Decision: Your call.")
            elif cut_off=="yes":
                print("Decision: Eat it.")
        elif value=="no":
            chocy=input("Is it chocolate? (yes/no)\n")
            if chocy=="yes":
                print("Decision: Eat it.")
            elif chocy=="no":
                print("Decision: Don't eat it.")
                