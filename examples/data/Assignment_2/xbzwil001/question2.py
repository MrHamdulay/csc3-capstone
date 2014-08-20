print("Welcome to the 30 Seconds Rule")
print("------------------------------")
print("Answer the following question by selecting from among the options")
q1=input("Did anyone see you? (yes/no)\n")
if q1=="yes":
    q2=input("Was it a boss/lover/parent? (yes/no)\n")
    if q2=="no":
        print("Decision: Eat it.")
    else:
        q3=input("Was it expensive? (yes/no)\n")
        if q3=="no":
            q4=input("Is is it a chocolate? (yes/no)\n")
            if q4=="no":
                print("Decision: Don't eat it.")
            else:
                print("Decision: Eat it.")
        else:
            q5=input("Can you cut off the part that touched the floor? (yes/no)\n")
            if q5=="yes":
                print("Decision: Eat it.")
            else:
                print("Decision: Your call")
else:
    q6=input("Was it sticky? (yes/no)\n")
    if q6=="no":
        q7=input("Is it an Emausaurus? (yes/no)\n")
        if q7=="yes":
            q8=input("Are you a Megalosaurus? (yes/no)\n")
            if q8=="no":
                print("Decision: Don't eat it.")
            else:
                print("Decision: Eat it.")
        else:
            q9=input("Did the cat lick it? (yes/no)\n")
            if q9=="no":
                print("Decision: Eat it.")
            else:
                q10=input("Is your cat healthy? (yes/no)\n")
                if q10=="no":
                    print("Decision: Your call")
                else:
                    print("Decision: Eat it.")
    else:
        q11=input("Is it a raw steak? (yes/no)\n")
        if q11=="no":
            q12=input("Did the cat lick it? (yes/no)\n")
            if q12=="no":
                print("Decision: Eat it.")
            else:
                q13=input("Are you a puma? (yes/no)\n")
                if q13=="yes":
                    print("Decision: Eat it.")
                else:
                    print("Decision: Don't eat it")
                    
         

 