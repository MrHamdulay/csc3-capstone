print("Welcome to the 30 Second Rule Expert\n------------------------------------\nAnswer the following questions by selecting from among the options.")
seen = input("Did anyone see you? (yes/no)\n")
if seen == 'yes' :
    who = input("Was it a boss/lover/parent? (yes/no)\n")
    if who == 'yes':
        cost = input("Was it expensive? (yes/no)\n")
        if cost == 'yes':
            adjustment = input("Can you cut off the part that touched the floor? (yes/no)\n")
            if adjustment == 'yes':
                print("Decision: Eat it.")
            else:
                print("Decision: Your call.")
        else:
            chocolate = input("Is it chocolate? (yes/no)\n")
            if chocolate == 'yes':
                print("Decision: Eat it.")
            else:
                print("Decision: Don't eat it.")
    else:
        print("Decision: Eat it.")
else:
    sticky = input("Was it sticky? (yes/no)\n")
    if sticky == 'yes':
        raw = input("Is it a raw steak? (yes/no)\n")
        if raw == 'yes':
            puma = input("Are you a puma? (yes/no)\n")
            if puma == 'yes':
                print("Decision: Eat it.")
            else:
                print("Decision: Don't eat it.")
        else:
            cat = input("Did the cat lick it? (yes/no)\n")
            if cat == 'yes':
                health = input("Is your cat healthy? (yes/no)\n")
                if health == 'yes':
                    print("Decision: Eat it.")
                else:
                    print("Decision: Your call.")
            else:
                print("Decision: Eat it.")
    else:
        emausaurus = input("Is it an Emausaurus? (yes/no)\n")
        if emausaurus == 'yes':
            megalosaurus = input("Are you a Megalosaurus? (yes/no)\n")
            if megalosaurus == 'yes':
                print("Decision: Eat it.")
            else:
                print("Decision: Don't eat it.")
        else:
            cat1 = input("Did the cat lick it? (yes/no)\n")
            if cat1 == 'yes':
                health2 = input("Is your cat healthy? (yes/no)\n")
                if health2 == 'yes':
                        print("Decision: Eat it.")
                else:
                    print("Decision: Your call.")
            else:
                print("Decision: Eat it.")            
                
            