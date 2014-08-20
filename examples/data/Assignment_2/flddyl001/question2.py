def CupCake():
    print("\nWelcome to the 30 Second Rule Expert")
    print("------------------------------------")
    print("Answer the following questions by selecting from among the options.")
    v_answer=input("Did anyone see you? (yes/no)\n")
    if v_answer=="yes":
        v_answer=input("Was it a boss/lover/parent? (yes/no)\n")
        if v_answer=="yes":
            v_answer=input("Was it expensive? (yes/no)\n")
            if v_answer=="yes":
                v_answer=input("Can you cut off the part that touched the floor? (yes/no)\n")
                if v_answer=="yes":
                    print("Decision: Eat it.")
                elif v_answer=="no":
                    print("Decision: Your call.")
            elif v_answer=="no":
                v_answer=input("Is it chocolate? (yes/no)\n")
                if v_answer=="yes":
                    print("Decision: Eat it.")
                elif v_answer=="no":
                    print("Decision: Don't eat it.")
        elif v_answer=="no":
            print("Decision: Eat it.")
    elif v_answer=="no":
        v_answer=input("Was it sticky? (yes/no)\n")
        if v_answer=="yes":
            v_answer=input("Is it a raw steak? (yes/no)\n")
            if v_answer=="yes":
                v_answer=input("Are you a puma? (yes/no)\n")
                if v_answer=="yes":
                    print("Decision: Eat it.")
                elif v_answer=="no":
                    print("Decision: Don't eat it.")
            elif v_answer=="no":
                v_answer=input("Did the cat lick it? (yes/no)\n")
                if v_answer=="yes":
                    v_answer=input("Is your cat healthy? (yes/no)\n")
                    if v_answer=="yes":
                        print("Decision: Eat it.")
                    elif v_answer=="no":
                        print("Decision: Your call.")
                elif v_answer=="no":
                    print("Eat it.")
        elif v_answer=="no":
            v_answer=input("Is it an Emausaurus? (yes/no)\n")
            if v_answer=="yes":
                v_answer=input("Are you a Megalosaurus? (yes/no)\n")
                if v_answer=="yes":
                    print("Decision: Eat it.")
                elif v_answer=="no":
                    print("Decision: Don't eat it.")                
            elif v_answer=="no":
                v_answer=input("Did the cat lick it? (yes/no)\n")
                if v_answer=="yes":
                    v_answer=input("Is your cat healthy? (yes/no)\n")
                    if v_answer=="yes":
                        print("Decision: Eat it.")
                    elif v_answer=="no":
                        print("Decision: Your call.")
                elif v_answer=="no":
                    print("Decision: Eat it.")
CupCake()