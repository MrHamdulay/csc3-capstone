print("Welcome to the 30 Second Rule Expert")
print("------------------------------------")
print("Answer the following questions by selecting from among the options.")
see=input("Did anyone see you? (yes/no)\n")
if (see=="yes"):
    who=input("Was it a boss/lover/parent? (yes/no)\n")
    if (who=="no"):
        print("Decision: Eat it.")
    if (who=="yes"):
        expensive=input("Was it expensive? (yes/no)\n")
        if (expensive=="no"):
            chocolate=input("Is it chocolate? (yes/no)\n")
            if (chocolate=="no"):
                print("Decision: Don't eat it.")
            if (chocolate=="yes"):
                print("Decision: Eat it.")
        if (expensive=="yes"):
            cut=input("Can you cut off the part that touched the floor? (yes/no)\n")
            if (cut=="yes"):
                print("Decision: Eat it.")
            if (cut=="no"):
                print("Decision: Your call.")
if (see=="no"):
    sticky=input("Was it sticky? (yes/no)\n")
    if (sticky=="yes"):
        steak=input("Is it a raw steak? (yes/no)\n")
        if (steak=="yes"):
            puma=input("Are you a puma? (yes/no)\n")
            if (puma=="yes"):
                print("Decision: Eat it.")
            if (puma=="no"):
                print("Decision: Don't eat it.")
        if (steak=="no"):
            lick=input("Did the cat lick it? (yes/no)\n")
            if (lick=="no"):
                print("Decision: Eat it.")
            if (lick=="yes"):
                healthy=input("Is your cat healthy? (yes/no)\n")
                if (healthy=="yes"):
                    print("Decision: Eat it.")
                if (healthy=="no"):
                    print("Decision: Your call.")
    if (sticky=="no"):
        emausaurus=input("Is it an Emausaurus? (yes/no)\n")
        if (emausaurus=="no"):
            lick=input("Did the cat lick it? (yes/no)\n")
            if (lick=="no"):
                print("Decision: Eat it.")
            if (lick=="yes"):
                healthy=input("Is your cat healthy? (yes/no)\n")
                if (healthy=="yes"):
                    print("Decision: Eat it.")
                if (healthy=="no"):
                    print("Decision: Your call.")
        if (emausaurus=="yes"):
            megalosaurus=input("Are you a Megalosaurus? (yes/no)\n")
            if (megalosaurus=="yes"):
                print("Decision: Eat it.")
            if (megalosaurus=="no"):
                print("Decision: Don't eat it.")
            
            
            
    
        
            
        
        
        
    

