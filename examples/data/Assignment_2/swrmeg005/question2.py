print("Welcome to the 30 Second Rule Expert")
print('------------------------------------')
print("Answer the following questions by selecting from among the options.")
print("Did anyone see you? (yes/no)")
a=input()
if a== 'yes':
    print("Was it a boss/lover/parent? (yes/no)")
    b=input()
    if b=='yes':
        print("Was it expensive? (yes/no)")
        c=input()
        if c=='yes':
            print("Can you cut off the part that touched the floor? (yes/no)")
            d=input()
            if d=='yes':
                print("Decision: Eat it.")
            else:
               print("Decision: Your call.")
     
        else:
            print("Is it chocolate? (yes/no)")
            e=input()
            if e=='yes':
                print("Decision: Eat it.")
            else:
                print("Decision: Don't eat it.")
    else:
        print("Decision: Eat it.")
else:
    print("Was it sticky? (yes/no)")
    f=input()
    if f=='yes':
        print("Is it a raw steak? (yes/no)")
        g=input()
        if g=='yes':
            print("Are you a puma? (yes/no)")
            h=input()
            if h=='yes':
                print("Decision: Eat it.")
            else:
                print("Decision: Don't eat it.")
        else:
            print("Did the cat lick it? (yes/no)")
            i=input()
            if i=='yes':
                print("Is your cat healthy? (yes/no)")
                j=input()
                if j=='yes':
                    print("Decision: Eat it.")
                else:
                    print("Decision: Your call.")
            else:
                print("Decision: Don't eat it.")
    else:
        print("Is it an Emausaurus? (yes/no)")
        k=input()
        if k =='yes':
            print("Are you a Megalosaurus? (yes/no)")
            l=input()
            if l=='yes':
                print("Decision: Eat it.")
            else:
                print("Decision: Don't eat it.")
        else:
            print("Did the cat lick it? (yes/no)")
            m=input()
            if m=='yes':
                print("Is your cat healthy? (yes/no)")
                n=input()
                if n=='no':
                    print("Decision: Your call.")
                else:
                    print("Decision: Eat it.")
            else:
                print("Decision: Eat it.")