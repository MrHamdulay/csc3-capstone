# Decison tree program 

def desiciontree():
    print("Welcome to the 30 Second Rule Expert")
    print("------------------------------------")
    print("Answer the following questions by selecting from among the options.")
    answer = input("Did anyone see you? (yes/no)\n")
    if(answer == 'yes'):
        answer = input("Was it a boss/lover/parent? (yes/no)\n")
        if(answer == 'no'):
            print("Decision: Eat it.")
            
        elif(answer == 'yes'):
            answer = input("Was it expensive? (yes/no)\n")
            if(answer == 'yes'):
                answer = input("Can you cut off the part that touched the floor? (yes/no)\n")
                if (answer == 'yes'):
                    print("Decision: Eat it.")
                elif (answer == 'no'):
                    print("Decision: Your call.")
                    
            elif(answer == 'no'):
                answer = input("Is it chocolate? (yes/no)\n")
                if(answer == 'yes'):
                    print("Decision: Eat it.")
                elif(answer =='no'):
                    print("Decision: Don't eat it.")
                    
    elif(answer == 'no'):
        answer2 = input("Was it sticky? (yes/no)\n")
        if(answer2 == 'yes'):
            answer2 = input("Is it a raw steak? (yes/no)\n")
            if(answer2 == 'yes'):
                answer2 = input("Are you a puma? (yes/no)\n")
                if(answer2 == 'yes'):
                    print("Decision: Eat it.")
                elif(answer2 == 'no'):
                    print("Decision: Don't eat it.")
                    
            elif(answer2 == 'no'):
                answer2 = input("Did the cat lick it? (yes/no)\n")
                if(answer2 == 'yes'):
                    answer2 = input("Is your cat healthy? (yes/no)\n")
                    if(answer2 == 'yes'):
                        print("Decision: Eat it.")
                    elif(answer2 == 'no'):
                        print("Decision: Your call")
                elif(answer2 == 'no'):
                    print("Decision: Eat it.")
        elif(answer2 == 'no'):
            answer2 = input("Is it an Emausaurus? (yes/no)\n")
            if(answer2 == 'yes'):
                answer2 = input("Are you a Megalosaurus? (yes/no)\n")
                if(answer2 == 'yes'):
                    print("Decision: Eat it.")
                elif(answer2 == 'no'):
                    print("Decision: Don't eat it.")
            elif(answer2 == 'no'):
                answer2 = input("Did the cat lick it? (yes/no)\n")
                if(answer2 == 'yes'):
                    answer2 = input("Is your cat healthy? (yes/no)\n")
                    if(answer2 == 'yes'):
                        print("Decision: Eat it.")
                    elif(answer2 == 'no'):
                        print("Decision: Your call")
                elif(answer2 == 'no'):
                    print("Decision: Eat it.")                    
desiciontree() 