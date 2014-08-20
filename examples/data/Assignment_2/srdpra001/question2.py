"""
SRDPRA001
Assignment 2
Question 2
"""

print ("Welcome to the 30 Second Rule Expert")
print ("------------------------------------")

print ("Answer the following questions by selecting from among the options.")

ui = input("Did anyone see you? (yes/no)\n")
if (ui == 'yes'):
    
    ui = input("Was it a boss/lover/parent? (yes/no)\n")
    if (ui == 'yes'):
        ui = input("Was it expensive? (yes/no)\n")
        if (ui == 'yes'):
            ui = input("Can you cut off the part that touched the floor? (yes/no)\n")
            if (ui == 'yes'):
                print ("Decision: Eat it.")
            elif(ui == 'no'):
                print ("Decision: Your call.")            
        elif(ui == 'no'):
            ui = input("Is it chocolate? (yes/no)\n")
            if (ui == 'yes'):
                print ("Decision: Eat it.")
            elif(ui == 'no'):
                print ("Decision: Don't eat it.")            
    elif(ui == 'no'):
        print ("Decision: Eat it.")    
elif(ui == 'no'):
    ui = input("Was it sticky? (yes/no)\n")
    if (ui == 'yes'):
        ui = input("Is it a raw steak? (yes/no)\n")
        if (ui == 'yes'):
            ui = input("Are you a puma? (yes/no)\n")
            if (ui == 'yes'):
                print ("Decision: Eat it.")
            elif(ui == 'no'):
                print ("Decision: Don't eat it.")             
        elif(ui == 'no'):
            ui = input("Did the cat lick it? (yes/no)\n")
            if (ui == 'yes'):
                ui = input("Is your cat healthy? (yes/no)\n")
                if (ui == 'yes'):
                    print ("Decision: Eat it.")
                elif(ui == 'no'):
                    print ("Decision: Don't eat it.")                 
            elif(ui == 'no'):
                print ("Decision: Eat it.")            
    elif(ui == 'no'):
        ui = input("Is it an Emausaurus? (yes/no)\n")
        if (ui == "yes"):
            ui = input("Are you a Megalosaurus? (yes/no)\n")
            if (ui == 'yes'):
                print ("Decision: Eat it.")
            elif (ui == 'no'):
                print ("Decision: Don't eat it.")
        elif (ui == 'no'):
            ui = input("Did the cat lick it? (yes/no)\n")
            if (ui == 'yes'):
                ui = input("Is your cat healthy? (yes/no)\n")
                if (ui == 'yes'):
                    print( "Decision: Eat it.")
                elif(ui == 'no'):
                    print ("Decision: Your call.")                 
            elif(ui == 'no'):
                    print ("Decision: Eat it.")                    
    