print('Welcome to the 30 Second Rule Expert')
print('------------------------------------')
print('Answer the following questions by selecting from among the options.')

#If Statement
Answer = input('Did anyone see you? (yes/no)\n')
#Anyone see you (YES)
if Answer == 'yes':
    Answer = input('Was it a boss/lover/parent? (yes/no)\n')
    #B/L/P (NO)
    if Answer == 'no':
        print('Decision: Eat it.')
    #B/L/P (YES)
    elif Answer == 'yes':
        Answer = input('Was it expensive? (yes/no)\n')
        #Was it Expensive (YES)
        if Answer == 'yes':
            Answer = input('Can you cut off the part that touched the floor? (yes/no)\n')
            #Cut off (YES)
            if Answer == 'yes':
                print('Decision: Eat it.')
            #Cut off (NO)
            elif Answer == 'no':
                print('Decision: Your call.')
        #Was is Expensive (NO)
        elif Answer == 'no':
            Answer = input('Is it chocolate? (yes/no)\n')
            #Chocolate (YES)
            if Answer == 'yes':
                print('Decision: Eat it.')
            #Chocolate (NO)
            elif Answer == 'no':
                print("Decision: Don't eat it.")
#Anyone see you (NO)
elif Answer == 'no':
    Answer = input('Was it sticky? (yes/no)\n')
    #Sticky (YES)
    if Answer == 'yes':
        Answer = input('Is it a raw steak? (yes/no)\n')
        #Raw Steak (YES)
        if Answer == 'yes':
            Answer = input('Are you a puma? (yes/no)\n')
            #Puma (YES)
            if Answer == 'yes':
                print('Decision: Eat it.')
            #Puma (NO)
            else: print("Decision: Don't eat it.")
        #Raw Steak (NO)
        elif Answer == 'no':
            Answer = input('Did the cat lick it? (yes/no)\n')
            #Lick (NO)
            if Answer == 'no':
                print('Decision: Eat it.')
            #Lick (YES)
            else:
                Answer = input('Is your cat healthy? (yes/no)\n')
                #CatH (YES)
                if Answer == 'yes':
                    print('Decision: Eat it.')
                #CatH (NO)
                else: print('Decision: Your call.')
    #Sticky (NO)
    elif Answer == 'no':
        Answer = input('Is it an Emausaurus? (yes/no)\n')
        #Emausaurus (YES)
        if Answer == 'yes':
            Answer = input('Are you a Megalosaurus? (yes/no)\n')
            #Mega (YES)
            if Answer == 'yes':
                print('Decision: Eat it.')
            #Mega (NO)
            else: print("Decision: Don't eat it.")
        #Emausaurus (NO)
        elif Answer == 'no':
            Answer = input('Did the cat lick it? (yes/no)\n')
            #Cat (NO)
            if Answer == 'no':
                print('Decision: Eat it.')
            #Cat (YES)
            else:
                Answer = input('Is your cat healthy? (yes/no)\n')
                #Health (YES)
                if Answer == 'yes':
                    print('Decision: Eat it.')
                #Health (NO)
                else: print('Decision: Your call.')            
            