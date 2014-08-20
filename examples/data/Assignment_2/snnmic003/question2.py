def catLick ():
    option = input ("Did the cat lick it? (yes/no)\n")
    
    if (option == "yes"):
        option = input ("Is your cat healthy? (yes/no)\n")
        
        if (option == "yes"):
            output(1)
            
        elif (option == "no"):
            output(3)  
            
    elif (option == "no"):
        output(1)


def main():
    
    print ("Welcome to the 30 Second Rule Expert")
    print ("------------------------------------")
    print ("Answer the following questions by selecting from among the options.")
    
    option = input ("Did anyone see you? (yes/no)\n")
    
    if (option == "yes"):
        option = input ("Was it a boss/lover/parent? (yes/no)\n")
        
        if (option == "no"):
            output(1)
        
        elif (option == "yes"):
            option = input ("Was it expensive? (yes/no)\n")
            
            if (option == "yes"):
                option = input ("Can you cut off the part that touched the floor? (yes/no)\n")
                
                if (option == "no"):
                    output(3)
                    
                elif (option == "yes"):
                    output(1)
                    
            elif (option == "no"):
                option = input ("Is it chocolate? (yes/no)\n")
                
                if (option == "yes"):
                    output(1)
                
                elif (option == "no"):
                    output(2)
                    
    elif (option == "no"):
        option = input ("Was it sticky? (yes/no)\n")
        
        if (option == "yes"):
            option = input ("Is it a raw steak? (yes/no)\n")
            
            if (option == "yes"):
                option = input ("Are you a puma? (yes/no)\n")
                
                if (option == "yes"):
                    output(1)
                    
                elif (option == "no"):
                    output(2)
                
            elif (option == "no"):
                catLick()
        
        elif (option == "no"):
            option = input ("Is it an Emausaurus? (yes/no)\n")
            
            if (option == "yes"):
                option = input ("Are you a Megalosaurus? (yes/no)\n")
                
                if (option == "yes"):
                    output(1)
                
                elif (option == "no"):
                    output(2)
                
            elif (option == "no"):
                catLick()
                
def output (decision):
    if (decision == 1):
        print ("Decision: Eat it.")
        
    if (decision == 2):
        print ("Decision: Don't eat it.")
        
    if (decision == 3):
        print ("Decision: Your call.")

main()
