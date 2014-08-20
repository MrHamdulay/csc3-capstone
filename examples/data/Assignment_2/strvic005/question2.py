#program to see if you should eat food that you've dropped

def food_floor():
    print("Welcome to the 30 Second Rule Expert")
    print("------------------------------------")
    print("Answer the following questions by selecting from among the options.")
    
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
                        print("Decision: Your call.")
                elif z=='no':
                    v=input("Is it chocolate? (yes/no)\n")
                    if v=='yes':
                        print("Decision: Eat it.")
                    elif v=='no':
                        print("Decision: Don't eat it.")
    elif x=='no':
        t=input("Was it sticky? (yes/no)\n")
        if t=='yes':
            a=input("Is it a raw steak? (yes/no)\n")
            if a=='yes':
                b=input("Are you a puma? (yes/no)\n")
                if b=='no':
                    print("Decision: Don't eat it.")
                elif b=='yes':
                    print("Decision: Eat it.")
            elif a=='no':
                c=input("Did the cat lick it? (yes/no)\n")
                if c=='yes':
                    d=input("Is your cat healthy? (yes/no)\n")
                    if d=='no':
                        print("Decision: Your call.")
                    elif d=='yes':
                        print("Decision: Eat it.")
                elif c=='no':
                    print("Decsion: Eat it.")
        elif t=='no':
            e=input("Is it an Emausaurus? (yes/no)\n")
            if e=='yes':
                f=input("Are you a Megalosaurus? (yes/no)\n")
                if f=='yes':
                    print("Decision: Eat it.")
                elif f=='no':
                    print("Decision: Don't eat it.")
            elif e=='no':
                g=input("Did the cat lick it? (yes/no)\n")
                if g=='yes':
                    h=input("Is your cat healthy? (yes/no)\n")
                    if h=='no':
                        print("Decision: Your call.")
                    elif h=='yes':
                        print("Decision: Eat it.")
                elif g=='no':
                        print("Decision: Eat it.")                
                
food_floor()
         
                        
        
    