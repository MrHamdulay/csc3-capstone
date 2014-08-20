

print("Welcome to the 30 Second Rule Expert")
print("------------------------------------")
print('Answer the following questions by selecting from among the options.')
q1 = input('Did anyone see you? (yes/no)''\n')
if (q1 == 'yes'):
    q2 = input('Was it a boss/lover/parent? (yes/no)''\n')
    if (q2 == 'no'):
        print('Decision: Eat it.')    
    elif (q2 =='yes'):
        q3 = input('Was it expensive? (yes/no)''\n')
        if (q3 == 'yes'):
            q4 = input('Can you cut off the part that touched the floor? (yes/no)''\n')
            if (q4 == 'yes'):
                    print("Decision: Eat it.")
            elif (q4 == 'no'):
                print('Decision: Your call.')
        elif (q3 == 'no'):
            q5 = input('Is it chocolate? (yes/no)''\n') 
            if (q5 == 'yes'):
                print('Decision: Eat it.')
            elif (q5 =='no'):
                print('Decision: Don\'t eat it.')                

if (q1 == 'no'):
    k1 = input('Was it sticky? (yes/no)''\n')
    if (k1 == 'yes'):
        k2 = input('Is it a raw steak? (yes/no)''\n')
        if (k2 == 'yes'):
            k3 = input('Are you a puma? (yes/no)''\n')
            if (k3 == 'yes'):
                print('Decision: Eat it.')
            elif (k3 == 'no'):
                print('Decision: Don\'t eat it.')
        elif (k2 == 'no'):
            k6 = input('Did the cat lick it? (yes/no)''\n')
            if (k6 =='yes'):
                k7 = input('Is your cat healthy? (yes/no)''\n')
                if (k7 =='yes'):
                    print('Decision: Eat it.')
                elif (k7 == 'no'):
                    print('Decision: Your call.')
            elif (k6 == 'no'):
                print('Decision: Eat it.')                                
                
    elif (k1 == 'no'):
        k4 = input('Is it an Emausaurus? (yes/no)''\n')
        if (k4 == 'yes'):
            k5 = input('Are you a Megalosaurus? (yes/no)''\n')
            if (k5 == 'yes'):
                print('Decision: Eat it.')
            elif (k5 == 'no'):
                print('Decision: Don\'t eat it.')

        elif (k4 == 'no'):
            k6 = input('Did the cat lick it? (yes/no)''\n')
            if (k6 =='yes'):
                k7 = input('Is your cat healthy? (yes/no)''\n')
                if (k7 =='yes'):
                    print('Decision: Eat it.')
                elif (k7 == 'no'):
                    print('Decision: Your call.')
                    
            elif (k6 == 'no'):
                print('Decision: Eat it.')
                    
        

      
          


    
        
    
    
    