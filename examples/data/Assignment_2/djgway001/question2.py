#follow the flow chart
print('Welcome to the 30 Second Rule Expert')
print('------------------------------------')
print('Answer the following questions by selecting from among the options.')

see=input('Did anyone see you? (yes/no)\n')
if see==('yes'):
    boss=input('Was it a boss/lover/parent? (yes/no)\n')
    if boss==('yes'):
        expen=input('Was it expensive? (yes/no)\n')
        if expen==('yes'):
            floor=input('Can you cut off the part that touched the floor? (yes/no)\n')
            if floor==('yes'):
                print('Decision: Eat it.')
            elif floor==('no'):
                print('Decision: Your call.')
        elif expen==('no'):
            choc=input('Is it chocolate? (yes/no)\n')
            if choc==('yes'):
                print('Decision: Eat it.')
            elif choc==('no'):
                print("Decision: Don't eat it.")
    elif boss==('no'):
        print('Decision: Eat it.')
elif see==('no'):
    sticky=input('Was it sticky? (yes/no)\n')
    if sticky==('yes'):
            raw=input('Is it a raw steak? (yes/no)\n')
            if raw==('yes'):
                puma=input('Are you a puma? (yes/no)\n')
                if puma==('yes'):
                    print('Decision: Eat it.')
                elif puma==('no'):
                    print("Decision: Don't eat it.")
            elif raw==('no'):
                cat=input('Did the cat lick it? (yes/no)\n')
                if cat==('yes'):
                    healthy=input('Is your cat healthy? (yes/no)\n')
                    if healthy==('yes'):
                        print('Decision: Eat it.')
                    elif healthy==('no'):
                        print('Decision: Your call.')
                elif cat==('no'):
                    print('Decision: Eat it.')
    elif sticky==('no'):
            emausaurus=input('Is it an Emausaurus? (yes/no)\n')
            if emausaurus==('yes'):
                megalorsaurus=input('Are you a Megalosaurus? (yes/no)\n')
                if megalorsaurus==('yes'):
                    print('Decision: Eat it.')
                elif megalorsaurus==('no'):
                    print("Decision: Don't eat it.")
            elif emausaurus==('no'):
                cat=input('Did the cat lick it? (yes/no)\n')
                if cat==('yes'):
                    healthy=input('Is your cat healthy? (yes/no)\n')
                    if healthy==('yes'):
                        print('Decision: Eat it.')
                    elif healthy==('no'):
                        print('Decision: Your call.')
                elif cat==('no'):
                    print('Decision: Eat it.')