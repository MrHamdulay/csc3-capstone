#Dumisani J Nyathi
#Looping
#So far toughest program I`ve had to make.
#12-03-14
print("Welcome to the 30 Second Rule Expert")
print("------------------------------------")
print("Answer the following questions by selecting from among the options.")

def flowchart():
    y='yes'
    n='no'
    a=input("Did anyone see you? (yes/no)\n")
    if a==y:
        b=input("Was it a boss/lover/parent? (yes/no)\n")
        if b==y:
            c=input("Was it expensive? (yes/no)\n")
            if c==y:
                d=input("Can you cut off the part that touched the floor? (yes/no)\n")
                if d==y:
                    print("Decision: Eat it.")
                elif d==n:
                    print("Decision: Your call.")
            elif c==n:
                e=input("Is it chocolate? (yes/no)\n")
                if e==y:
                    print("Decision: Eat it.")
                elif e==n:
                    print("Decision: Don't eat it.")
        else:print("Decision: Eat it.")
    elif a==n:
        f=input("Was it sticky? (yes/no)\n")
        if f==y:
            i=input("Is it a raw steak? (yes/no)\n")
            if i==y:
                l=input("Are you a puma? (yes/no)\n")
                if l==y:
                    print("Decision: Eat it.")
                elif l==n:
                    print("Decision: Don't eat it.")
            elif i==n:
                j=input("Did the cat lick it? (yes/no)\n")
                if j==y:
                    k=input("Is your cat healthy? (yes/no)\n")
                    if k==y:
                        print("Decision: Eat it.")
                    elif k==n:
                        print("Decision: Your call.")
                elif j==n:
                    print("Decision: Eat it.")
        elif f==n:
            g=input("Is it an Emausaurus? (yes/no)\n")
            if g==y:
                h=input("Are you a Megalosaurus? (yes/no)\n")
                if h==y:
                    print("Decision: Eat it.")
                elif h==n:
                    print("Decision: Don't eat it.")
            elif g==n:
                j=input("Did the cat lick it? (yes/no)\n")
                if j==y:
                    k=input("Is your cat healthy? (yes/no)\n")
                    if k==y:
                        print("Decision: Eat it.")
                    elif k==n:
                        print("Decision: Your call.")
                elif j==n:
                    print("Decision: Eat it.")
                    
flowchart()