#You dropped your cupcake on the ground-Question 2:Decision Tree

def cupcake():
    print("Welcome to the 30 Second Rule Expert")
    print("------------------------------------")
    print("Answer the following questions by selecting from among the options.")
    anyonesee=input("Did anyone see you? (yes/no)\n")        
    if anyonesee=="yes":
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
                cutpart=input("Can you cut off the part that touched the floor? (yes/no)\n")
                if cutpart=="yes":
                    print("Decision: Eat it.")
                elif cutpart=="no":
                    print("Decision: Your call.")
    if anyonesee=="no":
        sticky=input("Was it sticky? (yes/no)\n")
        if sticky=="no":
            emausauraus=input("Is it an Emausaurus? (yes/no)\n")
            if emausauraus=="no":
                catlick=input("Did the cat lick it? (yes/no)\n")
                if catlick=="no":
                    print("Decision: Eat it.")
                if catlick=="yes":
                    healthy=input("Is your cat healthy? (yes/no)\n")
                    if healthy=="no":
                        print("Decision: Your call.")
                    elif healthy=="yes":
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
                catlick=input("Did the cat lick it? (yes/no)\n")
                if catlick=="no":
                    print("Decision: Eat it.")
                if catlick=="yes":
                    healthy=input("Is your cat healthy? (yes/no)\n")
                    if healthy=="no":
                        print("Decision: Your call.")
                    elif healthy=="yes":
                        print("Decision: Eat it.")
            
    
cupcake()
 