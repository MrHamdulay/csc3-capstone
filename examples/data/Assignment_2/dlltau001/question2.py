#question 2
#Author : Tauriq Dolley

print("Welcome to the 30 Second Rule Expert")
print("-"*36)
print("Answer the following questions by selecting from among the options.")


see = input("Did anyone see you? (yes/no)\n")

if see == "yes":
    
    boss = input("Was it a boss/lover/parent? (yes/no)\n")
    
    if boss == "no" :
        
        print("Decision: Eat it.")        
        
    
    elif boss == "yes":
           
        expensive = input("Was it expensive? (yes/no)\n")
        
        if expensive == "yes" :
            floor = input("Can you cut off the part that touched the floor? (yes/no)\n")
            if floor == "yes":
                print("Decision: Eat it.")
            elif floor == "no":
                print("Decision: Your call.")
                
        elif expensive == "no":
            
            chocolate = input("Is it chocolate? (yes/no)\n")
            
            if chocolate == "yes":
                print("Decision: Eat it.")
               
                
            elif chocolate == "no":
                print("Decision: Don't eat it.")

elif see == "no":
    
    sticky = input("Was it sticky? (yes/no)\n")    
    if sticky == 'yes': #yes it was sticky       
        raw = input("Is it a raw steak? (yes/no)\n")       
        
        if raw == 'no': #no it isn't a raw steak           
            cat = input("Did the cat lick it? (yes/no)\n")
            if cat == 'no':
                print("Decision: Eat it.")
               
                
            elif cat == 'yes':
                healthycat = input("Is your cat healthy? (yes/no)\n")
                
                if healthycat == 'yes':
                    print("Decision: Eat it.")
                   
                
                elif healthycat == 'no':
                    print("Decision: Your call.")
        
        elif raw == 'yes':
            
            puma = input("Are you a puma? (yes/no)\n")

            if puma == 'yes':
                print("Decision: Eat it.")
               

            elif puma == 'no':
                print("Decision: Don't eat it.")
               
                
    elif sticky == 'no': #no it wasn't sticky     
       
        emasaurus = input("Is it an Emausaurus? (yes/no)\n")      

        if emasaurus == 'yes':
            
            megalosaurus = input("Are you a Megalosaurus? (yes/no)\n")
            
            if megalosaurus == "yes":
                print("Decision: Eat it.")
               
            
            elif megalosaurus == "no":
                print("Decision: Don't eat it.")
               
      
        elif emasaurus == 'no':
           
            cat = input("Did the cat lick it? (yes/no)\n")

            if cat == 'no':
                print("Decision: Eat it.")
               
           
            elif cat == 'yes':
                
                healthycat = input("Is your cat healthy? (yes/no)\n")
               
                if healthycat == 'yes':
                    print("Decision: Eat it.")
                 
                elif healthycat == 'no':
                    print("Decision: Your call.")
                  # 
            