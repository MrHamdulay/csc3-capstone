# A program to determine if you should eat food dropped on the floor or not
# Author: Afika Nyati
# 9 March 2014

def welcome():
    
    print("Welcome to the 30 Second Rule Expert")
    print("-"*36)

def main():
    
    print("Answer the following questions by selecting from among the options.")
    
    seen = input("Did anyone see you? (yes/no)\n")
    
    
    
    
    if (seen[0] == "y" or seen[0] == "Y"): # This is the right of 'Did anyone see you?' question. i.e. Yes, it's sticky
        
        knownperson = input("Was it a boss/lover/parent? (yes/no)\n")
        
        if (knownperson[0] == "y" or knownperson[0] == "Y"): # This is the right of 'Was it a boss,etc.?' question. i.e. Yes, it's a boss,etc.
            
            expensive = input("Was it expensive? (yes/no)\n")
            
            if (expensive[0] == "y" or expensive[0] == "Y"): # This is the right of 'Is it expensive?' question. i.e. Yes, it is expensive
                
                cutoff = input("Can you cut off the part that touched the floor? (yes/no)\n")
                
                if (cutoff[0] == "y" or cutoff[0] == "Y"): # This is the right of 'Can you cut off?' question. i.e. Yes, you can cut off.
                    
                    print("Decision: Eat it.")
                    
                else: # This is the left of 'Can you cut off?' question. i.e. No, you can't cut off.
                    
                    print("Decision: Your call.")
                    
            else: # This is the left of 'Is it expensive?' question. i.e. No, it's not expensive
            
                chocolate = input("Is it chocolate? (yes/no)\n")
                
                if (chocolate[0] == "y" or chocolate[0] == "Y"): # This is the right of 'Is it chocolate?' question. i.e. Yes, it is chocolate.
                    
                    print("Decision: Eat it.")
                    
                else: # This is the left of 'Is it chocolate?' question. i.e. No, it isn't chocolate.
                    
                    print("Decision: Don't eat it.")
                    
        else: # This is the left of 'Was it a boss,etc.?' question. i.e. No, it's not a boss,etc.
            
            print("Decision: Eat it.")
                    
                    
                    
                    
                    
                    
    else: # This is the left of 'Did anyone see you?' question. i.e. No, no one saw me
        
        sticky = input("Was it sticky? (yes/no)\n")
        
        if (sticky[0] == "y" or sticky[0] == "Y"): # This is the right of 'Was it sticky?' question. i.e. No it's not sticky
            
            rawsteak = input("Is it a raw steak? (yes/no)\n")
            
            if (rawsteak[0] == "y" or rawsteak[0] == "Y"): # This is the right of 'Is it raw steak?' question. i.e. Yes, it's raw steak
                
                puma = input("Are you a puma? (yes/no)\n")
                
                if (puma[0] == "y" or puma[0] == "Y"): # This is the right of 'Are you a puma?' question. i.e. Yes, I'm a puma.
                    print("Decision: Eat it.")
                    
                else: # This is the left of 'Are you a puma?' question. i.e. No, I'm not a puma.
                    print("Decision: Don't eat it.")
                    
            else: # This is the left of 'Is it raw steak?' question. i.e. No, it's not raw steak
                
                lick = input("Did the cat lick it? (yes/no)\n")
                
                if (lick[0] == "y" or lick[0] == "Y"): # This is the right of 'Did the cat lick it?' question. i.e. Yes, the cat licked it.
                    
                    healthycat = input("Is your cat healthy? (yes/no)\n")
                    
                    if (healthycat[0] == "y" or healthycat[0] == "Y"): # This is the right of 'Is the cat healthy?' question. i.e. Yes, the cat is healthy
                        
                        print("Decision: Eat it.")
                        
                    else: # This is the left of 'Is the cat healthy?' question. i.e. No, the cat isn't healthy
                        print("Decision: Your call.")
                        
                else: # This is the left of 'Did the cat lick it?' question. i.e. No, the cat didn't licked it.
                    print("Decision: Eat it.")
        
        else:
            emausaurus = input("Is it an Emausaurus? (yes/no)\n")
            
            if (emausaurus[0] == "y" or emausaurus[0] == "Y"): # This is the right of 'Is it an Emausaurus?' question. i.e. Yes, it is an Emausaurus.
                
                megalosaurus = input("Are you a Megalosaurus? (yes/no)\n")
                
                if (megalosaurus[0] == "y" or megalosaurus[0] == "Y"): # This is the right of 'Are you a Megalosaurus?' question. i.e. Yes, I am a Megalosaurus.
                    
                    print("Decision: Eat it.")
                    
                else: # This is the left of 'Are you a Megalosaurus?' question. i.e. No, I am not a Megalosaurus.
                    
                    print("Decision: Don't eat it.")
                    
            else: # This is the left of 'Is it an Emausaurus?' question. i.e. NO, it is not an Emausaurus.
                
                lick = input("Did the cat lick it? (yes/no)\n")
                
                if (lick[0] == "y" or lick[0] == "Y"): # This is the right of 'Did the cat lick it?' question. i.e. Yes, the cat licked it.
                    
                    healthycat = input("Is your cat healthy? (yes/no)\n")
                    
                    if (healthycat[0] == "y" or healthycat[0] == "Y"): # This is the right of 'Is the cat healthy?' question. i.e. Yes, the cat is healthy
                        
                        print("Decision: Eat it.")
                        
                    else: # This is the left of 'Is the cat healthy?' question. i.e. No, the cat isn't healthy
                        print("Decision: Your call.")
                        
                else: # This is the left of 'Did the cat lick it?' question. i.e. No, the cat didn't licked it.
                    print("Decision: Eat it.")
                
welcome()
main()