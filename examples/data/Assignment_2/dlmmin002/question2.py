#dropped food
#nolwazi 
#10 march 2014
print("Welcome to the 30 Second Rule Expert")
print("------------------------------------")
print("Answer the following questions by selecting from among the options.")
q=input("Did anyone see you? (yes/no)\n")
if q=="yes" :
    x=input("Was it a boss/lover/parent? (yes/no)\n")
    if x=="no" :
        print("Decision: Eat it.")
    elif x=="yes" :
        expence=input("Was it expensive? (yes/no)\n")
        if expence=="yes":
            y=input("Can you cut off the part that touched the floor? (yes/no)\n")
            if y=="yes":
                print("Decision: Eat it.")
            else:#y=="no":
                print("Decision: Your call.")
        elif expence== "no" :
                choc= input ("Is it chocolate? (yes/no)\n")
                if choc=="yes":
                    print("Decision: Eat it.")
                elif choc=="no" :
                    print("Decision: Don't eat it.\n") 
elif q=="no":
    r=input("Was it sticky? (yes/no)\n")
    if r== "yes":
        a=input("Is it a raw steak? (yes/no)\n")
        if a=="yes":
            b=input ("Are you a puma? (yes/no)\n")
            if b=="yes": 
                print("Decision: Eat it.")   
            elif b=="no":
                print("Decision: Don't eat it.")
        elif a=="no":
            c=input("Did the cat lick it? (yes/no)\n") 
            if c=="no":
                print("Decision: Eat it.")
            elif c=="yes":
                    d=input("Is your cat healthy? (yes/no)\n")
                    if d=="yes":
                        print("Decision: Eat it.")
                    elif d=="no":
                        print ("Decision: Your call.")
    elif r=="no":
        e=input("Is it an Emausaurus? (yes/no)\n")
        if e== "yes" :
            g=input("Are you a Megalosaurus? (yes/no)\n")
            if g== "yes":
                print("Decision: Eat it.")
            elif g== "no":
                print("Decision: Don't eat it.")
        elif e=="no":
            c=input("Did the cat lick it? (yes/no)\n")
            if c=="no":
                print("Decision: Eat it.")
            elif c=="yes":
                    d=input("Is your cat healthy? (yes/no)\n")
                    if d=="yes":
                        print("Decision: Eat it.")
                    elif d=="no":
                        print ("Decision: Your call.")
            