
print("Welcome to the 30 Second Rule Expert")

print("------------------------------------")

print("Answer the following questions by selecting from among the options.")


did=input("Did anyone see you? (yes/no) \n")
if(did=="yes"):
    did=input("Was it a boss/lover/parent? (yes/no) \n")
    if(did=="yes"):
        
        did=input("Was it expensive? (yes/no) \n")
        
        if(did=="yes"):
            did=input("Can you cut off the part that touched the floor? (yes/no) \n")
            if(did=="yes"):
                
                print("Decision: Eat it.")

            else:
            
                print("Decision: Your call.")
        
        else:
            did=input("Is it chocolate? (yes/no) \n")
            if(did=="yes"):
               
                print("Decision: Eat it.")
            else:
               
                print("Decision: Don't eat it.")
            
   
    else:
        print("Decision: Eat it.")
        
else:
    did=input("Was it sticky? (yes/no) \n")
    if(did=="yes"):

        did=input("Is it a raw steak? (yes/no) \n")
        
        if(did=="yes"):
            did=input("Are you a puma? (yes/no) \n")
          
            if(did=="yes"):
                print("Decision: Eat it.")

            else:
                print("Decision: Don't eat it.")

        else:
            did=input("Did the cat lick it? (yes/no) \n")

            if(did=="yes"):
                did=input("Is your cat healthy? (yes/no) \n")
                if(did=="yes"):
                    print("Decision: Eat it.")

                else:
                    print("Decision: Your call.")

            else:
                print("Decision: Eat it.")

    else:
        did=input("Is it an Emausaurus? (yes/no) \n")

        if(did=="yes"):
            did = input("Are you a Megalosaurus? (yes/no) \n")

            if(did =="yes"):
                print("Decision: Eat it.")
            else:
                print("Decision: Don't eat it.")

        else:
            did =input("Did the cat lick it? (yes/no) \n")

            if(did =="yes"):
                did=input("Is your cat healthy? (yes/no) \n")
                if(did =="yes"):
                    print("Decision: Eat it.")
                else:
                    print("Decision: Your call.")
            else:
                print("Decision: Eat it.")
        