#chumani nogwaza
print("Welcome to the 30 Second Rule Expert")
print("------------------------------------")
print("Answer the following questions by selecting from among the options.")

string1=input("Did anyone see you? (yes/no)\n")
if(string1=="yes"):
    test1=input("Was it a boss/lover/parent? (yes/no)\n")
    if(test1=="no"):
        print("Decision: Eat it.")
    else:
        if(test1=="yes"):
            test2=input("Was it expensive? (yes/no)\n")
            if(test2=="yes"):
                test3=input("Can you cut off the part that touched the floor? (yes/no)\n")
                if(test3=="yes"):
                    print("Decision: Eat it.")
                else:
                    print("Decision: Your call.")
            else:
                    if(test2=="no"):
                        test4=input("Is it chocolate? (yes/no)\n")
                        if(test4=="yes"):
                            print("Decision: Eat it.")
                        else:
                            print("Decision: Don't eat it.")
        

else:
    string2=input("Was it sticky? (yes/no)\n")
    if(string2=="yes"):
        numb1=input("Is it a raw steak? (yes/no)\n")
        if(numb1=="yes"):
            numb2=input("Are you a puma? (yes/no)\n")
            if(numb2=="no"):
                print("Decision: Don't eat it.")
            else:
                print("Decision: Eat it.")
        else:
            if(numb1=="no"):
                numb7=input("Did the cat lick it? (yes/no)\n")
                if(numb7=="yes"):
                    #print("hh")
                    numb8=input("Is your cat healthy? (yes/no)\n")
                    if(numb8=="yes"):
                        print("Decision: Eat it.")                     
                else:
                    if(numb7=="no"):
                        print("Decision: Your call.")
                 
    else:
        if(string2=="no"):
            numb3=input("Is it an Emausaurus? (yes/no)\n")
            if(numb3=="yes"):
                numb4=input("Are you a Megalosaurus? (yes/no)\n")
                if(numb4=="yes"):
                    print("Decision: Eat it.")
                else:
                    if(numb4=="no"):
                        print("Decision: Don't eat it.")
            else:
                if(numb3=="no"):
                    numb5=input("Did the cat lick it? (yes/no)\n")
                    if(numb5=="no"):
                        print("Decision: Eat it.")
                    else:
                        if(numb5=="yes"):
                                numb6=input("Is your cat healthy? (yes/no)\n")
                                if(numb6=="yes"):
                                    print("Decision: Eat it.")
                                else:
                                    print("Decision: Your call.")