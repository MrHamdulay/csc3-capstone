print ("Welcome to the 30 Second Rule Expert")
print ("------------------------------------")
print ("Answer the following questions by selecting from among the options.")
yn = input("Did anyone see you? (yes/no)\n")
if yn == 'yes':
    yn = input("Was it a boss/lover/parent? (yes/no)\n")
    if yn == "no":
        print("Decision: Eat it.")
    else:
        yn = input("Was it expensive? (yes/no)\n")
        if yn == 'yes':
            yn = input("Can you cut off the part that touched the floor? (yes/no)\n")
            if yn == 'yes':
                print("Decision: Eat it.")
            else:
                print("Decision: Your call.")
                
            
        else:
            yn = input("Is it chocolate? (yes/no)\n")
            if yn == 'yes':
                print("Decision: Eat it.")
            else:
                print("Decision: Don't eat it.")
             
else:
    yn=input("Was it sticky? (yes/no)\n")
    if yn == 'yes':
        yn=input("Is it a raw steak? (yes/no)\n")
        if yn == 'yes':
            yn = input("Are you a puma? (yes/no)\n")
            if yn == 'yes':
                print("Decision: Eat it.")
            else:
                print ("Decision: Don't eat it.")
        else:
            yn=input("Did the cat lick it? (yes/no)\n")
            if yn == 'yes':
                yn = input("Is your cat healthy? (yes/no)\n")
                if yn == 'yes':
                    print ("Decision: Eat it.")
                else:
                    print("Decision: Your call.")
            else:
                print("Decision: Eat it.")
            
        
    else:
        yn= input("Is it an Emausaurus? (yes/no)\n")
        if yn == 'yes':
            yn= input("Are you a Megalosaurus? (yes/no)\n")
            if yn == 'yes':
                print ("Decision: Eat it.")
            else:
                print ("Decision: Don't eat it.")
        else:
            yn=input("Did the cat lick it? (yes/no)\n")
            if yn == 'yes':
                yn = input("Is your cat healthy? (yes/no)\n")
                if yn =='yes':
                    print("Decision: Eat it.")
                else:
                    print("Decision: Your call.")
            else:
                print ("Decision: Eat it.")
        
    