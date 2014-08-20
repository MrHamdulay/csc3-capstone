print("Welcome to the 30 Second Rule Expert")
print("------------------------------------")
print("Answer the following questions by selecting from among the options.")

eat = "Decision: Eat it."
choice = "Decision: Your call."
dont = "Decision: Don't eat it."

a = input("Did anyone see you? (yes/no)\n")

if (a == "yes"):
    a = input("Was it a boss/lover/parent? (yes/no)\n")
    if (a == "yes"):
        a = input("Was it expensive? (yes/no)\n")
        if (a == "yes"):
            a = input("Can you cut off the part that touched the floor? (yes/no)\n")
            if (a== "yes"):
                print(eat)
            elif(a == "no"):
                print(choice)
        elif(a == "no"):
            a = input("Is it chocolate? (yes/no)\n")
            if (a == "yes"):
                print(eat)
            elif(a == "no"):
                print(dont)
    elif(a == "no"):
        print(eat)

elif(a == "no"):    
    a = input("Was it sticky? (yes/no)\n")
    if (a == "yes"):
        a = input("Is it a raw steak? (yes/no)\n")
        if (a == "yes"):
            a = input("Are you a puma? (yes/no)\n")
            if (a == "yes"):
                print (eat)
            elif(a == "no"):
                print(dont)
        elif (a == "no"):
            a = input("Did the cat lick it? (yes/no)\n")
            if (a == "yes"):
                a = input("Is your cat healthy? (yes/no)\n")
                if (a == "yes"):
                    print(eat)
                elif(a == "no"):
                    print(choice)
            elif(a == "no"):
                print(eat)        
    elif(a == "no"):
        a = input("Is it an Emausaurus? (yes/no)\n")
        if (a == "yes"):
            a = input("Are you a Megalosaurus? (yes/no)\n")
            if (a == "yes"):
                print(eat)
            elif(a == "no"):
                print(dont)
        elif (a == "no"):
            a = input("Did the cat lick it? (yes/no)\n")
            if (a == "yes"):
                a = input("Is your cat healthy? (yes/no)\n")
                if (a == "yes"):
                    print(eat)
                elif(a == "no"):
                    print(choice)
            elif(a == "no"):
                print(eat)