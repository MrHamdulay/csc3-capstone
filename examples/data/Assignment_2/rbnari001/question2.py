print("Welcome to the 30 Second Rule Expert")
print("------------------------------------")
print("Answer the following questions by selecting from among the options.")
ans = input ("Did anyone see you? (yes/no)\n")
if ans == "yes":
    bslvprnt = input ("Was it a boss/lover/parent? (yes/no)\n")
    if bslvprnt == "yes":
        expensive = input ("Was it expensive? (yes/no)\n")
        if expensive == "yes":
            touch = input ("Can you cut off the part that touched the floor? (yes/no)\n")
            if touch == "yes":
                print ("Decision: Eat it.")
            else:
                print("Decision: Your call.")
        else:
            choc = input("Is it chocolate? (yes/no)\n")
            if choc == "yes":
                print("Decision: Eat it.")
            else:
                print("Decision: Don't eat it.")
    else:
        print ("Decision: Eat it.")
else:
    sticky = input ("Was it sticky? (yes/no)\n")
    if sticky == "yes":
        steak = input ("Is it a raw steak? (yes/no)\n")
        if steak == "yes":
            puma = input ("Are you a puma? (yes/no)\n")
            if puma == "yes":
                print("Decision: Eat it.")
            else:
                print("Decision: Don't eat it.")
        else:
            cat = input ("Did the cat lick it? (yes/no)\n")
            if cat == "yes":
                health = input ("Is your cat healthy? (yes/no)\n")
                if health == "yes":
                    print("Decision: Eat it.")
                else:
                    print("Decision: Your call.")
            else:
                print("Decision: Eat it.")
    else:
        emau = input ("Is it an Emausaurus? (yes/no)\n")
        if emau == "yes":
            meglo = input ("Are you a Megalosaurus? (yes/no)\n")
            if meglo == "yes":
                print("Decision: Eat it.")
            else:
                print("Decision: Don't eat it.")
        else:
            cat = input ("Did the cat lick it? (yes/no)\n")
            if cat == "yes":
                health = input ("Is your cat healthy? (yes/no)\n")
                if health == "yes":
                    print("Decision: Eat it.")
                else:
                    print("Decision: Your call.")
            else:
                print("Decision: Eat it.")
    