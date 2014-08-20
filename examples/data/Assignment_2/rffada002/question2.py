print ("Welcome to the 30 Second Rule Expert")
print ("------------------------------------")
print ("Answer the following questions by selecting from among the options.")
seen=input("Did anyone see you? (yes/no)\n")
if (seen == 'no'):
    sticky=input("Was it sticky? (yes/no)\n")
    if (sticky == 'no'):
        emausaurus=input("Is it an Emausaurus? (yes/no)\n")
        if (emausaurus == 'no'):
            cat=input("Did the cat lick it? (yes/no)\n")
            if (cat == 'no'):
                print ("Decision: Eat it.")
            elif (cat == 'yes'):
                healthy=input("Is your cat healthy? (yes/no)\n")
                if (healthy == 'yes'):
                    print ("Decision: Eat it.")
                elif (healthy == 'no'):
                    print ("Decision: Your call.")
        elif (emausaurus == 'yes'):
            megalosaurus=input("Are you a Megalosaurus? (yes/no)\n")
            if (megalosaurus == 'yes'):
                print ("Decision: Eat it.")
            elif (megalosaurus == 'no'):
                print ("Decision: Don't eat it.")
    elif (sticky == 'yes'):
        steak=input("Is it a raw steak? (yes/no)\n")
        if (steak == 'no'):
            cat=input("Did the cat lick it? (yes/no)\n")
            if (cat == 'no'):
                print ("Decision: Eat it.")
            elif (cat == 'yes'):
                healthy=input("Is your cat healthy? (yes/no)\n")
                if (healthy == 'yes'):
                    print ("Decision: Eat it.")
                elif (healthy == 'no'):
                    print ("Decision: Your call.")            
        elif (steak == 'yes'):
            puma=input("Are you a puma? (yes/no)\n")
            if (puma == 'yes'):
                print ("Decision: Eat it.")
            elif (puma == 'no'):
                print ("Decision: Don't eat it.")
elif (seen == 'yes'):
    friend=input("Was it a boss/lover/parent? (yes/no)\n")
    if (friend == 'no'):
        print ("Decision: Eat it.")
    elif (friend == 'yes'):
        price=input("Was it expensive? (yes/no)\n")
        if (price == 'no'):
            chocolate=input("Is it chocolate? (yes/no)\n")
            if (chocolate == 'no'):
                print ("Decision: Don't eat it.")
            elif (chocolate == 'yes'):
                print ("Decision: Eat it.")
        elif (price == 'yes'):
            cut=input("Can you cut off the part that touched the floor? (yes/no)\n")
            if (cut == 'yes'):
                print ("Decision: Eat it.")
            elif (cut == 'no'):
                print ("Decision: Your call.")