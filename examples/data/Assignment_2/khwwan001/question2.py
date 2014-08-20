print("Welcome to the 30 Second Rule Expert")
print("------------------------------------")
print("Answer the following questions by selecting from among the options.")
a = input("Did anyone see you? (yes/no)\n")
if a == ("yes"):
    b = input("Was it a boss/lover/parent? (yes/no)\n")
    if b == ("no"):
        print("Decision: Eat it.")
    elif b == ("yes"):
        c = input("Was it expensive? (yes/no)\n")
        if c == ("no"):
            d = input("Is it chocolate? (yes/no)\n")
            if d == ("yes"):
                print("Decision: Eat it.")
            else:
                print("Decision: Don't eat it.")
        elif c == ("yes"):
            e = input("Can you cut off the part that touched the floor? (yes/no)\n")
            if e == ("no"):
                print("Decision: Your call.")
            elif e == ("yes"):
                print("Decision: Eat it.")
                
elif a == ("no"):
    f = input("Was it sticky? (yes/no)\n")
    if f == ("no"):
        g = input("Is it an Emausaurus? (yes/no)\n")
        if g == ("no"):
            h = input("Did the cat lick it? (yes/no)\n")
            if h == ("no"):
                print("Decision: Eat it.")
            elif h == ("yes"):
                i = input("Is your cat healthy? (yes/no)\n")
                if i == ("no"):
                    print("Decision: Your call.")
                elif i == ("yes"):
                    print("Decision: Eat it.")
        if g == ("yes"):
            j = input("Are you a Megalosaurus? (yes/no)\n")
            if j == ("no"):
                print("Decision: Don't eat it.")
            elif j == ("yes"):
                print("Decision: Eat it.")
    elif f == ("yes"):
        k = input("Is it a raw steak? (yes/no)\n")
        if k == ("no"):
            l = input("Did the cat lick it? (yes/no)\n")
            if l == ("yes"):
                m = input("Is your cat healthy? (yes/no)\n")
                if m == ("yes"):
                    print("Decision: Eat it.")
                elif m == ("no"):
                    print("Decision : Your call.")
                elif l == ("no"):
                    print("Decision: Eat it.")
        elif k == ("yes"):
            n = input("Are you a puma? (yes/no)\n")
            if n == ("no"):
                print("Decision: Don't eat it.")
            elif n == ("yes"):
                print("Decision: Eat it.")
                
    