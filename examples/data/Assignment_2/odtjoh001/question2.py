print("Welcome to the 30 Second Rule Expert")
print("------------------------------------")
print("Answer the following questions by selecting from among the options.")
answ1 = input("Did anyone see you? (yes/no)\n")
if(answ1 == "yes"):
    answ2 = input("Was it a boss/lover/parent? (yes/no)\n")
    if(answ2 == "yes"):
        answ3 = input("Was it expensive? (yes/no)\n")
        if(answ3 == "yes"):
            answ4 = input("Can you cut off the part that touched the floor? (yes/no)\n")
            if(answ4 == "yes"):
                print("Decision: Eat it.")
            else:
                print("Decision: Your call.")
        else:
            answ4 = input("Is it chocolate? (yes/no)\n")
            if(answ4 == "yes"):
                print("Decision: Eat it.")
            else:
                print("Decision: Don't eat it.")
    else:
        print("Decision: Eat it.")
else:
    answ2 = input("Was it sticky? (yes/no)\n")
    if(answ2 == "yes"):
        answ3 = input("Is it a raw steak? (yes/no)\n")
        if(answ3 == "yes"):
            answ4 = input("Are you a puma? (yes/no)\n")
            if(answ4 == "yes"):
                print("Decision: Eat it.")
            else:
                print("Decision: Don't eat it.")
        else:
            answ4 = input("Did the cat lick it? (yes/no)\n")
            if(answ4 == "yes"):
                answ5 = input("Is your cat healthy? (yes/no)\n")
                if(answ5 == "yes"):
                    print("Decision: Eat it.")
                else:
                    print("Decision: Your call.")
            else:
                print("Decision: Eat it.")
    else:
        answ3 = input("Is it an Emausaurus? (yes/no)\n")
        if(answ3 == "yes"):
            answ4 = input("Are you a Megalosaurus? (yes/no)\n")
            if(answ4 == "yes"):
                print("Decision: Eat it.")
            else:
                print("Decision: Don't eat it.")
        else:
            answ4 = input("Did the cat lick it? (yes/no)\n")
            if(answ4 == "yes"):
                answ5 = input("Is your cat healthy? (yes/no)\n")
                if(answ5 == "yes"):
                    print("Decision: Eat it.")
                else:
                    print("Decision: Your call.")
            else:
                print("Decision: Eat it.")                