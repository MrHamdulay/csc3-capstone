print("Welcome to the 30 Second Rule Expert")
print("------------------------------------")
print("Answer the following questions by selecting from among the options.")
ans=input("Did anyone see you? (yes/no)")
print("")
if ans=="yes":
    ans=input("Was it a boss/lover/parent? (yes/no)")
    print("")
    if ans=="yes":
        ans=input("Was it expensive? (yes/no)") 
        print("")
        if ans=="yes":
            ans=input("Can you cut off the part that touched the floor? (yes/no)")
            print("")
            if ans=="yes":
                print("Decision: Eat it.")
                print("")
            else:print("Decision: Your call.")
            print("")
        else:
            ans=input("Is it chocolate? (yes/no)")
            print("")
            if ans=="yes":
                print("Decision: Eat it.")
                print("")
            else:print("Decision: Don't eat it.")
            print("")
    else:
        print("Decision: Eat it.")
    print("")
else:
    ans=input("Was it sticky? (yes/no)")
    print("")
    if ans=="yes":
        ans=input("Is it a raw steak? (yes/no)")
        print("")
        if ans=="yes":
            ans=input("Are you a puma? (yes/no)")
            print("")
            if ans=="yes":
                print("Decision: Eat it.")
                print("")
            else:
                print("Decision: Don't eat it.")
                print("")
        else:
            ans=input("Did the cat lick it? (yes/no)")
            print("")
            if ans=="yes":
                ans=input("Is your cat healthy? (yes/no)")
                print("")
                if ans=="yes":
                    print("Decision: Eat it.")
                    print("")
                else:
                    print("Decision: Your call.")
                    print("")
            else:print("Decision: Eat it.")
            print("")
    else: 
        ans=input("Is it an Emausaurus? (yes/no)")
        print("")
        if ans=="yes":
            ans=input("Are you a Megalosaurus? (yes/no)")
            print("")
            if ans=="yes":
                print("Decision: Eat it.")
            else:
                print("Decision: Don't eat it.")
        else:
            ans=input("Did the cat lick it? (yes/no)")
            print("")
            if ans=="yes":
                ans=input("Is your cat healthy? (yes/no)")
                print("")
                if ans=="yes":
                    print("Decision: Eat it.")
                else:
                    print("Decision: Your call.")
            else: print("Decision: Eat it.")
   