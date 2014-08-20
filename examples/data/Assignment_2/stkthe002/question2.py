
print("Welcome to the 30 Second Rule Expert")
print("------------------------------------")
print("Answer the following questions by selecting from among the options.")

def cat():
    four = input("Did the cat lick it? (yes/no) \n")
    if four == ("yes"):
        five = input("Is your cat healthy? (yes/no) \n")
        if five == ("yes"):
            print("Decision: Eat it.")
        elif five == ("no"):
            print("Decision: Your call.")
    elif four == ("no"):
        print("Decision: Eat it.")


one = input("Did anyone see you? (yes/no) \n")
if one == ("yes"):
    two = input("Was it a boss/lover/parent? (yes/no) \n")
    if two == ("yes"):
        three = input("Was it expensive? (yes/no) \n")
        if three == ("yes"):
            four = input("Can you cut off the part that touched the floor? (yes/no) \n")
            if four == ("yes"):
                print("Decision: Eat it.")
            elif four == ("no"):
                print("Decision: Your call.")
        elif three == ("no"):
            four = input("Is it chocolate? (yes/no) \n")
            if four == ("yes"):
                print("Decision: Eat it.")
            elif four == ("no"):
                print("Decision: Don't eat it.")
    elif two == ("no"):
        print("Decision: Eat it.")
elif one == ("no"):
    two = input("Was it sticky? (yes/no) \n")
    if two == ("yes"):
        three = input("Is it a raw steak? (yes/no) \n")
        if three == ("yes"):
            four = input("Are you a puma? (yes/no) \n")
            if four == ("yes"):
                print("Decision: Eat it.")
            elif four == ("no"):
                print("Decision: Don't eat it.")
        elif three == ("no"):
            cat()
    elif two == ("no"):
        three = input("Is it an Emausaurus? (yes/no) \n")
        if three == ("yes"):
            four = input("Are you a Megalosaurus? (yes/no) \n")
            if four == ("yes"):
                print("Decision: Eat it.")
            elif four == ("no"):
                print("Decision: Don't eat it.")
        elif three == ("no"):
            cat()
        
        