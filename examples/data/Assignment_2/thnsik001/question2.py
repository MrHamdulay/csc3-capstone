#question 2 assignment 2
def trufal(answer):
    if(answer == "yes"):
        return True
    elif(answer == "no"):
        return False
    else:
        print("Yes or No answers please\n")
        import sys
        sys.exit()
print("Welcome to the 30 Second Rule Expert")
print("------------------------------------")
print("Answer the following questions by selecting from among the options.")
answer1 = input("Did anyone see you? (yes/no)\n").lower()
if(trufal(answer1)):
    answer2 = input("Was it a boss/lover/parent? (yes/no)\n").lower()
    if(trufal(answer2)):
        answer4 = input("Was it expensive? (yes/no)\n").lower()
        if(trufal(answer4)):
            answer5 =input("Can you cut off the part that touched the floor? (yes/no)\n").lower()
            if(trufal(answer5)):
                print("Decision: Eat it.")
            else:
                print("Decision: Your call.")
        else:
            answer6 = input("Is it chocolate? (yes/no)\n").lower()
            if(trufal(answer6)):
                print("Decision: Eat it.")
            else:
                print("Decision: Don't eat it.")
    else:
        print("Decision: Eat it.")
else: 
    answer3 = input("Was it sticky? (yes/no)\n")
    if(trufal(answer3)):
        answer7 = input("Is it a raw steak? (yes/no)\n").lower()
        if(trufal(answer7)):
            answer8 = input("Are you a puma? (yes/no)\n").lower()
            if(trufal(answer8)):
                print("Decision: Eat it.")
            else:
                print("Decision: Don't eat it.")
        else:
            answer10 = input("Did the cat lick it? (yes/no)\n").lower()
            if(trufal(answer10)):
                answer11 = input("Is your cat healthy? (yes/no)\n").lower()
                if(trufal(answer11)):
                    print("Decision: Eat it.")
                else:
                    print("Decision: Your call.")
            else:
                print("Decision: Eat it.")
    else:
        answer9 = input("Is it an Emausaurus? (yes/no)\n").lower()
        if(trufal(answer9)):
            answer13 = input("Are you a Megalosaurus? (yes/no)\n").lower()
            if(trufal(answer13)):
                print("Decision: Eat it.")
            else:
                print("Decision: Don't eat it.")
        else:
            answer10 = input("Did the cat lick it? (yes/no)\n").lower()
            if(trufal(answer10)):            
                answer11 = input("Is your cat healthy? (yes/no)\n").lower()
                if(trufal(answer11)):
                    print("Decision: Eat it.")
                else:
                    print("Decision: Your call.")
            else:
                print("Decision: Eat it.")            