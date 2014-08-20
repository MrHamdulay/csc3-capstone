print("Welcome to the 30 Second Rule Expert")
print("------------------------------------")
print("Answer the following questions by selecting from among the options.")
a1 = input("Did anyone see you? (yes/no)\n")
    
if (a1 == "yes"):
    a2 = input("Was it a boss/lover/parent? (yes/no)\n")
    if (a2 == "no"):
        print("Decision: Eat it.")
    if (a2 == "yes"):
        a3 = input("Was it expensive? (yes/no) \n")
        if (a3 == "no"):
            a5 = input("Is it chocolate? (yes/no)\n")
            if (a5== "no"):
                print("Decision: Don't eat it.")
            if (a5 == "yes"):
                print("Decision: Eat it.")
        if (a3 == "yes"):
            a4= input("Can you cut off the part that touched the floor? (yes/no)\n")
            if(a4 == "no"):
                print("Decision: Your call.")
            if (a4== "yes"):
                print("Decision: Eat it.")
if(a1 == "no"):
    a6 = input("Was it sticky? (yes/no)\n")
    if (a6 == "no"):
        a20 = input("Is it an Emausaurus? (yes/no)\n")
        if(a20 == "no"):
            a22 = input("Did the cat lick it? (yes/no)\n")
            if (a22 == "yes"):
                a23 = input("Is your cat healthy? (yes/no)\n")
                if (a23 == "yes"):
                    print("Decision: Eat it.")
                if (a23 == "no"):
                    print("Decision: Your call.")
            if (a22 == "no"):
                print("Decision: Eat it.")
                
        if (a20 == "yes"):
            a21 = input("Are you a Megalosaurus? (yes/no) \n")
            if(a21 == "no"):
                print("Decision: Don't eat it.")
            if (a21 == "yes"):
                print("Decision: Eat it.")
    if(a6== "yes"):
        a7= input("Is it a raw steak? (yes/no)\n")
        if(a7 == "no"):
            a9= input("Did the cat lick it? (yes/no)\n")
            if (a9 == "yes"):
                a10= input("Is your cat healthy? (yes/no)\n")
                if (a10 == "no"):
                    print("Decision: Your call.")
                if (a10 == "yes"):
                    print("Decision: Eat it.")
            if (a9 == "no"):
                print("Decision: Eat it.")
        if (a7 == "yes"):
            a8= input("Are you a puma? (yes/no)\n")
            if (a8 == "no"):
                print("Decision: Don't eat it.")
            if (a8 == "yes"):
                print("Decision: Eat it.")
    
    
