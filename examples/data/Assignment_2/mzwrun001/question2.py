print("Welcome to the 30 Second Rule Expert")
print("------------------------------------")
print("Answer the following questions by selecting from among the options.")
a=str(input("Did anyone see you? (yes/no)""\n"))
if a== "yes":
    b=str(input("Was it a boss/lover/parent? (yes/no)""\n"))
    if b== "yes":
        c=str(input("Was it expensive? (yes/no)""\n"))
        if c== "yes": 
            d=str(input("Can you cut off the part that touched the floor? (yes/no)""\n"))
            if d== "yes":
                print("Decision: Eat it.")
            else:
                print("Decision: Your call.")            
        else :
            e=str(input("Is it chocolate? (yes/no)""\n"))
            if e=="yes":
                print ("Decision: Eat it.")
            else :
                print("Decision: Don't eat it.")
    elif b=="no" :
        print("Decision: Eat it.")    

elif a == "no" : 
    f=str(input("Was it sticky? (yes/no)""\n")) 
    if f=="yes":
        g=str(input("Is it a raw steak? (yes/no)""\n"))
        if g=="yes":
            h=str(input("Are you a puma? (yes/no)""\n"))
            if h=="yes":
                print("Decision: Eat it.")
            else :
                print("Decision: Don't eat it.")
        else:
            i=str(input("Did the cat lick it? (yes/no)""\n"))
            if i=="no":
                print("Decision: Eat it.")
            else :
                j=str(input("Is your cat healthy? (yes/no)""\n"))
                if j=="yes":
                    print("Decision: Eat it.")
                else:
                    print("Decision: Your call.")
    else:
        k=str(input("Is it an Emausaurus? (yes/no)""\n"))
        if k=="no":
            i=str(input("Did the cat lick it? (yes/no)""\n"))
            if i== "no":
                print("Decision: Eat it.")
            else :
                j=str(input("Is your cat healthy? (yes/no)""\n"))
                if j=="no":
                    print("Decision: Your call.")
                else:
                    print("Decision: Eat it.")
        else:
            l=str(input("Are you a Megalosaurus? (yes/no)""\n"))
            if l=="yes":
                print("Decision: Eat it.")
            else:
                print("Decision: Don't eat it.")
