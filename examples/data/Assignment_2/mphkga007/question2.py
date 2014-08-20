print('Welcome to the 30 Second Rule Expert')
print('------------------------------------')
print('Answer the following questions by selecting from among the options.')
did_anyone_see_you=input("Did anyone see you? (yes/no)\n")
if did_anyone_see_you=="yes":
    who_was_it=input("Was it a boss/lover/parent? (yes/no)\n")
    if who_was_it=="yes":
        expensive=input("Was it expensive? (yes/no)\n")
        if  expensive=="yes":
            cut_it_off=input("Can you cut off the part that touched the floor? (yes/no)\n")
            if cut_it_off=="yes":
                print("Decision: Eat it.")
            elif cut_it_off=="no":
                print("Decision: Your call.")
        elif  expensive=="no":
            is_it_chocolate=input("Is it chocolate? (yes/no)\n") 
            if is_it_chocolate=="yes":
                print("Decision: Eat it.")
            elif is_it_chocolate=="no":
                print("Decision: Don't eat it.")
    elif  who_was_it=="no":
        print("Decision: Eat it.")
elif did_anyone_see_you=="no":
    sticky=input("Was it sticky? (yes/no)\n")
    if sticky=="yes":
        raw_steak=input("Is it a raw steak? (yes/no)\n")
        if raw_steak=="yes":
            puma=input("Are you a puma? (yes/no)\n")
            if puma=="yes":
                print("Decision: Eat it.")
            elif puma=="no":
                print("Decision: Don't eat it.")
        elif raw_steak=="no":
            cat=input("Did the cat lick it? (yes/no)\n")
            if cat=="yes":
                cat_healthy=input("Is your cat healthy? (yes/no)\n")
                if cat_healthy=="yes":
                    print("Decision: Eat it.")
                elif cat_healthy=="no":
                    print("Decision: Your call.")
            elif cat=="no":
                print("Decision: Eat it.")
                
            
    elif sticky=="no":
        emausaurus=input("Is it an Emausaurus? (yes/no)\n")
        if emausaurus=="yes":
            megalosaurus=input("Are you a Megalosaurus? (yes/no)\n")
            if megalosaurus=="yes":
                print("Decision: Eat it.")
            elif megalosaurus=="no":
                print("Decision: Don't eat it.")
        elif emausaurus=="no":
            cat=input("Did the cat lick it? (yes/no)\n")
            if cat=="yes":
                cat_healthy=input("Is your cat healthy? (yes/no)\n")
                if cat_healthy=="yes":
                    print("Decision: Eat it.")
                elif cat_healthy=="no":
                    print("Decision: Your call.")                 
            elif cat=="no":
                print("Decision: Eat it.")            
                     
                 
                
            
            
        
    
        