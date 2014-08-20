#You Droppe food on the floor
#Student Name: TEMA, Thabo Hebert
#Student Number: TMXTHA006
#Date: 11 March 2014

print("Welcome to the 30 Second Rule Expert")
print("------------------------------------")
print("Answer the following questions by selecting from among the options.")

ansM = input("Did anyone see you? (yes/no)\n")
if (ansM == "yes"):
    ansB1 = input("Was it a boss/lover/parent? (yes/no)\n")
    if (ansB1 == "yes"):
        ansB2 = input("Was it expensive? (yes/no)\n")
        if (ansB2 == "yes"):
            ansB3 = input("Can you cut off the part that touched the floor? (yes/no)\n")
            if (ansB3 == "yes"):
                print("Decision: Eat it.")
            elif (ansB3 == "no"):
                print("Decision: Your call.")
        elif (ansB2 == "no"):
            ansB4 = input("Is it chocolate? (yes/no)\n")
            if (ansB4 == "yes"):
                print("Decision: Eat it.")
            elif (ansB4 == "no"):
                print("Decision: Don't eat it.")
    elif (ansB1 == "no"):
        print("Decision: Eat it.")
elif (ansM == "no"):
    ansA1 = input("Was it sticky? (yes/no)\n")
    if (ansA1 == "yes"):
        ansA2 = input("Is it a raw steak? (yes/no)\n")
        if (ansA2 == "yes"):
            ansA3 = input("Are you a puma? (yes/no)\n")
            if (ansA3 == "yes"):
                print("Decision: Eat it.")
            elif (ansA3 == "no"):
                print("Decision: Don't eat it.")
        elif (ansA2 == "no"):
            ansC1 = input("Did the cat lick it? (yes/no)\n")
            if (ansC1=="yes"):
                ansC2 = input("Is your cat healthy? (yes/no)\n")
                if (ansC2 == "yes"):
                    print("Decision: Eat it.")
                elif (ansC2 == "no"):
                    print("Decision: Your call.")
            elif (ansC1 == "no"):
                print("Decision: Eat it.")
    elif (ansA1 == "no"):
        ansB1 = input("Is it an Emausaurus? (yes/no)\n")
        if (ansB1 == "yes"):
            ansB2 = input("Are you a Megalosaurus? (yes/no)\n")
            if (ansB2 == "yes"):
                print("Decision: Eat it.")
            elif (ansB2 == "no"):
                print("Decision: Don't eat it.")
        elif (ansB1 == "no"):
            ansC1 = input("Did the cat lick it? (yes/no)\n")
            if (ansC1=="yes"):
                ansC2 = input("Is your cat healthy? (yes/no)\n")
                if (ansC2 == "yes"):
                    print("Decision: Eat it.")
                elif (ansC2 == "no"):
                    print("Decision: Your call.")
            elif (ansC1 == "no"):
                print("Decision: Eat it.")