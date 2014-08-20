# Decision tree
# by: SLLMOG004

print("Welcome to the 30 Second Rule Expert")
print("------------------------------------")
print("Answer the following questions by selecting from among the options.")
x = input("Did anyone see you? (yes/no)\n")
if(x=="yes"):
    y = input("Was it a boss/lover/parent? (yes/no)\n")
    if (y == "yes"):
        z = input("Was it expensive? (yes/no)\n")
        if (z == "yes"):
            a = input("Can you cut off the part that touched the floor? (yes/no)\n")
            if (a == "yes"):
                print("Decision: Eat it.")
            elif(a=="no"):
                print("Decision: Your call.")
        elif(z=="no"):
            b=input("Is it chocolate? (yes/no)\n")
            if (b == "yes"):
                print("Decision: Eat it.")
            elif (b=="no"): 
                print("Decision: Don't eat it.")
    elif (y=="no"):
        print("Decision: Eat it.")
if(x=="no"):
    c=input("Was it sticky? (yes/no)\n")
    if (c=="yes"):
        d=input("Is it a raw steak? (yes/no)\n")
        if (d=="yes"):
            e=input("Are you a puma? (yes/no)\n")
            if (e=="yes"):
                print("Decision: Eat it.")
            elif(e=="no"):
                print("Decision: Don't eat it.")
        elif(d=="no"):
            f=input("Did the cat lick it? (yes/no)\n")
            if (f=="no"):
                print("Decision: Eat it")
            elif (f=="yes"):
                g=input("Is your cat healthy? (yes/no)\n")
                if (g=="no"):
                    print("Decision: Your call.")
                elif(g=="yes"):
                    print("Decision: Eat it.")
    elif(c=="no"):
        h=input("Is it an Emausaurus? (yes/no)\n")
        if (h=="yes"):
            j=input("Are you a Megalosaurus? (yes/no)\n")
            if(j=="yes"):
                print("Decision: Eat it.")
            elif(j=="no"):
                print("Decision: Don't eat it.")
        elif(h=="no"):
            k=input("Did the cat lick it? (yes/no)\n")
            if(k=="yes"):
                m=input("Is your cat healthy? (yes/no)\n")
                if (m=="yes"):
                    print("Decision: Eat it.")
                elif (m=="no"):
                    print("Decision: Your call.")
            elif(k=="no"):
                print("Decision: Eat it.")