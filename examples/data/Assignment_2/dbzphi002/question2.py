#Thembekile Dubazana
#DBZPHI002
#11 March 2013

print('Welcome to the 30 Second Rule Expert')
print('------------------------------------')
print('Answer the following questions by selecting from among the options.')
a=(input('Did anyone see you? (yes/no)\n'))
if a=="yes":
    a=(input('Was it a boss/lover/parent? (yes/no)\n'))
    if a=="yes":
        a=input('Was it expensive? (yes/no)\n')
        if a=="yes":
            a=input('Can you cut off the part that touched the floor? (yes/no)\n')
            if a=="yes":
                print('Decision: Eat it.')
            else:#else of can you cut off etc
                print('Decision: Your call.')
        else:#else of was it expensive
            b=input('Is it chocolate? (yes/no)\n')
            if b=="yes": 
                print('Decision: Eat it.')
            else:#else of is it chocolate
                print("Decision: Don't eat it.")
    else:#else of was it a boss etc
        print('Decision: Eat it.')
else:#else of did anyone see you
    a=input('Was it sticky? (yes/no)\n')
    if a=="yes":
        a=input('Is it a raw steak? (yes/no)\n')
        if a=="yes":
            a=input('Are you a puma? (yes/no)\n')
            if a=="yes":
                print('Decision: Eat it.')
            else:#else of are you a puma
                print("Decision: Don't eat it.")
        else:#else of is it a raw steak
            a=input('Did the cat lick it? (yes/no)\n')
            if a=="yes":
                a=input('Is your cat healthy? (yes/no)\n')
                if a=="yes":
                    print('Decision: Eat it.')
                else:
                    print('Decision: Your call.')
            else:#else of did the cat lick it
                print('Decision: Eat it.')
    else:#else of was it sticky
        a=input('Is it an Emausaurus? (yes/no)\n')
        if a=="yes":
            a=input('Are you a Megalosaurus? (yes/no)\n')
            if a=="yes":
                print('Decision: Eat it.')
            else:#else of are you a Mega...
                print("Decision: Don't eat it.")
        else:#else of is it a Ema... thus repeat conditions of did the cat lick it
            a=input('Did the cat lick it? (yes/no)\n')
            if a=="yes":
                    a=input('Is your cat healthy? (yes/no)\n')
                    if a=="yes":
                        print('Decision: Eat it.')
                    else:#repeat:else of is the cat healthy
                        print('Decision: Your call.')
            else:#repeat:else of did the cat lick it
                print('Decision: Eat it.')            

        
