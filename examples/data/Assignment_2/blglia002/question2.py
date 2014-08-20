#Liam Blignaut
#A series of questions to detremine if you should eat the food or not.
#09/03/2014

print("Welcome to the 30 Second Rule Expert")
print("------------------------------------")
print("Answer the following questions by selecting from among the options.")
answer = input("Did anyone see you? (yes/no) \n")
if answer=='no':
    answer1=input("Was it sticky? (yes/no) \n")
    if answer1=='no':
        answer2=input("Is it an Emausaurus? (yes/no) \n")
        if answer2=='yes':
            answer3=input("Are you a Megalosaurus? (yes/no) \n")
            if answer3=='no':
                print("Decision: Don't eat it.")
            if answer3=='yes':
                print("Decision: Eat it.")
        if answer2=='no':
            answer5=input('Did the cat lick it? (yes/no) \n')
            if answer5=='no':
                print('Decision: Eat it.')
            if answer5=='yes':
                answer6=input('Is your cat healthy? (yes/no) \n')
                if answer6=='no':
                    print("Decision: Your call.")
                if answer6=='yes':
                    print('Decision: Eat it.')
                
    if answer1=='yes':
        answer4=input('Is it a raw steak? (yes/no) \n')
        if answer4=='no':
            answer5=input('Did the cat lick it? (yes/no) \n')
            if answer5=='no':
                print('Decision: Eat it.')
            if answer5=='yes':
                answer6=input('Is your cat healthy? (yes/no) \n')
                if answer6=='yes':
                    print('Decision: Eat it.')
                if answer6=='no':
                    print('Decision: Your call.')
        if answer4=='yes':
            answer7=input('Are you a puma? (yes/no) \n')
            if answer7=='yes':
                print('Decision: Eat it.')
            if answer7=='no':
                print("Decision: Don't eat it.")
if answer=='yes':
    answer8=input('Was it a boss/lover/parent? (yes/no) \n')
    if answer8=='no':
        print('Decision: Eat it.')
    if answer8=='yes':
        answer9=input('Was it expensive? (yes/no) \n')
        if answer9=='no':
            answer10=input('Is it chocolate? (yes/no) \n')
            if answer10=='yes':
                print('Decision: Eat it.')
            if answer10=='no':
                print("Decision: Don't eat it.")
        if answer9=='yes':
            answer11=input("Can you cut off the part that touched the floor? (yes/no) \n")
            if answer11=='yes':
                print('Decision: Eat it.')
            if answer11=='no':
                print('Decision: Your call.')