print("Welcome to the 30 Second Rule Expert")
print("------------------------------------")
print("Answer the following questions by selecting from among the options.")



choice1=input("Did anyone see you? (yes/no) \n")
if choice1=="yes":
    choice2=input("Was it a boss/lover/parent? (yes/no) \n") 
    if choice2=="yes":
        choice3=input("Was it expensive? (yes/no) \n")
        if choice3=="yes":
            choice4=input("Can you cut off the part that touched the floor? (yes/no) \n")
            if choice4 == "yes":
                print("Decision: Eat it.")
            else:
                    print("Decision: Your call.")        
        else:
            choice10=input("Is it chocolate? (yes/no) \n")
            if choice10=="yes":
                print("Decision: Eat it.")
            else:
                print("Decision: Don't eat it.")
                                
    if choice2=="no":
        print("Decision: Eat it.")
        
if choice1=="no":
    choice5=input("Was it sticky? (yes/no) \n")
    if choice5=="yes":
        choice6=input("Is it a raw steak? (yes/no) \n")
        if choice6=="yes":
                choice7=input("Are you a puma? (yes/no) \n")   
                
                if choice7=="yes":
                    print("Decision: Eat it.") 
                else:
                    print("Decision: Don't eat it.")
        else: 
            choice8=input("Did the cat lick it? (yes/no) \n")
              
            if choice8=="no":
                print("Decision: Eat it.")
            else:
                choice9=input("Is your cat healthy? (yes/no) \n")
                if choice9=="yes":
                    print("Decision: Eat it.")
                else:
                    print("Decision: Your call.")
            
        
             
                   
    if choice5=="no":
        choice11=input("Is it an Emausaurus? (yes/no) \n")
        if choice11=="yes":
            choice12=input("Are you a Megalosaurus? (yes/no) \n")
            if choice12=="yes":
                print("Decision: Eat it.")
            else:
                print("Decision: Don't eat it.") 
                
        if choice11=="no":
            choice8=input("Did the cat lick it? (yes/no) \n")
              
            if choice8=="no":
                print("Decision: Eat it.")
            else:
                choice9=input("Is your cat healthy? (yes/no) \n")
                if choice9=="yes":
                    print("Decision: Eat it.")
                else:
                    print("Decision: Your call.")

                
                
            
            
                    
            
        

                
                
            
           
