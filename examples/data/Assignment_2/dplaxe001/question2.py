print("Welcome to the 30 Second Rule Expert")
print("------------------------------------");
print("Answer the following questions by selecting from among the options.")
caught = input("Did anyone see you? (yes/no)\n")

if caught=='yes' or caught == 'Yes':
    whoCaught = input("Was it a boss/lover/parent? (yes/no)\n")
    if whoCaught=='yes' or whoCaught == 'Yes':
        expensive = input("Was it expensive? (yes/no)\n")
        if expensive == 'yes' or expensive == 'Yes':
            cut = input("Can you cut off the part that touched the floor? (yes/no)\n")
            if(cut == 'yes' or cut == 'Yes'):
                print("Decision: Eat it.")
            else:
                print("Decision: Your call.")
        else:
            choc = input("Is it chocolate? (yes/no)\n")
            if(choc == 'yes' or choc == 'Yes'):
                print("Decision: Eat it.")
            else:
                print("Decision: Don't eat it.") 
    else:
        print("Decision: Eat it.")
else:
    sticky = input("Was it sticky? (yes/no)\n")
    if(sticky == 'yes' or sticky == 'Yes'):
        steak = input("Is it a raw steak? (yes/no)\n")
        if(steak == 'yes' or steak == 'Yes'):
            puma = input("Are you a puma? (yes/no)\n")
            if(puma == 'yes' or puma == 'Yes'):
                print("Decision: Eat it.")
            else:
                print("Decision: Don't eat it.")
        else:
            lick = input("Did the cat lick it? (yes/no)\n")
            if(lick == 'yes' or lick == 'Yes'):
                health = input("Is your cat healthy? (yes/no)\n")
                if(health == 'yes' or health == 'Yes'):
                    print("Decision: Eat it.") 
            else:
                print("Decision: Eat it.")
                
    else:
        emau = input("Is it an Emausaurus? (yes/no)\n")
        if(emau == 'yes' or emau == 'Yes'):
            mega = input("Are you a Megalosaurus? (yes/no)\n")
            if(mega == 'yes' or mega == 'Yes'):
                print("Decision: Eat it.")
            else:
                print("Decision: Don't eat it.")
        else:
            lick = input("Did the cat lick it? (yes/no)\n")
            if(lick == 'yes' or lick == 'Yes'):
                health = input("Is your cat healthy? (yes/no)\n")
                if(health == 'yes' or health == 'Yes'):
                    print("Decision: Eat it.")
                else:
                    print("Decision: Your call.")
            else:
                print("Decision: Eat it.")            
            


