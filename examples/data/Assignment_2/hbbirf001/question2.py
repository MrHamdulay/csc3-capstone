# 30 second Rule Expert
# Irfan Habib 
# 7 March 2014

print('Welcome to the 30 Second Rule Expert')
print('------------------------------------')
d = "Decision: Don't eat it."
e = "Decision: Eat it."
y = "Decision: Your call."
print('Answer the following questions by selecting from among the options.')
if input('Did anyone see you? (yes/no)\n') == 'yes':
    if input('Was it a boss/lover/parent? (yes/no)\n') == 'yes':
        if input('Was it expensive? (yes/no)\n') == 'yes':
            if input('Can you cut off the part that touched the floor? (yes/no)\n') == 'yes':
                print(e)
            else: print(y)
        else: 
            if input('Is it chocolate? (yes/no)\n') == 'yes':
                print(e)
            else: print(d)
    else: print(e)
else:
    if input('Was it sticky? (yes/no)\n') == 'yes':
        if input('Is it a raw steak? (yes/no)\n') == 'yes':
            if input('Are you a puma? (yes/no)\n') == 'yes':
                print(e)
            else: print(d)
        else: 
            if input('Did the cat lick it? (yes/no)\n') == 'yes':
                if input('Is your cat healthy? (yes/no)\n') == 'yes':
                    print(e)
                else: print(y)
            else: print(e)
    else: 
        if input('Is it an Emausaurus? (yes/no)\n') == 'yes':
            if input('Are you a Megalosaurus? (yes/no)\n') == 'yes':
                print(e)
            else: print(d)
        else: 
            if input('Did the cat lick it? (yes/no)\n') == 'yes':
                if input('Is your cat healthy? (yes/no)\n') == 'yes':
                    print(e)
                else: print(y)
            else: print(e)            
            
        
            
    
            