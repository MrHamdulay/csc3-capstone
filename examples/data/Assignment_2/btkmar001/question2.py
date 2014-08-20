print("Welcome to the 30 Second Rule Expert")
print("------------------------------------")
print("Answer the following questions by selecting from among the options.")
answer1 = input("Did anyone see you? (yes/no)\n")
if answer1 == "yes":
    answer2 = input("Was it a boss/lover/parent? (yes/no)\n")
    if answer2 == "yes":
        answer3 = input("Was it expensive? (yes/no)\n")
        if answer3 == "yes":
            answer4 = input("Can you cut off the part that touched the floor? (yes/no)\n")
            if answer4 == "yes":
                print("Decision: Eat it.")
            else:
                print("Decision: Your call.")
        else:
            answer4 = input("Is it chocolate? (yes/no)\n")
            if answer4 == "yes":
                print("Decision: Eat it.")
            else:
                print("Decision: Don't eat it.")
    else:
        print("Decision: Eat it.")
else:
    answer2 = input("Was it sticky? (yes/no)\n")
    if answer2 == "yes":
        answer3 = input("Is it a raw steak? (yes/no)\n")
        if answer3 == "yes":
            answer4 = input("Are you a puma? (yes/no)\n")
            if answer4 == "yes":
                print("Decision: Eat it.")
            else:
                print("Decision: Don't eat it.")
        else:
            answer4 = input("Did the cat lick it? (yes/no)\n")
            if answer4 == "yes":
                answer5 = input("Is your cat healthy? (yes/no)\n")
                if answer5 == "yes":
                    print("Decision: Eat it.")
                else:
                    print("Decision: Your call.")
            else:
                print("Decision: Eat it.")
    else:
        answer3 = input("Is it an Emausaurus? (yes/no)\n")
        if answer3 == "yes":
            answer4 = input("Are you a Megalosaurus? (yes/no)\n")
            if answer4 == "yes":
                print("Decision: Eat it.")
            else:
                print("Decision: Don't eat it.")
        else:
            answer4 = input("Did the cat lick it? (yes/no)\n")
            if answer4 == "yes":
                answer5 = input("Is your cat healthy? (yes/no)\n")
                if answer5 == "yes":
                    print("Decision: Eat it.")
                else:
                    print("Decision: Your call.")
            else:
                print("Decision: Eat it.")                     