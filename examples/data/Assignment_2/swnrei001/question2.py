EAT = "Eat it."
DONT = "Don't eat it."
YOUR_CALL = "Your call."

def header():
    head = "Welcome to the 30 Second Rule Expert"
    print(head)
    print(len(head) * '-')
    print("Answer the following questions by selecting from among the options.")

def ask(q):
    print(q, "(yes/no)")
    return (input() == "yes")

def decide(d):
    print("Decision:", d)
    
def tree():
    if ask("Did anyone see you?"):
        if ask("Was it a boss/lover/parent?"):
            if ask("Was it expensive?"):
                if ask("Can you cut off the part that touched the floor?"):
                    decide(EAT)
                else:
                    decide(YOUR_CALL)
            else:
                if ask("Is it chocolate?"):
                    decide(EAT)
                else:
                    decide(DONT)
        else:
            decide(EAT)
    else:
        if ask("Was it sticky?"):
            if ask("Is it a raw steak?"):
                if ask("Are you a puma?"):
                    decide(EAT)
                else:
                    decide(DONT)
            else:
                if ask("Did the cat lick it?"):
                    if ask("Is your cat healthy?"):
                        decide(EAT)
                    else:
                        decide(YOUR_CALL)
                else:
                    decide(EAT)
        else:
            if ask("Is it an Emausaurus?"):
                if ask("Are you a Megalosaurus?"):
                    decide(EAT)
                else:
                    decide(DONT)
            else:
                if ask("Did the cat lick it?"):
                    if ask("Is your cat healthy?"):
                        decide(EAT)
                    else:
                        decide(YOUR_CALL)
                else:
                    decide(EAT)                
                    
header()
tree()