

print('Welcome to the 30 Second Rule Expert')
print('------------------------------------')
print('Answer the following questions by selecting from among the options.')
a1 = input("Did anyone see you? (yes/no)\n")
if a1 == 'no':
    a1_1= input("Was it sticky? (yes/no)\n")
    if a1_1=='no':
        a1_11= input('Is it an Emausaurus? (yes/no)\n')
        if a1_11 == 'no':
            a1_12=input('Did the cat lick it? (yes/no)\n')
            if a1_12=='no':
                print('Decision: Eat it.')
            else:
                a1_13=input('Is your cat healthy? (yes/no)\n')
                if a1_13=='yes':
                    print('Decision: Eat it.')
                else:
                    print('Decision: Your call.')
        else:
            a1_112=input("Are you a Megalosaurus? (yes/no)\n")
            if a1_112=='yes':
                print("Decision: Eat it.")
            else:
                print("Decision: Don't eat it.")
    else:
        a2_1=input("Is it a raw steak? (yes/no)\n")
        if a2_1=='no':
            a1_12=input('Did the cat lick it? (yes/no)\n')
            if a1_12=='no':
                print('Decision: Eat it.')
            else:
                a5_1=input('Is your cat healthy? (yes/no)\n')
                if a5_1=='yes':
                    print('Decision: Eat it.')
                else:
                    print('Decision: Your call.')
        else:
            a2_2= input('Are you a puma? (yes/no)\n')
            if a2_2=='yes':
                print('Decision: Eat it.')
            else:
                print("Decision: Don't eat it.")

else:
    a3_1=input('Was it a boss/lover/parent? (yes/no)\n')
    if a3_1=='no':
        print('Decision: Eat it.')
    else:
        a3_2=input('Was it expensive? (yes/no)\n')
        if a3_2=='no':
            a3_3= input('Is it chocolate? (yes/no)\n')
            if a3_3 =='no':
                print("Decision: Don't eat it.")
            else:
                print('Decision: Eat it.')
        else:
            a3_21= input("Can you cut off the part that touched the floor? (yes/no)\n")
            if a3_21=='yes':
                print("Decision: Eat it.")
            else:
                print('Decision: Your call.')
            
    