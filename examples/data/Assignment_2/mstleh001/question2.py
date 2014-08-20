def andile():
    q1=input("Did the cat lick it? (yes/no)\n").lower()
    if q1=="yes":
        q1=input("Is your cat healthy? (yes/no)\n").lower()
    if q1=="yes":
        print("Decision: Eat it.")
    elif q1=="no":
        print("Decision: Your call.")
    elif q1=="no":
        print("Decision: Eat it.")

def Thirty_sec_rule():
    print("Welcome to the 30 Second Rule Expert")
    print("------------------------------------")
    print("Answer the following questions by selecting from among the options.")
    q1=input("Did anyone see you? (yes/no)\n")
    if q1=="no":
        q1=input("Was it sticky? (yes/no)\n").lower()
        if q1=="yes":
            q1=input("Is it a raw steak? (yes/no)\n").lower()
            if q1=="yes":
                q1=input("Are you a puma? (yes/no)\n").lower()
                if q1=="yes":
                    print("Decision: Eat it.")
                elif q1=="no":
                    print("Decision: Don't eat it.")
            elif q1=="no":
                andile()
        elif q1=="no":
            q1=input("Is it an Emausaurus? (yes/no)\n").lower()
            if q1=="no":
                andile()
            elif q1=="yes":
                q1=input("Are you a Megalosaurus? (yes/no)\n")
                if q1=="no":
                    print("Decision: Don't eat it.")
                elif q1=="yes":
                    print("Decision: Eat it.")
    if q1=="yes":
        q1=input("Was it a boss/lover/parent? (yes/no)\n")
        if q1=="no":
            print("Decision: Eat it.")
        elif q1=="yes":
            q1=input("Was it expensive? (yes/no)\n")
            if q1=="no":
                q1=input("Is it chocolate? (yes/no)\n")
                if q1=="no":
                    print("Decision: Don't eat it.")
                elif q1=="yes":
                    print("Decision: Eat it.")
            elif q1=="yes":
                q1=input("Can you cut off the part that touched the floor? (yes/no)\n")
                if q1=="yes":
                    print("Decision: Eat it.")
                elif q1=="no":
                    print("Decision: Your call.")
Thirty_sec_rule()