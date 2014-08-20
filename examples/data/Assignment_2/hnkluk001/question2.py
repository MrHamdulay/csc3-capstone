# Luke Henkeman
# HNKLUK001
# Assignment 2, Question 2, CSC1015F
# 7 March 2014

print("")
print("Welcome to the 30 Second Rule Expert")
print("------------------------------------")
print("Answer the following questions by selecting from among the options.")

def dropped():
    eatit = "Decision: Eat it."
    dont = "Decision: Don't eat it."
    yours = "Decision: Your call."
    
    spotted = input("Did anyone see you? (yes/no)\n")
    if(spotted == 'yes'):
        whosaw = input("Was it a boss/lover/parent? (yes/no)\n")
        if(whosaw == 'yes'):
            cost = input("Was it expensive? (yes/no)\n")
            if(cost == 'yes'):
                salvage = input("Can you cut off the part that touched the floor? (yes/no)\n")
                if(salvage == 'yes'):
                    print(eatit)
                else:
                    print(yours)
            elif(cost == 'no'):
                choc = input("Is it chocolate? (yes/no)\n")
                if(choc == 'yes'):
                    print(eatit)
                else:
                    print(dont)
        else:
            print(eatit)
    elif(spotted == 'no'):    
        sticky = input("Was it sticky? (yes/no)\n")
        if(sticky == 'yes'):
            steak = input("Is it a raw steak? (yes/no)\n")
            if(steak == 'yes'):
                puma = input("Are you a puma? (yes/no)\n")
                if(puma == 'yes'):
                    print(eatit)
                else:
                    print(dont)
            elif(steak == 'no'):
                cat = input("Did the cat lick it? (yes/no)\n")
                if(cat == 'yes'):
                    goodcat = input("Is your cat healthy? (yes/no)\n")
                    if(goodcat == 'yes'):
                        print(eatit)
                    else:
                        print(yours)
                else:
                    print(eatit)
        elif(sticky == 'no'):    
            dino1 = input("Is it an Emausaurus? (yes/no)\n")
            if(dino1 == 'yes'):
                dino2 = input("Are you a Megalosaurus? (yes/no)\n")
                if(dino2 == 'yes'):
                    print(eatit)
                else:
                    print(dont)
            elif(dino1 == 'no'):        
                cat = input("Did the cat lick it? (yes/no)\n")
                if(cat == 'yes'):
                    goodcat = input("Is your cat healthy? (yes/no)\n")
                    if(goodcat == 'yes'):
                        print(eatit)
                    else:
                        print(yours)
                else:
                    print(eatit)
        
dropped()