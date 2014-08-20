print("Welcome to the 30 Second Rule Expert")
print("------------------------------------")
print("Answer the following questions by selecting from among the options.")
q1=input("Did anyone see you? (yes/no)\n")
if q1=="yes":
    q2=input("Was it a boss/lover/parent? (yes/no)\n")
    if q2=='no':
            print("Decision: Eat it.")
    if q2=="yes":
        q10=input("Was it expensive? (yes/no)\n")
        if q10=="no":
            q11=input("Is it chocolate? (yes/no)\n")
            if q11=="no":
                print("Decision: Don't eat it.")
            if q11=="yes":
                print("Decision: Eat it.")
        if q10=="yes":
            q12=input("Can you cut off the part that touched the floor? (yes/no)\n")
            if q12=="yes":
                print("Decision: Eat it.")
            if q12=="no":
                print("Decision: Your call.")
if q1=="no":
    q3=input("Was it sticky? (yes/no)\n")
    if q3=="yes":
        q4=input("Is it a raw steak? (yes/no)\n")
        if q4=="yes":
            q6=input("Are you a puma? (yes/no)\n")
            if q6=="yes":
                print("Decision: Eat it.")
            if q6=="no":
                print("Decision: Don't eat it.")
        if q4=="no":
            q7=input("Did the cat lick it? (yes/no)\n")
            if q7=="no":
                print("Decision: Eat it.")
            if q7=="yes":
                q8=input("Is your cat healthy? (yes/no)\n")
                if q8=="no":
                    print("Decision: Your call.")
                if q8=="yes":
                    print("Decision: Eat it.")
    if q3=="no":
        q5=input("Is it an Emausaurus? (yes/no)\n")
        if q5=="no":
            q7=input("Did the cat lick it? (yes/no)\n")
            if q7=="no":
                print("Decision: Eat it.")
            if q7=="yes":
                q8=input("Is your cat healthy? (yes/no)\n")
                if q8=="yes":
                    print("Decision: Eat it.")
                if q8=="no":
                    print("Decision: Your call.")
        if q5=="yes":
            q9=input("Are you a Megalosaurus? (yes/no)\n")
            if q9=="yes":
                print("Decision: Eat it.")
            if q9=="no":
                print("Decision: Don't eat it.")
