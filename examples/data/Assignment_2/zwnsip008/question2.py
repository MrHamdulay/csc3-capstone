print("Welcome to the 30 Second Rule Expert")
print('------------------------------------')
print('Answer the following questions by selecting from among the options.')

x=input('Did anyone see you? (yes/no)\n')
if x=='yes':
    y=input('Was it a boss/lover/parent? (yes/no)\n')
    if y=='no':
        print('Decision: Eat it.')
    if y=='yes':
        z=input('Was it expensive? (yes/no)\n')
        if z=='no':
            r=input('Is it chocolate? (yes/no)\n')
            if r=='yes':
                print('Decision: Eat it.') 
            if r=='no':
                print("Decision: Don't eat it.") 
        if z=='yes': 
            j=input('Can you cut off the part that touched the floor? (yes/no)\n')
            if j=='yes':
                print('Decision: Eat it.')
            else: print('Decision: Your call.')
if x=='no':
    u=input('Was it sticky? (yes/no)\n')
    if u=='yes':
        t=input('Is it a raw steak? (yes/no)\n')
        if t=='yes':
            w=input('Are you a puma? (yes/no)\n')
            if w=='yes':
                print('Decision: Eat it.')
            if w=='no':
                print("Decision: Don't eat it.")
        if t=='no':
            q=input('Did the cat lick it? (yes/no)\n')
            if q=='no':
                print('Decision: Eat it.') 
            if q=='yes':
                a=input('Is your cat healthy? (yes/no)\n')
                if a=='no':
                    print('Decision: Your call.') 
                if a=='yes':
                    print('Decision: Eat it.')
    if u=='no':
        b=input('Is it an Emausaurus? (yes/no)\n')
        if b=='yes':
            g=input('Are you a Megalosaurus? (yes/no)\n')
            if g=='no':
                print("Decision: Don't eat it.")
            else: print('Decision: Eat it.') 
        if b=='no':
            o=input('Did the cat lick it? (yes/no)\n')
            if o=='yes':
                p=input('Is your cat healthy? (yes/no)\n')
                if p=='no':
                    print('Decision: Your call.') 
                if p=='yes':
                    print('Decision: Eat it.') 
            else: print('Decision: Eat it.')        
            
        
    

                