print("Welcome to the 30 Second Rule Expert")
print("------------------------------------")
print("Answer the following questions by selecting from among the options.")

choice = input("Did anyone see you? (yes/no)\n")
if choice=="yes":
    choiceA=input("Was it a boss/lover/parent? (yes/no)\n")
    if choiceA=="no":
        print("Decision: Eat it.\n")    
    elif choiceA=="yes" :
        choiceB=input("Was it expensive? (yes/no)\n")
        if choiceB=='yes' :
            choiceC=input("Can you cut off the part that touched the floor? (yes/no)\n")
            if choiceC=='yes':
                print("Decision: Eat it.\n")
            else:
                print("Decision: Your call.\n")
        else :
            choiceD=input("Is it chocolate? (yes/no)\n")                    
            if choiceD=='yes':
                print("Decision: Eat it.\n")
            else :
                    print("Decision: Don't eat it.\n")
else :
    choiceE=input("Was it sticky? (yes/no)\n")
    if choiceE=='yes':
        choiceF=input("Is it a raw steak? (yes/no)\n")
        if choiceF=='yes':
            choiceG=input("Are you a puma? (yes/no)\n")
            if choiceG=='yes':
                print("Decision: Eat it.\n")
            else :
                print("Decision: Don't eat it.\n")                
        if choiceF=='no':
            choiceH=input("Did the cat lick it? (yes/no)\n")
            if choiceH=='yes':
                choiceI=input("Is your cat healthy? (yes/no)\n")
                if choiceI=='yes':
                    print("Decision: Eat it.\n")
                else:
                    print("Decision: Your call.\n")
    else:
        choiceJ=input('Is it an Emausaurus? (yes/no)\n') 
        if choiceJ=='yes':
            choiceK=input('Are you a Megalosaurus? (yes/no)\n')
            if choiceK=='yes':
                    print("Decision: Eat it.\n")
            else:
                    print("Decision: Don't eat it.\n")    
        else:
            choiceL=input("Did the cat lick it? (yes/no)\n")
            if choiceL=='yes':
                choiceM=input("Is your cat healthy? (yes/no)\n")
                if choiceM=='yes':
                    print("Decision: Eat it.")
                else:
                    print("Decision: Your call.")
            else:
                print("Decision: Eat it.")
                    
                    
                        
                        
                
                
                    





    
    