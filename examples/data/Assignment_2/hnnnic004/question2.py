#Welcome to the 30 Second Rule Expert
#------------------------------------
#Answer the following questions by selecting from among the options.
#Did anyone see you? (yes/no)
#yes
#Was it a boss/lover/parent? (yes/no)
#yes
#Was it expensive? (yes/no)
#yes
#Can you cut off the part that touched the floor? (yes/no)
#no
#Decision: Your call.
def cupcake():
    print("Welcome to the 30 Second Rule Expert")
    print("-"*36)
    print("Answer the following questions by selecting from among the options.")
    ans_1=input("Did anyone see you? (yes/no)\n")
    if ans_1=="yes":
        ans_2=input("Was it a boss/lover/parent? (yes/no)\n")
        if ans_2=="yes":
            ans_3=input("Was it expensive? (yes/no)\n")
            if ans_3=="yes":
                ans_4=input("Can you cut off the part that touched the floor? (yes/no)\n")
                if ans_4=="yes":
                    print("Decision: Eat it.")
                if ans_4=="no":
                    print("Decision: Your call.")
            if ans_3=="no":
                ans_4=input("Is it chocolate? (yes/no)\n")
                if ans_4=="yes":
                    print("Decision: Eat it.")
                if ans_4=="no":
                    print("Decision: Don't eat it.")
        if ans_2=="no":
            print("Decision: Eat it.")
    if ans_1=="no":
        ans_2=input("Was it sticky? (yes/no)\n")
        if ans_2=="yes":
            ans_3=input("Is it a raw steak? (yes/no)\n")
            if ans_3=="yes":
                ans_4=input("Are you a puma? (yes/no)\n")
                if ans_4=="yes":
                    print("Decision: Eat it.")
                if ans_4=="no":
                    print("Decision: Don't eat it.")
            if ans_3=="no":
                ans_4=input("Did the cat lick it? (yes/no)\n")
                if ans_4=="yes":
                    ans_5=input("Is your cat healthy? (yes/no)\n")
                    if ans_5=="yes":
                        print("Decision: Eat it.")
                    if ans_5=="no":
                        print("Decision: Your call.")
                if ans_4=="no":
                        print("Decision: Eat it.")
        if ans_2=="no":
            ans_3=input("Is it an Emausaurus? (yes/no)\n")
            if ans_3=="yes":
                ans_4=input("Are you a Megalosaurus? (yes/no)\n")
                if ans_4=="yes":
                    print("Decision: Eat it.")
                if ans_4=="no":
                    print("Decision: Don't eat it.")
            if ans_3=="no":
                ans_4=input("Did the cat lick it? (yes/no)\n")
                if ans_4=="yes":
                    ans_5=input("Is your cat healthy? (yes/no)\n")
                    if ans_5=="yes":
                        print("Decision: Eat it.")
                    if ans_5=="no":
                        print("Decision: Your call.")
                if ans_4=="no":
                    print("Decision: Eat it.")                

cupcake()
