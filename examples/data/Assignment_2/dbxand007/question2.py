# Cherise Dube
# 13 March 2013
# "Should I Eat It?" Program

def seconds():
    print ("Welcome to the 30 Second Rule Expert")
    print ("------------------------------------")
    print ("Answer the following questions by selecting from among the options.")
    seen= input ("Did anyone see you? (yes/no)\n")
    
    if seen == "yes": 
        boss=input ("Was it a boss/lover/parent? (yes/no)\n")
        if boss == "no": print("Decision: Eat it.") 
        elif boss =="yes": 
            expensive= input("Was it expensive? (yes/no)\n")
            if expensive=="yes": 
                cut= input ("Can you cut off the part that touched the floor? (yes/no)\n")
                if cut=="no": print("Decision: Your call.")
                elif cut=="yes": print("Decision: Eat it.") 
                
            elif expensive=="no": 
                chocolate= input ("Is it chocolate? (yes/no)\n")
                if chocolate == "yes": print("Decision: Eat it.") 
                elif chocolate== "no": print("Decision: Don't eat it.")    
                
            
    elif seen=="no": 
        sticky=input ("Was it sticky? (yes/no)\n")
        if sticky=="yes": 
            steak= input ("Is it a raw steak? (yes/no)\n")
            if steak=="yes": 
                puma= input("Are you a puma? (yes/no)\n")
                if puma=="no": print("Decision: Don't eat it.")
                elif puma=="yes": print("Decision: Eat it.")                   
            elif steak=="no":
                lick= input("Did the cat lick it? (yes/no)\n")
                if lick=="no": print("Decision: Eat it.")
                elif lick=="yes":  
                    healthy= input ("Is your cat healthy? (yes/no)\n")
                    if healthy=="no": print("Decision: Your call.")
                    elif healthy=="yes": print ("Decision: Eat it.")                        
                        
        elif sticky=="no": 
            emausaurus= input("Is it an Emausaurus? (yes/no)\n")
            if emausaurus=="no": 
                lick= input("Did the cat lick it? (yes/no)\n")
                if lick=="no": print("Decision: Eat it.")
                elif lick=="yes":  
                    healthy= input ("Is your cat healthy? (yes/no)\n")
                    if healthy=="no": print("Decision: Your call.")
                    elif healthy=="yes": print ("Decision: Eat it.")                 
                
            elif emausaurus=="yes":
                megalosaurus= input("Are you a Megalosaurus? (yes/no)\n") 
                if megalosaurus=="no": print ("Decision: Don't eat it.")
                elif megalosaurus=="yes": print ("Decision: Eat it.")     
       
seconds()