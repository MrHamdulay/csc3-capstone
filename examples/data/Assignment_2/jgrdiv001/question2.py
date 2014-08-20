print("Welcome to the 30 Second Rule Expert")
print("------------------------------------")
print("Answer the following questions by selecting from among the options.")
Q11=input("Did anyone see you? (yes/no)\n")
if Q11=="yes":
    Q12=input("Was it a boss/lover/parent? (yes/no)\n")
    if Q12=="yes":
        Q13=input("Was it expensive? (yes/no)\n")
        if Q13=="yes":
            Q15=input("Can you cut off the part that touched the floor? (yes/no)\n")
            if Q15=="yes":
                print("Decision: Eat it.")
            elif Q15=="no":
                print("Decision: Your call.")
        elif Q13=="no":
            Q131=input("Is it chocolate? (yes/no)\n")
            if Q131=="yes":
                print("Decision: Eat it.")
            elif Q131=="no":
                print("Decision: Don't eat it.")
    elif Q12=="no":
        print("Decision: Eat it.")
elif Q11=="no":
    Q22=input("Was it sticky? (yes/no)\n")
    if Q22=="yes":
        Q23=input("Is it a raw steak? (yes/no)\n")
        if Q23=="yes":
            Q24=input("Are you a puma? (yes/no)\n")
            if Q24=="yes":
                print("Decision: Eat it.")
            elif Q24=="no":
                print("Decision: Don't eat it.")
        elif Q23=="no":
            Q231=input("Did the cat lick it? (yes/no)\n")
            if Q231=="yes":
                Q2312=input("Is your cat healthy? (yes/no)\n")
                if Q2312=="yes":
                    print("Decision: Eat it.")
                elif Q2312=="no":
                    print("Decision: Your call.")
            elif Q231=="no":
                print("Decision: Eat it.")
    elif Q22=="no":
        Q221=input("Is it an Emausaurus? (yes/no)\n")
        if Q221=="yes":
            Q222=input("Are you a Megalosaurus? (yes/no)\n")
            if Q222=="yes":
                print("Decision: Eat it.")
            elif Q222=="no":
                print("Decision: Don't eat it.")
        elif Q221=="no":
            Q231=input("Did the cat lick it? (yes/no)\n")
            if Q231=="yes":
                Q2312=input("Is your cat healthy? (yes/no)\n")
                if Q2312=="yes":
                    print("Decision: Eat it.")
                elif Q2312=="no":
                    print("Decision: Your call.")
            elif Q231=="no":
                print("Decision: Eat it.")
            
                    
