#dropped food on flour, eat or not
def decision():
    print("Welcome to the 30 Second Rule Expert")
    print("------------------------------------")
    print("Answer the following questions by selecting from among the options.")
    x=input("Did anyone see you? (yes/no)\n")
    if (x=='yes'):
        y=input("Was it a boss/lover/parent? (yes/no)\n")
        if (y=='no'):
            print('Decision: Eat it.')
        elif (y=='yes'):
            r=input("Was it expensive? (yes/no)\n")
            if (r=='yes'):
                s=input("Can you cut off the part that touched the floor? (yes/no)\n")
                if (s=='no'):
                    print('Decision: Your call.')
                elif (s=='yes'):
                    print('Decision: Eat it.')
            elif (r=='no'):
                t=input("Is it chocolate? (yes/no)\n")
                if (t=='yes'):
                    print('Decision: Eat it.')
                elif (t=='no'):
                    print("Decision: Don't eat it.")
    elif (x=='no'):
        u=input("Was it sticky? (yes/no)\n")
        if (u=='yes'):
            v=input("Is it a raw steak? (yes/no)\n")
            if (v=='yes'):
                w=input("Are you a puma? (yes/no)\n")
                if (w=='no'):
                    print("Decision: Don't eat it.")
                elif (w=='yes'):
                    print("Decision: Eat it.")
            elif (v=='no'):
                a=input("Did the cat lick it? (yes/no)\n")
                if (a=='no'):
                    print("Decision: Eat it.")
                elif (a=='yes'):
                    b=input("Is your cat healthy? (yes/no)\n")
                    if (b=='no'):
                        print("Decision: Your call.")
                    elif (b=='yes'):
                        print("Decision: Eat it.")
        elif (u=='no'):
            c=input("Is it an Emausaurus? (yes/no)\n")
            if (c=='yes'):
                d=input("Are you a Megalosaurus? (yes/no)\n")
                if (d=='no'):
                    print("Decision: Don't eat it.")
                elif (d=='yes'):
                    print("Decision: Eat it.")
            elif (c=='no'):
                a=input("Did the cat lick it? (yes/no)\n")
                if (a=='no'):
                    print("Decision: Eat it.")
                elif (a=='yes'):
                    b=input("Is your cat healthy? (yes/no)\n")
                    if (b=='no'):
                        print("Decision: Your call.")
                    elif (b=='yes'):
                        print("Decision: Eat it.")                    
decision()
