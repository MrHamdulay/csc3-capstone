print("Welcome to the 30 Second Rule Expert")
print("------------------------------------")
print("Answer the following questions by selecting from among the options.")
food= input("Did anyone see you? (yes/no) \n")
if food == "yes":
    food= input("Was it a boss/lover/parent? (yes/no) \n")
    if food == "yes":
        food= input("Was it expensive? (yes/no) \n")
        if food == "yes":
            food= input("Can you cut off the part that touched the floor? (yes/no) \n")
            if food == "yes":
                print("Decision: Eat it.")
            elif food == "no":
                print("Decision: Your call.")         
        elif food == "no" :
            food= input("Is it chocolate? (yes/no) \n")
            if food == "yes":
                print("Decision: Eat it.") 
            elif food== "no":
                print("Decision: Don't eat it.")
    elif food=="no":
        print("Decision: Eat it.")         
     
elif food=="no":
    food= input("Was it sticky? (yes/no) \n") 
    if food == "yes":
        food = input("Is it a raw steak? (yes/no) \n")
        if food == "yes":
            food = input("Are you a puma? (yes/no) \n")
            if food == "yes":
                print("Decision: Eat it.")
            elif food == "no":
                print("Decision: Don't eat it.") 
        elif food=="no":
            food = input("Did the cat lick it? (yes/no) \n")
            if food == "yes":
                food = input("Is your cat healthy? (yes/no) \n")
                if food == "yes":
                    print("Decision: Eat it.")
                elif food== "no":  
                    print("Decision: Your call.")
            elif food== "no": 
                print("Decision: Eat it.")                      
            
            
            
        elif food== "no":
            food = input("Did the cat lick it? (yes/no) \n")
            if food == "yes":
                food = input("Is your cat healthy? (yes/no) \n")
                if food == "yes":
                    print("Decision: Eat it.")
                elif food== "no":  
                    print("Decision: Your call.")
            elif food== "no":
                print("Decision: Eat it.")                                
    elif food== "no":
        food = input("Is it an Emausaurus? (yes/no) \n")
        if food == "yes":
            food = input("Are you a Megalosaurus? (yes/no) \n")
            if food == "yes":
                print("Decision: Eat it.")              
            elif food== "no":
                print("Decision: Don't eat it.")
            
                
        elif food== "no": 
            food = input("Did the cat lick it? (yes/no) \n")
            if food == "yes":
                            food = input("Is your cat healthy? (yes/no) \n")
                            if food == "yes":
                                print("Decision: Eat it.")
                            elif food== "no":  
                                print("Decision: Your call.")
            elif food== "no":
                print("Decision: Eat it.")              
            