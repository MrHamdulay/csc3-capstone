print("Welcome to the 30 Second Rule Expert")
print("------------------------------------")
print("Answer the following questions by selecting from among the options.")
x1 = input("Did anyone see you? (yes/no)\n")
if x1 == 'yes':
    x2 = input("Was it a boss/lover/parent? (yes/no)\n")
    if x2 == 'yes':
        x3= input("Was it expensive? (yes/no)\n")
        if x3 == 'yes':
            x4= input("Can you cut off the part that touched the floor? (yes/no)\n")
            if x4 == 'yes':
                print("Decision: Eat it.")
            else:print("Decision: Your call.")
        else: 
            x5 = input("Is it chocolate? (yes/no)\n")
            if x5 == 'yes':
                print("Decision: Eat it.")
            else: print("Decision: Don't eat it.")
    else: print("Decision: Eat it.")
else: 
    x6 =input("Was it sticky? (yes/no)\n")
    if x6 == 'yes':
        x7=input("Is it a raw steak? (yes/no)\n")
        if x7 == 'yes':
            x8=input("Are you a puma? (yes/no)\n")
            if x8 == 'yes':
                print("Decision: Eat it.")
            else: print("Decision: Don't eat it.")
        else: 
            x9=input("Did the cat lick it? (yes/no)\n")
            if x9 == 'yes':
                x10=input("Is your cat healthy? (yes/no)\n")
                if x10 == 'yes':
                    print("Decision: Eat it.")
                else: print("Decision: Your call.")
            else: print("Decision: Eat it.")
    else: 
        x11= input("Is it an Emausaurus? (yes/no)\n")
        if x11 == 'yes':
            x12= input("Are you a Megalosaurus? (yes/no)\n")
            if x12 == 'yes':
                print("Decision: Eat it.")
            else: print("Decision: Don't eat it.")
        else:
            cat=input("Did the cat lick it? (yes/no)\n")
            if cat == 'yes':
                health=input("Is your cat healthy? (yes/no)\n")
                if health == 'yes':
                    print("Decision: Eat it.")
                else: print("Decision: Your call.")
            else: print("Decision: Eat it.")                
