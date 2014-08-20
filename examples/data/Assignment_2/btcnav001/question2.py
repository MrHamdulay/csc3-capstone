def choice():
    print("Welcome to the 30 Second Rule Expert")
    print("------------------------------------")
    print("Answer the following questions by selecting from among the options.")
    x=input("Did anyone see you? (yes/no)\n")
    n="no"
    m="yes"
    if x==m:
        y=input("Was it a boss/lover/parent? (yes/no)\n")
        if y==m:
            z=input("Was it expensive? (yes/no)\n")
            if z==m:
                a=input("Can you cut off the part that touched the floor? (yes/no)\n")
                if a==m:
                    print("Decision: Eat it.")
                else:
                    print("Decision: Your call.")
            else:
                b=input("Is it chocolate? (yes/no)\n")
                if b==m:
                    print("Decision: Eat it.")
                else:
                    print("Decision: Don't eat it.")
        else:
            print("Decision: Eat it.")
    else:
        c=input("Was it sticky? (yes/no)\n")
        if c==m:
            d=input("Is it a raw steak? (yes/no)\n")
            if d==m:
                e=input("Are you a puma? (yes/no)\n")
                if e==m:
                    print("Decision: Eat it.")
                else:
                    print("Decision: Don't eat it.")
            else:
                f=input("Did the cat lick it? (yes/no)\n")
                if f==m:
                    g=input("Is your cat healthy? (yes/no)\n")
                    if g==m:
                        print("Decision: Eat it.")
                    else:
                        print("Decision: Your call.")
                else:
                    print("Decision: Eat it.")
        else:
            h=input("Is it an Emausaurus? (yes/no)\n")
            if h==m:
                i=input("Are you a Megalosaurus? (yes/no)\n")
                if i==m:
                    print("Decision: Eat it.")
                else:
                    print("Decision: Don't eat it.")
            else:
                j=input("Did the cat lick it? (yes/no)\n")
                if j==m:
                    l=input("Is your cat healthy? (yes/no)\n")
                    if l==m:
                        print("Decision: Eat it.")
                    else:
                        print("Decision: Your call.")
                else:
                    print("Decision: Eat it.")
                
choice()