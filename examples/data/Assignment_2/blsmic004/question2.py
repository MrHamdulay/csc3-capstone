# 30 Second Rule Expert
# Michele Balestra BLSMIC004   
# 10 March 2014

print("Welcome to the 30 Second Rule Expert\n------------------------------------\nAnswer the following questions by selecting from among the options.")
ask = input("Did anyone see you? (yes/no)\n")
if ask=="yes":
    ask = input("Was it a boss/lover/parent? (yes/no)\n")
    if ask=="yes":
        ask = input("Was it expensive? (yes/no)\n")
        if ask=="yes":
            ask = input("Can you cut off the part that touched the floor? (yes/no)\n")
            if ask=="yes":
                print("Decision: Eat it.")
            elif ask=="no":
                print("Decision: Your call.")
        elif ask=="no":
            ask = input("Is it chocolate? (yes/no)\n")
            if ask=="yes":
                print("Decision: Eat it.")
            elif ask=="no":
                print("Decision: Don't eat it.")
    elif ask=="no":
        print("Decision: Eat it.")
elif ask=="no":
    ask = input("Was it sticky? (yes/no)\n")
    if ask=="yes":
        ask = input("Is it a raw steak? (yes/no)\n")
        if ask=="yes":
            ask = input("Are you a puma? (yes/no)\n")
            if ask=="yes":
                print("Decision: Eat it.")
            elif ask=="no": 
                print("Decision: Don't eat it.")
        elif ask=="no":
            ask = input("Did the cat lick it? (yes/no)\n")
            if ask=="yes":
                ask = input("Is your cat healthy? (yes/no)\n")
                if ask=="yes":
                    print("Decision: Eat it.")
                elif ask=="no":
                    print("Decision: Your call.")
            elif ask=="no":
                print("Decision: Eat it.") 
    elif ask=="no":
        ask = input("Is it an Emausaurus? (yes/no)\n")
        if ask=="yes":
            ask = input("Are you a Megalosaurus? (yes/no)\n")
            if ask=="yes":
                print("Decision: Eat it.")
            elif ask=="no":
                print("Decision: Don't eat it.")
        elif ask=="no":
            ask = input("Did the cat lick it? (yes/no)\n")
            if ask=="yes":
                ask = input("Is your cat healthy? (yes/no)\n")
                if ask=="yes":
                    print("Decision: Eat it.")
                elif ask=="no":
                    print("Decision: Your call.")
            elif ask=="no":
                print("Decision: Eat it.")
                