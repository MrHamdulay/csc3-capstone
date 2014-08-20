def eatornottest():
    a="yes"
    b="no"
    print("Welcome to the 30 Second Rule Expert")
    print("------------------------------------")
    print("Answer the following questions by selecting from among the options.")
    didanyonesee=input("Did anyone see you? (yes/no)\n")
    if didanyonesee==a:
        wasitabossloverparent=input("Was it a boss/lover/parent? (yes/no)\n")
        if wasitabossloverparent==b:
            print("Decision: Eat it.")
        elif wasitabossloverparent==a:
                wasitexpensive=input("Was it expensive? (yes/no)\n")
                if wasitexpensive==a:
                    canyoucutoff=input("Can you cut off the part that touched the floor? (yes/no)\n")
                    if canyoucutoff==a:
                        print("Decision: Eat it.")
                    elif canyoucutoff==b:
                        print("Decision: Your call.")
                elif wasitexpensive==b:
                    isitchocolate=input("Is it chocolate? (yes/no)\n")
                    if isitchocolate==a:
                        print("Decision: Eat it.")
                    elif isitchocolate==b:
                        print("Decision: Don't eat it.")
    elif didanyonesee==b:
            wasitsticky=input("Was it sticky? (yes/no)\n")  
            if wasitsticky==b:
                emausaurus=input("Is it an Emausaurus? (yes/no)\n")
                if emausaurus==a:
                    megalosaurus=input("Are you a Megalosaurus? (yes/no)\n")
                    if megalosaurus==a:
                        print("Decision: Eat it.")
                    elif megalosaurus==b:
                        print("Decision: Don't eat it.")
                elif emausaurus==b:
                    catlick=input("Did the cat lick it? (yes/no)\n")
                    if catlick==a:
                        cathealthy=input("Is your cat healthy? (yes/no)\n")
                        if cathealthy==a:
                            print("Decision: Eat it.")
                        elif cathealthy==b:
                            print("Decision: Your call.") 
                    elif catlick==b:
                        print("Decision: Eat it.")                            
            elif wasitsticky==a:              
                rawsteak=input("Is it a raw steak? (yes/no)\n")
                if rawsteak==a:
                    puma=input("Are you a puma? (yes/no)\n")
                    if puma==a:
                        print("Decision: Eat it.")
                    elif puma==b:
                        print("Decision: Don't eat it.")
                elif rawsteak==b:
                    catlick=input("Did the cat lick it? (yes/no)\n")
                    if catlick==a:
                        cathealthy=input("Is your cat healthy? (yes/no)\n")
                        if cathealthy==a:
                            print("Decision: Eat it.")
                        elif cathealthy==b:
                            print("Decision: Your call.")
                    elif catlick==b:
                        print("Decision: Eat it.")
                        
eatornottest()