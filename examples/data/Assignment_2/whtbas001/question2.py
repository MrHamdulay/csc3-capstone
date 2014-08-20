#ASSIGNMENT 2
#QUESTION 2
#WHTBAS001
#BASIL T WHITEHEAD
#10-03-2014

print("Welcome to the 30 Second Rule Expert", end="\n")
print("------------------------------------", end="\n")
print("Answer the following questions by selecting from among the options.", end="\n")

def decision():
    anyone_see = input("Did anyone see you? (yes/no)\n")
    if anyone_see == "yes":
        blp = input("Was it a boss/lover/parent? (yes/no)\n")
        if blp == "yes":
            expense = input("Was it expensive? (yes/no)\n")
            if expense == "yes":
                cut = input("Can you cut off the part that touched the floor? (yes/no)\n")
                if cut == "yes":
                    print("Decision: Eat it.\n")
                else:
                    print("Decision: Your call.\n")
            else:
                choc = input("Is it chocolate? (yes/no)\n")
                if choc == "yes":
                    print("Decision: Eat it.\n")
                else:
                    print("Decision: Don't eat it.\n")
        else:
            print("Decision: Eat it.\n")
    else:
        sticky = input("Was it sticky? (yes/no)\n")
        if sticky == "yes":
            steak = input("Is it a raw steak? (yes/no)\n")
            if steak == "yes":
                puma = input("Are you a puma? (yes/no)\n")
                if puma == "yes":
                    print("Decision: Eat it.\n")
                else:
                    print("Decision: Don't eat it.\n")
            else:
                cat = input("Did the cat lick it? (yes/no)\n")
                if cat == "yes":
                    health = input("Is your cat healthy? (yes/no)\n")
                    if health == "yes":
                        print("Decision: Eat it.\n")
                    else:
                        print("Decision: Your call.\n")
                else:
                    print("Decision: Eat it.")
        else:
            emausaurus = input("Is it an Emausaurus? (yes/no)\n")
            if emausaurus == "yes":
                megalosaurus = input("Are you a Megalosaurus? (yes/no)\n")
                if megalosaurus == "yes":
                    print("Decision: Eat it.\n")
                else:
                    print("Decision: Don't eat it.\n")
            else:
                cat = input("Did the cat lick it? (yes/no)\n")
                if cat == "yes":
                    health = input("Is your cat healthy? (yes/no)\n")
                    if health == "yes":
                        print("Decision: Eat it.\n")
                    else:
                        print("Decision: Your call.\n")
                else:
                    print("Decision: Eat it.\n")                
    
decision()