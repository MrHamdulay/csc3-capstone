#Question2
#Keanon Fell
#Program to determine whther you should eat food that you dropped or not
#AI AKA Expert system /Decision tree
print("Welcome to the 30 Second Rule Expert")
print("------------------------------------")
print("Answer the following questions by selecting from among the options.")
q1 = input("Did anyone see you? (yes/no)\n")
if q1=="yes":
    q2= input("Was it a boss/lover/parent? (yes/no)\n")
    if q2=="yes":
        q3=input("Was it expensive? (yes/no)\n")
        if q3 =="yes":
            q4=input("Can you cut off the part that touched the floor? (yes/no)\n")
            if q4=="yes":
                print("Decision: Eat it.")
            elif q4=="no":
                print("Decision: Your call.")
        elif q3=="no":
            q4=input("Is it chocolate? (yes/no)\n")
            if q4=="yes":
                print("Decision: Eat it.")
            elif q4=="no":
                print("Decision: Don't eat it.")
    elif q2=="no":
        print("Decision: Eat it.")
elif q1=="no":
    q2=input("Was it sticky? (yes/no)\n")
    if q2=="yes":
        q3=input("Is it a raw steak? (yes/no)\n")
        if q3=="yes":
            q4=input("Are you a puma? (yes/no)\n")
            if q4=="yes":
                print("Decision: Eat it.")
            elif q4=="no":
                print("Decision: Don't eat it.")
        elif q3=="no":
            q4=input("Did the cat lick it? (yes/no)\n")
            if q4=="yes":
                q5=input("Is your cat healthy? (yes/no)\n")
                if q5=="yes":
                    print("Decision: Eat it.")
                elif q5=="no":
                    print("Decision: Your call.")
            elif q4=="no":
                print("Decision: Eat it.")
    elif q2=="no":
        q3=input("Is it an Emausaurus? (yes/no)\n")
        if q3=="yes":
            q4=input("Are you a Megalosaurus? (yes/no)\n")
            if q4=="yes":
                print("Decision: Eat it.")
            elif q4=="no":
                print("Decision: Don't eat it.")
        elif q3=="no":
            q4=input("Did the cat lick it? (yes/no)\n")
            if q4=="yes":
                q5=input("Is your cat healthy? (yes/no)\n")
                if q5=="yes":
                    print("Decision: Eat it.")
                elif q5=="no":
                    print("Decision: Your call.")
            elif q4=="no":
                print("Decision: Eat it.")