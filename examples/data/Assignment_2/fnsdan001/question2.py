print("Welcome to the 30 Second Rule Expert \n------------------------------------ \nAnswer the following questions by selecting from among the options.")

see = input("Did anyone see you? (yes/no) \n")
if see == "yes":
    
    typa = input("Was it a boss/lover/parent? (yes/no) \n")
    if typa == "yes":
        expensive = input("Was it expensive? (yes/no)\n")
        
        if expensive == "yes":
            
                can = input("Can you cut off the part that touched the floor? (yes/no) \n")
                if can == "yes":
                    print("Decision: Eat it.")
                else:
                    print("Decision: Your call.")
        else:
            choc = input("Is it chocolate? (yes/no) \n")
            if choc == "yes":
                print("Decision: Eat it.")
            else:
                print("Decision: Don't eat it.")
    else:
        print("Decision: Eat it.")
       
            
                

else:
    sticky = input("Was it sticky? (yes/no) \n")
    if sticky == "yes":
        what = input("Is it a raw steak? (yes/no)\n")
        if what == "yes":
            you = input ("Are you a puma? (yes/no)\n")
            if you == "yes":
                print("Decision: Eat it.")
            else:
                print("Decision: Don't eat it.")
        else:
            cat = input("Did the cat lick it? (yes/no)\n")
                        
            if cat == "yes":
                clean = input("Is your cat healthy? (yes/no)\n")
                if clean == "yes":
                    print("Decision: Eat it.")
                else:
                    print("Decision: Your call.")
            else:
                print("Decision: Eat it.")            
            
            
    else:
        what = input("Is it an Emausaurus? (yes/no)\n")
        if what == "yes":
            dino = input("Are you a Megalosaurus? (yes/no) \n")
            if dino == "yes":
                print("Decision: Eat it.")
            else:
                print("Decision: Don't eat it.")
        else:
            cat = input("Did the cat lick it? (yes/no)\n")
            
            if cat == "yes":
                clean = input("Is your cat healthy? (yes/no)\n")
                if clean == "yes":
                    print("Decision: Eat it.")
                else:
                    print("Decision: Your call.")
            else:
                print("Decision: Eat it.")
        
