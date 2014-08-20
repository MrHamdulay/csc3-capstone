def food_flowchart():
    print("Welcome to the 30 Second Rule Expert\n------------------------------------")
    print("Answer the following questions by selecting from among the options.")
    question = input("Did anyone see you? (yes/no)\n")
    if question == 'yes':
        question = input("Was it a boss/lover/parent? (yes/no)\n")
        if question == 'yes':
            question = input("Was it expensive? (yes/no)\n")
            if question == 'yes':
                question = input("Can you cut off the part that touched the floor? (yes/no)\n")
                if question == 'yes':
                    print("Decision: Eat it.")
                elif question == 'no':
                    print("Decision: Your call.")
            elif question == 'no':
                question = input("Is it chocolate? (yes/no)\n")
                if question == "yes":
                    print("Decision: Eat it.")
                elif question == "no":
                    print("Decision: Don't eat it.")
                    
                
        elif question == 'no':
            print("Decision: Eat it.")
    elif question == 'no':
        question = input("Was it sticky? (yes/no)\n")
        if question == 'no':
            question = input("Is it an Emausaurus? (yes/no)\n")
            if question == 'yes':
                question = input("Are you a Megalosaurus? (yes/no)\n")
                if question == 'yes':
                    print("Decision: Eat it.")
                elif question == 'no':
                    print("Decision: Don't eat it.")
            elif question == 'no':
                question = input("Did the cat lick it? (yes/no)\n")
                if question == 'yes':
                    question = input("Is your cat healthy? (yes/no)\n")
                    if question == 'yes':
                        print("Decision: Eat it.")
                    elif question == 'no':
                        print("Decision: Your call.")
                elif question == 'no':
                    print("Decision: Eat it.")
                    
                
        elif question == 'yes':
            question = input("Is it a raw steak? (yes/no)\n")
            if question == 'yes':
                question = input("Are you a puma? (yes/no)\n")
                if question == 'yes':
                    print("Decision: Eat it.")
                elif question == 'no':
                    print("Decision: Don't eat it.")
            elif question == 'no':
                question = input("Did the cat lick it? (yes/no)\n")
                if question == 'yes':
                    question = input("Is your cat healthy? (yes/no)\n")
                    if question == 'yes':
                        print("Decision: Eat it.")
                    elif question == 'no':
                        print("Decision: Your call.")
                elif question == 'no':
                    print("Decision: Eat it.")                
                
                
            
            

        


food_flowchart()