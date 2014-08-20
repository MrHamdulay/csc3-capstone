print("Welcome to the 30 Second Rule Expert")
print("------------------------------------")
print("Answer the following questions by selecting from among the options.")
see=input("Did anyone see you? (yes/no)\n")
if (see=='yes'):
    who=input("Was it a boss/lover/parent? (yes/no)\n")
    if (who=='yes'):
        cost=input("Was it expensive? (yes/no)\n")
        if (cost=='yes'):
            cut=input("Can you cut off the part that touched the floor? (yes/no)\n")
            if (cut=='yes'):
                print("Decision: Eat it.") 
            if (cut=='no'):
                print("Decision: Your call.")
        if (cost=='no'):
            choc=input("Is it chocolate? (yes/no)\n")
            if (choc=='yes'):
                print("Decision: Eat it.")
            if (choc=='no'):
                print("Decision: Don't eat it.")
    if (who=='no'):
        print("Decision: Eat it.")
if (see=='no'):
    sticky=input("Was it sticky? (yes/no)\n")
    if (sticky=='yes'):
        raw=input("Is it a raw steak? (yes/no)\n")
        if (raw=='yes'):
            puma=input("Are you a puma? (yes/no)\n")
            if (puma=='no'):
                print("Decision: Don't eat it.")
            if (puma=='yes'):
                print("Decision: Eat it.")
        if (raw=='no'):
            lick=input("Did the cat lick it? (yes/no)\n")
            if (lick=='no'):
                print("Decision: Eat it.")
            if (lick=='yes'):
                healthy=input("Is your cat healthy? (yes/no)\n")
                if (healthy=='yes'):
                    print("Decision: Eat it.")
                if (healthy=='no'):
                    print("Decision: Your call.")
    if (sticky=='no'):
        ema=input("Is it an Emausaurus? (yes/no)\n")
        if (ema=='no'):
            lick=input("Did the cat lick it? (yes/no)\n")
            if (lick=='no'):
                print("Decision: Eat it.")
            if (lick=='yes'):
                healthy=input("Is your cat healthy? (yes/no)\n")
                if (healthy=='yes'):
                    print("Decision: Eat it.")
                if (healthy=='no'):
                    print("Decision: Your call.")
        if (ema=='yes'):
            mega=input("Are you a Megalosaurus? (yes/no)\n")
            if (mega=='yes'):
                print("Decision: Eat it.")
            if (mega=='no'):
                print("Decision: Don't eat it.")