print("Welcome to the 30 Second Rule Expert")
print("------------------------------------")
print('Answer the following questions by selecting from among the options.')
ans=input('Did anyone see you? (yes/no)\n')
if(ans=='yes'):
    ans2=input('Was it a boss/lover/parent? (yes/no)\n')
    if(ans2=='no'):
        print('Decision: Eat it.')
    else:
        ans3=input('Was it expensive? (yes/no)\n')
        if(ans3=='yes'):
            ans4=input('Can you cut off the part that touched the floor? (yes/no)\n')
            if(ans4=='no'):
                print('Decision: Your call.')
            else:
                print('Decision: Eat it.')
        else:
            ans5=input('Is it chocolate? (yes/no)\n')
            if(ans5=='yes'):
                print('Decision: Eat it.')
            else:
                print("Decision: Don't eat it.")
else:
    ans6=input('Was it sticky? (yes/no)\n')
    if(ans6=='yes'):
        ans7=input('Is it a raw steak? (yes/no)\n')
        if(ans7=='yes'):
            ans8=input('Are you a puma? (yes/no)\n')
            if(ans8=='no'):
                print("Decision: Don't eat it.")
            else:
                print('Decision: Eat it.')
        else:
            e=input('Did the cat lick it? (yes/no)\n')
            if(e=='no'):
                print('Decision: Eat it.')
            else:
                f=input('Is your cat healthy? (yes/no)\n')
                if(f=='no'):
                    print('Decision: Your call.')
                else:
                    print('Decision: Eat it.')
    else:
        g=input('Is it an Emausaurus? (yes/no)\n')
        if(g=='no'):
            h=input('Did the cat lick it? (yes/no)\n')
            if(h=='no'):
                print('Decision: Eat it.')
            else:
                ans10=input('Is your cat healthy? (yes/no)\n')
                if(ans10=='no'):
                    print('Decision: Your call.')
                else:
                    print('Decision: Eat it.')
        else:
            ans9=input('Are you a Megalosaurus? (yes/no)\n')
            if(ans9=='no'):
                print("Decision: Don't eat it.")
            else:
                print('Decision: Eat it.')