#30 Second Rule Expert
#Khwezi Majola
#MJLKHW001
#10 March 2014

def expert():
    print("Welcome to the 30 Second Rule Expert")
    print("------------------------------------")
    print("Answer the following questions by selecting from among the options.")
    seeyou = input("Did anyone see you? (yes/no)\n")
    if seeyou == "no":
        sticky = input("Was it sticky? (yes/no)\n")
        if sticky == "no":
            emau = input("Is it an Emausaurus? (yes/no)\n")
            if emau == "no":
                catlick = input("Did the cat lick it? (yes/no)\n")
                if catlick == "no":
                    print("Decision: Eat it.")
                elif catlick == "yes":
                    cathealth = input("Is your cat healthy? (yes/no)\n")
                    if cathealth == "no":
                        print("Decision: Your call.")
                    elif cathealth == "yes":
                        print("Decision: Eat it.")
            elif emau == "yes":
                mega = input("Are you a Megalosaurus? (yes/no)\n")
                if mega == "no":
                    print("Decision: Don't eat it.")
                elif mega == "yes":
                    print("Decision: Eat it.")
        elif sticky == "yes":
            rawsteak = input("Is it a raw steak? (yes/no)\n")
            if rawsteak == "no":
                catlick = input("Did the cat lick it? (yes/no)\n")
                if catlick == "no":
                    print("Decision: Eat it.")
                elif catlick == "yes":
                    cathealth = input("Is your cat healthy? (yes/no)\n")
                    if cathealth == "no":
                        print("Decision: Your call.")
                    elif cathealth == "yes":
                        print("Decision: Eat it.")
            elif rawsteak == "yes":
                puma = input("Are you a puma? (yes/no)\n")
                if puma == "no":
                    print("Decision: Don't eat it.")
                elif puma == "yes":
                    print("Decision: Eat it.")
    elif seeyou == "yes":
        person = input("Was it a boss/lover/parent? (yes/no)\n")
        if person == "no":
            print("Decision: Eat it.")
        elif person == "yes":
            expen = input("Was it expensive? (yes/no)\n")
            if expen == "no":
                choc = input("Is it chocolate? (yes/no)\n")
                if choc == "no":
                    print("Decision: Don't eat it.")
                elif choc == "yes":
                    print("Decision: Eat it.")
            elif expen == "yes":
                cut = input("Can you cut off the part that touched the floor? (yes/no)\n")
                if cut == "no":
                    print("Decision: Your call.")
                elif cut == "yes":
                    print("Decision: Eat it.")

expert()