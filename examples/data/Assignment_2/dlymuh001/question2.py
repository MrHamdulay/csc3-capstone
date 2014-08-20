def cat():
    lick = input("Did the cat lick it? (yes/no)\n")
    if (lick == "yes"):
        healthy = input("Is your cat healthy? (yes/no)\n")
        if (healthy == "yes"):
            return "Eat it"
        elif (healthy == "no"):
            return "Your call"
    elif (lick == "no"):
        return "Eat it"

print("Welcome to the 30 Second Rule Expert")
print("------------------------------------")
print("Answer the following questions by selecting from among the options.")
decision = ""
seen = input("Did anyone see you? (yes/no)\n")
if (seen == "yes"):
    person = input("Was it a boss/lover/parent? (yes/no)\n")
    if (person == "yes"):
        expensive = input("Was it expensive? (yes/no)\n")
        if (expensive == "yes"):
            cut_off = input("Can you cut off the part that touched the floor? (yes/no)\n")
            if (cut_off == "yes"):
                decision = "Eat it"
            elif (cut_off == "no"):
                decision = "Your call"
        elif (expensive == "no"):
            chocolate = input("Is it chocolate? (yes/no)\n")
            if (chocolate == "yes"):
                decision = "Eat it"
            elif (chocolate == "no"):
                decision = "Don\'t eat it" 
    elif (person == "no"):
        decision = "Eat it"
elif (seen == "no"):
    sticky = input("Was it sticky? (yes/no)\n")
    if (sticky == "yes"):
        raw_steak = input("Is it a raw steak? (yes/no)\n")
        if (raw_steak == "yes"):
            puma = input("Are you a puma? (yes/no)\n")
            if (puma == "yes"):
                decision = "Eat it"
            elif (puma == "no"):
                decision = "Don\'t eat it"
        elif (raw_steak == "no"):
            decision = cat()
    elif (sticky == "no"):
        emausaurus = input("Is it an Emausaurus? (yes/no)\n")
        if (emausaurus == "yes"):
            megalosaurus = input("Are you a Megalosaurus? (yes/no)\n")
            if (megalosaurus == "yes"):
                decision = "Eat it"
            elif (megalosaurus == "no"):
                decision = "Don\'t eat it"
        elif (emausaurus == "no"):
            decision = cat()
##output decision
print ("Decision:", decision, sep = " ", end = ".")
        
    