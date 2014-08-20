#A program to ask a series of questions to determine if you should eat the food or not
#ATISANG MOLAPO
#STUDENT NUMBER:MLPATI001
def main():
    print('Welcome to the 30 Second Rule Expert')
    print('------------------------------------')
    print('Answer the following questions by selecting from among the options.')
    b1=(input('Did anyone see you? (yes/no)\n'))
    if b1=='yes':
        b2=input('Was it a boss/lover/parent? (yes/no)\n')
        if b2=='yes':
            b3=input('Was it expensive? (yes/no)\n')
            if b3=='yes':
                b4=input('Can you cut off the part that touched the floor? (yes/no)\n')
                if b4=='yes':
                    print('Decision: Eat it.')
                elif b4=='no':
                    print('Decision: Your call.')
            elif b3=='no':
                b5=input('Is it chocolate? (yes/no)\n')
                if b5=='yes':
                    print('Decision: Eat it.')
                elif b5=='no':
                    print("Decision: Don't eat it.")
        elif b2=='no':
            print('Decision: Eat it.')
    elif b1=='no':
        d2=input('Was it sticky? (yes/no)\n')
        if d2=='yes':
            d3=input('Is it a raw steak? (yes/no)\n')
            if d3=='yes':
                d5=input('Are you a puma? (yes/no)\n')
                if d5=='yes':
                    print('Decision: Eat it.')
                elif d5=='no':
                    print("Decision: Don't eat it.") 
            elif d3=='no':
                d6=input('Did the cat lick it? (yes/no)\n')
                if d6=='yes':
                    d7=input('Is your cat healthy? (yes/no)\n')
                    if d7=='yes':
                        print('Decision: Eat it.')
                    elif d7=='no':
                        print('Decision: Your call.')
                elif d6=='no':
                    print('Decision: Eat it.')
        elif d2=='no':
            d4=input('Is it an Emausaurus? (yes/no)\n')
            if d4=='yes':
                d8=input('Are you a Megalosaurus? (yes/no)\n')
                if d8=='yes':
                    print('Decision: Eat it.')
                elif d8=='no':
                    print("Decision: Don't eat it.")
            elif d4=='no':
                d6=input('Did the cat lick it? (yes/no)\n')
                if d6=='yes':
                    d7=input('Is your cat healthy? (yes/no)\n')
                    if d7=='yes':
                        print('Decision: Eat it.')
                    elif d7=='no':
                        print('Decision: Your call.') 
                elif d6=='no':
                        print('Decision: Eat it.')
main()