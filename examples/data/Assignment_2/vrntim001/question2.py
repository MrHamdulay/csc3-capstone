print("Welcome to the 30 Second Rule Expert\n------------------------------------", sep="")
print("Answer the following questions by selecting from among the options.")
question_one = input("Did anyone see you? (yes/no)\n")
if question_one == "yes":
    question_two = input("Was it a boss/lover/parent? (yes/no)\n")
    if question_two == "yes":
        question_three = input("Was it expensive? (yes/no)\n")
        if question_three == "yes":
            question_four = input("Can you cut off the part that touched the floor? (yes/no)\n")
            if question_four == "yes":
                print("Decision: Eat it.")
            elif question_four == "no":
                print("Decision: Your call.")
        elif question_three == "no":
            question_five = input("Is it chocolate? (yes/no)\n")
            if question_five == "yes":
                print("Decision: Eat it.")
            elif question_five == "no":
                print("Decision: Don't eat it.")
    elif question_two == "no":
        print("Decision: Eat it.")
elif question_one == "no":
    question_six = input("Was it sticky? (yes/no)\n")
    if question_six == "yes":
        question_seven = input("Is it a raw steak? (yes/no)\n")
        if question_seven == "yes":
            question_eight = input("Are you a puma? (yes/no)\n")
            if question_eight == "no":
                print("Decision: Don't eat it.")
            elif question_eight == "yes":
                print("Decision: Eat it.")
        elif question_seven == "no":
            question_nine = input("Did the cat lick it? (yes/no)\n")
            if question_nine == "no":
                print("Decision: Eait it.")
            elif question_nine == "yes":
                question_ten = input("Is your cat healthy? (yes/no)\n")
                if question_ten == "yes":
                    print("Decision: Eat it.")
                elif question_ten == "no":
                    print("Decision: Your call.")
    elif question_six == "no":
        question_eleven = input("Is it an Emausaurus? (yes/no)\n")
        if question_eleven == "no":
            question_nine = input("Did the cat lick it? (yes/no)\n")
            if question_nine == "no":
                print("Decision: Eat it.")
            elif question_nine == "yes":
                question_ten = input("Is your cat healthy? (yes/no)\n")
                if question_ten == "yes":
                    print("Decision: Eat it.")
                elif question_ten == "no":
                    print("Decision: Your call.")  
        elif question_eleven == "yes":
            question_final = input("Are you a Megalosaurus? (yes/no)\n")
            if question_final == "yes":
                print("Decision: Eat it.")
            elif question_final == "no":
                print("Decision: Don't eat it.")

            
                