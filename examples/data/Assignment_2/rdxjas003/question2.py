print('Welcome to the 30 Second Rule Expert')
print('------------------------------------')
print('Answer the following questions by selecting from among the options.')
a = input('Did anyone see you? (yes/no)\n')
if (a=='yes'):
    b = input('Was it a boss/lover/parent? (yes/no)\n')
    if (b=='no'):
        print('Decision: Eat it.')
    if (b=='yes'):
        c = input('Was it expensive? (yes/no)\n')
        if (c=='yes'):
            d = input('Can you cut off the part that touched the floor? (yes/no)\n')
            if (d=='yes'):
                print('Decision: Eat it.')
            if (d=='no'):
                print('Decision: Your call.')
        if (c=='no'):
            e = input('Is it chocolate? (yes/no)\n')
            if (e=='yes'):
                print('Decision: Eat it.')
            if (e=='no'):
                print("Decision: Don't eat it.")
if (a=='no'):
    f = input('Was it sticky? (yes/no)\n')
    if (f=='yes'):
        g = input('Is it a raw steak? (yes/no)\n')
        if (g=='yes'):
            h = input('Are you a puma? (yes/no)\n')
            if (h=='yes'):
                print('Decision: Eat it.')
            if (h=='no'):
                print("Decision: Don't eat it.")            
        if (g=='no'):  
            i = input('Did the cat lick it? (yes/no)\n')
            if (i=='no'):
                print('Decision: Eat it.')
            if (i=='yes'):
                j = input('Is your cat healthy? (yes/no)\n')
                if (j=='yes'):
                    print('Decision: Eat it.')
                if (j=='no'):
                    print('Decision: Your call.')                                
    if (f=='no'):
        k = input('Is it an Emausaurus? (yes/no)\n')
        if (k=='no'):
            l = input('Did the cat lick it? (yes/no)\n')
            if (l=='no'):
                print('Decision: Eat it.')
            if (l=='yes'):
                m = input('Is your cat healthy? (yes/no)\n')
                if (m=='yes'):
                    print('Decision: Eat it.')
                if (m=='no'):
                    print('Decision: Your call.')            
        if (k=='yes'):  
            n = input('Are you a Megalosaurus? (yes/no)\n')
            if (n=='no'):
                print("Decision: Don't eat it.")
            if (n=='yes'):
                print('Decision: Eat it.')     
        
            
    


