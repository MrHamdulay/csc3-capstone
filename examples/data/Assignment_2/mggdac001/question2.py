#30 second rule expert
#author:Dacod Magagula
def main():
    print('Welcome to the 30 Second Rule Expert')
    print('------------------------------------')
    print('Answer the following questions by selecting from among the options.')
    ddany1=input('Did anyone see you? (yes/no)\n')
    #print(ddany1)
    if (ddany1=='yes'):
        wasita1=input('Was it a boss/lover/parent? (yes/no)\n')
        if (wasita1=='no'):
            print('Decision: Eat it.')
        elif (wasita1=='yes'):
            wasitexp1=input('Was it expensive? (yes/no)\n')
            if (wasitexp1=='yes'):
                cnyou1=input('Can you cut off the part that touched the floor? (yes/no)\n')
                if (cnyou1=='yes'):
                    print('Decision: Eat it.')
                elif (cnyou1=='no'):
                    print('Decision: Your call.')
            elif (wasitexp1=='no'):
                isit1=input('Is it chocolate? (yes/no)\n')
                if (isit1=='yes'):
                    print('Decision: Eat it.')
                elif(isit1=='no'):
                    print("Decision: Don't eat it.")

    elif (ddany1=='no'):
        wasitsti1=input('Was it sticky? (yes/no)\n')
        if (wasitsti1=='yes'):
            isit2=input('Is it a raw steak? (yes/no)\n')
            if (isit2=='yes'):
                areu1=input('Are you a puma? (yes/no)\n')
                if (areu1=='yes'):
                    print('Decision: Eat it.')
                elif (areu1=='no'):
                    print("Decision: Don't eat it.")
            elif (isit2=='no'):
                ddthecat=input('Did the cat lick it? (yes/no)\n')
                if (ddthecat=='no'):
                    print('Decision: Eat it.')
                elif (ddthecat=='yes'):
                    isycat=input('Is your cat healthy? (yes/no)\n')
                    if (isycat=='no'):
                        print('Decision: Your call.')
                    elif(isycat=='yes'):
                        print('Decision: Eat it.')
        elif(wasitsti1=='no'):
            isit3=input('Is it an Emausaurus? (yes/no)\n')
            if(isit3=='no'):
                ddthecat=input('Did the cat lick it? (yes/no)\n')
                if (ddthecat=='no'):
                    print('Decision: Eat it.')
                elif (ddthecat=='yes'):
                    isycat=input('Is your cat healthy? (yes/no)\n')
                    if (isycat=='no'):
                        print('Decision: Your call.')
                    elif(isycat=='yes'):
                        print('Decision: Eat it.')
            elif(isit3=='yes'):
                areu2=input('Are you a Megalosaurus? (yes/no)\n')
                if (areu2=='no'):
                    print("Decision: Don't eat it.")
                elif(areu2=='yes'):
                    print('Decision: Eat it.')
                
                
                        
                
                
                
                
          
                        
             
main()