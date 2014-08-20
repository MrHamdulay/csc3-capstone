print("Welcome to the 30 Second Rule Expert")
print("------------------------------------")
print("Answer the following questions by selecting from among the options.")

eat = "Decision: Eat it."
yourcall = "Decision: Your call."
donteat = "Decision: Don't eat it."
yes = "yes"
no = "no"

seen = input("Did anyone see you? (yes/no)\n")
if seen == yes:
    blp = input("Was it a boss/lover/parent? (yes/no)\n")
    if blp == yes:
        expensive = input("Was it expensive? (yes/no)\n")
        if expensive == yes:
            cut_off = input("Can you cut off the part that touched the floor? (yes/no)\n")
            if cut_off == yes:
                print(eat)
            elif cut_off == no:
                print(yourcall)
        elif expensive == no:
            chocolate = input("Is it chocolate? (yes/no)\n")
            if chocolate == yes:
                print(eat)
            elif chocolate == no:
                print(donteat)
    elif blp == no:
        print(eat)
    
elif seen == no:
    sticky = input("Was it sticky? (yes/no)\n")
    if sticky == yes:
        steak = input("Is it a raw steak? (yes/no)\n")
        if steak == yes:
            puma = input("Are you a puma? (yes/no)\n")
            if puma == yes:
                print(eat)
            elif puma == no:
                print(donteat)
            
        elif steak == no:
            cat = input("Did the cat lick it? (yes/no)\n")
            if cat == yes:
                health_cat = input("Is your cat healthy? (yes/no)\n")
                if health_cat == yes:
                    print(eat)
                elif health_cat == no:
                    print(yourcall)
            elif cat == no:
                print(eat)
        
    elif sticky == no:
        emausaur = input("Is it an Emausaurus? (yes/no)\n")
        if emausaur == yes:
            megalosaur = input("Are you a Megalosaurus? (yes/no)\n")
            if megalosaur == yes:
                print(eat)
            elif megalosaur == no:
                print(donteat)
        elif emausaur == no:
            cat = input("Did the cat lick it? (yes/no)\n")
            if cat == yes:
                health_cat = input("Is your cat healthy? (yes/no)\n")
                if health_cat == yes:
                    print(eat)
                elif health_cat == no:
                    print(yourcall)
            elif cat == no:
                print(eat)            