#RSNADA001
#Adam Rosendorff
#key: question, yes, no
questions = {'sticky':['Was it sticky? (yes/no)','steak','emausaurus'],            
             'steak':['Is it a raw steak? (yes/no)','puma','lick'],
             'puma':['Are you a puma? (yes/no)','EAT','DONT'],
             'lick':['Did the cat lick it? (yes/no)','healthy','EAT'],
             'healthy':['Is your cat healthy? (yes/no)','EAT','CALL'],
             'emausaurus':['Is it an Emausaurus? (yes/no)','megalosaurus','lick'],
             'megalosaurus':['Are you a Megalosaurus? (yes/no)','EAT','DONT'],
             'seen':['Was it a boss/lover/parent? (yes/no)','expensive','EAT'],
             'expensive':['Was it expensive? (yes/no)','cut','chocolate'],
             'cut':['Can you cut off the part that touched the floor? (yes/no)','EAT','CALL'],
             'chocolate':['Is it chocolate? (yes/no)','EAT','DONT'],
             }
done = False
options = ['seen','sticky']
print('''Welcome to the 30 Second Rule Expert
------------------------------------
Answer the following questions by selecting from among the options.
Did anyone see you? (yes/no)''')
#not found an eat/DONT
while (done == False):
    ans = input()
    if ans == 'yes':
        #checks if we reached an eat/DONT
        if 'EAT' in options[0]:
            print('Decision: Eat it.')
            done = True
            break
        elif 'DONT' in options[0]:
            print('Decision: Don\'t eat it.')
            done = True
            break
        elif 'CALL' in options[0]:
            print('Decision: Your call.')
            done = True
            break
        #print next question
        print(questions[options[0]][0])
        #sets next options
        options = questions[options[0]][1:]
    elif ans == 'no':
        #checks if we reached an eat/DONT
        if 'EAT' in options[1]:
            print('Decision: Eat it.')
            done = True
            break
        elif 'DONT' in options[1]:
            print('Decision: Don\'t eat it.')
            done = True
            break
        elif 'CALL' in options[1]:
            print('Decision: Your call.')
            done = True
            break
        print(questions[options[1]][0])
        options = questions[options[1]][1:]
    

