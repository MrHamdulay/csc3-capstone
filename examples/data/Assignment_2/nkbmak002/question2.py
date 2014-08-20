print("Welcome to the 30 Second Rule Expert")
for i in range(36):
    print("-",end="")
print()
print("Answer the following questions by selecting from among the options.")
Q1 = input("Did anyone see you? (yes/no)\n")
if Q1 == "yes" :
    Q1A = input("Was it a boss/lover/parent? (yes/no)\n")
    if Q1A == "no" :
        print("Decision: Eat it.")
    elif Q1A == "yes" :
        cost = input("Was it expensive? (yes/no)\n")
        if cost == "yes" :
            floor =  input("Can you cut off the part that touched the floor? (yes/no)\n")
            if floor == "yes":
                print("Decision: Eat it.")
            elif floor == "no":
                print("Decision: Your call.")
        elif cost == "no" :
            chocolate = input("Is it chocolate? (yes/no)\n")
            if chocolate  == "yes" :
                print("Decision: Eat it.")
            elif chocolate == "no" :
                print("Decision: Don't eat it.")
elif Q1 == "no" :
    sticky = input("Was it sticky? (yes/no)\n")
    if sticky == "yes" :
        steak = input("Is it a raw steak? (yes/no)\n")
        if steak == "yes" :
            puma = input("Are you a puma? (yes/no)\n")
            if puma == "no" :
                print("Decision: Don't eat it.")
            elif puma == "yes" :
                print("Decision: Eat it.")
        elif steak == "no" :
            cat = input("Did the cat lick it? (yes/no)\n")
            if cat == "no" :
                print("Decision: Eat it.")
            elif cat == "yes" :
                health = input("Is your cat healthy? (yes/no)\n")
                if health == "no" :
                    print("Decision: Your call.")
                elif health == "yes" :
                    print("Decision: Eat it.")
                
    elif sticky == "no" :
        emausaurus = input("Is it an Emausaurus? (yes/no)\n")
        if emausaurus == "no" :
            cat = input("Did the cat lick it? (yes/no)\n")
            if cat == "no" :
                print("Decision: Eat it.")
            elif cat == "yes" :
                health = input("Is your cat healthy? (yes/no)\n")
                if health == "no" :
                    print("Decision: Your call.")
                elif health == "yes" :
                        print("Decision: Eat it.")
        elif emausaurus == "yes" :
            megalosaurus = input("Are you a Megalosaurus? (yes/no)\n")
            if megalosaurus == "no" :
                print("Decision: Don't eat it.")
            elif megalosaurus == "yes" :
                print("Decision: Eat it.")
            
        