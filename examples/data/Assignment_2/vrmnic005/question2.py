#VRMNIC005
#assignment 2.2

def food():
    print ("Welcome to the 30 Second Rule Expert \n------------------------------------ \nAnswer the following questions by selecting from among the options.")
    dropped = input("Did anyone see you? (yes/no) \n")
    if dropped == "yes":
        boss = input ("Was it a boss/lover/parent? (yes/no) \n")
        if boss == "yes":
            price = input("Was it expensive? (yes/no) \n")
            if price == "yes":
                cut = input("Can you cut off the part that touched the floor? (yes/no) \n")
                if cut == "yes":
                    print ("Decision: Eat it.")
                elif cut == "no":
                        print("Decision: Your call.")
            else:
                chocolate = input("Is it chocolate? (yes/no) \n")
                if chocolate == "yes":
                    print ("Decision: Eat it.")
                else:
                    print ("Decision: Don't eat it.")
        else:
            print ("Decision: Eat it.")
      
    else:
        sticky = input("Was it sticky? (yes/no) \n")
        if sticky == "yes":
            steak = input("Is it a raw steak? (yes/no) \n")  
            if steak == "yes":
                puma = input("Are you a puma? (yes/no) \n")
                if puma == "yes":
                    print ("Decision: Eat it.")
                else:
                    print ("Decision: Don't eat it.")
            else:
                cat = input("Did the cat lick it? (yes/no) \n")
                if cat == "yes":
                    health = input("Is your cat healthy? (yes/no) \n")
                    if health == "yes":
                        print("Decision: Eat it.")
                    else:
                        print("Decision: Your call.")
                else:
                    print ("Decision: Eat it.")
        else:
            saurus = input("Is it an Emausaurus? (yes/no) \n")
            if saurus == "yes":
                megasaurus = input("Are you a Megalosaurus? (yes/no) \n")
                if megasaurus == "yes":
                    print("Decision: Eat it.")
                else:
                    print("Decision: Don't eat it.")
            else:
                cat = input("Did the cat lick it? (yes/no) \n")
                if cat == "yes":
                    health = input("Is your cat healthy? (yes/no) \n")
                    if health == "yes":
                        print("Decision: Eat it.")
                    else:
                        print("Decision: Your call.")
                else:
                    print("Decision: Eat it.")
food()
