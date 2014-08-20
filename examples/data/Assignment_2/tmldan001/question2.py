print ("Welcome to the 30 Second Rule Expert")
print ("------------------------------------")
print ("Answer the following questions by selecting from among the options.")
#You Dropped Food on the Floor Do You Eat it?
question=input("Did anyone see you? (yes/no)\n")
if question=='no':
    question=input ("Was it sticky? (yes/no)\n")
    if question=='no':
        question=input ("Is it an Emausaurus? (yes/no)\n")
        if question=='yes':
            question=input("Are you a Megalosaurus? (yes/no)\n")
            if question=='no':
                reply=print("Decision: Don't eat it.")
            if question=='yes':
                reply=print("Decision: Eat it.")                
        elif question=='no':
            question=input("Did the cat lick it? (yes/no)\n")
            if question=='yes':
                question=input("Is your cat healthy? (yes/no)\n")
                if question=='no':
                    reply=print("Decision: Your call.")
                if question=='yes':
                    reply=print("Decision: Eat it.")
            elif question=='no':
                reply=print("Decision: Eat it.")
    elif question=='yes':
        question=input ("Is it a raw steak? (yes/no)\n")
        if question=='yes':
            question=input("Are you a puma? (yes/no)\n")
            if question=='yes':
                reply=print("Decision: Eat it.")
            if question=='no':
                reply=print("Decision: Don't eat it.")
        elif question=='no':
            question=input("Did the cat lick it? (yes/no)\n")
            if question=='no':
                reply=print("Decision: Eat it.")
            if question=='yes':
                question=input("Is your cat healthy? (yes/no)\n")
                if question=='yes':
                    reply=print("Decision: Eat it.")
                if question=='no':
                    reply=print("Decision: Your call.") 
elif question=='yes':
    question=input("Was it a boss/lover/parent? (yes/no)\n")
    if question=='no':
        question=print("Decision: Eat it.")
    if question=='yes':
        question=input("Was it expensive? (yes/no)\n")
        if question=='no':
            question=input("Is it chocolate? (yes/no)\n")
            if question=='no':
                question=print("Decision: Don't eat it.")
            if question=='yes':
                question=print("Decision: Eat it.")
                    
        elif question=='yes':
            question=input("Can you cut off the part that touched the floor? (yes/no)\n")
            if question=='no':
                question==print("Decision: Your call.")
            if question=='yes':
                question=print("Decision: Eat it.")                
    
