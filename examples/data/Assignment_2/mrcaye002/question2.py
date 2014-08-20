#30 Second Rule Expert
#Ayesha Marcus
#10/03/2014

def Cupcake():
    print("Welcome to the 30 Second Rule Expert")
    print("------------------------------------")
    print("Answer the following questions by selecting from among the options.")
    See_You=input("Did anyone see you? (yes/no) \n")
    if (See_You=="yes"):
        Boss_Lover_Parent=input("Was it a boss/lover/parent? (yes/no) \n")
        if (Boss_Lover_Parent=="yes"):
            Expensive=input("Was it expensive? (yes/no) \n")
            if (Expensive=="yes"):
                Touch_Floor=input("Can you cut off the part that touched the floor? (yes/no) \n")                
                if (Touch_Floor=="yes"):
                    print("Decision: Eat it.")
                else:
                    print("Decision: Your call.")
                
            else: 
                Chocolate=input("Is it chocolate? (yes/no)\n")
                if (Chocolate=="yes"):
                    print("Decision: Eat it.")
                else:
                    print("Decision: Don't eat it.")
        else:
            print("Decision: Eat it.")
    else: 
        Sticky=input("Was it sticky? (yes/no) \n")
        if (Sticky=="yes"):
            Steak=input("Is it a raw steak? (yes/no) \n")
            if (Steak=="yes"):
                Puma=input("Are you a puma? (yes/no) \n")
                if (Puma=="yes"):
                    print("Decision: Eat it.")
                else:
                    print("Decision: Don't eat it.")
            else:
                Cat=input("Did the cat lick it? (yes/no) \n")
                if (Cat=="yes"):
                    Healthy=input("Is your cat healthy? (yes/no) \n")
                    if (Healthy=="yes"):
                        print("Decision: Eat it.")
                    else:
                        print("Decision: Your call.")
                else:
                    print("Decision: Eat it.")
        else:
            Emausaurus=input("Is it an Emausaurus? (yes/no) \n")
            if (Emausaurus=="yes"):
                Megalosaurus=input("Are you a Megalosaurus? (yes/no) \n")
                if (Megalosaurus=="yes"):
                    print("Decision: Eat it.")
                else:
                    print("Decision: Don't eat it.")
            else:
                Cat=input("Did the cat lick it? (yes/no) \n")
                if (Cat=="yes"):
                    Healthy=input("Is your cat healthy? (yes/no) \n")
                    if (Healthy=="yes"):
                        print("Decision: Eat it.")
                    else:
                        print("Decision: Your call.")
                else:
                    print("Decision: Eat it.")                
Cupcake()