print("Welcome to the 30 Second Rule Expert\n------------------------------------\nAnswer the following questions by selecting from among the options.")

def food():
    a=input("Did anyone see you? (yes/no)\n")
    if a=="yes":
        b=input("Was it a boss/lover/parent? (yes/no)\n")
        if b=="yes":
            c=input("Was it expensive? (yes/no)\n")
            if c=="yes":
                d=input("Can you cut off the part that touched the floor? (yes/no)\n")
                if d=="yes":
                    print("Decision: Eat it.")
                else:
                    print("Decision: Your call.")
            else :
                e=input("Is it chocolate? (yes/no)\n")
                if e=="yes":
                    print("Decision: Eat it.")
                else:
                    print("Decision: Don't eat it.")
        else:
            print("Decision: Eat it.")
        
    else:
        f=input("Was it sticky? (yes/no)\n")
        if f=="yes":
            g=input("Is it a raw steak? (yes/no)\n")
            if g=="yes":
                h=input("Are you a puma? (yes/no)\n")
                if h=="yes":
                    print("Decision: Eat it.")
                else :
                    print("Decision: Don't eat it.")
            else:
                i=input("Did the cat lick it? (yes/no)\n")
                if i=="yes":
                    j=input("Is your cat healthy? (yes/no)\n")
                    if j=="yes":
                        print("Decision: Eat it.")
                    else:
                        print("Decision: Your call.")
                else:
                    print("Decision: Eat it.")
        else:
            k=input("Is it an Emausaurus? (yes/no)\n")
            if k=="yes":
                l=input("Are you a Megalosaurus? (yes/no)\n")
                if l=="yes":
                    print("Decision: Eat it.")
                else:
                    print("Decision: Don't eat it.")
            else:
                i=input("Did the cat lick it? (yes/no)\n")
                if i=="yes":
                    j=input("Is your cat healthy? (yes/no)\n")
                    if j=="yes":
                        print("Decision: Eat it.")
                    else:
                        print("Decision: Your call.")
                else:
                    print("Decision: Eat it.")                
                
food()