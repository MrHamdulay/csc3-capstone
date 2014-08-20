#question2.py
# A program to determine whether or not you should the food you just dropped.
#Michell Ndlozi
#NDLMIC004
#2014/03/08

def eat():
    print("Welcome to the 30 Second Rule Expert")
    print("-"*36)
    print("Answer the following questions by selecting from among the options.")
    question_1=input("Did anyone see you? (yes/no)\n")
    if (question_1== 'yes'):
            question_2=input("Was it a boss/lover/parent? (yes/no)\n")
            if (question_2== 'yes'):
                question_3=input('Was it expensive? (yes/no)\n')
                if (question_3 == 'yes'):
                    question_4=input('Can you cut off the part that touched the floor? (yes/no)\n')
                    if (question_4 == 'yes'):
                        print("Decision: Eat it.")
                    elif question_4== 'no':
                        print('Decision: Your call.')
                elif question_3== 'no':
                    question_5 =input("Is it chocolate? (yes/no)\n")
                    if (question_5 == 'yes'):
                        print("Decision: Eat it.")
                    elif question_5 == 'no':
                        print("Decision: Don't eat it.")
            elif question_2 =='no':
                print("Decision: Eat it.")
    elif question_1 == 'no':
        question_6= input("Was it sticky? (yes/no)\n")
        if question_6 == 'yes':
            question_7=input("Is it a raw steak? (yes/no)\n")
            if question_7 == 'yes':
                question_8=input("Are you a puma? (yes/no)\n")
                if question_8 == 'yes':
                    print("Decision: Eat it.")
                elif question_8 == 'no':
                    print("Decision: Don't eat it.")
            elif question_7 == 'no':
                question_9=input("Did the cat lick it? (yes/no)\n")
                if question_9 =='no':
                    print("Decision: Eat it.")
                elif question_9 =='yes':
                    question_10=input("Is your cat healthy? (yes/no)\n")
                    if question_10 =='no':
                        print("Decision: Your call.")
                    elif question_10 =='yes':
                        print('Decision: Eat it.')
        elif question_6 =='no':
            question_11=input("Is it an Emausaurus? (yes/no)\n")
            if question_11 =='no':
                question_12=input("Did the cat lick it? (yes/no)\n")
                if question_12 =='yes':
                    question_13=input("Is your cat healthy? (yes/no)\n")
                    if question_13 =='yes':
                        print("Decision: Eat it.")
                    elif question_13 == 'no':
                        print("Decision: Your call.")
                elif question_12 =='no':
                    print("Decision: Eat it.")
            elif question_11 =='yes':
                question_14=input("Are you a Megalosaurus? (yes/no)\n")
                if question_14 =='yes':
                    print("Decision: Eat it.")
                elif question_14 =='no':
                    print("Decision: Don't eat it.")
eat()
                    
                    
                        
            
                    
                    
                    
            
            
                    
        
        
            
                    
                    

                           



            

        

    
    
