print("Welcome to the 30 Second Rule Expert")
print("------------------------------------")
print("Answer the following questions by selecting from among the options.")
x=("Decision: Eat it.")
y=("Decision: Don't eat it.")
z=("Decision: Your call.")
a=input("Did anyone see you? (yes/no)\n")
if (a=="yes"):
    b=input("Was it a boss/lover/parent? (yes/no)\n")
    if (b=="no"):
        print(x)
    if (b=="yes"):
        c=input("Was it expensive? (yes/no)\n")
        if (c=="no"):
            d=input("Is it chocolate? (yes/no)\n")
            if (d=="no"):
                print(y)
            if(d=="yes"):
                print(x)
        if (c=="yes"):
            e=input("Can you cut off the part that touched the floor? (yes/no)\n")
            if (e=="no"):
                print(z)
            if (e=="yes"):
                print(x)
if (a=="no"):
    f=input("Was it sticky? (yes/no)\n")
    if (f=="no"):
        g=input("Is it an Emausaurus? (yes/no)\n")
        if (g=="no"):
            h=input("Did the cat lick it? (yes/no)\n")
            if (h=="no"):
                print(x)
            if (h=="yes"):
                i=input("Is your cat healthy? (yes/no)\n")
                if (i=="no"):
                    print(z)
                if (i=="yes"):
                    print(x)
        if (g=="yes"):
            j=input("Are you a Megalosaurus? (yes/no)\n")
            if (j=="no"):
                print(y)
            if (j=="yes"):
                print(x)
    if (f=="yes"):
        k=input("Is it a raw steak? (yes/no)\n")
        if (k=="yes"):
            l=input("Are you a puma? (yes/no)\n")
            if (l=="yes"):
                print(x)
            if (l=="no"):
                print(y)
        if (k=="no"):
            m=input("Did the cat lick it? (yes/no)\n")
            if (m=="no"):
                    print(x)
            if (m=="yes"):
                n=input("Is your cat healthy? (yes/no)\n")
                if (n=="no"):
                    print(z)
                if (n=="yes"):
                    print(x)