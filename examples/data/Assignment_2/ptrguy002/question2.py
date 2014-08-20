def a(q):
    if input(q+" (yes/no)\n") == "yes":
        return True
    return False

def ask():
    if a("Did anyone see you?"):
        if a("Was it a boss/lover/parent?"):
            if a("Was it expensive?"):
                if a("Can you cut off the part that touched the floor?"):
                    return "Eat it."
                else:
                    return "Your call."
            else:
                if a("Is it chocolate?"):
                    return "Eat it."
                else:
                    return "Don't eat it."
        else:
            return "Eat it."
    else:
        if a("Was it sticky?"):
            if a("Is it a raw steak?"):
                if a("Are you a puma?"):
                    return "Eat it."
                else:
                    return "Don't eat it."
            else:
                if a("Did the cat lick it?"):
                    if a("Is your cat healthy?"):
                        return "Eat it."
                    else:
                        return "Your call."
                else:
                    return "Eat it."
        else:
            if a("Is it an Emausaurus?"):
                if a("Are you a Megalosaurus?"):
                    return "Eat it."
                else:
                    return "Don't eat it."
            else:
                if a("Did the cat lick it?"):
                    if a("Is your cat healthy?"):
                        return "Eat it."
                    else:
                        return "Your call."
                else:
                    return "Eat it."

print("Welcome to the 30 Second Rule Expert\n------------------------------------")
print("Answer the following questions by selecting from among the options.")
print("Decision: " + ask())
