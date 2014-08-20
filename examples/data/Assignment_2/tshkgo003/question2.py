#ASSIGNMENT2 QUESTION2 
print("Welcome to the 30 Second Rule Expert")
print("------------------------------------")
print("Answer the following questions by selecting from among the options.")
# Z AND X ARE CHAINS OF OF QUESTIONS STEMMING FROM YOUR ANSWER TO THE FIRST TWO QUESTION EITHER YES OR NO
x=input("Did anyone see you? (yes/no)\n")
if (x) == "yes":
    b=input("Was it a boss/lover/parent? (yes/no)\n")
    if (b) == "no":
        print("Decision: Eat it.")
    else:
        a=input("Was it expensive? (yes/no)\n")
        if (a) == "yes":
            s=input("Can you cut off the part that touched the floor? (yes/no)\n")
            if (s) == "yes":
                print("Decision: Eat it.")
            else:
                print("Decision: Your call.")
        else:
            f=input("Is it chocolate? (yes/no)\n")
            if (f) == "yes":
                print("Decision: Eat it.")
            else:
                print("Decision: Don't eat it.")
else:
    z=input("Was it sticky? (yes/no)\n")
    if (z) == "yes":
        v=input("Is it a raw steak? (yes/no)\n")
        if (v) == "yes":
            m=input("Are you a puma? (yes/no)\n")
            if (m) == "yes":
                print("Decision: Eat it.")
            else:
                print("Decision: Don't eat it.")
        else:
            n=input("Did the cat lick it? (yes/no)\n")
            if (n) == "yes":
                g=input("Is your cat healthy? (yes/no)\n")
                if (g) == "yes":
                    print("Decision: Eat it.")
                else:
                    print("Decision: Your call.")
            else:
                print("Decision: Eat it.")               
    else:
        c=input("Is it an Emausaurus? (yes/no)\n")
        if (c) == "yes":
            d=input("Are you a Megalosaurus? (yes/no)\n")
            if (d) == "yes":
                print("Decision: Eat it.")
            else:
                print("Decision: Don't eat it.")
        else:
            n=input("Did the cat lick it? (yes/no)\n")
            if (n) == "yes":
                g=input("Is your cat healthy? (yes/no)\n")
                if (g) == "yes":
                    print("Decision: Eat it.")
                else:
                    print("Decision: Your call.")
            else:
                print("Decision: Eat it.")