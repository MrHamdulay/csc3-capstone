YC='Decision: Your call.'
EI='Decision: Eat it.'
DEI="Decision: Don't eat it."
print("Welcome to the 30 Second Rule Expert")
print("------------------------------------")
print("Answer the following questions by selecting from among the options.")


see=input("Did anyone see you? (yes/no)\n")
if see == 'yes':
    who=input("Was it a boss/lover/parent? (yes/no)\n")
    if who =='yes':
        price = input("Was it expensive? (yes/no)\n")
        if price =='yes':
            floor = input("Can you cut off the part that touched the floor? (yes/no)\n")
            if floor == 'yes':
                print("Decision: Eat it.")
            else:
                print("Decision: Your call.")
        else:
            choc = input("Is it chocolate? (yes/no)\n")
            if choc== 'yes':
                print("Decision: Eat it.")
            else:
                print(DEI)
    else:
        print(EI)
else:
    sticky = input("Was it sticky? (yes/no)\n")
    if sticky == 'yes':
        steak = input("Is it a raw steak? (yes/no)\n")
        if steak =='yes':
            puma = input("Are you a puma? (yes/no)\n")
            if puma == 'yes':
                print(EI)
            else:
                print(DEI)
        else:
            cat = input("Did the cat lick it? (yes/no)\n")
            if cat=='yes':
                health =input("Is your cat healthy? (yes/no)\n")
                if health == 'yes':
                    print(EI)
                else:
                    print(YC)
            else:
                print(EI)
    else:
        ern=input("Is it an Emausaurus? (yes/no) \n")
        if ern == 'yes':
            mega =input("Are you a Megalosaurus? (yes/no)\n")
            if mega == 'yes':
                print("Decision: Eat it.")
            else: 
                print(DEI)
        else:
            cat = input("Did the cat lick it? (yes/no)\n")
            if cat=='yes':
                health =input("Is your cat healthy? (yes/no)\n")
                if health == 'yes':
                    print(EI)
                else:
                    print(YC)
            else:
                print(EI)            