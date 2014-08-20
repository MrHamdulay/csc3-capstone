print("Welcome to the 30 Second Rule Expert")
print("------------------------------------")
print("Answer the following questions by selecting from among the options.")
x=input("Did anyone see you? (yes/no)" '\n')
if (x=='yes'):
    who=input("Was it a boss/lover/parent? (yes/no)"'\n')
    if (who=='no'):
                print("Decision: Eat it.")      
    else: 
        price=input("Was it expensive? (yes/no)" '\n')
        if (price== 'yes'):
            cut=input("Can you cut off the part that touched the floor? (yes/no)" '\n') 
            if (cut== 'yes'):
                print("Decision: Eat it.")
            else:
                print("Decision: Your call.") 
        else:
            choc=input("Is it chocolate? (yes/no)"'\n')
            if (choc=='yes'):
                print("Decision: Eat it.")
            else:    
                print("Decision: Don't eat it.")     
else:
    stick=input("Was it sticky? (yes/no)"'\n')
    if (stick=='yes'):
        steak=input("Is it a raw steak? (yes/no)"'\n')
   
        
        if (steak== 'yes'):
            puma=input("Are you a puma? (yes/no)"'\n')
            if (puma=='yes'):
                print("Decision: Eat it.")
            else:
                print("Decision: Don't eat it.")
        else:
            cat=input("Did the cat lick it? (yes/no)"'\n')
            if (cat=='yes'):
                health=input("Is your cat healthy? (yes/no)"'\n')
                if (health=='yes'):
                    print("Decision: Eat it.")
            else:
                print("Decision: Eat it.")
    else:
        ema=input("Is it an Emausaurus? (yes/no)"'\n')
        if (ema=='yes'):
            mega=input("Are you a Megalosaurus? (yes/no)"'\n')
            if (mega== 'yes'):
                print("Decision: Eat it.")
            else:
                print("Decision: Don't eat it.")
        else:
            cats=input("Did the cat lick it? (yes/no)"'\n')
            if (cats=='yes'):
                healthy=input("Is your cat healthy? (yes/no)"'\n')
                if (healthy== 'yes'):
                    print("Decision: Eat it.")
                else:
                    print("Decision: Your call.")
            else:
                print("Decision: Eat it.")
                       
           
           
   
           