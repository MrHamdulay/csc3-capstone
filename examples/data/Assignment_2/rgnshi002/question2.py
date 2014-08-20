#Program to test if food is still edible after dropping it
#Shivam Ragoonaden
#9 March 2014

print("Welcome to the 30 Second Rule Expert")
print("------------------------------------")
print("Answer the following questions by selecting from among the options.")

Q = input("Did anyone see you? (yes/no)\n")
if Q == "yes":
    Q = input("Was it a boss/lover/parent? (yes/no)\n")
    if Q == "yes":
        Q = input("Was it expensive? (yes/no)\n")
        if Q == "yes":
            Q = input("Can you cut off the part that touched the floor? (yes/no)\n")
            if Q == "yes":
                print("Decision: Eat it.")
            else:
                    print("Decision: Your call.")
                    
    
            
        else:
            if Q == "no":
                Q = input("Is it chocolate? (yes/no)\n")
                if Q == "yes":
                    print("Decision: Eat it.")
                else:
                    print("Decision: Don't eat it.")
                    
    else: 
        if Q == "no":
            print("Decision: Eat it.")    
else:
    if Q == "no":
        Q = input("Was it sticky? (yes/no)\n")
        if Q == "yes":
            Q = input("Is it a raw steak? (yes/no)\n")
            if Q == "yes":
                Q = input("Are you a puma? (yes/no)\n")
                if Q == "yes":
                    print("Decision: Eat it.")
                else: 
                    print("Decision: Don't eat it.")
                    
            else:
                if Q == "no":
                    Q = input("Did the cat lick it? (yes/no)\n")
                    if Q == "yes":
                        Q = input("Is your cat healthy? (yes/no)\n")
                        if Q == "yes":
                            print("Decision: Eat it.")
                        else:
                            print("Decision: Your call.")    
                            
                    else:
                        if Q == "no":
                            print("Decision: Eat it.")

        else:
            if Q == "no":
                Q = input("Is it an Emausaurus? (yes/no)\n")
                if Q == "yes":
                    Q = input("Are you a Megalosaurus? (yes/no)\n")
                    if Q == "yes":
                        print("Decision: Eat it.")
                    else:
                        print("Decision: Don't eat it.")
                        
                else:
                    if Q == "no":
                        Q = input("Did the cat lick it? (yes/no)\n")
                        if Q == "yes":
                            Q = input("Is your cat healthy? (yes/no)\n")
                            if Q == "yes":
                                print("Decision: Eat it.")
                            else:
                                print("Decision: Your call.")
                                
                        else:
                            if Q == "no":
                                print("Decision: Eat it.")                        