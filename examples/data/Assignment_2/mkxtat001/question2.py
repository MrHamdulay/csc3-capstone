#Tato Moaki MKXTAT001
#Decision tree on thirty second rule
#question2 Assignment2
def main():
    print("Welcome to the 30 Second Rule Expert")
    print("------------------------------------")
    print("Answer the following questions by selecting from among the options.")
    Selection1 =  (input("Did anyone see you? (yes/no)\n"))
    
    if(Selection1 == 'yes'):
        Selection2 = (input("Was it a boss/lover/parent? (yes/no)\n"))
        if(Selection2 == 'no'):
            print("Decision: Eat it.")
        elif(Selection2 == 'yes'):
            Selection3 = (input("Was it expensive? (yes/no)\n"))
            if(Selection3 == 'yes'):
                Selection4 = (input("Can you cut off the part that touched the floor? (yes/no)\n"))
                if(Selection4 == 'yes'):
                    print("Decision: Eat it.")
                elif(Selection4 == 'no'):
                    print("Decision: Your call.")
            elif(Selection3 == 'no'):
                Selection5 = input("Is it chocolate? (yes/no)\n")
                if(Selection5 == 'yes'):
                    print("Decision: Eat it.")
                elif(Selection5 == 'no'):
                    print("Decision: Don't eat it.")
                    
    elif(Selection1 == 'no'):
        Selection6 = input("Was it sticky? (yes/no)\n")
        if(Selection6 == 'yes'):
            Selection7 = (input("Is it a raw steak? (yes/no)\n"))
            if(Selection7 == 'yes'):
                Selection8 = (input("Are you a puma? (yes/no)\n"))
                if(Selection8 == 'yes'):
                    print("Decision: Eat it.")
                elif(Selection8 == 'no'):
                    print("Decision: Don't eat it.")
            elif(Selection7 == 'no'):
                Selection9 = input("Did the cat lick it? (yes/no) \n")
                if(Selection9 == 'yes'):
                    Selection10 = input("Is your cat healthy? (yes/no)\n")
                    if(Selection10 == 'yes'):
                        print("Decision: Eat it.")
                    elif(Selection10 == 'no'):
                        print("Decision: Your call.")
                elif(Selection9 == 'no'):
                    print("Decision: Eat it.")
        elif(Selection6 == 'no'):
            Selection11 = input("Is it an Emausaurus? (yes/no)\n")
            if(Selection11 == 'yes'):
                Selection12 = input("Are you a Megalosaurus? (yes/no)\n")
                if(Selection12 == 'yes'):
                    print("Decision: Eat it.")
                elif(Selection12 == 'no'):
                    print("Decision: Don't eat it.")
            elif(Selection11 == 'no'):
                Selection13 = input("Did the cat lick it? (yes/no)\n")
                if(Selection13 == 'yes'):
                    Selection14 = input("Is your cat healthy? (yes/no)\n")
                    if(Selection14 == 'yes'):
                        print("Decision: Eat it.")
                    elif(Selection14 == 'no'):
                        print("Decision: Your call.")
                elif(Selection13 == 'no'):
                    print("Decision: Eat it.")
main()                  
                        
