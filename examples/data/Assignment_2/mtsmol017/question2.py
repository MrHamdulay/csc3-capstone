print("Welcome to the 30 Second Rule Expert")
print("------------------------------------")
print("Answer the following questions by selecting from among the options.")
Q1=input("Did anyone see you? (yes/no)\n")
if Q1=="yes":
    Q2=input("Was it a boss/lover/parent? (yes/no)\n")
    if Q2=="no":
        print("Decision: Eat it.")
    elif Q2=="yes":     
        Q3=input("Was it expensive? (yes/no)\n")
        if Q3=="no":
            Q4=input("Is it chocolate? (yes/no)\n")
            if Q4=="no":
                print("Decision: Don't eat it.")
            elif Q4=="yes":
                print("Decision: Eat it.")
        elif Q3=="yes":
            Q5=input("Can you cut off the part that touched the floor? (yes/no)\n")
            if Q5=="yes":
                print("Decision: Eat it.")
            elif Q5=="no":
                print("Decision: Your call.")
                
elif Q1=="no":
    Q6=input("Was it sticky? (yes/no)\n")
    if Q6=="no":
        Q7=input("Is it an Emausaurus? (yes/no)\n")
        if Q7=="yes":
            Q8=input("Are you a Megalosaurus? (yes/no)\n")
            if Q8=="yes":
                print("Decision: Eat it.")
            elif Q8=="no":
                print("Decision: Don't eat it.")
        elif Q7=="no":
            Q9=input("Did the cat lick it? (yes/no)\n")
            if Q9=="no":
                print("Decision: Eat it.")
            elif Q9=="yes":
                Q10=input("Is your cat healthy? (yes/no)\n")
                if Q10=="no":
                    print("Decision: Your call.")
                elif Q10=="yes":
                    print("Decision: Eat it.")
    elif Q6=="yes":
        Q11=input("Is it a raw steak? (yes/no)\n")
        if Q11=="no":
            Q12=input("Did the cat lick it? (yes/no)\n")
            if Q12=="yes":
                Q13=input("Is your cat healthy? (yes/no)\n")
                if Q13=="yes":
                    print("Decision: Eat it.")
                elif Q13=="no":
                    print("Decision: Your call.")
        
        elif Q11=="yes":
            Q14=input("Are you a puma? (yes/no)\n")
            if Q14=="yes":
                print("Decision: Eat it.")
            elif Q14=="no":
                print("Decision: Don't eat it.")