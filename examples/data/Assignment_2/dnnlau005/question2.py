#'The 30 Second Rule Expert' Program (Assignment 2: Question 2)"
#Name: Lauren Denny
#Student Number: DNNLAU005
#Date: 10 March 2014

print("Welcome to the 30 Second Rule Expert")
print("-"*36)
print("Answer the following questions by selecting from among the options.")

see=input("Did anyone see you? (yes/no)\n")
if see=="yes":
    who=input("Was it a boss/lover/parent? (yes/no)\n")
    if who=="no":
        print("Decision: Eat it.")
    elif who=="yes":
        price=input("Was it expensive? (yes/no)\n")
        if price=="yes":
            cut=input("Can you cut off the part that touched the floor? (yes/no)\n")
            if cut=="yes":
                print("Decision: Eat it.")
            elif cut=="no":
                print("Decision: Your call.")
        elif price=="no":
            choc=input("Is it chocolate? (yes/no)\n")
            if choc=="yes":
                print("Decision: Eat it.")
            elif choc=="no":
                print("Decision: Don't eat it.")
elif see=="no":
    sticky=input("Was it sticky? (yes/no)\n")
    if sticky=="yes":
        steak=input("Is it a raw steak? (yes/no)\n")
        if steak=="yes":
            puma=input("Are you a puma? (yes/no)\n")
            if puma=="no":
                print("Decision: Don't eat it.")
            elif puma=="yes":
                print("Decision: Eat it.")
        elif steak=="no":
            lick=input("Did the cat lick it? (yes/no)\n")
            if lick=="no":
                print("Decision: Eat it.")
            elif lick=="yes":
                healthy=input("Is your cat healthy? (yes/no)\n")
                if healthy=="no":
                    print("Decision: Your call.")
                elif healthy=="yes":
                    print("Decision: Eat it.")
    elif sticky=="no":
        Emausaurus=input("Is it an Emausaurus? (yes/no)\n")
        if Emausaurus=="no":
            lick=input("Did the cat lick it? (yes/no)\n")
            if lick=="no":
                print("Decision: Eat it.")
            elif lick=="yes":
                healthy=input("Is your cat healthy? (yes/no)\n")
                if healthy=="no":
                    print("Decision: Your call.")
                elif healthy=="yes":
                    print("Decision: Eat it.")  
        elif Emausaurus=="yes":
            Mega=input("Are you a Megalosaurus? (yes/no)\n")
            if Mega=="no":
                print("Decision: Don't eat it.")
            elif Mega=="yes":
                print("Decision: Eat it.")
            