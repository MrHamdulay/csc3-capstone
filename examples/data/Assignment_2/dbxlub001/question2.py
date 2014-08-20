print("Welcome to the 30 Second Rule Expert")
print("------------------------------------")
print("Answer the following questions by selecting from among the options.")
def eat_it():
    see=input("Did anyone see you? (yes/no)\n")
    if(see=="yes"):
        who=input("Was it a boss/lover/parent? (yes/no)\n")
        if(who=="no"):
            print("Decision: Eat it.")
        else:
            if(who=="yes"):
                price=input("Was it expensive? (yes/no)\n")
                if(price=="yes"):
                    floor=input("Can you cut off the part that touched the floor? (yes/no)\n")
                    if(floor=="yes"):
                        print("Decision: Eat it.")
                    else:
                        if(floor=="no"):
                            print("Decision: Your call.")
                else:
                    if(price=="no"):
                        choc=input("Is it chocolate? (yes/no)\n")
                        if(choc=="yes"):
                            print("Decision: Eat it.")
                        else:
                            if(choc=="no"):
                                print("Decision: Don't eat it.")
    else:
        if(see=="no"):
            sticky=input("Was it sticky? (yes/no)\n")
            if(sticky=="yes"):
                raw=input("Is it a raw steak? (yes/no)\n")
                if(raw=="yes"):
                    puma=input("Are you a puma? (yes/no)\n")
                    if(puma=="no"):
                        print("Decision: Don't eat it.")
                    else:
                        if(puma=="yes"):
                            print("Decision: Eat it.")
                else:
                    if(raw=="no"):
                        cat=input("Did the cat lick it? (yes/no)\n")
                        if(cat=="no"):
                            print("Decision: Eat it.")
                        else:
                            if(cat=="yes"):
                                health=input("Is your cat healthy? (yes/no)\n")
                                if(health=="no"):
                                    print("Decision: Your call.")
                                else:
                                    if(health=="yes"):
                                        print("Decision: Eat it.")
            else:
                if(sticky=="no"):
                    sorus=input("Is it an Emausaurus? (yes/no)\n")
                    if(sorus=="no"):
                        cat=input("Did the cat lick it? (yes/no)\n")
                        if(cat=="no"):
                            print("Decision: Eat it.")
                        else:
                            if(cat=="yes"):
                                health=input("Is your cat healthy? (yes/no)\n")
                                if(health=="no"):
                                    print("Decision: Your call.")
                                else:
                                    if(health=="yes"):
                                        print("Decision: Eat it.")
                    else:
                        if(sorus=="yes"):
                            mega=input("Are you a Megalosaurus? (yes/no)\n")
                            if(mega=="no"):
                                print("Decision: Don't eat it.")
                            else:
                                if(mega=="yes"):
                                    print("Decision: Eat it.")
eat_it()
                                