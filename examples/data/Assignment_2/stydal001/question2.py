# Dalise Steynfaard
# STYDAL001
# Assignment 2, question 2
# March 2013

answer = ''
decision = ["Decision: Eat it.", "Decision: Don't eat it.", "Decision: Your call."]

def check_answer(x):
    if x == 'yes':
        return True
    else:
        return False

def cat_branch():
    global answer
    answer = input("Did the cat lick it? (yes/no)\n")
    if check_answer(answer):
        answer = input("Is your cat healthy? (yes/no)\n")
        if check_answer(answer):
            print(decision[0])
        else:
            print(decision[2])
    else:
        print(decision[0])
        
print("Welcome to the 30 Second Rule Expert")
print("------------------------------------")
print("Answer the following questions by selecting from among the options.")

answer = input("Did anyone see you? (yes/no)\n")
if check_answer(answer):
    answer = input("Was it a boss/lover/parent? (yes/no)\n")
    if check_answer(answer):
        answer = input("Was it expensive? (yes/no)\n")
        if check_answer(answer):
            answer = input("Can you cut off the part that touched the floor? (yes/no)\n")
            if check_answer(answer):
                print(decision[0])
            else:
                print(decision[2])
        else:
            answer = input("Is it chocolate? (yes/no)\n")
            if check_answer(answer):
                print(decision[0])
            else:
                print(decision[1])
    else:
        print(decision[0])
else:
    answer = input("Was it sticky? (yes/no)\n")
    if check_answer(answer):
        answer = input("Is it a raw steak? (yes/no)\n")
        if check_answer(answer):
            answer = input("Are you a puma? (yes/no)\n")
            if check_answer(answer):
                print(decision[0])
            else:
                print(decision[1])
        else:
            cat_branch()
    else:
        answer = input("Is it an Emausaurus? (yes/no)\n")
        if check_answer(answer):
            answer = input("Are you a Megalosaurus? (yes/no)\n")
            if check_answer(answer):
                print(decision[0])
            else:
                print(decision[1])
        else:
            cat_branch()