# Assignment 2
# Question 2
# 30 Second Expert Rule

def rule():
    print("Welcome to the 30 Second Rule Expert")
    print("-"*36)
    print("Answer the following questions by selecting from among the options.") 
    see=input("Did anyone see you? (yes/no)\n")
    if (see=='yes'):
        who=input("Was it a boss/lover/parent? (yes/no)\n")
        if who=='no':
            print("Decision: Eat it.")
        elif who=='yes':
            expensive=input("Was it expensive? (yes/no)\n")
            if expensive=='yes':
                part=input("Can you cut off the part that touched the floor? (yes/no)\n")
                if part=='yes':
                    print("Decision: Eat it.")
                elif part== 'no':
                    print("Decision: Your call.")
            elif expensive=='no':
                chocolate=input("Is it chocolate? (yes/no)\n")
                if (chocolate=='yes'):
                    print("Decision: Eat it.")
                elif (chocolate=='no'):
                    print("Decision: Don't eat it.")
    elif (see=='no'):
        sticky=input("Was it sticky? (yes/no)\n")
        if (sticky=='yes'):
            steak=input("Is it a raw steak? (yes/no)\n")
            if (steak=='yes'):
                puma=input("Are you a puma? (yes/no)\n")
                if (puma=='yes'):
                    print("Decision: Eat it.")
                elif (puma=='no'):
                    print("Decision: Don't eat it.")
            elif (steak=='no'):
                cat=input("Did the cat lick it? (yes/no)\n")
                if (cat=='yes'):
                    healthy=input("Is your cat healthy? (yes/no)\n")
                    if (healthy=='yes'):
                        print("Decision: Eat it.")
                    elif (healthy == 'no'):
                        print("Decision: Your call.")
                elif (cat=='no'):
                    print("Decision: Eat it.")
        elif (sticky=='no'):
            emausaurus=input("Is it an Emausaurus? (yes/no)\n")
            if (emausaurus=='yes'):
                megalosaurus=input("Are you a Megalosaurus? (yes/no)\n")
                if (megalosaurus=='yes'):
                    print("Decision: Eat it.")
                elif (megalosaurus=='no'):
                    print("Decision: Don't eat it.")
            elif (emausaurus=='no'):
                cat=input("Did the cat lick it? (yes/no)\n")
                if (cat=='yes'):
                    healthy=input("Is your cat healthy? (yes/no)\n")
                    if (healthy=='yes'):
                        print("Decision: Eat it.")
                    elif (healthy == 'no'):
                        print("Decision: Your call.")
                elif (cat=='no'):
                    print("Decision: Eat it.")                    
rule()
