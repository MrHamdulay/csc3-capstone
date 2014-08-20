# Mpho Natalie Raselo
print("Welcome to the 30 Second Rule Expert")
print("------------------------------------")
print("Answer the following questions by selecting from among the options.")
x = input("Did anyone see you? (yes/no)\n")
if x == "yes":
    y = input("Was it a boss/lover/parent? (yes/no)\n")
    if y == "yes":
        c = input("Was it expensive? (yes/no)\n")
        if c == "yes":
            d = input("Can you cut off the part that touched the floor? (yes/no)\n")
            if d == "yes":
                print("Decision: Eat it.\n")
            else:
                if d == "no":
                    print("Decision: Your call.")
        else:
            if c == "no":
                e = input("Is it chocolate? (yes/no)\n")
                if e == "yes":
                    print("Decision: Eat it.\n")
                else:
                    if e == "no":
                        print("Decision: Don't eat it.\n")
    else:
        if y == "no":
            print("Decision: Eat it.\n")
else:
    if x == "no":
        f = input("Was it sticky? (yes/no)\n")
        if f == "yes":
            g = input("Is it a raw steak? (yes/no)\n")
            if g == "yes":
                h = input("Are you a puma? (yes/no)\n")
                if h == "yes":
                    print("Decision: Eat it.")
                else:
                    if h == "no":
                        print("Decision: Don't eat it.\n")
            else:
                if g == "no":
                    i = input("Did the cat lick it? (yes/no)\n")
                    if i == "yes":
                        j = input("Is your cat healthy? (yes/no)\n")
                        if j == "yes":
                            print("Decision: Eat it.")
                        else:
                            if j == "no":
                                print("Decision: Your call.\n")
                    else:
                        if i == "no":
                            print("Decision: Eat it.")
        if f == "no":
            k = input("Is it an Emausaurus? (yes/no)\n")
            if k == "yes":
                l = input("Are you a Megalosaurus? (yes/no)\n")
                if l == "yes":
                    print("Decision: Eat it.\n")
                else:
                    if l == "no":
                        print("Decision: Don't eat it.\n")
            else:
                if k == "no":
                    m = input("Did the cat lick it? (yes/no)\n")
                    if m == "yes":
                        n = input("Is your cat healthy? (yes/no)\n")
                        if n == "yes":
                            print("Decision: Eat it.")
                        else:
                            if n == "no":
                                print("Decision: Your call.\n")
                    else:
                        if m == "no":
                            print("Decision: Eat it.\n")
