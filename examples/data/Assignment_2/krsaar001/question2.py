print("Welcome to the 30 Second Rule Expert\n", "------------------------------------\n", "Answer the following questions by selecting from among the options.", sep = "")
see = input("Did anyone see you? (yes/no)\n")
if (see == "yes"):
    person = input("Was it a boss/lover/parent? (yes/no)\n")
    if (person == "yes"):
        expensive = input("Was it expensive? (yes/no)\n")
        if(expensive == "yes"):
            cut_off = input("Can you cut off the part that touched the floor? (yes/no)\n")
            if(cut_off == "yes"):
                print("Decision: Eat it.")
            else:
                print("Decision: Your call.")
        else:
            chocolate = input("Is it chocolate? (yes/no)\n")
            if(chocolate == "yes"):
                print("Decision: Eat it.")
            else:
                print("Decision: Don't eat it.")
    else:
        print("Decision: Eat it.")
else:
    sticky = input("Was it sticky? (yes/no)\n")
    if(sticky == "yes"):
        raw = input("Is it a raw steak? (yes/no)\n")
        if(raw == "yes"):
            puma = input("Are you a puma? (yes/no)\n")
            if(puma == "yes"):
                print("Decision: Eat it.")
            else:
                print("Decision: Don't eat it.")
        else:
            lick = input("Did the cat lick it? (yes/no)\n")
            if(lick == "yes"):
                healthy = input("Is your cat healthy? (yes/no)\n")
                if(healthy == "yes"):
                    print("Decision: Eat it.")
                else:
                    print("Decision: Your call.")
            else:
                print("Decision: Eat it.")
    else:
        Emausaurus = input("Is it an Emausaurus? (yes/no)\n")
        if(Emausaurus == "yes"):
            Megalosaurus = input("Are you a Megalosaurus? (yes/no)\n")
            if(Megalosaurus == "yes"):
                print("Decision: Eat it.")
            else:
                print("Decision: Don't eat it.")
        else:
            lick = input("Did the cat lick it? (yes/no)\n")
            if(lick == "yes"):
                healthy = input("Is your cat healthy? (yes/no)\n")
                if(healthy == "yes"):
                    print("Decision: Eat it.")
                else:
                    print("Decision: Your call.")
            else:
                print("Decision: Eat it.")            