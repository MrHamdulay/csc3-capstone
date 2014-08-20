print("Welcome to the 30 Second Rule Expert")
print("------------------------------------")
print('Answer the following questions by selecting from among the options.')
x=input('Did anyone see you? (yes/no)\n')
if(x=='yes'):
    y=input('Was it a boss/lover/parent? (yes/no)\n')
    if(y=='no'):
        print('Decision: Eat it.')
    else:
        z=input('Was it expensive? (yes/no)\n')
        if(z=='yes'):
            a=input('Can you cut off the part that touched the floor? (yes/no)\n')
            if(a=='no'):
                print('Decision: Your call.')
            else:
                print('Decision: Eat it.')
        else:
            b=input('Is it chocolate? (yes/no)\n')
            if(b=='yes'):
                print('Decision: Eat it.')
            else:
                print("Decision: Don't eat it.")
else:
    c=input('Was it sticky? (yes/no)\n')
    if(c=='yes'):
        d=input('Is it a raw steak? (yes/no)\n')
        if(d=='yes'):
            z=input('Are you a puma? (yes/no)\n')
            if(z=='no'):
                print("Decision: Don't eat it.")
            else:
                print('Decision: Eat it.')
        else:
            e=input('Did the cat lick it? (yes/no)\n')
            if(e=='no'):
                print('Decision: Eat it.')
            else:
                f=input('Is your cat healthy? (yes/no)\n')
                if(f=='no'):
                    print('Decision: Your call.')
                else:
                    print('Decision: Eat it.')
    else:
        g=input('Is it an Emausaurus? (yes/no)\n')
        if(g=='no'):
            h=input('Did the cat lick it? (yes/no)\n')
            if(h=='no'):
                print('Decision: Eat it.')
            else:
                j=input('Is your cat healthy? (yes/no)\n')
                if(j=='no'):
                    print('Decision: Your call.')
                else:
                    print('Decision: Eat it.')
        else:
            k=input('Are you a Megalosaurus? (yes/no)\n')
            if(k=='no'):
                print("Decision: Don't eat it.")
            else:
                print('Decision: Eat it.')