print("Welcome to the 30 Second Rule Expert")
print("------------------------------------")
print("Answer the following questions by selecting from among the options.")
ans1 = input("Did anyone see you? (yes/no) \n")
if ans1 == "yes":
    a1 = input("Was it a boss/lover/parent? (yes/no) \n")
    
    if a1 == "yes":
        a2 = input("Was it expensive? (yes/no) \n")
        if a2 == "yes":
            a3 = input("Can you cut off the part that touched the floor? (yes/no) \n")
                        
            if a3 == "yes":
                print("Decision: Eat it.")
            elif a3 == "no":
                print("Decision: Your call.")            
            
        elif a2 == "no":
            a4 = input("Is it chocolate? (yes/no) \n")
            
            if a4 == "yes":
                print("Decision: Eat it.")
            elif a4 == "no":
                print("Decision: Don't eat it.")
            
                
                

    elif a1 == "no":
        print("Decision: Eat it.")

    
elif ans1 == "no":
    b1 = input("Was it sticky? (yes/no) \n")
    
    if b1 == "yes":
        b2 = input("Is it a raw steak? (yes/no) \n")
        
        if b2 == "yes":
            b3 = input("Are you a puma? (yes/no) \n")
            
            if b3 == "yes":
                print("Decision: Eat it.")
                
            elif b3 == "no":
                print("Decision: Don't eat it.")
            
        elif b2 == "no":
            b4 = input("Did the cat lick it? (yes/no) \n")
            
            if b4 == "no":
                print("Decision: Eat it.")
            elif b4 == "yes":
                b5 = input("Is your cat healthy? (yes/no) \n")
                
                if b5 == "yes":
                    print("Decision: Eat it.")
                    
                elif b5 == "no":
                    print("Decision: Your call.")
                    
                
        
    
    elif b1 == "no":
        b6 = input("Is it an Emausaurus? (yes/no) \n")
        
        if b6 == "yes":
            b7 = input("Are you a Megalosaurus? (yes/no) \n")
            
            if b7 == "yes":
                print("Decision: Eat it.")
                
            elif b7 == "no":
                print("Decision: Don't eat it.")
            
        elif b6 == "no":
            b8 = input("Did the cat lick it? (yes/no) \n")
            
            if b8 == "no":
                print("Decision: Eat it.")
                
            elif b8 == "yes":
                b9 = input("Is your cat healthy? (yes/no) \n")
                
                if b9 == "yes":
                    print("Decision: Eat it.")
                    
                elif b9 == "no":
                     print("Decision: Your call.")
                    
            
        
        