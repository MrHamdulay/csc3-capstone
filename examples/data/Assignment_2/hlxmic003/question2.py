# Michaela Heale
# Assignment 2 Question 2

print("Welcome to the 30 Second Rule Expert\n------------------------------------\nAnswer the following questions by selecting from among the options.")
opt = input("Did anyone see you? (yes/no)\n")
if(opt=="yes"):
    opt = input("Was it a boss/lover/parent? (yes/no)\n")
    if(opt=="yes"):
        opt = input("Was it expensive? (yes/no)\n")
        if(opt=="yes"):
            opt = input("Can you cut off the part that touched the floor? (yes/no)\n")
            if(opt=="yes"):
                print("Decision: Eat it.")
            elif(opt=="no"):
                print("Decision: Your call.")
        elif(opt=="no"):
            opt = input("Is it chocolate? (yes/no)\n")
            if(opt=="yes"):
                print("Decision: Eat it.")
            elif(opt=="no"):
                print("Decision: Don't eat it.")
    elif(opt=="no"):
        print("Decision: Eat it.")
elif(opt=="no"):
    opt = input("Was it sticky? (yes/no)\n")
    if(opt=="yes"):
        opt = input("Is it a raw steak? (yes/no)\n")
        if(opt=="yes"):
            opt = input("Are you a puma? (yes/no)\n")
            if(opt=="yes"):
                print("Decision: Eat it.")
            elif(opt=="no"):
                print("Decision: Don't eat it.")
        elif(opt=="no"):
            opt = input("Did the cat lick it? (yes/no)\n")
            if(opt=="yes"):
                opt = input("Is your cat healthy? (yes/no)\n")
                if(opt=="yes"):
                    print("Decision: Eat it.")
                elif(opt=="no"):
                    print("Decision: Your call.")
            elif(opt=="no"):
                print("Decision: Eat it.")                 
    elif(opt=="no"):
        opt = input("Is it an Emausaurus? (yes/no)\n")
        if(opt=="yes"):
            opt = input("Are you a Megalosaurus? (yes/no)\n")
            if(opt=="yes"):
                print("Decision: Eat it.")
            elif (opt=="no"):
                print("Decision: Don't eat it.")
        elif(opt=="no"):
            opt = input("Did the cat lick it? (yes/no)\n")
            if(opt=="yes"):
                opt = input("Is your cat healthy? (yes/no)\n")
                if(opt=="yes"):
                    print("Decision: Eat it.")
                elif(opt=="no"):
                    print("Decision: Your call.")
            elif(opt=="no"):
                print("Decision: Eat it.")

        