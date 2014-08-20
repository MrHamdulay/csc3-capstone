eat = "Decision: Eat it."
yours = "Decision: Your call."
dont = "Decision: Don't eat it."
yes = "yes"
no = "no"

print("Welcome to the 30 Second Rule Expert")
print("------------------------------------")
print("Answer the following questions by selecting from among the options.")
q1 = input("Did anyone see you? (yes/no)\n")
if q1 == yes:
    if input("Was it a boss/lover/parent? (yes/no)\n") == yes:
        if input("Was it expensive? (yes/no)\n") == yes:
            if input("Can you cut off the part that touched the floor? (yes/no)\n") == yes:
                print(eat)
            else:
                print(yours)            
        else:
            if input("Is it chocolate? (yes/no)\n") == yes:
                print(eat)
            else:
                print(dont)
    else:
        print(eat)
        
if q1 == no:
    if input("Was it sticky? (yes/no)\n") == yes:
        if input("Is it a raw steak? (yes/no) \n") == yes:
            if input("Are you a puma? (yes/no) \n") == yes:
                print(eat)
            else:
                print(dont)
        else:
            if input("Did the cat lick it? (yes/no)\n") == yes:
                if input("Is your cat healthy? (yes/no)\n") == yes:
                    print(eat)
                else:
                    print(yours)
            else:
                print(eat)
    else:
        if input("Is it an Emausaurus? (yes/no)\n") == yes:
            if input("Are you a Megalosaurus? (yes/no)\n") == yes:
                print(eat)
            else:
                print(dont)
        else:
            if input("Did the cat lick it? (yes/no)\n") == yes:
                if input("Is your cat healthy? (yes/no)\n") == yes:
                    print(eat)
                else:
                    print(yours)
            else:
                print(eat)