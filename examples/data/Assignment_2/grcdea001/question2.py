print("Welcome to the 30 Second Rule Expert")
print("------------------------------------")
print("Answer the following questions by selecting from among the options.")
final = 0 # 0 = dont eat it, 1 = eat it, 2 = your call

seeyou = input("Did anyone see you? (yes/no)\n")

if (seeyou == "yes"):
    wasita = input("Was it a boss/lover/parent? (yes/no)\n")
    
    if (wasita == "no"):
        final = 1
    else: #wasita == yes
        expensive = input("Was it expensive? (yes/no)\n")
        
        if (expensive == "yes"):
            cutoff = input("Can you cut off the part that touched the floor? (yes/no)\n")
            
            if (cutoff == "yes"):
                final = 1
            else:
                final = 2
        else:
            choc = input("Is it chocolate? (yes/no)\n")
            if (choc == "yes"):
                final = 1
            else:
                final = 0
                
else:
    sticky = input("Was it sticky? (yes/no)\n")
    if (sticky == "yes"):
        steak = input("Is it a raw steak? (yes/no)\n")
        
        if (steak == "yes"):
            puma = input("Are you a puma? (yes/no)\n")
            
            if (puma == "yes"):
                final = 1
            else:
                final = 0
            
        else: # steak = no    
            cat = input("Did the cat lick it? (yes/no)\n")
            if (cat == "yes"):
                healthy = input("Is your cat healthy? (yes/no)\n")
            
                if (healthy == "yes"):
                    final = 1
                else:
                    final = 2
            else:
                final = 1
        
    else: # stickey = no
        ema = input("Is it an Emausaurus? (yes/no)\n")
        if (ema== "yes"):
            mega = input("Are you a Megalosaurus? (yes/no)\n")
            if (mega == "yes"):
                final = 1
                
            else:
                final = 0
            
        else: #ema = no
            cat = input("Did the cat lick it? (yes/no)\n")
            if (cat == "yes"):
                healthy = input("Is your cat healthy? (yes/no)\n")
            
                if (healthy == "yes"):
                    final = 1
                else:
                    final = 2
            else:
                final = 1
                
if (final == 0):
    print("Decision: Don't eat it.")
if (final == 1):
        print("Decision: Eat it.")   
if (final == 2):
        print("Decision: Your call.")        


