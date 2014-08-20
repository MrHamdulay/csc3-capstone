# Program-expert system
# Author: Litha Maqungo
# 11 March 2014

print("Welcome to the 30 Second Rule Expert")
print("------------------------------------")
print("Answer the following questions by selecting from among the options.")
print("Did anyone see you? (yes/no)")
seen=input()
if seen == "yes":
    print("Was it a boss/lover/parent? (yes/no)")
    person=input()
    if person == "yes":
        print("Was it expensive? (yes/no)")
        expensive=input()
        if expensive == "yes":
            print("Can you cut off the part that touched the floor? (yes/no)")
            cut=input()
            if cut == "yes":
                print("Decision: Eat it.")
            else:
                print("Decision: Your call.")
        if expensive == "no":
            print("Is it chocolate? (yes/no)")
            chocolate=input()
            if chocolate == "yes":
                print("Decision: Eat it.")
            else:
                print("Decision: Don't eat it.")      
    if person == "no":
        print("Decision: Eat it.")
                       
if seen == "no":
    print("Was it sticky? (yes/no)")
    sticky=input()
    if sticky == "yes":
        print("Is it a raw steak? (yes/no)")
        raw=input()
        if raw == "yes":
            print("Are you a puma? (yes/no)")
            puma=input()
            if puma == "no":
                print("Decision: Don't eat it.")
            else:
                print("Decision: Eat it.")
        if raw == "no":
            print("Did the cat lick it? (yes/no)")
            cat=input()
            if cat == "yes":
                print("Is your cat healthy? (yes/no)")
                healthy=input()
            if healthy == "yes":
                print("Decision: Eat it.")
            else:
                print("Decison: Your call.")
            if cat == "no":
                print("Decision: Eat it.")        

    if sticky == "no":
        print("Is it an Emausaurus? (yes/no)")
        emausaurus=input()
        if emausaurus == "yes":
            print("Are you a Megalosaurus? (yes/no)")
            mega=input()
            if mega == "yes":
                print("Decision: Eat it.")
            else:
                print("Decision: Don't eat it.")
        if emausaurus == "no":
            print("Did the cat lick it? (yes/no)")
            cat=input()
            if cat == "yes":
                print("Is your cat healthy? (yes/no)")
                healthy=input()
                if healthy == "yes":
                    print("Decision: Eat it.")
                else:
                    print("Decision: Your call.")
            if cat == "no":
                print("Decision: Eat it.")

                
                