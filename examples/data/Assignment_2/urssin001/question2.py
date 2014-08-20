print("Welcome to the 30 Second Rule Expert\n------------------------------------")
print("Answer the following questions by selecting from among the options.")
yesno=input("Did anyone see you? (yes/no)\n")
if(yesno.lower()=="yes"):
    yesno=input("Was it a boss/lover/parent? (yes/no)\n")
    if(yesno.lower()=="yes"):
        yesno=input("Was it expensive? (yes/no)\n")
        if(yesno.lower()=="yes"):
            yesno=input("Can you cut off the part that touched the floor? (yes/no)\n")
            if(yesno.lower()=="yes"):
                print("Decision: Eat it.")
            elif(yesno.lower()=="no"):
                print("Decision: Your call.")           
        elif(yesno.lower()=="no"):
            yesno=input("Is it chocolate? (yes/no)\n")  
            if(yesno.lower()=="yes"):
                print("Decision: Eat it.")
            elif(yesno.lower()=="no"):
                print("Decision: Don't eat it.")           
    elif(yesno.lower()=="no"):
        print("Decision: Eat it.") 
elif(yesno.lower()=="no"):
    yesno=input("Was it sticky? (yes/no)\n")
    if(yesno.lower()=="yes"):
        yesno=input("Is it a raw steak? (yes/no)\n")    
        if(yesno.lower()=="yes"):
            yesno=input("Are you a puma? (yes/no)\n")
            if(yesno.lower()=="yes"):
                print("Decision: Eat it.")
            elif(yesno.lower()=="no"):
                print("Decision: Don't eat it.")        
        elif(yesno.lower()=="no"):
            yesno=input("Did the cat lick it? (yes/no)\n") 
            if(yesno.lower()=="yes"):
                yesno=input("Is your cat healthy? (yes/no)\n")
                if(yesno.lower()=="yes"):
                    print("Decision: Eat it.")
                elif(yesno.lower()=="no"):
                    print("Decision: Your call.")
                
            elif(yesno.lower()=="no"):
                print("Decision: Eat it.")
    elif(yesno.lower()=="no"):   
        yesno=input("Is it an Emausaurus? (yes/no)\n")
        if(yesno.lower()=="yes"):
            yesno=input("Are you a Megalosaurus? (yes/no)\n")
            if(yesno.lower()=="yes"):
                print("Decision: Eat it.")
            elif(yesno.lower()=="no"):
                print("Decision: Don't eat it.")                        
            
        elif(yesno.lower()=="no"):
            yesno=input("Did the cat lick it? (yes/no)\n") 
            if(yesno.lower()=="yes"):
                yesno=input("Is your cat healthy? (yes/no)\n")
                if(yesno.lower()=="yes"):
                    print("Decision: Eat it.")
                elif(yesno.lower()=="no"):
                    print("Decision: Your call.")
            elif(yesno.lower()=="no"):
                print("Decision: Eat it.")                    
            
        
                
            
            
        

        
                
            
else:
    print("")
    
