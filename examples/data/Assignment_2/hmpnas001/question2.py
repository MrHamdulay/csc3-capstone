def main():
    print("Welcome to the 30 Second Rule Expert")
    print('-'*36)
    print("Answer the following questions by selecting from among the options.")
    v=input("Did anyone see you? (yes/no)\n")
    if (v=='yes'): 
        w=input("Was it a boss/lover/parent? (yes/no)\n")
        if w=='no':
            print("Decision: Eat it.")
        else:
            x=input("Was it expensive? (yes/no)\n")
            if x=='yes':
                y=input("Can you cut off the part that touched the floor? (yes/no)\n")
                if y=='yes':
                    print("Decision: Eat it.")            
                else:
                    print("Decision: Your call.")
            else:
                z=input("Is it chocolate? (yes/no)\n")
                if z=='yes':
                    print("Decision: Eat it.")
                else:
                    print("Decision: Don't eat it.")
    else:
        a=input("Was it sticky? (yes/no)\n")
        if a=='yes':
            b=input("Is it a raw steak? (yes/no)\n")
            if b=='yes':
                c=input("Are you a puma? (yes/no)\n")
                if c=='yes':
                    print("Decision: Eat it.")
                else:
                    print("Decision: Don't eat it.")
            else:
                d=input("Did the cat lick it? (yes/no)\n")
                if d=='no':
                    print("Decision: Eat it.")
                else:
                    e=input("Is your cat healthy? (yes/no)\n")
                    if e=='no':
                        print("Decision: Your call.")
                    else:
                        print("Decision: Eat it.")
                        
        else:
            f=input("Is it an Emausaurus? (yes/no)\n")
            if f=='no':
                g=input("Did the cat lick it? (yes/no)\n")
                if g=='no':
                    print("Decision: Eat it.")
                else:
                    h=input("Is your cat healthy? (yes/no)\n")
                    if h=='no':
                        print("Decision: Your call.")
                    else:
                        print("Decision: Eat it.") 
            else:
                j=input("Are you a Megalosaurus? (yes/no)\n")
                if j=='yes':
                    print("Decision: Eat it.")
                else:
                    print("Decision: Don't eat it.")
                    
main()