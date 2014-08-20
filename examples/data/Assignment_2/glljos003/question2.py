print("Welcome to the 30 Second Rule Expert")
print("------------------------------------")
print("Answer the following questions by selecting from among the options.")

answer=input("Did anyone see you? (yes/no)\n")  

if (answer=="yes"): 
    A=input("Was it a boss/lover/parent? (yes/no)\n")  
    if(A=="no"):
        print("Decision: Eat it.")
    elif(A=="yes"):
        A=input("Was it expensive? (yes/no)\n")
        if(A=="yes"):
            A=input("Can you cut off the part that touched the floor? (yes/no)\n")
            if(A=="yes"):
                print("Decision: Eat it.")
            elif(A=="no"):
                print("Decision: Your call.")
        elif(A=="no"):
            A=input("Is it chocolate? (yes/no)\n")
            if(A=="yes"):
                print("Decision: Eat it.")
            elif(A=="no"):
                print("Decision: Don't eat it.")
elif(answer=="no"):
    B=input("Was it sticky? (yes/no)\n")
    if(B=="yes"):
        B=input("Is it a raw steak? (yes/no)\n")
        if(B=="yes"):
            B=input("Are you a puma? (yes/no)\n")
            if(B=="yes"):
                print("Decision: Eat it.")
            elif(B=="no"):
                print("Decision: Don't eat it.")
        elif(B=="no"):
            B=input("Did the cat lick it? (yes/no)\n")
            if(B=="yes"):
                B=input("Is your cat healthy? (yes/no)\n")
                if(B=="yes"):
                    print("Decision: Eat it.")
                elif(B=="no"):
                    print("Decision: Your call.")
            elif(B=="no"):
                print("Eat it.")
    elif(B=="no"):
        B=input("Is it an Emausaurus? (yes/no)\n")
        if(B=="yes"):
            B=input("Are you a Megalosaurus? (yes/no)\n")
            if(B=="yes"):
                print("Decision: Eat it.")
            elif(B=="no"):
                print("Decision: Don't eat it.")
        elif(B=="no"):
            B=input("Did the cat lick it? (yes/no)\n")
            if(B=="yes"):
                B=input("Is your cat healthy? (yes/no)\n")
                if(B=="yes"):
                    print("Decision: Eat it.")
                elif(B=="no"):
                    print("Decision: Your call.")
            elif(B=="no"):
                print("Decision: Eat it.")            
                
    
        
        
        
    
