print("Welcome to the 30 Second Rule Expert")
print("------------------------------------")
print("Answer the following questions by selecting from among the options.")


ans = input("Did anyone see you? (yes/no)""\n")
if ans == 'yes':
    ans2 = input("Was it a boss/lover/parent? (yes/no)""\n")
    if ans2 == 'yes':
        ans3 = input("Was it expensive? (yes/no)""\n")
        if ans3 == 'yes':
            ans4= input("Can you cut off the part that touched the floor? (yes/no)""\n")
            if ans4 == 'yes':
                print("Decision: Eat it.")
            elif ans4 == 'no':
                print("Decision: Your call.")
        elif ans3 == 'no':
            ans5 = input("Is it chocolate? (yes/no)""\n")
            if ans5 == 'yes':
                print("Decision: Eat it.")
            elif ans5 == 'no':
                print("Decision: Don't eat it.")
    elif ans2 == 'no':
        print("Decision: Eat it.")
elif ans == 'no':
    ans6 = input("Was it sticky? (yes/no)""\n")
    if ans6 == 'yes':
        ans7 = input("Is it a raw steak? (yes/no)""\n")
        if ans7 == 'yes':
            ans8 = input("Are you a puma? (yes/no)""\n")
            if ans8 == 'yes':
                print("Decision: Eat it.")
            elif ans8 == 'no':
                print("Decision: Don't eat it.")
        elif ans7 == 'no':
            ans9 = input("Did the cat lick it? (yes/no)""\n")
            if ans9 == 'yes':
                ans10 = input("Is your cat healthy? (yes/no)""\n")
                if ans10=='yes':
                    print("Decision: Eat it.")
                elif ans10 == 'no':
                    print("Decision: Your call.")
            elif ans9 == 'no':
                print("Decision: Eat it.")
    elif ans6 == 'no':
        ans11 = input("Is it an Emausaurus? (yes/no)""\n")
        if ans11 == 'yes':
            ans12 = input("Are you a Megalosaurus? (yes/no)""\n")
            if ans12 == 'yes':
                print("Decision: Eat it.")
            elif ans12 == 'no':
                print("Decision: Don't eat it.")
        elif ans11 == 'no':
            ans13 = input("Did the cat lick it? (yes/no)""\n")
            if ans13 == 'yes':
                ans14 = input("Is your cat healthy? (yes/no)""\n")
                if ans14 == 'yes':
                    print("Decision: Eat it.")
                elif ans14 == 'no':
                    print("Decision: Your call.")
            elif ans13 == 'no':
                print("Decision: Eat it.")