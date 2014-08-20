def food_floor ():
    print ("Welcome to the 30 Second Rule Expert")
    print ("------------------------------------")
    print ("Answer the following questions by selecting from among the options.")
  
    x=input("Did anyone see you? (yes/no)\n")
    if x=='yes':
        y=input("Was it a boss/lover/parent? (yes/no)\n") 
        if y=='no':
            print("Decision: Eat it.")
        elif y=='yes':
            z=input("Was it expensive? (yes/no)\n")
            if z=='yes':
                w=input("Can you cut off the part that touched the floor? (yes/no)\n")
                if w=='yes':
                    print("Decision: Eat it.")
                elif w=='no':
                    print ("Decision: Your call.")
            elif z=='no':
                p=input("Is it chocolate? (yes/no)\n")
                if p=='yes':
                    print("Decision: Eat it.")
                elif p=='no':
                    print("Decision: Don't eat it.")
                    
    elif x=='no':
        v=input("Was it sticky? (yes/no)\n")
        if v=='yes':
            q=input("Is it a raw steak? (yes/no)\n")
            if q=='yes':
                d=input("Are you a puma? (yes/no)\n")
                if d=='yes':
                    print("Decision: Eat it.")
                elif d=='no':
                    print("Decision: Don't eat it.")
            elif q=='no':
                s=input("Did the cat lick it? (yes/no)\n")
                if s=='no':
                    print("Decision: Eat it.")
                elif s=='yes':
                    t=input("Is your cat healthy? (yes/no)\n")
                    if t=='no':
                        print("Decision: Your call.")
                    elif t=='yes':
                        print("Decision: Eat it.")
        elif v=='no':
            c=input("Is it an Emausaurus? (yes/no)\n")
            if c=='yes':
                e=input("Are you a Megalosaurus? (yes/no)\n")
                if e=='yes':
                    print("Decision: Eat it.")
                elif e=='no':
                    print("Decision: Don't eat it.")
            elif c=='no':
                g=input("Did the cat lick it? (yes/no)\n")
                if g=='yes':
                    k=input("Is your cat healthy? (yes/no)\n")
                    if k=='yes':
                        print("Decision: Eat it.")
                    elif k=='no':
                        print("Decision: Your call.")
                elif g=='no':
                    print("Decision: Eat it.")
food_floor ()
                    
                    
                    
            
                
            
            
                
                    
      
     
    