# Author : Rayaan Fakier FKRRAY001
# Date : 07 - 03 - 2014

# Define main function
def main():
    print("\nWelcome to the 30 Second Rule Expert")
    print("------------------------------------")
    print("Answer the following questions by selecting from among the options.")
    seen = input("Did anyone see you? (yes/no)\n")
    
    #If statement + subsequent questions for being seen 
    if (seen == "yes"):
        who = input("Was it a boss/lover/parent? (yes/no)\n")
        if (who == "yes"):
            expensive = input("Was it expensive? (yes/no)\n")
            if (expensive == "yes"):
                cut_off = input("Can you cut off the part that touched the floor? (yes/no)\n")
                if (cut_off == "yes"):
                    print("Decision: Eat it.")
                elif (cut_off == "no"):
                    print("Decision: Your call.")
            elif (expensive == "no"):
                chocolate = input("Is it chocolate? (yes/no)\n")
                if (chocolate == "yes"):
                    print("Decision: Eat it.")
                elif (chocolate == "no"):
                    print("Decision: Don't eat it.")
        elif (who == "no"):
            print("Decision: Eat it.")
    #If statement + subsequent questions for not being seen         
    elif (seen == "no"):
        sticky = input("Was it sticky? (yes/no)\n")
        if(sticky == "yes"):
            raw_steak = input("Is it a raw steak? (yes/no)\n")
            if (raw_steak == "yes"):
                puma = input("Are you a puma? (yes/no)\n")
                if (puma == "yes"):
                    print("Decision: Eat it.")
                elif (puma == "no"):
                    print("Decision: Don't eat it.")
            elif (raw_steak == "no"):
                cat_lick1 = input("Did the cat lick it? (yes/no)\n")
                if (cat_lick1 == "yes"):
                    cat_healthy1 = input("Is your cat healthy? (yes/no)\n")
                    if (cat_healthy1 == "yes"):
                        print("Decision: Eat it.")
                    elif(cat_healthy1 == "no"):
                        print("Decision: Your call.")
                elif (cat_lick1 == "no"):
                    print("Decision: Eat it.")
        elif (sticky == "no"):
            emausaurus = input("Is it an Emausaurus? (yes/no)\n")
            if (emausaurus == "yes"):
                megalosaurus = input("Are you a Megalosaurus? (yes/no)\n")
                if (megalosaurus == "yes"):
                    print("Decision: Eat it.")
                elif (megalosaurus == "no"):
                    print("Decision: Don't eat it.")
            elif (emausaurus == "no"):
                cat_lick2 = input("Did the cat lick it? (yes/no)\n")
                if (cat_lick2 == "yes"):
                    cat_healthy2 = input("Is your cat healthy? (yes/no)\n")
                    if (cat_healthy2 == "yes"):
                        print("Decision: Eat it.")
                    elif (cat_healthy2 == "no"):
                        print("Decision: Your call.")
                elif (cat_lick2 == "no"):
                    print("Decision: Eat it.")
                  
main()