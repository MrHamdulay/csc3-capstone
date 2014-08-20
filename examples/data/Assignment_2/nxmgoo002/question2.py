print("Welcome to the 30 Second Rule Expert")
print("------------------------------------")
print("Answer the following questions by selecting from among the options.")
def eat():
    b=input("Did anyone see you? (yes/no)\n")
    if (b=="yes"):
        c=input("Was it a boss/lover/parent? (yes/no)\n")
        if (c=="yes"):
            x=input("Was it expensive? (yes/no)\n")
            if (x=="yes"):
                r=input("Can you cut off the part that touched the floor? (yes/no)\n")
                if (r=="yes"):
                    print("Decision: Eat it.")
                elif (r=="no"):
                    print("Decision: Your call.")
            elif (x=="no"):
                q=input("Is it chocolate? (yes/no)\n")
                if (q=="yes"):
                    print("Decision: Eat it.")
                elif (q=="no"):
                    print("Decision: Don't eat it.")
        elif (c=="no"):
            print("Decision: Eat it.")
    elif (b=="no"):
        g=input("Was it sticky? (yes/no)\n")
        if (g=="yes"):
            d=input("Is it a raw steak? (yes/no)\n")
            if (d=="yes"):
                f=input("Are you a puma? (yes/no)\n")
                if (f=="yes"):
                    print("Decision: Eat it.")
                elif (f=="no"):
                    print("Decision: Don't eat it.")
            elif (d=="no"):
                h=input("Did the cat lick it? (yes/no)\n")
                if (h=="yes"):
                    s=input("Is your cat healthy? (yes/no)\n")
                    if (s=="yes"):
                        print("Decision: Eat it.")
                    elif (s=="no"):
                        print("Decision: Your call.")
                elif (h=="no"):
                    print("Decision: Eat it.")
        elif (g=="no"):
            p=input("Is it an Emausaurus? (yes/no)\n")
            if (p=="yes"):
                t=input("Are you a Megalosaurus? (yes/no)\n")
                if (t=="yes"):
                    print("Decision: Eat it.")
                elif (t=="no"):
                    print("Decision: Don't eat it.")
            elif (p=="no"):
                j=input("Did the cat lick it? (yes/no)\n")                
                if (j=="yes"):
                    m=input("Is your cat healthy? (yes/no)\n")
                    if (m=="yes"):
                        print("Decision: Eat it.")
                    elif (m=="no"):
                        print("Decision: Your call.")
                elif (j=="no"):
                    print("Decision: Eat it.")                  
eat()