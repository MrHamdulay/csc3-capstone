print("Welcome to the 30 Second Rule Expert")
print("------------------------------------")
print("Answer the following questions by selecting from among the options.")
x=input("Did anyone see you? (yes/no)\n")
if(x=="yes" or x=="Yes"):
    y=input("Was it a boss/lover/parent? (yes/no)\n")
    if(y=="yes" or y=="Yes"):
            w=input("Was it expensive? (yes/no)\n")
            if(w=="yes" or w=="Yes"):
                t=input("Can you cut off the part that touched the floor? (yes/no)\n")
                if(t=="yes" or t=="Yes"):
                    print("Decision: Eat it.")
                else:
                    print("Decision: Your call.")
            else:
                t=input("Is it chocolate? (yes/no)\n")
                if(t=="yes" or t=="Yes"):
                    print("Decision: Eat it.")
                else:
                    print("Decision: Don't eat it.")
    else:
        print("Decision: Eat it.")
else:
    y=input("Was it sticky? (yes/no)\n")
    if(y=="Yes" or y=="yes"):
        w=input("Is it a raw steak? (yes/no)\n")
        if(w=="Yes" or w=="yes"):
            t=input("Are you a puma? (yes/no)\n")
            if(t=="yes" or t=="yes"):
                print("Decision: Eat it.")
            else:
                print("Decision: Don't eat it.")
        else:
            t=input("Did the cat lick it? (yes/no)\n")
            if(t=="yes" or t=="Yes"):
                c=input("Is your cat healthy? (yes/no)\n")
                if(c=="Yes" or c=="yes"):
                                    print("Decision: Eat it.")
                else:
                    print("Decision: Your call.")
    else:
        w=input("Is it an Emausaurus? (yes/no)\n")
        if(w=="Yes" or w=="yes"):
            t=input("Are you a Megalosaurus? (yes/no)\n")
            if(t=="Yes" or t=="yes"):
                print("Decision: Eat it.")
            else:
                print("Decision: Don't eat it.")
        else:
            t=input("Did the cat lick it? (yes/no)\n")
            if(t=="yes" or t=="Yes"):
                c=input("Is your cat healthy? (yes/no)\n")
                if(c=="Yes" or c=="yes"):
                    print("Decision: Eat it.")
                else:
                    print("Decision: Your call.")
            else:
                print("Decision: Eat it.")
                
    



