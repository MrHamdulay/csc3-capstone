print("Welcome to the 30 Second Rule Expert\n------------------------------------\nAnswer the following questions by selecting from among the options.")
see = input("Did anyone see you? (yes/no)\n")
if see == "yes":
    who = input("Was it a boss/lover/parent? (yes/no)\n")
    if who == "no":
        print("Decision: Eat it.")
    elif who == "yes":
        expensive = input("Was it expensive? (yes/no)\n")
        if expensive == "yes":
            cut = input("Can you cut off the part that touched the floor? (yes/no)\n")
            if cut == "yes":
                print("Decision: Eat it.")
            elif cut == "no":
                print("Decision: Your call.")
        elif expensive == "no":
            chocolate = input("Is it chocolate? (yes/no)\n")
            if chocolate == "yes":
                print("Decision: Eat it.")
            elif chocolate == "no":
                print("Decision: Don't eat it.")
if see == "no":
    sticky = input("Was it sticky? (yes/no)\n")
    if sticky == "no":
        emausaurus = input("Is it an Emausaurus? (yes/no)\n")
        if emausaurus == "yes":
            megalosaurus = input("Are you a Megalosaurus? (yes/no)\n")
            if megalosaurus == "no":
                print("Decision: Don't eat it.")
            elif megalosaurus == "yes":
                print("Decision: Eat it.")
        elif emausaurus == "no":
            cat = input("Did the cat lick it? (yes/no)\n")
            if cat == "no":
                print("Decision: Eat it.")
            elif cat == "yes":
                healthy = input("Is your cat healthy? (yes/no)\n")
                if healthy == "yes":
                    print("Decision: Eat it.")
                elif healthy == "no":
                    print("Decision: Your call.")
    elif sticky == "yes":
        steak = input("Is it a raw steak? (yes/no)\n")
        if steak == "no":
            cat = input("Did the cat lick it? (yes/no)\n")
            if cat == "no":
                print("Decision: Eat it.")
            elif cat == "yes":
                healthy = input("Is your cat healthy? (yes/no)\n")
                if healthy == "yes":
                    print("Decision: Eat it.")
                elif healthy == "no":
                    print("Decision: Your call.") 
        elif steak == "yes":
            puma = input("Are you a puma? (yes/no)\n")
            if puma == "yes":
                print("Decision: Eat it.")
            elif puma == "no":
                print("Decision: Don't eat it.")