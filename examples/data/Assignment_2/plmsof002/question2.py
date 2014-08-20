# Eat Cupcake?
# 11/3/14
# Sofia Palmer

def cupcake():
    print()
    print("Welcome to the 30 Second Rule Expert")
    print("------------------------------------")
    print("Answer the following questions by selecting from among the options.")
    seen = input("Did anyone see you? (yes/no)\n")
    if seen == 'yes':
        who = input("Was it a boss/lover/parent? (yes/no)\n")
        if who == 'yes':
            expense = input("Was it expensive? (yes/no)\n")
            if expense == 'yes':
                cut = input("Can you cut off the part that touched the floor? (yes/no)\n") 
                if cut == 'yes':
                    print("Decision: Eat it.")    
                else:
                    print("Decision: Your call.")
            else:
                chocolate = input("Is it chocolate? (yes/no)\n")
                if chocolate == 'yes':
                    print("Decision: Eat it.")  
                else:
                    print("Decision: Don't eat it.") 
        if who == 'no':
            print("Decision: Eat it.")         
    if seen == 'no':
        sticky = input("Was it sticky? (yes/no)\n")
        if sticky =='yes':
            steak = input("Is it a raw steak? (yes/no)\n")
            if steak == 'yes':
                puma = input("Are you a puma? (yes/no)\n")
                if puma == 'yes':
                    print("Decision: Eat it.")
                else:
                    print("Decision: Don't eat it.")
            if steak == 'no':
                cat = input("Did the cat lick it? (yes/no)\n")
                if cat == 'no':
                    print("Decision: Eat it.")
                if cat =='yes':
                    health = input("Is your cat healthy? (yes/no)\n")
                    if health =='yes':
                        print("Decision: Eat it.")
                    else:
                        print("Decision: Your call.")
        if sticky == 'no':
            emausaurus = input("Is it an Emausaurus? (yes/no)\n")
            if emausaurus == 'no':
                cat = input("Did the cat lick it? (yes/no)\n")
                if cat == 'no':
                    print("Decision: Eat it.")
                if cat == 'yes':
                    health = input("Is your cat healthy? (yes/no)\n")
                    if health == 'yes':
                        print("Decision: Eat it.")
                    else:
                        print("Decision: Your call.")   
            if emausaurus == 'yes':
                megalosaurus = input("Are you a Megalosaurus? (yes/no)\n")
                if megalosaurus == 'no':
                    print("Decision: Don't eat it.")
                else:
                    print("Decision: Eat it.")
cupcake()



                
            
            
            
                    
                    
                
                
 
    