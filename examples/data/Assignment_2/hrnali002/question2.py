#The 30 second food on floor program
#Alison Hoernle
#HRNALI002
#8 March 2014

print("Welcome to the 30 Second Rule Expert")
print("------------------------------------")
print("Answer the following questions by selecting from among the options.")
see = input("Did anyone see you? (yes/no)\n")
if (see == 'yes'):
    who = input("Was it a boss/lover/parent? (yes/no)\n")
    if (who == 'yes'):
        price = input("Was it expensive? (yes/no)\n")
        if (price == 'yes'):
            cut_off = input("Can you cut off the part that touched the floor? (yes/no)\n")
            if (cut_off == 'yes'):
                print("Decision: Eat it.")
            else:
                print("Decision: Your call.")
        else:
            chocolate = input("Is it chocolate? (yes/no)\n")
            if (chocolate == 'yes'):
                print("Decision: Eat it.")
            else:
                print("Decision: Don't eat it.")
    else:
        print("Decision: Eat it.")
else:
    sticky = input("Was it sticky? (yes/no)\n")
    if (sticky == 'yes'):
        what = input("Is it a raw steak? (yes/no)\n")
        if (what == 'yes'):
            puma = input("Are you a puma? (yes/no)\n")
            if (puma == 'yes'):
                print("Decision: Eat it.")
            else:
                print("Decision: Don't eat it.")
        else:
            cat = input("Did the cat lick it? (yes/no)\n")
            if (cat == 'yes'):
                cat_healthy = input("Is your cat healthy? (yes/no)\n")
                if (cat_healthy == 'yes'):
                    print("Decision: Eat it.")
                else:
                    print("decision: Your call.")
            else:
                print("Decision: Eat it.")
    else:
        emausaurus = input("Is it an Emausaurus? (yes/no)\n")
        if (emausaurus == 'yes'):
            megalosaurus = input("Are you a Megalosaurus? (yes/no)\n")
            if (megalosaurus == 'yes'):
                print("Decision: Eat it.")
            else:
                print("Decision: Don't eat it.")
        else:
            cat = input("Did the cat lick it? (yes/no)\n")
            if (cat == 'yes'):
                cat_healthy = input("Is your cat healthy? (yes/no)\n")
                if (cat_healthy == 'yes'):
                    print("Decision: Eat it.")
                else:
                    print("Decision: Your call.")
            else:
                print("Decision: Eat it.")
            
            

    
    

                
        
    

