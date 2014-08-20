#A program for determining if you should eat the food or not
#Maisha Ivha
#MSHVH001
#14/03/2014
def main():
    print('Welcome to the 30 Second Rule Expert')
    print('------------------------------------')
    print('Answer the following questions by selecting from among the options.')
    q1=(input('Did anyone see you? (yes/no)\n'))
    if q1=='yes':
        q2=input('Was it a boss/lover/parent? (yes/no)\n')
        if q2=='yes':
            q3=input('Was it expensive? (yes/no)\n')
            if q3=='yes':
                q4=input('Can you cut off the part that touched the floor? (yes/no)\n')
                if q4=='yes':
                    print('Decision: Eat it.')
                elif q4=='no':
                    print('Decision: Your call.')
            elif q3=='no':
                q5=input('Is it chocolate? (yes/no)\n')
                if q5=='yes':
                    print('Decision: Eat it.')
                elif q5=='no':
                    print("Decision: Don't eat it.")
        elif q2=='no':
            print('Decision: Eat it.')
    elif q1=='no':
        Q2=input('Was it sticky? (yes/no)\n')
        if Q2=='yes':
            Q3=input('Is it a raw steak? (yes/no)\n')
            if Q3=='yes':
                Q5=input('Are you a puma? (yes/no)\n')
                if Q5=='yes':
                    print('Decision: Eat it.')
                elif Q5=='no':
                    print("Decision: Don't eat it.") 
            elif Q3=='no':
                Q6=input('Did the cat lick it? (yes/no)\n')
                if Q6=='yes':
                    Q7=input('Is your cat healthy? (yes/no)\n')
                    if Q7=='yes':
                        print('Decision: Eat it.')
                    elif Q7=='no':
                        print('Decision: Your call.')
                elif Q6=='no':
                    print('Decision: Eat it.')
        elif Q2=='no':
            Q4=input('Is it an Emausaurus? (yes/no)\n')
            if Q4=='yes':
                Q8=input('Are you a Megalosaurus? (yes/no)\n')
                if Q8=='yes':
                    print('Decision: Eat it.')
                elif Q8=='no':
                    print("Decision: Don't eat it.")
            elif Q4=='no':
                Q6=input('Did the cat lick it? (yes/no)\n')
                if Q6=='yes':
                    Q7=input('Is your cat healthy? (yes/no)\n')
                    if Q7=='yes':
                        print('Decision: Eat it.')
                    elif Q7=='no':
                        print('Decision: Your call.') 
                elif Q6=='no':
                        print('Decision: Eat it.')
main()