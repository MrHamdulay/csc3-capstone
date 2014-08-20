print("Welcome to the 30 Second Rule Expert")
print("------------------------------------")
print("Answer the following questions by selecting from among the options.")
x=("Decision: Eat it.")
y=("Decision: Don't eat it.")
z=("Decision: Your call.")
a=input("Did anyone see you? (yes/no)\n")
if a==("yes"):
            b=input("Was it a boss/lover/parent? (yes/no)\n")
            if b==("no"):
                        print(x)
            if b==("yes"):
                        c=input("Was it expensive? (yes/no)\n")
                        if c==("yes"):
                                    n=input("Can you cut off the part that touched the floor? (yes/no)\n")
                                    if n==("yes"):
                                                print(x)
                                    if n==("no"):
                                                print(z)
                        if c==("no"):
                                    d=input("Is it chocolate? (yes/no)\n")
                                    if d==("yes"):
                                                print(x)
                                    if d==("no"):
                                                print(y)
if a==("no"):
            e=input("Was it sticky? (yes/no)\n")
            if e==("yes"):
                        f=input("Is it a raw steak? (yes/no)\n")
                        if f==("yes"):
                                    g=input("Are you a puma? (yes/no)\n")
                                    if g==("yes"):
                                                print(x)
                                    if g==("no"):
                                                print(y)
                        if f==("no"):
                                    h=input("Did the cat lick it? (yes/no)\n")
                                    if h==("yes"):
                                                i=input("Is your cat healthy? (yes/no)\n")
                                                if i==("yes"):
                                                            print(x)
                                                if i==("no"):
                                                            print(z)
                                    if h==("no"):
                                                print(x)

            if e==("no"):
                        j=input("Is it an Emausaurus? (yes/no)\n")
                        if j==("yes"):
                                    k=input("Are you a Megalosaurus? (yes/no)\n")
                                    if k==('no'):
                                                print(y)
                                    if k==('yes'):
                                                print(x)
                        if j==("no"):
                                    l=input("Did the cat lick it? (yes/no)\n")
                                    if l==("yes"):
                                                m=input("Is your cat healthy? (yes/no)\n")
                                                if m==("yes"):
                                                            print(x)
                                                if m==("no"):
                                                            print(z)
                                    if l==("no"):
                                                print(x)
                        