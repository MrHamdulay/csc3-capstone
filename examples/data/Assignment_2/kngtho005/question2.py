# question2
# a program to decide whether to eat a cupcake that has fallen on the floor
# Thomas Konigkramer
# 8 March 2014

# introduction to what the program does
print("Welcome to the 30 Second Rule Expert")
print("------------------------------------")
print("Answer the following questions by selecting from among the options.")

witness = input("Did anyone see you? (yes/no)\n")
if witness == "yes":
    who_witnessed = input("Was it a boss/lover/parent? (yes/no)\n")
    if who_witnessed == "no":
        print("Decision: Eat it.")
    elif who_witnessed == "yes":
        price = input("Was it expensive? (yes/no)\n")
        if price == "yes":
            cut_off = input("Can you cut off the part that touched the floor? (yes/no) \n")
            if cut_off == "yes":
                print("Decision: Eat it.")
            elif cut_off == "no":
                print("Decision: Your call.")
        elif price == "no":
            chocolate = input("Is it chocolate? (yes/no)\n")
            if chocolate == "yes":
                print("Decision: Eat it.")
            elif chocolate == "no":
                print("Decision: Don't eat it.")
elif witness == "no":
    sticky = input("Was it sticky? (yes/no)\n")
    if sticky == "yes":
        steak = input("Is it a raw steak? (yes/no)\n")
        if steak == "yes":
            puma = input("Are you a puma? (yes/no)\n")
            if puma == "no":
                print("Decision: Don't eat it.")
            elif puma == "yes":
                print("Decision: Eat it.")
        elif steak == "no":
            cat = input("Did the cat lick it? (yes/no)\n")
            if cat == "no":
                print("Decision: Eat it.")
            elif cat == "yes":
                healthy = input("Is your cat healthy? (yes/no)\n")
                if healthy == "no":
                    print("Decision: Your call.")
                elif healthy == "yes":
                    print("Decision: Eat it.")
    elif sticky == "no":
        emausaurus = input("Is it an Emausaurus? (yes/no)\n")
        if emausaurus == "no":
            cat = input("Did the cat lick it? (yes/no)\n")
            if cat == "no":
                print("Decision: Eat it.")
            elif cat == "yes":
                healthy = input("Is your cat healthy? (yes/no)\n")
                if healthy == "no":
                    print("Decision: Your call.")
                elif healthy == "yes":
                    print("Decision: Eat it.")
        elif emausaurus == "yes":
            megalosaurus = input("Are you a Megalosaurus? (yes/no)\n")
            if megalosaurus == "no":
                print("Decision: Don't eat it.")
            elif megalosaurus == "yes":
                print("Decision: Eat it.")