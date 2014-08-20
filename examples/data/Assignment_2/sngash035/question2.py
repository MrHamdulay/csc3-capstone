print("Welcome to the 30 Second Rule Expert")
print("------------------------------------")
print("Answer the following questions by selecting from among the options.")
ans1 = input("Did anyone see you? (yes/no)\n")
    
if (ans1 == "yes"):
    ans2 = input("Was it a boss/lover/parent? (yes/no)\n")
    if (ans2 == "no"):
        print("Decision: Eat it.")
    if (ans2 == "yes"):
        ans3 = input("Was it expensive? (yes/no) \n")
        if (ans3 == "no"):
            ans5 = input("Is it chocolate? (yes/no)\n")
            if (ans5== "no"):
                print("Decision: Don't eat it.")
            if (ans5 == "yes"):
                print("Decision: Eat it.")
        if (ans3 == "yes"):
            ans4= input("Can you cut off the part that touched the floor? (yes/no)\n")
            if(ans4 == "no"):
                print("Decision: Your call.")
            if (ans4== "yes"):
                print("Decision: Eat it.")
if(ans1 == "no"):
    ans6 = input("Was it sticky? (yes/no)\n")
    if (ans6 == "no"):
        ans20 = input("Is it an Emausaurus? (yes/no)\n")
        if(ans20 == "no"):
            ans22 = input("Did the cat lick it? (yes/no)\n")
            if (ans22 == "yes"):
                ans23 = input("Is your cat healthy? (yes/no)\n")
                if (ans23 == "yes"):
                    print("Decision: Eat it.")
                if (ans23 == "no"):
                    print("Decision: Your call.")
            if (ans22 == "no"):
                print("Decision: Eat it.")
                
        if (ans20 == "yes"):
            ans21 = input("Are you a Megalosaurus? (yes/no) \n")
            if(ans21 == "no"):
                print("Decision: Don't eat it.")
            if (ans21 == "yes"):
                print("Decision: Eat it.")
    if(ans6== "yes"):
        ans7= input("Is it a raw steak? (yes/no)\n")
        if(ans7 == "no"):
            ans9= input("Did the cat lick it? (yes/no)\n")
            if (ans9 == "yes"):
                ans10= input("Is your cat healthy? (yes/no)\n")
                if (ans10 == "no"):
                    print("Decision: Your call.")
                if (ans10 == "yes"):
                    print("Decision: Eat it.")
            if (ans9 == "no"):
                print("Decision: Eat it.")
        if (ans7 == "yes"):
            ans8= input("Are you a puma? (yes/no)\n")
            if (ans8 == "no"):
                print("Decision: Don't eat it.")
            if (ans8 == "yes"):
                print("Decision: Eat it.")
    
    
