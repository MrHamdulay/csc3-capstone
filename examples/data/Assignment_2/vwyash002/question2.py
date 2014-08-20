#30 seccond rule
#VWYASH002

print("Welcome to the 30 Second Rule Expert")
print("------------------------------------")
print("Answer the following questions by selecting from among the options.")
see = input('Did anyone see you? (yes/no)\n')
if see =='yes':
    parent = input('Was it a boss/lover/parent? (yes/no)\n')
    if parent=='no':
        print('Decision: Eat it.')
    elif parent == 'yes':
        exp=input('Was it expensive? (yes/no)\n' )
        if exp=='no':
            chocolate=input('Is it chocolate? (yes/no)\n')
            if chocolate=='no': 
                print("Decision: Don't eat it.")
            elif chocolate=='yes':
                print('Decision: Eat it.')            
        elif exp=='yes':
            cut=input('Can you cut off the part that touched the floor? (yes/no)\n')
            if cut=='yes':
                print('Decision: Eat it.')
            elif cut=='no':
                print('Decision: Your call.')
elif see=='no':
    sticky=input('Was it sticky? (yes/no)\n')
    if sticky=='yes':
        steak= input('Is it a raw steak? (yes/no)\n')
        if steak=='yes':
            puma=input('Are you a puma? (yes/no)\n')
            if puma=='no':
                print("Decision: Don't eat it.")
            elif puma == 'yes':
                print('Decision: Eat it.')
        elif steak=='no':
            cat=input('Did the cat lick it? (yes/no)\n')
            if cat=='no':
                print('Decision: Eat it.')
            elif cat=='yes':
                cat2=input('Is your cat healthy? (yes/no)\n')
                if cat2=='yes':
                    print('Decision: Eat it.')
                elif cat2=='no':
                    print('Decision: Your call.')
    elif sticky=='no':
        ema=input('Is it an Emausaurus? (yes/no)\n')
        if ema=='yes':
            mega=input('Are you a Megalosaurus? (yes/no)\n')
            if mega=='yes':
                print('Decision: Eat it.')
            elif mega=='no':
                print("Decision: Don't eat it.")
        if ema=='no':
            cat=input('Did the cat lick it? (yes/no)\n')
            if cat=='no':
                print('Decision: Eat it.')
            elif cat=='yes':
                cat2=input('Is your cat healthy? (yes/no)\n')
                if cat2=='yes':
                    print('Decision: Eat it.')
                elif cat2=='no':
                    print('Decision: Your call.')            
            