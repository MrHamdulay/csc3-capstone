def main():
    print("Welcome to the 30 Second Rule Expert")
    print("-"*36,sep=" ")
    print("Answer the following questions by selecting from among the options.")
    See = input("Did anyone see you? (yes/no)\n")
    if See == "yes" :
        boss = input("Was it a boss/lover/parent? (yes/no)\n")            
        if boss == "yes":            
            exp = input("Was it expensive? (yes/no)\n") 
            if exp == "yes":
                cut = input("Can you cut off the part that touched the floor? (yes/no)\n")  
                if  cut == "yes":
                    print("Decision: Eat it.")    
                elif cut == "no":
                    print("Decision: Your call.")
            elif exp == "no":
                choc = input("Is it chocolate? (yes/no)\n")
                if   choc == "yes":
                    print("Decision: Eat it.")
                elif choc == "no":
                    print("Decision: Don't eat it.")
        elif boss == "no":
            print( "Decision: Eat it.") 
          
    elif See == "no":
        stick = input("Was it sticky? (yes/no)\n")
        if stick == "yes":
            raw = input("Is it a raw steak? (yes/no)\n")
            if raw == "yes":
                puma = input("Are you a puma? (yes/no)\n")
                if puma == "yes":
                    print("Decision: Eat it.")
                elif puma == "no":
                    print("Decision: Don't eat it.")
            elif raw == "no":
                lick = input("Did the cat lick it? (yes/no)\n")
                if lick == "yes":
                    heal = input("Is your cat healthy? (yes/no)\n")
                    if heal == "yes":
                        print("Decision: Eat it.")
                    elif heal == "no":
                        print("Decision: Your call.")
                elif lick == "no":
                    print("Decision: Eat it.")
        elif stick == "no":
            ema = input("Is it an Emausaurus? (yes/no)\n")
            if ema == "yes":
                mega = input("Are you a Megalosaurus? (yes/no)\n")
                if mega == "yes":
                    print("Decision: Eat it.")
                elif mega == "no":
                    print("Decision: Don't eat it.")
            elif ema == "no":
                lick = input("Did the cat lick it? (yes/no)\n")
                if lick == "yes":
                    heal = input("Is your cat healthy? (yes/no)\n")
                    if heal == "yes":
                        print("Decision: Eat it.")
                    elif heal == "no":
                        print("Decision: Your call.")
                elif lick == "no":
                    print("Decision: Eat it.")                
               
                    
                        
        
main()
            
            
        
    
    