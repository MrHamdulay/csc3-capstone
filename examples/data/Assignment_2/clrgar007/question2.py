def cupcake():
    print("Welcome to the 30 Second Rule Expert")
    print("------------------------------------")
    print("Answer the following questions by selecting from among the options.")
    anyone=input("Did anyone see you? (yes/no)\n")        
    if anyone=="yes":
        who=input("Was it a boss/lover/parent? (yes/no)\n")
        if who=="no":
            print("Decision: Eat it.")
        elif who=="yes":
            expensive=input("Was it expensive? (yes/no)\n")
            if expensive=="no":
                chocolate=input("Is it chocolate? (yes/no)\n")
                if chocolate=="no":  
                    print("Decision: Don't eat it.")
                elif chocolate=="yes":
                    print("Decision: Eat it.")
            elif expensive=="yes":
                cut=input("Can you cut off the part that touched the floor? (yes/no)\n")
                if cut=="yes":
                    print("Decision: Eat it.")
                elif cut=="no":
                    print("Decision: Your call.")
    if anyone=="no":
        sticky=input("Was it sticky? (yes/no)\n")
        if sticky=="no":
            emausauraus=input("Is it an Emausaurus? (yes/no)\n")
            if emausauraus=="no":
                cat=input("Did the cat lick it? (yes/no)\n")
                if cat=="no":
                    print("Decision: Eat it.")
                if cat=="yes":
                    cat_healthy=input("Is your cat healthy? (yes/no)\n")
                    if cat_healthy=="no":
                        print("Decision: Your call.")
                    elif cat_healthy=="yes":
                        print("Decision: Eat it.")
            if emausauraus=="yes":
                megalosauraus=input("Are you a Megalosaurus? (yes/no)\n")
                if megalosauraus=="yes":
                    print("Decision: Eat it.")
                elif megalosauraus=="no":
                    print("Decision: Don't eat it.")            
        if sticky=="yes":
            rawsteak=input("Is it a raw steak? (yes/no)\n")
            if rawsteak=="yes":
                puma=input("Are you a puma? (yes/no)\n")
                if puma=="yes":
                    print("Decision: Eat it.")
                if puma=="no":
                    print("Decision: Don't eat it.")
            if rawsteak=="no":
                cat=input("Did the cat lick it? (yes/no)\n")
                if cat=="no":
                    print("Decision: Eat it.")
                if cat=="yes":
                    cat_healthy=input("Is your cat healthy? (yes/no)\n")
                    if cat_healthy=="no":
                        print("Decision: Your call.")
                    elif cat_healthy=="yes":
                        print("Decision: Eat it.")
            
    
cupcake()
 