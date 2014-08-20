#Phillip Ruhesi
#Q1=Did any one see you?
#Q2=Was it boss/lover/parent?
#Q3=Was it sticky?
#Q4=Was it expensive?
#Q5=Can you cut off the part that touched the floor?
#Q6=Is it choclate?
#Q7=Is it a raw steak?
#Q8=Is it an Emausaurus?
#Q9=Are you a puma?
#Q10=Did the cat lick it?
#Q11=Are you a Megalosaurus?
#Q12=Is your cat healthy?
def main():
    print('Welcome to the 30 Second Rule Expert')
    print('------------------------------------')
    print('Answer the following questions by selecting from among the options.')


    Q1 = input('Did anyone see you? (yes/no)\n')
    if Q1=='yes':
        Q2 = input('Was it a boss/lover/parent? (yes/no)\n')
        if Q2=='no':
            print('Decision: Eat it.')                        
        elif Q2=='yes':
            Q4= input('Was it expensive? (yes/no)\n')
            if Q4=='yes':
                Q5 =input('Can you cut off the part that touched the floor? (yes/no)\n')
                if Q5=='yes':
                    print('Decision: Eat it.')
                elif Q5=='no':
                    print('Decision: Your call.')
            elif Q4=='no':
                Q6= input('Is it chocolate? (yes/no)\n') 
                if Q6=='yes':
                    print('Decision: Eat it.')
                elif Q6=='no':
                        print("Decision: Don't eat it.")
        

    elif Q1=='no':
        Q3= input('Was it sticky? (yes/no)\n')
        if Q3=='yes':
            Q7=input('Is it a raw steak? (yes/no)\n')
            if Q7=='yes':
                Q9=input('Are you a puma? (yes/no)\n')
                if Q9=='yes':
                    print('Decision: Eat it.')
                elif Q9=='no':
                    print("Decision: Don't eat it.")
            elif Q7=='no':
                Q10=input('Did the cat lick it? (yes/no)\n')
                if Q10=='no':
                    print("Decision: Eat it.")
                elif Q10=='yes':
                    Q12=input('Is your cat healthy? (yes/no)\n')
                    if Q12=='yes':
                        print('Decision: Eat it.')
                    elif Q12=='no':
                        print('Decision: Your call.')
        elif Q3=='no':
            Q8=input('Is it an Emausaurus? (yes/no)\n')
            if Q8=='yes':
                Q11=input('Are you a Megalosaurus? (yes/no)\n')
                if Q11=='yes':
                    print('Decision: Eat it.')
                elif Q11=='no':
                    print("Decision: Don't eat it.")
            elif Q8=='no':
                Q10=input('Did the cat lick it? (yes/no)\n')
                if Q10=='no':
                    print('Decision: Eat it.')
                elif Q10=='yes':
                    Q12=input('Is your cat healthy? (yes/no)\n')
                    if Q12=='yes':
                        print('Decision: Eat it.')
                    elif Q12=='no':
                        print('Decision: Your call.')                
            
 
main()


