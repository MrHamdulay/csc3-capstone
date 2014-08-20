def ask(question):
    answer = input(question+" (yes/no)\n")
    if answer=='yes':
        return True
    elif answer=='no':
        return False

decision = "Your call."

print("""
Welcome to the 30 Second Rule Expert
------------------------------------
Answer the following questions by selecting from among the options.""")

if ask("Did anyone see you?"):
    if ask("Was it a boss/lover/parent?"):
        if ask("Was it expensive?"):
            if ask("Can you cut off the part that touched the floor?"):
                decision = "Eat it."
            else:
                decision = "Your call."
        else:
            if ask("Is it chocolate?"):
                decision = "Eat it."
            else:
                decision = "Don't eat it."
    else:
        decision = "Eat it."
else:
    if ask("Was it sticky?"):
        if ask("Is it a raw steak?"):
            if ask("Are you a puma?"):
                decision = "Eat it."
            else:
                decision = "Don't eat it."
        else:
            if ask("Did the cat lick it?"):
                if ask("Is your cat healthy?"):
                    decision = "Eat it."
                else:
                    decision = "Your call."
            else:
                decision = "Eat it."
    else:
        if ask("Is it an Emausaurus?"):
            if ask("Are you a Megalosaurus?"):
                decision = "Eat it."
            else:
                decision = "Don't eat it."
        else:
            if ask("Did the cat lick it?"):
                if ask("Is your cat healthy?"):
                    decision = "Eat it."
                else:
                    decision = "Your call."
            else:
                decision = "Eat it."
            

print("Decision:",decision)