#A program that tells you whether or not to eat something you dropped on the floor
#Jason Findlay
#13/03/2013

Eat = 'Decision: Eat it.'
DEat = 'Decision: Don\'t eat it.'
Choose = 'Decision: Your call.'
y = 'yes'

#Print header
print('Welcome to the 30 Second Rule Expert')
print('------------------------------------')
print('Answer the following questions by selecting from among the options.')
Answer = input('Did anyone see you? (yes/no)\n')

if Answer == y:
    Answer = input('Was it a boss/lover/parent? (yes/no)\n')
    if Answer == y:
        Answer = input('Was it expensive? (yes/no)\n')
        if Answer == y:
            Answer = input('Can you cut off the part that touched the floor? (yes/no)\n')
            if Answer == y:
                print(Eat)
            else:
                print(Choose)
        else:
            Answer = input('Is it chocolate? (yes/no)\n')
            if Answer == y:
                print(Eat)
            else:
                print(DEat)
    else:
        print(Eat)
else:
    Answer = input('Was it sticky? (yes/no)\n')
    if Answer == y:
        Answer = input('Is it a raw steak? (yes/no)\n')
        if Answer == y:
            Answer = input('Are you a puma? (yes/no)\n')
            if Answer == y:
                print(Eat)
            else:
                print(DEat)
        else:
            Answer = input('Did the cat lick it? (yes/no)\n')
            if Answer == y:
                Answer = input('Is your cat healthy? (yes/no)\n')
                if Answer == y:
                    print(Eat)
                else:
                    print(Choose)
            else:
                print(Eat)
    else:
        Answer = input('Is it an Emausaurus? (yes/no)\n')
        if Answer == y:
            Answer = input('Are you a Megalosaurus? (yes/no)\n')
            if Answer == y:
                print(Eat)
            else:
                print(DEat)
        else:
             Answer = input('Did the cat lick it? (yes/no)\n')
             if Answer == y:
                  Answer = input('Is your cat healthy? (yes/no)\n')
                  if Answer == y:
                        print(Eat)
                  else:
                      print(Choose)
             else:
                 print(Eat)
            
            
