print("Welcome to the 30 Second Rule Expert\n------------------------------------")
print("Answer the following questions by selecting from among the options.")

see = input("Did anyone see you? (yes/no)\n")

if see == "yes":
    lover = input("Was it a boss/lover/parent? (yes/no)\n")
    
    if lover == "yes":
        expensive = input("Was it expensive? (yes/no)\n") 
        
        if expensive == "yes":
            cut = input("Can you eat the part that touched the floor? (yes/no)\n")
            
            if cut == "yes":
                print("Decision: Eat it.")
                
            elif cut == "no":
                print("Decision: Your call.")
            
        elif expensive == "no":
            choc = input("Is it chocolate? (yes/no)\n")
            
            if choc == "yes":
                print("Decision: Eat it.")
                
            elif choc == "no":
                print("Decision: Don\'t eat it.")
        
    elif lover == "no":
        print("Decision: Eat it.")

elif see == "no":
    sticky = input("Was it sticky? (yes/no)\n")
    
    if sticky == "yes":
        steak = input("Is it a raw steak? (yes/no)\n")
        
        if steak == "yes":
            puma = input("Are you a puma? (yes/no)\n")
            
            if puma == "yes":
                print("Decision: Eat it.")
                
            elif puma == "no":
                print("Decision: Don\'t eat it.")
            
        elif steak == "no":
            cat = input("Did the cat lick it? (yes/no)\n")
            
            if cat == "yes":
                healthy = input("Is the cat healthy? (yes/no)\n")
                
                if healthy == "yes":
                    print ("Decision: Eat it.")
                    
                elif healthy == "no":
                    print ("Decision: Your call.")
                
            elif cat == "no":
                print ("Decision: Eat it.")
        
    elif sticky == "no":
        emausaurus = input("Is it an Emausaurus? (yes/no)\n")
        
        if emausaurus == "yes":
            mega = input("Are you a Megalosaurus?(yes/no)\n")
            
            if mega == "yes":
                print ("Decision: Eat it.")
                
            elif mega == "no":
                print ("Decision: Don\'t eat it.")
            
        elif emausaurus == "no":
            cat = input("Did the cat lick it? (yes/no)\n")
            
            if cat == "yes":
                healthy = input("Is the cat healthy? (yes/no)\n")
                
                if healthy == "yes":
                    print ("Decision: Eat it.")
                    
                elif healthy == "no":
                    print ("Decision: Your call.")
                
            elif cat == "no":
                print ("Decision: Eat it.")


            