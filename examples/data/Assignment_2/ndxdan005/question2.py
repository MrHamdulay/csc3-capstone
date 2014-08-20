greeting="Welcome to the 30 Second Rule Expert"
print(greeting)
length_greet=len(greeting)
print("-"*length_greet)

print("Answer the following questions by selecting from among the options.")

answer_1=input("Did anyone see you? (yes/no)\n")
if answer_1=="yes":
    answer_2=input("Was it a boss/lover/parent? (yes/no)\n")
    if answer_2=="yes":
        answer_4=input("Was it expensive? (yes/no)\n")
        if answer_4=="yes":
            answer_6=input("Can you cut off the part that touched the floor? (yes/no)\n")
            if answer_6=="yes":
                print("Decision: Eat it.")
            else:
                print("Decision: Your call.")
        else:
            answer_8=input("Is it chocolate? (yes/no)\n")
            if answer_8=="yes":
                print("Decision: Eat it.")
            else:
                print("Decision: Don't eat it")
    else:
        print("Decision: Eat it.")
else:
    answer_3=input("Was it sticky? (yes/no)\n")
    if answer_3=="yes":
        answer_5=input("Is it a raw steak? (yes/no)\n")
        if answer_5=="yes":
            answer_9=input("Are you a puma? (yes/no)\n")
        else:
            answer_11=input("Did the cat lick it? (yes/no)\n")
            if answer_11=="yes":
                answer_15=input("Is your cat healthy? (yes/no)\n")
                if answer_15=="yes":
                    print("Decision: Eat it.")
                else:
                    print("Decision: Your call.")
            else:
                print("Decision: Eat it.")
    else:
        answer_7=input("Is it an Emausaurus? (yes/no)\n")
        if answer_7=="yes":
            answer_13=input("Are you a Megalosaurus? (yes/no)\n")
            if answer_13=="yes":
                print("Decision: Eat it.")
            else:
                print("Decision: Don't eat it.")
        else:
            answer_11=input("Did the cat lick it? (yes/no)\n")
            if answer_11=="yes":
                answer_15=input("Is your cat healthy? (yes/no)\n")
                if answer_15=="yes":
                    print("Decision: Eat it.")
                else:
                    print("Decision: Your call.")                
            else:
                print("Decision: Your call.")