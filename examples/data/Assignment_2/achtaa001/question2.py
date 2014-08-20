print("Welcome to the 30 Second Rule Expert")
print("------------------------------------")
print("Answer the following questions by selecting from among the options.")
answer1= input("Did anyone see you? (yes/no)\n")
if answer1 == "yes":
    ans2 = input("Was it a boss/lover/parent? (yes/no)\n")
    if ans2 == "yes":
        ans3=input("Was it expensive? (yes/no)\n")
        if ans3 == "yes":
            ans4=input("Can you cut off the part that touched the floor? (yes/no)\n")
            if ans4 == "no":
                print("Decision: Your call.")
            else:
                print("Decision: Eat it.")
        else:
            ans4 = input("Is it chocolate? (yes/no)\n")
            if ans4 == "yes":
                print("Decision: Eat it.")
            else:
                print("Decision: Don't eat it.")
    else:
        print("Decision: Eat it.")
else:
    ans5 = input("Was it sticky? (yes/no)\n")
    if ans5 == "yes":
        ans6=input("Is it a raw steak? (yes/no)\n")
        if ans6 == "yes":
            ans7 = input("Are you a puma? (yes/no)\n")
            if ans7 == "yes":
                print("Decision: Eat it.")
            else:
                print("Decision: Don't eat it.")
        else:
            ans8=input("Did the cat lick it? (yes/no)\n")
            if ans8 == "no":
                print("Decision: Eat it.")
            else:
                ans11=input("Is your cat healthy? (yes/no)\n")
                if ans11 == "yes":
                    print("Decision: Eat it.")
                else:
                    print("Decision: Your call.")
    else:
        ans9=input("Is it an Emausaurus? (yes/no)\n")
        if ans9 == "yes":
            ans10=input("Are you a Megalosaurus? (yes/no)\n")
            if ans10 == "yes":
                print("Decision: Eat it.")
            else:
                print("Decision: Don't eat it.")
        else:
            ans11=input("Did the cat lick it? (yes/no)\n")
            if ans11 == "yes":
                ans12=input("Is your cat healthy? (yes/no)\n")
                if ans12 == "yes":
                    print("Decision: Eat it.")
                else:
                    print("Decision: Your call.")
            else:
                print("Decision: Eat it.")