def main():
    print("Welcome to the 30 Second Rule Expert")
    print("-"*36,sep=" ")
    print("Answer the following questions by selecting from among the options.")
    red=(input("Did anyone see you? (yes/no)\n"))
    if (red=="yes"):
        black=(input("Was it a boss/lover/parent? (yes/no)\n")) 
        if (black=="yes"):
            green=input("Was it expensive? (yes/no)\n")
            if (green=="yes"):   
                dark=input("Can you cut off the part that touched the floor? (yes/no)\n")
                if dark=="yes":           
                    print("Decision: Eat it.")
                elif dark=="no":
                        print("Decision: Your call.")
            elif green=="no":
                    brown = input("Is it chocolate? (yes/no)\n")
                    if brown == "yes":
                        print("Decision: Eat it.")
                    elif brown=="no":
                        print("Decision: Don't eat it.")
        elif black=="no":
            print("Decision: Eat it.")    
    elif red=="no":
        pink=input("Was it sticky? (yes/no)\n")
        if pink=="yes":
            maroon=input("Is it a raw steak? (yes/no)\n")
            if maroon=="yes":
                purple=input("Are you a puma? (yes/no)\n")
                if purple=="yes":
                    print("Decision: Eat it.")
                elif purple == "no":
                    print("Decision: Don't eat it.")
            elif maroon=="no":
                peach=input("Did the cat lick it? (yes/no)\n")
                if peach=="yes":
                    blue=input("Is your cat healthy? (yes/no)\n")
                    if blue=="yes":
                        print("Decision: Eat it.")
                    elif blue=="no":
                        print("Decision: Your call.")
                elif peach=="no":
                    print("Decision: Eat it.")
        elif pink=="no":
            grey=input("Is it an Emausaurus? (yes/no)\n")
            if grey=="yes":
                mink=input("Are you a Megalosaurus? (yes/no)\n")
                if mink=="yes":
                    print("Decision: Eat it.")
                elif mink == "no":
                    print("Decision: Don't eat it.")
            elif grey=="no":
                peach=input("Did the cat lick it? (yes/no)\n")
                if peach=="yes":
                    blue=input("Is your cat healthy? (yes/no)\n")
                    if blue=="yes":
                        print("Decision: Eat it.")
                    elif blue=="no":
                        print("Decision: Your call.")
                elif peach=="no":
                    print("Decision: Eat it.")    
                
main()
            
            