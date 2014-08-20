def ifff():
    resp1=input("Was it a boss/lover/parent? (yes/no)\n")
    if resp1=="yes":
        resp2=input("Was it expensive? (yes/no)\n")
        if resp2=="yes":
            resp3=input("Can you cut off the part that touched the floor? (yes/no)\n")
            if resp3=="yes":
                print("Decision: Eat it.")
            else:
                print("Decision: Your call.")
        else:
            resp21=input("Is it chocolate? (yes/no)\n")
            if resp21=="yes":
                print("Decision: Eat it.")
            else:
                print("Decision: Don't eat it.")
    else:
        print("Decision: Eat it.")
        
        
def ifff1():
    resp11=input("Was it sticky? (yes/no)\n")
    if resp11=="yes":
        resp21=input("Is it a raw steak? (yes/no)\n")
        if resp21=="yes":
            resp31=input("Are you a puma? (yes/no)\n")
            if resp31=="yes":
                print("Decision: Eat it.")
            else:
                print("Decision: Don't eat it.")
        else:
            resp41=input("Did the cat lick it? (yes/no)\n")
            if resp41=="yes":
                resp51=input("Is your cat healthy? (yes/no)\n")
                if resp51=="yes":
                    print("Decision: Eat it.")
                else:
                    print("Decision: Your call.")
    else:
        resp61=input("Is it an Emausaurus? (yes/no)\n")
        if resp61=="yes":
            resp71=input("Are you a Megalosaurus? (yes/no)\n")
            if resp71=="yes":
                print("Decision: Eat it.")
            else:
                print("Decision: Don't eat it.")
        else:
            resp81=input("Did the cat lick it? (yes/no)\n")
            if resp81=="yes":
                resp91=input("Is your cat healthy? (yes/no)\n")
                if resp91=="yes":
                    print("Decision: Eat it.")
                else:
                    print("Decision: Your call.")
            else:
                print("Decision: Eat it.")
        
def decisionTree():
    print("Welcome to the 30 Second Rule Expert")
    print("------------------------------------")
    print("Answer the following questions by selecting from among the options.")
    resp00=input("Did anyone see you? (yes/no)\n")
    if resp00=="yes":
        ifff()
    else:
        ifff1()
decisionTree()
        
        
        
                

    