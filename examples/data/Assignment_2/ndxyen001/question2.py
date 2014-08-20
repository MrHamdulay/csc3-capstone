print("Welcome to the 30 Second Rule Expert")
print("------------------------------------")
print("Answer the following questions by selecting from among the options.")
Answer = input("Did anyone see you? (yes/no)\n")
if( Answer == "yes"):
    Answer = input("Was it a boss/lover/parent? (yes/no)\n")
    if(Answer == "yes"):
        Answer = input("Was it expensive? (yes/no)\n")
        if(Answer == "yes"):
            Answer = input("Can you cut off the part that touched the floor? (yes/no)\n")
            if(Answer == "yes"):
                print("Decision: Eat it.")
            elif(Answer == "no"):         
                print("Decision: Your call.")
        elif(Answer == "no"):
            Answer =input("Is it chocolate? (yes/no)\n")
            if(Answer == "yes"):
                print("Decision: Eat it.")
            elif(Answer == "no"):
                print("Decision: Don't eat it.")
    elif(Answer == "no"):
        print("Decision: Eat it.")
elif(Answer == "no"):
    Answer =input("Was it sticky? (yes/no)\n") 
    if(Answer == "yes"):
        Answer =input("Is it a raw steak? (yes/no)\n")
        if(Answer== "yes"):
            Answer =input("Are you a puma? (yes/no)\n")
            if(Answer == "yes"):
                print("Decision: Eat it.")
            elif(Answer == "no"):
                print("Decision: Don't eat it.")
        elif(Answer == "no"):
            Answer =input("Did the cat lick it? (yes/no)\n")
            if(Answer== "yes"):
                Answer =input("Is your cat healthy? (yes/no)\n")
                if(Answer == "yes"):
                    print("Decision: Eat it.")
                elif(Answer  == "no"):
                    print("Decision: Your call.")
            elif(Answer == "no"):
                print("Decision: Eat it.")           
    elif(Answer == "no"):
        Answer = input("Is it an Emausaurus? (yes/no)\n")       
        if(Answer == "yes"):
            Answer = input("Are you a Megalosaurus? (yes/no)\n")            
            if(Answer == "yes"):
                print("Decision: Eat it.")
            elif(Answer == "no"):
                print("Decision: Don't eat it.")
        elif(Answer == "no"):
            Answer = input("Did the cat lick it? (yes/no)\n")
            if(Answer == "yes"):
                Answer = input("Is your cat healthy? (yes/no)\n")
                if(Answer == "yes"):
                    print("Decision: Eat it.")
                elif(Answer == "no"):
                    print("Decision: Your call.")
            elif(Answer == "no"):
                print("Decision: Eat it.")           


                