ans=str('yes')
print("Welcome to the 30 Second Rule Expert")
print("------------------------------------")
print("Answer the following questions by selecting from among the options.")
while True:
    a=input("Did anyone see you? (yes/no)\n")
    if a==ans:
        b=input("Was it a boss/lover/parent? (yes/no)\n")
        if b==ans:
            c=input("Was it expensive? (yes/no)\n")
            if c==ans:
                d=input("Can you cut off the part that touched the floor? (yes/no)\n")
                if d==ans:
                    print("Decision: Eat it.")
                else:
                    print("Decision: Your call.")
            else:
                e=input("Is it chocolate? (yes/no)\n")
                if e==ans:
                    print("Decision: Eat it.")
                else:
                    print("Decision: Don't eat it.")
        else:
            print("Decision: Eat it.")
    else:
        f=input("Was it sticky? (yes/no)\n")
        if f==ans:
            g=input("Is it a raw steak? (yes/no)\n")
            if g==ans:
                h=input("Are you a puma? (yes/no)\n")
                if h==ans:
                    print("Decision: Eat it.")
                else:
                    print("Decision: Don't eat it.")
            else:
                k=input("Did the cat lick it? (yes/no)\n")
                if k==ans:
                    l=input("Is your cat healthy? (yes/no)\n")
                    if l==ans:
                        print("Decision: Eat it.")
                    else:
                        print("Decision: Your call.")
                else:
                    print("Decision: Eat it.")
        else:
            m=input("Is it an Emausaurus? (yes/no)\n")
            if m==ans:
                n=input("Are you a Megalosaurus? (yes/no)\n")
                if n==ans:
                    print("Decision: Eat it.")
                else:
                    print("Decision: Don't eat it.")
            else:
                k=input("Did the cat lick it? (yes/no)\n")
                if k==ans:
                    l=input("Is your cat healthy? (yes/no)\n")
                    if l==ans:
                        print("Decision: Eat it.")
                    else:
                        print("Decision: Your call.")
                else:
                    print("Decision: Eat it.")
    break
