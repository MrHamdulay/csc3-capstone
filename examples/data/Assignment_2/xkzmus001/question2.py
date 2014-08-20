#question2.py
#Author : Musa Xakaza
#Date : 07/03/2014

print("Welcome to the 30 Second Rule Expert")
print("-"*36)
print("Answer the following questions by selecting from among the options.")
answer = input("Did anyone see you? (yes/no)\n")
decision = "Eat it."

def catLick():
    answer = input("Did the cat lick it? (yes/no)\n")
    if (answer) == "yes":
        answer = input("Is the cat healthy? (yes/no)\n")
        if (answer) == "no":
            return "Your call."
    
    return "Eat it."


if (answer) == "yes":
    answer = input("Was it a boss/lover/parent? (yes/no)\n")
    if (answer) == "yes":
        answer = input("Was it expensive? (yes/no)\n")
        if (answer) == "yes":
            answer = input("Can you eat the part that touched the floor? (yes/no)\n")
            if (answer) == "no":
                decision = "Your call."
        else :
            answer = input("Is it chocolate? (yes/no)\n")
            if (answer) == "no":
                decision = "Don't eat it."
                

elif (answer) == "no":
    answer = input("Was it sticky? (yes/no)\n")
    if (answer) == "yes":
        answer = input("Is it a raw steak? (yes/no)\n")
        if (answer) == "yes":
            answer = input("Are you a puma? (yes/no)\n")
            if (answer) == "no":
                decision = "Don't eat it."
        else:
            decision = catLick()
    else:
        answer = input("Is it an Emausaurus? (yes/no)\n")
        if (answer) == "yes":
            answer = input("Are you a Megalosaurus?(yes/no)\n")
            if (answer) == "no":
                decision = "Don't eat it."
        else:
            decision = catLick()

print("Decision:",decision)

