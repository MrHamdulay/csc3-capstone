def dropped_food():
    see=input("Did anyone see you? (yes/no) \n")
    if see=="no":
        sticky=input("Was it sticky? (yes/no) \n")
        if sticky=="no":
            Emausaurus=input("Is it an Emausaurus? (yes/no) \n")
            if Emausaurus=="yes":
                megalo=input("Are you a Megalosaurus? (yes/no) \n")
                if megalo=="yes":
                    print("Decision: Eat it.")
                else:
                    if megalo=="no":
                        print("Decision: Don't eat it.")
            else:
                if Emausaurus=="no":
                    cat=input("Did the cat lick it? (yes/no) \n")
                    if cat=="yes":
                        health=input("Is your cat healthy? (yes/no) \n")
                        if health=="yes":
                            print("Decision: Eat it.")
                        else:
                            if health=="no":
                                print("Decision: Your call.")
                    else:
                        if cat=="no":
                            print("Decision: Eat it.")
        if sticky=="yes":
            steak=input("Is it a raw steak? (yes/no) \n")
            if steak=="no":
                cat=input("Did the cat lick it? (yes/no) \n")
                if cat=="no":
                    print("Decision: Eat it.")
                else:
                    if cat=="yes":
                        health=input("Is your cat healthy? (yes/no) \n")
                        if health=="yes":
                            print("Decision: Eat it.")
                        else:
                            if health=="no":
                                print("Decision: Your call.")
            else:
                if steak=="yes":
                    puma=input("Are you a puma? (yes/no) \n")
                    if puma=="yes":
                        print("Decision: Eat it.")
                    else:
                        print("Decision: Don't eat it.")

    else:
        if see=="yes":
            who=input("Was it a boss/lover/parent? (yes/no) \n")
            if who=="no":
                print("Decision: Eat it.")
            else:
                    expense=input("Was it expensive? (yes/no)\n")
                    if expense=="no":
                        chocolate=input("Is it chocolate? (yes/no) \n")
                        if chocolate=="no":
                            print("Decision: Don't eat it.")
                        else:
                            if chocolate=="yes":
                                print("Decision: Eat it.")
                    else:
                        if expense=="yes":
                            cut=input("Can you cut off the part that touched the floor? (yes/no) \n")
                            if cut=="yes":
                                print("Decision: Eat it.")
                            else:
                                if cut=="no":
                                    print("Decision: Your call.")
print("Welcome to the 30 Second Rule Expert")
print("------------------------------------")
print("Answer the following questions by selecting from among the options.")
dropped_food()
            
                            
                            
                            
                        
                            
                
             
             
                          
                       
                         
                    
                    
                
                    
        
                    

    
    
    