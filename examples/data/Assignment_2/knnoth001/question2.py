# Program that helps one to decide on either take or leave its cupcake that dropped
# Name: Othniel KONAN
# Student number: KNNOTH001
# Date: 14/03/2014

print('Welcome to the 30 Second Rule Expert')
print('------------------------------------')
print('Answer the following questions by selecting from among the options.')
print('Did anyone see you? (yes/no)')
answer = input()
if answer == 'yes':
    print('Was it a boss/lover/parent? (yes/no)')
    answer = input()
    if answer == 'yes': 
        print('Was it expensive? (yes/no)')
        answer = input()
        if answer == 'yes':
            print('Can you cut off the part that touched the floor? (yes/no)')
            answer = input()
            if answer == 'yes':
                print('Decision: Eat it.')
            else:
                print('Decision: Your call.')
        else:
            print('Is it chocolate? (yes/no)')
            answer = input()
            if answer == 'yes':
                print('Decision: Eat it.')
            else:
                print('Decision: Don\'t eat it.')
                
    else:
        print('Decision: Eat it.')

else:
    print('Was it sticky? (yes/no)')
    answer = input()
    if answer == 'yes':
        print('Is it a raw steak? (yes/no)')
        answer = input()
        if answer == 'yes':
            print('Are you a puma? (yes/no)')
            answer = input()
            if answer == 'yes':
                print('Decision: Eat it.')
            else:
                print('Decision: Don\'t eat it.')
                 
        else:
            print('Did the cat lick it? (yes/no)')
            answer = input()
            if answer == 'yes':
                print('Is your cat healthy? (yes/no)')
                answer = input()
                if answer == 'yes': 
                    print('Decision: Eat it.')
                else:
                    print('Decision: Your call.')
                    
            else:
                print('Decision: Eat it.')
                
    else:
        print('Is it an Emausaurus? (yes/no)')
        answer = input()
        if answer == 'yes':
            print('Are you a Megalosaurus? (yes/no)')
            answer = input()
            if answer == 'yes':
                print('Decision: Eat it.')
            else:
                print('Decision: Don\'t eat it.')
        else:
            print('Did the cat lick it? (yes/no)')
            answer = input()
            if answer == 'yes':
                print('Is your cat healthy? (yes/no)')
                answer = input()
                if answer == 'yes': 
                    print('Decision: Eat it.')
                else:
                    print('Decision: Your call.')
                                
            else:
                print('Decision: Eat it.')            