# program to determine whether to eat food you dropped or not.
# Auther: Nangamso Mgoqi
# Date: 14 March 2014

print("Welcome to the 30 Second Rule Expert")
print("------------------------------------")
print("Answer the following questions by selecting from among the options.")
a = input("Did anyone see you? (yes/no)\n")
if(a == "yes"):
    a = input("Was it a boss/lover/parent? (yes/no)\n")
    if(a == "yes"):
        a = input("Was it expensive? (yes/no)\n")
        if(a == "yes"):
            a = input("Can you cut off the part that touched the floor? (yes/no)\n")
            if(a == "yes"):
                print("Decision: Eat it.")
            elif(a == "no"):
                print("Decision: Your call.")
        elif(a == "no"):
            a = input("Is it chocolate? (yes/no)\n")
            if(a == "yes"):
                print("Decision: Eat it.")
            elif(a == "no"):
                print("Decision: Don't eat it.")
    elif(a=="no"):
        print("Decision: Eat it.")
elif(a == "no"):
    a = input("Was it sticky? (yes/no)\n")
    if(a == "yes"):
        a = input("Is it a raw steak? (yes/no)\n")
        if(a == "yes"):
            a = input("Are you a puma? (yes/no)\n")
            if(a == "yes"):
                print("Decision: Eat it.")
            elif(a == "no"):
                print("Decision: Don't eat it.")
        elif(a == "no"):
            a = input("Did the cat lick it? (yes/no)\n")
            if(a == "no"):
                print("Decision: Eat it.")
            elif(a == "yes"):
                a = input("Is your cat healthy? (yes/no)\n")
                if(a == "no"):
                    print("Decision: Your call.")
                elif(a == "yes"):
                    print("Decision: Eat it.")
    elif(a == "no"):
        a = input("Is it an Emausaurus? (yes/no)\n")
        if(a == "no"):
            a = input("Did the cat lick it? (yes/no)\n")
            if(a == "no"):
                print("Decision: Eat it.")
            elif(a == "yes"):
                a = input("Is your cat healthy? (yes/no)\n")
                if(a == "no"):
                    print("Decision: Your call.")
                elif(a == "yes"):
                    print("Decision: Eat it.") 
        elif(a == "yes"):
            a = input("Are you a Megalosaurus? (yes/no)\n")
            if(a == "no"):
                print("Decision: Don't eat it.")
            elif(a == "yes"):
                print("Decision: Eat it.")
                
            
            
        
                
        
    
                
        
    
   
    