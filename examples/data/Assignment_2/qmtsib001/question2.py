

#question2.py
#Created by Sibabalwe Qamata

def SecondRuleexpect():
    print("Welcome to the 30 Second Rule Expert")
    print("------------------------------------")
    print('Answer the following questions by selecting from among the options.')
    
SecondRuleexpect()

def questions():
    que_1=input('Did anyone see you? (yes/no)\n')
    if(que_1=='yes'):
        que_2=input('Was it a boss/lover/parent? (yes/no)\n')
        if(que_2=='no'):
            print('Decision: Eat it.')
        else:
            que_3=input('Was it expensive? (yes/no)\n')
            if(que_3=='yes'):
                que_4=input('Can you cut off the part that touched the floor? (yes/no)\n')
                if(que_4=='no'):
                    print('Decision: Your call.')
                else:
                    print('Decision: Eat it.')
            else:
                que_5=input('Is it chocolate? (yes/no)\n')
                if(que_5=='yes'):
                    print('Decision: Eat it.')
                else:
                    print("Decision: Don't eat it.")
    else:
        que_6=input('Was it sticky? (yes/no)\n')
        if(que_6=='yes'):
            que_7=input('Is it a raw steak? (yes/no)\n')
            if(que_7=='yes'):
                que_8=input('Are you a puma? (yes/no)\n')
                if(que_8=='no'):
                    print("Decision: Don't eat it.")
                else:
                    print('Decision: Eat it.')
            else:
                que_9=input('Did the cat lick it? (yes/no)\n')
                if(que_9=='no'):
                    print('Decision: Eat it.')
                else:
                    que_10=input('Is your cat healthy? (yes/no)\n')
                    if(que_10=='no'):
                        print('Decision: Your call.')
                    else:
                        print('Decision: Eat it.')
        else:
            que_11=input('Is it an Emausaurus? (yes/no)\n')
            if(que_11=='no'):
                que_12=input('Did the cat lick it? (yes/no)\n')
                if(que_12=='no'):
                    print('Decision: Eat it.')
                else:
                    que_13=input('Is your cat healthy? (yes/no)\n')
                    if(que_13=='no'):
                        print('Decision: Your call.')
                    else:
                        print('Decision: Eat it.')
            else:
                que_14=input('Are you a Megalosaurus? (yes/no)\n')
                if(que_14=='no'):
                    print("Decision: Don't eat it.")
                else:
                    print('Decision: Eat it.')
                    
questions()