

print("Welcome to the 30 Second Rule Expert")
print("-"*36)
print("Answer the following questions by selecting from among the options.")
q1=input("Did anyone see you? (yes/no)\n")
if q1=='yes':
    q2=input("Was it a boss/lover/parent? (yes/no)\n")
    if q2=='no':
        print("Decision: Eat it.")
    elif q2=='yes':
        q3=input("Was it expensive? (yes/no)\n")
        if q3=='yes':
            q4=input('Can you cut off the part that touched the floor? (yes/no)\n')
            if q4=='yes':
                print('Decision: Eat it.')
            elif q4=='no':
                print('Decision: Your call.')
        elif q3=='no':
            q5=input('Is it chocolate? (yes/no)\n')
            if q5=='yes':
                print('Decision: Eat it.')
            elif q5=='no':
                print("Decision: Don't eat it.")
elif q1=='no':
    p1=input("Was it sticky? (yes/no)\n")
    if p1=="yes":
        p2=input("Is it a raw steak? (yes/no)\n")
        if p2=='yes':
            p3=input("Are you a puma? (yes/no)\n")
            if p3=='no':
                print("Decision: Don't eat it.")
            elif p3=='yes':
                print("Decision: Eat it.")

        elif p2=='no':
            p4=input('Did the cat lick it? (yes/no)\n')
            if p4=='no':
                print("Decision: Eat it.")
            elif p4=='yes':
                p7=input('Is your cat healthy? (yes/no)\n')
                if p7=='no':
                    print("Decision: Your call.")
                elif p7=='yes':
                    print("Decision: Eat it.")                
                
    elif p1=='no':
        p6=input("Is it an Emausaurus? (yes/no)\n")
        if p6=='no':
            p4=input('Did the cat lick it? (yes/no)\n')
            if p4=='no':
                print("Decision: Eat it.")
            elif p4=='yes':
                p7=input('Is your cat healthy? (yes/no)\n')
                if p7=='no':
                    print("Decision: Your call.")
                elif p7=='yes':
                    print("Decision: Eat it.")
        elif p6=='yes':
            p8=input("Are you a Megalosaurus? (yes/no)\n")
            if p8=='yes':
                print("Decision: Eat it.")
            elif p8=='no':
                print("Decision: Don't eat it.")








