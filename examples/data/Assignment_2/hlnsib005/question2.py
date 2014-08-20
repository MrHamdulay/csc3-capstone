print("Welcome to the 30 Second Rule Expert")
print("------------------------------------")
print("Answer the following questions by selecting from among the options.")

Start= input("Did anyone see you? (yes/no)\n")
if Start=="yes":
    AnswerThird=input("Was it a boss/lover/parent? (yes/no) \n")
    #option yes stream
    if AnswerThird=="yes":
        Expensive=input("Was it expensive? (yes/no)\n")
        if Expensive=="yes":
            Cut=input("Can you cut off the part that touched the floor? (yes/no)\n")
            if Cut=="yes":
                print("Decision: Eat it.")
            else:
                print("Decision: Your call.")
        else:
            Chocolate=input("Is it chocolate? (yes/no)\n")
            if Chocolate=="yes":
                print("Decision: Eat it.")
            else:
                print("Decision: Don't eat it.")
    if AnswerThird=="no":
        print("Decision: Eat it.")

if Start=="no":
    Sticky=input("Was it sticky? (yes/no)\n")
    #no stream
    if Sticky=="no":
        Emausaurus=input("Is it an Emausaurus? (yes/no)\n")
        if Emausaurus=="yes":
            Megalosaurus=input("Are you a Megalosaurus? (yes/no)\n")
            if Megalosaurus=="yes":
                print("Decision: Eat it.")
            else:
                    print("Decision: Don't eat it.")
        else: 
            cat2=input("Did the cat lick it? (yes/no)\n")
            if cat2=="no":
                print("Decision: Eat it.")
            else:
                Healthy=input("Is your cat healthy? (yes/no)\n")
                if Healthy=="yes":
                    print("Decision: Eat it.")
                else:
                    print("Decision: Your call.")
            
        
    else: 
        Steak=input("Is it a raw steak? (yes/no)\n")
        if Steak=="no":
            Cat=input("Did the cat lick it? (yes/no)\n")
            if Cat=="no":
                print("Decision: Eat it.")
            else:
                Healthy=input("Is your cat healthy? (yes/no)\n")
                if Healthy=="yes":
                    print("Decision: Eat it.")
                else:
                    print("Decision: Your call.")
        else:
            Puma=input("Are you a puma? (yes/no)\n")
            if Puma=="no":
                print("Decision: Don't eat it.")
            else:
                print("Decision: Eat it.")
             
        
    
    
     
    



#Answer2= input("Was it a boss/lover/parent? (yes/no)\n")
#Answer3= input("Was it expensive? (yes/no)\n")
#Answer4= input("Can you cut off the part that touched the floor? (yes/no)\n")

