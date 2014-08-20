print("Welcome to the 30 Second Rule Expert")
print("------------------------------------")
print("Answer the following questions by selecting from among the options.") 
a = input("Did anyone see you? (yes/no)\n")
if a == ("yes"):
    b = input("Was it a boss/lover/parent? (yes/no)\n")
    if b == ("no"):
        print("Decision: Eat it.")
    else:
        if b == ("yes"):
            c = input("Was it expensive? (yes/no)\n")
            if c == ("no"):
                d = input("Is it chocolate? (yes/no)\n")
                if d == ("yes"):
                    print("Decision: Eat it.")
                else:
                    if d == ("no"):
                        print("Decision: Don't eat it.")
            else:
                if c == ("yes"):
                    e = input("Can you cut off the part that touched the floor? (yes/no)\n")
                    if e == ("yes"):
                        print("Decision: Eat it.")
                    else:
                            if e == ("no"):
                                print("Decision: Your call.")
else:
    if a == ("no"):
        f = input("Was it sticky? (yes/no)\n")
        if f == ("yes"):
            g = input("Is it a raw steak? (yes/no)\n")
            if g == ("yes"):
                h = input("Are you a puma? (yes/no)\n")
                if h == ("no"):
                    print("Decision: Don't eat it.")
                else:
                    if h == ("yes"):
                        print("Decision: Eat it.")
            else:
                if g == ("no"):
                    i = input("Did the cat lick it? (yes/no)\n")
                    if i == ("no"):
                        print("Decision: Eat it.")
                    else:
                        if i == ("yes"):
                            j = input("Is your cat healthy? (yes/no)\n")
                            if j == ("no"):
                                print("Decision: Your call.")
                            else:
                                if j == ("yes"): 
                                    print("Decision: Eat it.")
        else:
            if f == ("no"):
                k = input("Is it an Emausaurus? (yes/no)\n")
                if k == ("no"):
                    i = input("Did the cat lick it? (yes/no)\n")
                    if i == ("no"):
                        print("Decision: Eat it.")
                    else:
                        if i == ("yes"):
                            j = input("Is your cat healthy? (yes/no)\n")
                            if j == ("no"):
                                print("Decision: Your call.")
                            else:
                                if j == ("yes"): 
                                    print("Decision: Eat it.")                    
                else:
                    if k == ("yes"):
                        l = input("Are you a Megalosaurus? (yes/no)\n")
                        if l == ("no"):
                            print("Decision: Don't eat it.")
                        else:
                            if l == ("yes"):
                                print("Decision: Eat it.")
                                                                    
                                    