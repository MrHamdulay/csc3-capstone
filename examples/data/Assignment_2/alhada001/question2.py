print("Welcome to the 30 Second Rule Expert")
print("------------------------------------")
print("Answer the following questions by selecting from among the options.")
seeyou = input("Did anyone see you? (yes/no)\n")
if seeyou == "yes":
    who = input("Was it a boss/lover/parent? (yes/no)\n")
    if who == "no":
        print("Decision: Eat it.")
    else:
        expensive = input("Was it expensive? (yes/no)\n")
        if expensive == "yes":
            cutoffpart = input("Can you cut off the part that touched the floor? (yes/no)\n")
            if cutoffpart == "yes":
                print("Decision: Eat it.")
               
            else:
                print("Decision: Your call.")
        else:
            coco = input("Is it chocolate? (yes/no)\n")
            if coco == "yes":
                print("Decision: Eat it.")
            else:
                print("Decision: Don't eat it.")
else:
    sticky = input("Was it sticky? (yes/no)\n")
    if sticky == "yes":
        steak = input("Is it a raw steak? (yes/no)\n")
        if steak == "yes":
            puma = input("Are you a puma? (yes/no)\n")
            if puma == "yes":
                print("Decision: Eat it.")
            else: 
                print("Decision: Don't eat it.")
        else:
            cat = input("Did the cat lick it? (yes/no)\n")
            if cat == "no":
                print("Decision: Eat it.")
            else:
                healthycat = input("Is your cat healthy? (yes/no)\n")
                if healthycat == "no":
                    print("Decision: Your call.")
                else: 
                    print("Decision: Eat it.")
    else:
        eman = input("Is it an Emausaurus? (yes/no)\n")
        if eman == "no":
            cat = input("Did the cat lick it? (yes/no)\n")
            if cat == "no":
                print("Decision: Eat it.")
            else:
                healthycat  = input("Is your cat healthy? (yes/no)\n")
                if healthycat == "no":
                    print("Decision: Your call.")
                else:
                    print("Decision: Eat it.")
        else:
            mega = input("Are you a Megalosaurus? (yes/no)\n")
            if mega == "yes":
                print("Decision: Eat it.")
            else: 
                print("Decision: Don't eat it.")    
                  
        