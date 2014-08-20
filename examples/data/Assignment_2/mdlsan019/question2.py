print("Welcome to the 30 Second Rule Expert")
print("------------------------------------")
print("Answer the following questions by selecting from among the options.")
question1=input("Did anyone see you? (yes/no)\n")
if question1=="no" or question1=="NO":
    question2=input("Was it sticky? (yes/no)\n")
    if question2=="no" or question2=="NO":
        question3=input("Is it an Emausaurus? (yes/no)\n")
        if question3=="no" or question3=="NO":
            question4=(input("Did the cat lick it? (yes/no)\n"))
            if question4=="no" or question4=="NO":
                print("Decision: Eat it.")
            elif "yes" or "YES":
                question5=input("Is your cat healthy? (yes/no)\n")
                if question5=="no" or question5=="NO":
                    print("Decision: Your call.")
                else:
                    print("Decision: Eat it.")
            else:
                print()
        elif "yes" or "YES":
            question6=input("Are you a Megalosaurus? (yes/no)\n")
            if question6=="no" or question6=="NO":
                print("Decision: Don't eat it.")
                
            elif "yes" or "YES":
                print("Decision: Eat it.")
            else:
                print()
        else:
            print()
    elif "yes" or "YES":
        question7=input("Is it a raw steak? (yes/no)\n")
        if question7=="no":
            question4=(input("Did the cat lick it? (yes/no)\n"))
            if question4=="no":
                print("Decision: Eat it.")
            elif "yes" or "YES":
                question5=input("Is your cat healthy? (yes/no)\n")
                if question5=="no" or question5=="NO":
                    print("Decision: Your call.")
                elif "yes" or "YES":
                    print("Decision: Eat it.")
                else:
                    print()
        elif "yes" or "YES":
            question6=input("Are you a puma? (yes/no)\n")
            if question6=="no" or question6=="NO":
                print("Decision: Don't eat it.")
            elif "yes" or "YES":
                print("Decision: Eat it.")
            else:
                print()
        else:
            print()
    else:
        print()
elif "yes" or "YES":
    question9=input("Was it a boss/lover/parent? (yes/no)\n")
    if question9=="no" or question9=="NO":
        print("Decision: Eat it.")
    elif "yes" or "YES":
        question10=input("Was it expensive? (yes/no)\n")
        if question10=="no" or question10=="NO":
            question11=input("Is it chocolate? (yes/no)\n")
            if question11=="no" or question11=="NO":
                print("Decision: Don't eat it.")
            elif "yes" or "YES":
                print("Decision: Eat it.")
            else:
                print()
        elif "yes" or "YES":
            question12=input("Can you cut off the part that touched the floor? (yes/no)\n")
            if question12=="no" or question12=="NO":
                print("Decision: Your call.")
            elif "yes" or "YES":
                print("Decision: Eat it.")
            else:
                print()
        else:
            print()
    else:
        print()
else:
    print()

