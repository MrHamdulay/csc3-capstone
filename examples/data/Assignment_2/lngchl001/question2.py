print("Welcome to the 30 Second Rule Expert")
print("------------------------------------")
print("Answer the following questions by selecting from among the options.")
answer1=input("Did anyone see you? (yes/no)\n")
if answer1=="yes":
    answer2=input("Was it a boss/lover/parent? (yes/no)\n")
    if answer2=="no":
        print("Decision: Eat it.")
    elif answer2=="yes":
        answer3=input("Was it expensive? (yes/no) \n")
        if answer3=="yes":
            answer4=input("Can you cut off the part that touched the floor? (yes/no) \n")
            if answer4=="yes":
                print("Decision: Eat it.")
            elif answer4=="no":
                print("Decision: Your call.")
        elif answer3=="no":
            answer5=input("Is it chocolate? (yes/no) \n")
            if answer5=="yes":
                print("Decision: Eat it.")
            elif answer5=="no":
                print("Decision: Don't eat it.")
elif answer1=="no":
        answer20=input("Was it sticky? (yes/no)\n")
        if answer20=="no":
            answer21=input("Is it an Emausaurus? (yes/no)\n")
            if answer21=="yes":
                    answer22=input("Are you a Megalosaurus? (yes/no) \n")
                    if answer22=="yes":
                        print("Decision: Eat it.")
                    elif answer22=="no":
                        print("Decision: Don't eat it.")
            elif answer21=="no":
                answer15=input("Did the cat lick it? (yes/no) \n")
                if answer15=="yes":
                    answer25=input("Is your cat healthy? (yes/no) \n")
                    if answer25=="yes":
                        print("Decision: Eat it.")
                    elif answer25=="no":
                        print("Decision: Your call.")
                elif answer15=="no":
                    print("Decision: Eat it.")
        elif answer20=="yes":
                answer23=input("Is it a raw steak? (yes/no) \n")  
                if answer23=="no":
                    answer24=input("Did the cat lick it? (yes/no) \n")
                    if answer24=="yes":
                        answer25=input("Is your cat healthy? (yes/no) \n")
                        if answer25=="yes":
                            print("Decision: Eat it.")
                        elif answer25=="no":
                            print("Decision: Your call.")
                    elif answer24=="no":
                        print("Decision: Eat it.")
                elif answer23=="yes":
                    answer26=input("Are you a puma? (yes/no) \n")
                    if answer26=="no":
                        print("Decision: Don't eat it.")
                    elif answer26=="yes":
                        print("Decision: Eat it.")
