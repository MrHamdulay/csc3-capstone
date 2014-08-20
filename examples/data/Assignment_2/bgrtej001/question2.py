#Assignment 2, Question 2
#Tejasvin Bagirathi BGRTEJ001
#11/03/2014

print("Welcome to the 30 Second Rule Expert")
print("------------------------------------")
print("Answer the following questions by selecting from among the options.")
seen = input("Did anyone see you? (yes/no)\n")
if seen == 'yes':
    who = input("Was it a boss/lover/parent? (yes/no)\n")
    if who == 'yes':
        expensive = input("Was it expensive? (yes/no)\n")
        if expensive ==  'yes':
            cutPart = input("Can you cut off the part that touched the floor? (yes/no)\n")
            if cutPart == 'yes':
                print("Decision: Eat it.")
            else: print("Decision: Your call.")
        else:
            isChocolate = input("Is it chocolate? (yes/no)\n")
            if isChocolate == 'yes':
                print("Decision: Eat it.")
            else: print("Decision: Don't eat it.")
    else: print("Decision: Eat it.")
else:
    sticky = input("Was it sticky? (yes/no)\n")
    if sticky == 'no':
        isEmausaurus = input("Is it an Emausaurus? (yes/no)\n")
        if isEmausaurus == 'yes':
            isMega = input("Are you a Megalosaurus? (yes/no)\n")
            if isMega=='yes': print("Decision: Eat it.")
            else: print("Decision: Don't eat it.")
        else:
            catLick = input("Did the cat lick it? (yes/no)\n")
            if catLick == 'yes':
                catHealth = input("Is your cat healthy? (yes/no)\n")
                if catHealth == 'yes':
                    print("Decision: Eat it.")
                else: print("Decision: Your call.")
            else: print("Decision: Eat it.")
    else:
        isSteak = input("Is it a raw steak? (yes/no)\n")
        if isSteak == 'no':
            catLick = input("Did the cat lick it? (yes/no)\n")
            if catLick == 'yes':
                catHealth = input("Is your cat healthy? (yes/no)\n")
                if catHealth == 'yes':
                    print("Decision: Eat it.")
                else: print("Decision: Your Call.")
            else: print("Decision: Eat it.")
        else:
            puma = input("Are you a puma? (yes/no)\n")
            if puma == 'yes':
                print("Decision: Eat it.")
            else: print("Decision: Don't eat it.")
         
            
        
    