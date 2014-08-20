print("Welcome to the 30 Second Rule Expert\n------------------------------------")
print("Answer the following questions by selecting from among the options.")
seen = input("Did anyone see you? (yes/no)\n")
if seen == "yes":
    blp = input("Was it a boss/lover/parent? (yes/no)\n") 
    if blp == "yes":
        expensive = input("Was it expensive? (yes/no)\n")
        if expensive == "yes":
            cut_off = input("Can you cut off the part that touched the floor? (yes/no)\n")
            if cut_off == "yes":
                print("Decision: Eat it.")
            if cut_off == "no":
                print("Decision: Your call.")
        if expensive == "no":
            chocolate = input("Is it chocolate? (yes/no)\n")
            if chocolate == "yes":
                print("Decision: Eat it.")
            if chocolate == "no":
                print("Decision: Don't eat it.")
    if blp == "no":
        print("Decision: Eat it.")
if seen == "no":
    sticky = input("Was it sticky? (yes/no)\n")
    if sticky == "yes":
        raw_steak = input("Is it a raw steak? (yes/no)\n")
        if raw_steak == "yes":
            puma = input("Are you a puma? (yes/no)\n")
            if puma == "yes":
                print("Decision: Eat it.")
            if puma == "no":
                print("Decision: Don't eat it.")
        if raw_steak == "no":
            cat = input("Did the cat lick it? (yes/no)\n")
            if cat == "yes":
                cat_healthy = input("Is your cat healthy? (yes/no)\n")
                if cat_healthy == "yes":
                    print("Decision: Eat it.")
                if cat_healthy == "no":
                    print("Decision: Your call.")
            if cat == "no":
                print("Decision: Eat it.")
    if sticky == "no":
        ema = input("Is it an Emausaurus? (yes/no)\n")
        if ema == "yes":
            mega = input("Are you a Megalosaurus? (yes/no)\n")
            if mega == "yes":
                print("Decision: Eat it.")
            if mega == "no":
                print("Decision: Don't eat it.")
        if ema == "no":
            cat = input("Did the cat lick it? (yes/no)\n")
            if cat == "yes":
                cat_healthy = input("Is your cat healthy? (yes/no)\n")
                if cat_healthy == "yes":
                    print("Decision: Eat it.")
                if cat_healthy == "no":
                    print("Decision: Your call.")
            if cat == "no":
                    print("Decision: Eat it.")