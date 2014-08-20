# Program to determine whether to eat food or not
# Nevarr Pillay - PLLNEV006
# 8 March 2014

def cat():
    cat = input("Did the cat lick it? (yes/no)\n")
    if(cat == "no"):
        print("Decision: Eat it.")
    else:
        health = input("Is your cat healthy? (yes/no)\n")
        if(health == "yes"):
            print("Decision: Eat it.")
        else:
            print("Decision: Your call.")    

def main():
    welcome = "Welcome to the 30 Second Rule Expert"
    print(welcome)
    print("-"*len(welcome))
    print("Answer the following questions by selecting from among the options.")
    
    seen = input("Did anyone see you? (yes/no)\n")
    if(seen == "yes"):
        person = input("Was it a boss/lover/parent? (yes/no)\n")
        if(person == "no"):
            print("Decision: Eat it.")
        else:
            expensive = input("Was it expensive? (yes/no)\n")
            if(expensive == "yes"):
                cut = input("Can you cut off the part that touched the floor? (yes/no)\n")
                if(cut == "yes"):
                    print("Decision: Eat it.")
                else:
                    print("Decision: Your call.")
            else:
                choc = input("Is it chocolate? (yes/no)\n")
                if(choc == "yes"):
                    print("Decision: Eat it.")
                else:
                    print("Decision: Don't eat it.")
    else:
        sticky = input("Was it sticky? (yes/no)\n")
        if (sticky == "yes"):
            steak = input("Is it a raw steak? (yes/no)\n")
            if(steak == "yes"):
                puma = input("Are you a puma? (yes/no)\n")
                if(puma == "yes"):
                    print("Decision: Eat it.")
                else:
                    print("Decision: Don't eat it.")
            else:
                cat()
        else:
            emau = input("Is it an Emausaurus? (yes/no)\n")        
            if(emau == "yes"):
                meg = input("Are you a Megalosaurus? (yes/no)\n")
                if(meg == "yes"):
                    print("Decision: Eat it.")
                else:
                    print("Decision: Don't eat it.")
            else:
                cat()
            
    
main()  

