def run_q4c():
    q4b=input('Did the cat lick it? (yes/no)\n')
    if q4b == 'yes':
        q5=input('Is your cat healthy? (yes/no)\n')
        if q5 == 'yes':
            print('Decision: Eat it.')
        if q5 == 'no':
            print('Decision: Your call.')
    if q4b == 'no':
        print('Decision: Eat it.')    



print('Welcome to the 30 Second Rule Expert\n------------------------------------\nAnswer the following questions by selecting from among the options.')
q1=input('Did anyone see you? (yes/no)\n')
if q1 == 'yes':
    q2b=input('Was it a boss/lover/parent? (yes/no)\n')
    if q2b == 'yes':
        q3c=input('Was it expensive? (yes/no)\n')
        if q3c == 'yes':
            q4e=input('Can you cut off the part that touched the floor? (yes/no)\n')
            if q4e =='yes':
                print('Decision: Eat it.')
            if q4e =='no':
                print('Decision: Your call.')
        if q3c == 'no':
            q4d=input('Is it chocolate? (yes/no)\n')
            if q4d=='yes':
                print('Decision: Eat it.')
            if q4d=='no':
                print("Decision: Don't eat it.")
    if q2b == 'no':
        print('Decision: Eat it.') 
if q1 == 'no':
    q2a=input('Was it sticky? (yes/no)\n')
    if q2a == 'yes':
        q3b=input('Is it a raw steak? (yes/no)\n')
        if q3b =='yes':
            q4c=input('Are you a puma? (yes/no)\n')
            if q4c == 'yes':
                print('Decision: Eat it.')
            if q4c == 'no':
                print("Decision: Don't eat it.")
        if q3b == 'no':
            run_q4c()
    if q2a == 'no':
        q3a=input('Is it an Emausaurus? (yes/no)\n')
        if q3a == 'no':
            run_q4c()
        if q3a == 'yes':
            q4a=input('Are you a Megalosaurus? (yes/no)\n')
            if q4a == 'yes':
                print('Decision: Eat it.')
            if q4a == 'no':
                print("Decision: Don't eat it.")
        
        

        
