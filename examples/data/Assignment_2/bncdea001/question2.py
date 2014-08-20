def food():
    print("Welcome to the 30 Second Rule Expert")
    print("------------------------------------")
    print("Answer the following questions by selecting from among the options.")
    ans=input("Did anyone see you? (yes/no)\n")
    if ans=="yes":
        blp=input("Was it a boss/lover/parent? (yes/no)\n")
        if blp=="yes":
            exp=input("Was it expensive? (yes/no)\n")
            if exp=="yes":
                cut=input("Can you cut off the part that touched the floor? (yes/no)\n")
                if cut=="yes":
                    print("Decision: Eat it.")
                elif cut=="no":
                    print("Decision: Your call.")
            elif exp=="no":
                choc=input("Is it chocolate? (yes/no)\n")
                if choc=="yes":
                    print("Decision: Eat it.")
                elif choc=="no":
                    print("Decision: Don't eat it.")
        elif blp=="no":
            print("Decision: Eat it.")
    elif ans=="no":
        sticky=input("Was it sticky? (yes/no)\n")
        if sticky=="yes":
            raw=input("Is it a raw steak? (yes/no)\n")
            if raw=="yes":
                puma=input("Are you a puma? (yes/no)\n")
                if puma=="yes":
                    print("Decision: Eat it.")
                elif puma=="no":
                    print("Decision: Don't eat it.")
            elif raw=="no":
                cat=input("Did the cat lick it? (yes/no)\n")
                if cat=="no":
                    print("Decision: Eat it.")
                if cat=="yes":
                    healthy=input("Is your cat healthy? (yes/no)\n")
                    if healthy=="yes":
                        print("Decision: Eat it.")
                    elif healthy=="no":
                        print("Decision: Your call.")
        elif sticky=="no":
            emau=input("Is it an Emausaurus? (yes/no)\n")
            if emau=="yes":
                mega=input("Are you a Megalosaurus? (yes/no)\n")
                if mega=="yes":
                    print("Decision: Eat it.")
                elif mega=="no":
                    print("Decision: Don't eat it.")
            elif emau=="no":
                cat=input("Did the cat lick it? (yes/no)\n")
                if cat=="no":
                    print("Decision: Eat it.")
                if cat=="yes":
                    healthy=input("Is your cat healthy? (yes/no)\n")
                    if healthy=="yes":
                        print("Decision: Eat it.")
                    elif healthy=="no":
                        print("Decision: Your call.")                
        
        

        
food()

