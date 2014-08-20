def welcome():
    message = "Welcome to the 30 Second Rule Expert"
    print(message)
    print('-' * len(message))
    print("Answer the following questions by selecting from among the options.")
    
def question(string):
    answer = input(string + " (yes/no)\n")
    if answer == "yes":
        return True
    else:
        #Assume no on any other input, as per assignment
        return False

# print heading
welcome()

# define action constants
EAT = "Eat it."
DONT_EAT = "Don't eat it."
MAYBE = "Your call."

action = ''

# begin interrogation
if question("Did anyone see you?"):
    if question("Was it a boss/lover/parent?"):
        if question("Was it expensive?"):
            if question("Can you cut off the part that touched the floor?"):
                action = EAT
            else:
                action = MAYBE
        else:
            if question("Is it chocolate?"):
                action = EAT
            else:
                action = DONT_EAT
    else:
        action = EAT
else:
    if question("Was it sticky?"):
        if question("Is it a raw steak?"):
            if question("Are you a puma?"):
                action = EAT
            else:
                action = DONT_EAT
        else:
            if question("Did the cat lick it?"):
                if question("Is your cat healthy?"):
                    action = EAT
                else:
                    action = MAYBE
            else:
                action = EAT
    else:
        if question("Is it an Emausaurus?"):
            if question("Are you a Megalosaurus?"):
                action = EAT
            else:
                action = DONT_EAT
        else:
            if question("Did the cat lick it?"):
                if question("Is your cat healthy?"):
                    action = EAT
                else:
                    action = MAYBE
            else:
                action = EAT

print('Decision:', action)
    