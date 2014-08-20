print('Welcome to the 30 Second Rule Expert')
print('------------------------------------')
print('Answer the following questions by selecting from among the options.')
               
reply=input('Did anyone see you? (yes/no)\n')
if reply=='yes':
    reply=input('Was it a boss/lover/parent? (yes/no)\n')
    if reply=='no':
        print('Decision: Eat it.')
    else :
        reply=input('Was it expensive? (yes/no)\n')
        if reply=='yes':
            reply=input('Can you cut off the part that touched the floor? (yes/no)\n')
            if reply=='yes':
                print('Decision: Eat it.')
            else:
                print('Decision: Your call.')
        else:
            reply=input('Is it chocolate? (yes/no)\n')
            if reply=='yes':
                print('Decision: Eat it.')
            else:
                print('Decision: Don\'t eat it.')
else:
    reply=input('Was it sticky? (yes/no)\n')
    if reply=='yes':
        reply=input('Is it a raw steak? (yes/no)\n')
        if reply=='yes':
            reply=input('Are you a puma? (yes/no)\n')
            if reply=='yes':
                print('Decision: Eat it.')
            else:
                print('Decision: Don\'t eat it.')
        else:
            reply=input('Did the cat lick it? (yes/no)\n')
            if reply=='yes':
                reply=input('Is your cat healthy? (yes/no)\n')
                if reply=='yes':
                    print('Decision: Eat it.')
                else:
                    print('Decision: Your call.')
            else:
                print('Decision: Eat it.')
    else:
        reply=input('Is it an Emausaurus? (yes/no)\n')
        if reply=='yes':
            reply=input('Are you a Megalosaurus? (yes/no)\n')
            if reply=='yes':
                print('Decision: Eat it.')
            else:
                print('Decision: Don\'t eat it.')
        else:
            reply=input('Did the cat lick it? (yes/no)\n')
            if reply=='yes':
                reply=input('Is your cat healthy? (yes/no)\n')
                if reply=='yes':
                    print('Decision: Eat it.')
                else:
                    print('Decision: Your call.')
            else:
                print('Decision: Eat it.')            
     
    
