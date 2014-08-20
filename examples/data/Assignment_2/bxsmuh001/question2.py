#Assignment 2, Question 2
#Author: Sabir Buxsoo
#Class: CSC1015F 2014
#Date Created: 08/03/2014

#A cupcake was dropped and you are in a dilemma. The program is designed to find out whether you eat the cupcake or not, by asking a series of questions.

#Pre-condition: Ask a series of questions to determine if cupcake is edible.
#Post-condition: Output decision.

#Defining the function edibleCupcake() to make the decision.
def edibleCupcake():
    #Welcome output
    print("Welcome to the 30 Second Rule Expert")
    print("------------------------------------")
    print("Answer the following questions by selecting from among the options.")
    
    #Variables
    seen = input("Did anyone see you? (yes/no)\n")
    
    #Defining a function to check if cat licked the food
    def checkCatLick():
        catLick = input("Did the cat lick it? (yes/no)\n")
        if(catLick == "yes"):
            healthyCat = input("Is your cat healthy? (yes/no)\n")
            if(healthyCat == "yes"):
                print("Decision: Eat it.")
            if(healthyCat == "no"):
                print("Decision: Your call.")
                
        if(catLick == "no"):
            print("Decision: Eat it.") #End checkCatLick() function.      
    
    #Pre-condition: Check whether someone saw you or not.
    #Post-condition: Follow with a series of questions and output decision.
    if(seen == "yes"): #Someone saw you.
        
        #Pre-condition: Check who saw you.
        #Post-condition: Follow with a series of questions and output decision.        
        whoWasIt = input("Was it a boss/lover/parent? (yes/no)\n")
        
        if(whoWasIt == "yes"): #Boss, lover or parent saw you.            
            #Pre-condition: Check if price was expensive or not.
            #Post-condition: Follow with a series of questions and output decision.            
            price = input("Was it expensive? (yes/no)\n")
            
            if(price == "yes"): #Expensive
                #Pre-condition: Check if you can cut off the part in contact with floor.
                #Post-condition: Output decision.                
                cutOff = input("Can you cut off the part that touched the floor? (yes/no)\n")                
                if(cutOff == "yes"): #Can cut off
                    print("Decision: Eat it.")
                if(cutOff == "no"): #Cannot cut off
                    print("Decision: Your call.")
            
            if(price == "no"): #Not expensive
                #Pre-condition: Check if chocolate or not.
                #Post-condition: Output decision.
                chocolate = input("Is it chocolate? (yes/no)\n")
                if(chocolate == "yes"): #Is chocolate
                    print("Decision: Eat it.")
                if(chocolate == "no"): #Is not chocolate
                    print("Decision: Don't eat it.")                
              
        if(whoWasIt == "no"): #Was not Boss, lover or parent.
            print("Decision: Eat it.")
          
    if(seen == "no"): #Noone saw you.
        #Pre-condition: Check whether it was sticky or not.
        #Post-condition: Follow with a series of questions and make decision.
        sticky = input("Was it sticky? (yes/no)\n")
        if(sticky == "yes"): #It was sticky
            
            #Pre-condition: Check whether it is a raw steak or not.
            #Post-condition: Check if you're a puma or a cat and output decision.            
            rawSteak = input("Is it a raw steak? (yes/no)\n")                        
            if(rawSteak == "yes"): #Raw steak.
                puma = input("Are you a puma? (yes/no)\n") #Check puma.
                if(puma == "yes"): #Is puma.
                    print("Decision: Eat it.")
                if(puma == "no"): #Is not puma.
                    print("Decision: Don't eat it.")
            
            if(rawSteak == "no"): #Not raw steak.
                checkCatLick() #Check cat.
        
        if(sticky == "no"): #It was not sticky.
            #Pre-condition: Check whether it is an Emausaurus or not.
            #Post-condition: Check if you're a megalosaurus or checkCatLick() and output decision.            
            emausaurus = input("Is it an Emausaurus? (yes/no)\n")
            if(emausaurus == "yes"): #Is Emausaurus.
                megalosaurus = input("Are you a Megalosaurus? (yes/no)\n")
                if(megalosaurus == "yes"): #Is Megalosaurus.
                    print("Decision: Eat it.")
                
                if(megalosaurus == "no"): #Is not Megalosaurus.
                    print("Decision: Don't eat it.")
                    
            
            if(emausaurus == "no"): #Is not Emausaurus.
                checkCatLick() #Check if cat licked or not.
                    
edibleCupcake()