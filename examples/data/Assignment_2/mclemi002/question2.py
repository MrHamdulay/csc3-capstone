#emile mclennan
#q2
#09/3/14


print("Welcome to the 30 Second Rule Expert")
print("------------------------------------")
print("Answer the following questions by selecting from among the options.")

question=input("Did anyone see you? (yes/no)\n")
if question=="yes":
    boss=input("Was it a boss/lover/parent? (yes/no)\n")
    if boss=="yes":
        cost=input("Was it expensive? (yes/no)\n")
        if cost=="yes":
            fall=input("Can you cut off the part that touched the floor? (yes/no)\n")
            if fall=="yes":
                print("Decision: Eat it.")
            elif fall=="no":
                print("Decision: Your call.")
        elif cost=="no":
            choc=input("Is it chocolate? (yes/no)\n")
            if choc=="yes":
                print("Decision: Eat it.")  
            elif choc=="no":
                print("Decision: Don't eat it.")
    elif boss=="no":
        print("Decision: Eat it.")    
elif question=="no":
    sticky=input("Was it sticky? (yes/no)\n")
    if sticky=="yes":
        steak=input("Is it a raw steak? (yes/no)\n")
        if steak=="yes":
            puma=input("Are you a puma? (yes/no)\n")
            if puma=="yes":
                print("Decision: Eat it.")  
            elif puma=="no":
                print("Decision: Don't eat it.")
        elif steak=="no":
            lick=input("Did the cat lick it? (yes/no)\n")
            if lick=="yes":
                healthy=input("Is your cat healthy? (yes/no)\n")
                if healthy=="yes":
                    print("Decision: Eat it.")
                elif healthy=="no":
                    print("Decision: Your call.")
            elif lick=="no":
                print("Decision: Eat it.")            
    elif sticky=="no":
        emau=input("Is it an Emausaurus? (yes/no)\n")
        if emau=="yes":
            mega=input("Are you a Megalosaurus? (yes/no)\n")
            if mega=="yes":
                print("Decision: Eat it.")
            elif mega=="no":
                print("Decision: Don't eat it.")
        if emau=="no":
            lick=input("Did the cat lick it? (yes/no)\n")
            if lick=="yes":
                healthy=input("Is your cat healthy? (yes/no)\n")
                if healthy=="yes":
                    print("Decision: Eat it.")
                elif healthy=="no":
                    print("Decision: Your call.")
            elif lick=="no":
                print("Decision: Eat it.")