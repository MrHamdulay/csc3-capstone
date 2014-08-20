print("Welcome to the 30 Second Rule Expert")
print("------------------------------------")
print("Answer the following questions by selecting from among the options.")
eat='Eat it.'
u='Your call.'
dont="Don't eat it."
see= input("Did anyone see you? (yes/no)\n")
if see=='yes':
    who=input("Was it a boss/lover/parent? (yes/no)\n")
    if who=='yes':
        cost=input("Was it expensive? (yes/no)\n")
        if cost=='yes':
            cut=input("Can you cut off the part that touched the floor? (yes/no)\n")
            if cut=='yes':
                print("Decision:",eat)
                
            else:
                print("Decision:",u)
        else:
            choc=input("Is it chocolate? (yes/no)\n")
            if choc=='yes':
                print("Decision:",eat)
            else:
                print("Decision:",dont)
        
    else: 
        print("Decision:",eat)
    
else:
    sticky=input("Was it sticky? (yes/no)\n")
    if sticky=='yes':
        steak=input("Is it a raw steak? (yes/no)\n")
        if steak=='yes':
            puma=input("Are you a puma? (yes/no)\n")
            if puma =='yes':
                print("Decision:",eat)
            else:
                print("Decision:",dont)
        else:
            cat=input("Did the cat lick it? (yes/no)\n")
            if cat=='yes':
                health=input("Is your cat healthy? (yes/no)\n")
                if health=='yes':
                    print("Decision:",eat)
                else:
                    print("Decision:",u)
            else:
                print("Decision:",eat)
    else:
        e=input("Is it an Emausaurus? (yes/no)\n")
        if e=='yes':
            meg=input("Are you a Megalosaurus? (yes/no)\n")
            if meg=='yes':
                print("Decision:",eat)
            else:
                print("Decision:",dont)
        else:
            cat=input("Did the cat lick it? (yes/no)\n")
            if cat=='yes':
                health=input("Is your cat healthy? (yes/no)\n")
                if health=='yes':
                    print("Decision:",eat)
                else:
                    print("Decision:",u)
            else:
                print("Decision:",eat)            