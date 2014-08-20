#30 second rule

def rule():
    y="yes"
    n="no"
    print("Welcome to the 30 Second Rule Expert")
    print("------------------------------------")
    
    print("Answer the following questions by selecting from among the options.")
    reply=input("Did anyone see you? (yes/no) \n")
    if reply==y:
        reply=input("Was it a boss/lover/parent? (yes/no) \n")
        if reply==y:
            reply1=input("Was it expensive? (yes/no) \n")
            if reply1==y:
                reply2=input("Can you cut off the part that touched the floor? (yes/no) \n")
                if reply2==y:
                    print("Decision: Eat it.")
                elif reply2==n:
                    print("Decision: Your call.")
                
            elif reply1==n:
                reply3=input("Is it chocolate? (yes/no) \n")
                if reply3==y:
                    print("Decision: Eat it.")
                elif reply3==n:
                    print("Decision: Don't eat it.")
                
                
        elif reply==n:
            print("Decision: Eat it.")
    

    elif reply==n:
        rep1=input("Was it sticky? (yes/no) \n")
        if rep1==y:
            rep2=input("Is it a raw steak? (yes/no) \n")
            if rep2==y:
                rep3=input("Are you a puma? (yes/no) \n")
                if rep3==y:
                    print("Decision: Eat it.")
                    
                elif rep3==n:
                    print("Decision: Don't eat it.")
                
            elif rep2==n:
                rep4=input("Did the cat lick it? (yes/no) \n")
                if rep4==y:
                    rep5=input("Is your cat healthy? (yes/no) \n")
                    if rep5==y:
                        print("Decision: Eat it.")
                    elif rep5==n:
                        print("Decision: Your call.")
                    
                
                elif rep4==n:
                    print("Decision: Eat it.")
            
        
        
        
        
        elif rep1==n:
            rep10=input("Is it an Emausaurus? (yes/no) \n")
            if rep10==y:
                rep11=input("Are you a Megalosaurus? (yes/no) \n")
                if rep11==y:
                    print("Decision: Eat it.")
                elif rep11==n:
                    print("Decision: Don't eat it.")
                    
                    
                    
            elif rep10==n:
                rep12=input("Did the cat lick it? (yes/no) \n")
                if rep12==y:
                    rep13=input("Is your cat healthy? (yes/no) \n")
                    if rep13==y:
                        print("Decision: Eat it.")
                    elif rep13==n:
                        print("Decision: Your call.")
               
               
                elif rep12==n:
                    print("Decision: Eat it.")
            
            
    
    
                
    
   
        
        
        
rule()       
        
                
                
                
 