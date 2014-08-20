#you dropped your food. now decide whether to eat it or no
#13 March 2014

def food():
    print("Welcome to the 30 Second Rule Expert \n------------------------------------")
    print("Answer the following questions by selecting from among the options.")
    
    food = input("Did anyone see you? (yes/no)\n")
    if food == "yes":        
        person = input("Was it a boss/lover/parent? (yes/no)\n")
        if person == "yes":
            cost = input("Was it expensive? (yes/no)\n")       
            if cost == "yes":
                floor = input("Can you cut off the part that touched the floor? (yes/no)\n")                
                if floor == "yes":
                    print("Decision: Eat it.")
                if floor == "no":
                    print("Decision: Your call.")              
                    
            if cost == "no":
                chocolate = input("Is it chocolate? (yes/no)\n")
                if chocolate == "yes":
                    print("Decision: Eat it.")
                if chocolate == "no":
                    print("Decision: Don't eat it.")
                
        if person == "no":
            print("Decision: Eat it.")
    
    if food == "no":
        sticky = input("Was it sticky? (yes/no)\n")
        if sticky == "yes":
            raw = input("Is it a raw steak? (yes/no)\n")
            if raw == "yes":
                puma = input("Are you a puma? (yes/no)\n")
                if puma == "yes":
                    print("Decision: Eat it.")
                if puma == "no":
                    print("Decision: Don't eat it.")
            if raw == "no":
                lick_it = input("Did the cat lick it? (yes/no)\n")
                if lick_it == "yes":
                    healthy = input("Is your cat healthy? (yes/no)\n")
                    if healthy == "yes":
                        print("Decision: Eat it.")
                    if healthy == "no":
                        print("Decision: Your call.")
                if lick_it == "no":
                    print("Decision: Eat it.")
        if sticky == "no":
            emausaurus = input("Is it an Emausaurus? (yes/no)\n")
            if emausaurus == "yes":
                megalosaurus = input("Are you a Megalosaurus? (yes/no)\n")
                if megalosaurus == "yes":
                    print("Decision: Eat it.")
                if megalosaurus == "no":
                    print("Decision: Don't eat it.")
 
            if emausaurus == "no":
                lick_it = input("Did the cat lick it? (yes/no)\n")
                if lick_it == "yes":
                    healthy = input("Is your cat healthy? (yes/no)\n")
                    if healthy == "yes":
                        print("Decision: Eat it.")
                    if healthy == "no":
                        print("Decision: Your call.")
                if lick_it == "no":
                    print("Decision: Eat it.")                
food()       