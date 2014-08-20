#Program for 30 second rule
#Tinotenda Chemvura (CHMTIN004)
#08 March 2014

#__________________program starts here_______________

def game():
    print("Welcome to the 30 Second Rule Expert")
    print("------------------------------------")
    print("Answer the following questions by selecting from among the options.")
    
    ans1=str(input("Did anyone see you? (yes/no)\n"))
    
    if ans1=="yes":
        ans2=str(input("Was it a boss/lover/parent? (yes/no)\n"))
        
        if ans2=="no": print("Decision: Eat it.")
        elif ans2=="yes":
            ans3=str(input("Was it expensive? (yes/no)\n"))
          
            if ans3=="yes": 
                ans4=str(input("Can you cut off the part that touched the floor? (yes/no)\n"))
  
                if ans4=="no": 
                    print("Decision: Your call.")
                elif ans4=="yes": 
                    print("Decision: Eat it.")

            elif ans3=="no":
                ans5=str(input("Is it chocolate? (yes/no)\n"))

                if ans5=="yes": 
                    print("Decision: Eat it.")
                elif ans5=="no":
                    print("Decision: Don't eat it.")

                    
    elif ans1=="no":
        ans6=str(input("Was it sticky? (yes/no)\n"))

        if ans6=="no":
            ans7=str(input("Is it an Emausaurus? (yes/no)\n"))

            if ans7=="yes":
                ans8=str(input("Are you a Megalosaurus? (yes/no)\n"))
                
                if ans8=="yes":
                    print("Decision: Eat it.")
                elif ans8=="no":
                    print("Decision: Don't eat it.")
            
            elif ans7=="no":
                ans9=str(input("Did the cat lick it? (yes/no)\n"))
                
                if ans9=="no":
                    print("Decision: Eat it.")
                elif ans9=="yes":
                    ans10=(input("Is your cat healthy? (yes/no)\n"))
                    
                    if ans10=="no":
                        print("Decision: Your call.")
                    elif ans10=="yes":
                        print("Decision: Eat it.")
                        
        elif ans6=="yes":
            ans11=str(input("Is it a raw steak? (yes/no)\n"))
            
            if ans11=="no":
                ans12=str(input("Did the cat lick it? (yes/no)\n"))
        
                if ans12=="no":
                    print("Decision: Eat it.")
                elif ans12=="yes":
                    ans13=(input("Is your cat healthy? (yes/no)\n"))
                 
                    if ans13=="no":
                        print("Decision: Your call.")
                    elif ans13=="yes":
                        print("Decision: Eat it.")
            
            elif ans11=="yes":
                ans14=str(input("Are you a puma? (yes/no)\n"))
                
                if ans14=="yes":
                    print("Decision: Eat it.")
                elif ans14=="no":
                    print("Decision: Don't eat it.")
                    
#_____________End of the program________________*

game()