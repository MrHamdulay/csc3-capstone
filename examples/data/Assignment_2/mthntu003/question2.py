# Question2
# Assignment2
# 12 March 2014

print('Welcome to the 30 Second Rule Expert')
print('------------------------------------')
print('Answer the following questions by selecting from among the options.')
q1 = input("Did anyone see you? (yes/no)\n")
if q1 == 'no':
    q1_1= input("Was it sticky? (yes/no)\n")
    if q1_1=='no':
        q1_11= input('Is it an Emausaurus? (yes/no)\n')
        if q1_11 == 'no':
            q1_12=input('Did the cat lick it? (yes/no)\n')
            if q1_12=='no':
                print('Decision: Eat it.')
            else:
                q1_13=input('Is your cat healthy? (yes/no)\n')
                if q1_13=='yes':
                    print('Decision: Eat it.')
                else:
                    print('Decision: Your call.')
        else:
            q1_112=input("Are you a Megalosaurus? (yes/no)\n")
            if q1_112=='yes':
                print("Decision: Eat it.")
            else:
                print("Decision: Don't eat it.")
    else:
        q2_1=input("Is it a raw steak? (yes/no)\n")
        if q2_1=='no':
            q1_12=input('Did the cat lick it? (yes/no)\n')
            if q1_12=='no':
                print('Decision: Eat it.')
            else:
                q5_1=input('Is your cat healthy? (yes/no)\n')
                if q5_1=='yes':
                    print('Decision: Eat it.')
                else:
                    print('Decision: Your call.')
        else:
            q2_2= input('Are you a puma? (yes/no)\n')
            if q2_2=='yes':
                print('Decision: Eat it.')
            else:
                print("Decision: Don't eat it.")

else:
    q3_1=input('Was it a boss/lover/parent? (yes/no)\n')
    if q3_1=='no':
        print('Decision: Eat it.')
    else:
        q3_2=input('Was it expensive? (yes/no)\n')
        if q3_2=='no':
            q3_3= input('Is it chocolate? (yes/no)\n')
            if q3_3 =='no':
                print("Decision: Don't eat it.")
            else:
                print('Decision: Eat it.')
        else:
            q3_21= input("Can you cut off the part that touched the floor? (yes/no)\n")
            if q3_21=='yes':
                print("Decision: Eat it.")
            else:
                print('Decision: Your call.')
            
    