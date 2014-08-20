print("Welcome to the 30 Second Rule Expert")
print("------------------------------------")
print("Answer the following questions by selecting from among the options.")
x=input("Did anyone see you? (yes/no)\n")
if x=="yes" :
    x1=input("Was it a boss/lover/parent? (yes/no)\n")
    if x1=="no":
        print("Decision: Eat it.")
    if x1=="yes":
        x2=input("Was it expensive? (yes/no)\n")
        if x2=="no" :
            x3=input("Is it chocolate? (yes/no)\n")
            if x3=="yes" :
                print("Decision: Eat it.")
            if x3=="no" :
                print("Decision: Don't eat it.")
            
        if x2=="yes" :
            x4=input("Can you cut off the part that touched the floor? (yes/no)\n")
            if x4=="yes" :
                print("Decision: Eat it.")
            if x4=="no" :
                print("Decision: Your call.")
if x=="no" :
    x5=input("Was it sticky? (yes/no)\n")
    if x5=="yes" :
        x6=input("Is it a raw steak? (yes/no)\n")
        if x6=="yes" :
            x7=input("Are you a puma? (yes/no)\n")
            if x7=="yes" :
                print("Decision: Eat it.")
            if x7=="no" :
                print("Decision: Don't eat it.")
        if x6=="no" :
            x8=input("Did the cat lick it? (yes/no)\n")
            if x8=="no" :
                print("Decision: Eat it.")
            if x8=="yes" :
                x9=input("Is your cat healthy? (yes/no)\n")
                if x9=="yes" :
                    print("Decision: Eat it.")
                if x9=="no" :
                    print("Decision: Don't eat it.")
    if x5=="no" :
        x10=input("Is it an Emausaurus? (yes/no)\n")
        if x10=="no" :
            x11=input("Did the cat lick it? (yes/no)\n")
            if x11=="no":
                print("Decision: Eat it.")
            if x11=="yes":
                x12=input("Is your cat healthy? (yes/no)\n")
                if x12=="no" :
                    print("Decision: Your call.")
                if x12=="yes" :
                    print("Decision: Eat it.")
        if x10=="yes" :
            x13=input("Are you a Megalosaurus? (yes/no)\n")
            if x13=="no" :
                print("Decision: Don't eat it.")
            if x13=="yes" :
                print("Decision: Eat it.")
    
    
    
                
                
    