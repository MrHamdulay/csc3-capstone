print("Welcome to the 30 Second Rule Expert")
print("------------------------------------")
print("Answer the following questions by selecting from among the options.")

def inp(y):
    k = input(str(y+" (yes/no)\n"))
    if k == "yes":
        return True
    else: 
        return False
    
t = inp("Did anyone see you?")
if t:
    t = inp("Was it a boss/lover/parent?")
    if t:
        t = inp("Was it expensive?")
        if t:
            t = inp("Can you cut off the part that touched the floor?")
            if t:
                print("Decision: Eat it.")
            else:
                print("Decision: Your call.")
        else:
            t = inp("Is it chocolate?")
            if t:
                print("Decision: Eat it.")
            else:
                print("Decision: Don't eat it.")
    else:
        print("Decision: Eat it.")
else:
    t = inp("Was it sticky?")
    if t:
        t = inp("Is it a raw steak?")
        if t:
            t = inp("Are you a puma?")
            if t:
                print("Decision: Eat it.")
            else:
                print("Decision: Don't eat it.")
        else:
            t = inp("Did the cat lick it?")
            if t:
                t = inp("Is your cat healthy?")
                if t:
                    print("Decision: Eat it.")
                else:
                    print("Decision: Your call.")
            else:
                print("Decision: Eat it.")
    else:
        t = inp("Is it an Emausaurus?")
        if t:
            t = inp("Are you a Megalosaurus?")
            if t:
                print("Decision: Eat it.")
            else:
                print("Decision: Don't eat it.")
        else:
            t = inp("Did the cat lick it?")
            if t:
                t = inp("Is your cat healthy?")
                if t:
                    print("Decision: Eat it.")
                else:
                    print("Decision: Your call.")
            else:
                print("Decision: Eat it.")            
    
    