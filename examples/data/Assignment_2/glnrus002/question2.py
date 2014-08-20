#Question 2.1
print("Welcome to the 30 Second Rule Expert")
print("------------------------------------")
print("Answer the following questions by selecting from among the options.")
see=input("Did anyone see you? (yes/no)\n")
if see=="yes":
    who=input("Was it a boss/lover/parent? (yes/no)\n")
    if who=="yes":
        cost=input("Was it expensive? (yes/no)\n")
        if cost=="yes":
            can=input("Can you cut off the part that touched the floor? (yes/no)\n")
            if can=="yes":
                print("Decision: Eat it.\n")
            else:
                print("Decision: Your call.\n")
        else:
            choc=input("Is it chocolate? (yes/no)\n")
            if choc=="yes":
                print ("Decision: Eat it.\n")
            else:
                print("Decision: Don't eat it.\n")
    else:
        print("Decision: Eat it.\n")
else:
    how=input("Was it sticky? (yes/no)\n")
    if how=="yes":
        raw=input("Is it a raw steak? (yes/no)\n")
        if raw=="yes":
            puma=input("Are you a puma? (yes/no)\n")
            if puma=="yes":
                print("Decision: Eat it.\n")
            else:
                print("Decision: Don't eat it.\n")
        else:
            cat=input("Did the cat lick it? (yes/no)\n")
            if cat=="yes":
                health =input("Is your cat healthy? (yes/no)\n")
                if health=="yes":
                    print("Decision: Eat it.\n")
                else:
                    print("Decision: Your call.\n")
            else:
                print("Decision: Eat it.\n")
    else:
        em=input("Is it an Emausaurus? (yes/no)\n")
        if em=="yes":
            meg=input("Are you a Megalosaurus? (yes/no)\n")
            if meg=="yes":
                print("Decision: Eat it.\n")
            else:
                print("Decision: Don't eat it.\n")
        else:
            cat=input("Did the cat lick it? (yes/no)\n")
            if cat=="yes":
                health =input("Is your cat healthy? (yes/no)\n")
                if health=="yes":
                    print("Decision: Eat it.\n")
                else:
                    print("Decision: Your call.\n")
            else:
                print("Decision: Eat it.\n")            
    
    
      