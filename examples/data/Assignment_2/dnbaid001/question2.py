print ("Welcome to the 30 Second Rule Expert") #Title
print ("------------------------------------") #Line break
print ("Answer the following questions by selecting from among the options.") #Instructions

a = input("Did anyone see you? (yes/no)\n")
if a == "yes":
    b = input("Was it a boss/lover/parent? (yes/no)\n")
    if b == "yes":
        c = input("Was it expensive? (yes/no)\n")
        if c == "yes":
            d = input("Can you cut off the part that touched the floor? (yes/no)\n")
            if d == "yes":
                print ("Decision: Eat it.")
            elif d == "no":
                print ("Decision: Your call.")
        elif c == "no":
            e = input("Is it chocolate? (yes/no)\n")
            if e == "yes":
                print ("Decision: Eat it.")
            elif e == "no": 
                print ("Decision: Don't eat it.")
    elif b == "no":
        print ("Decision: Eat it.")
elif a == "no":
    f = input("Was it sticky? (yes/no)\n")
    if f == "yes":
        g = input("Is it a raw steak? (yes/no)\n")
        if g == "yes":
            h = input("Are you a puma? (yes/no)\n")
            if h == "yes":
                print ("Decision: Eat it.")
            elif h == "no":
                print ("Decision: Don't eat it.")
        elif g == "no":
            i = input("Did the cat lick it? (yes/no)\n")
            if i == "yes":
                j = input("Is your cat healthy? (yes/no)\n")
                if j == "yes":
                    print ("Decision: Eat it.")
                elif j == "no":
                    print ("Decision: Your call.")
            elif i == "no":
                print ("Decision: Eat it.")
    elif f == "no":
        k = input("Is it an Emausaurus? (yes/no)\n")
        if k == "no": 
            i = input("Did the cat lick it? (yes/no)\n")
            if i == "yes":
                j = input("Is your cat healthy? (yes/no)\n")
                if j == "yes":
                    print ("Decision: Eat it.")
                elif j == "no":
                    print ("Decision: Your call.")
            elif i == "no":
                print ("Decision: Eat it.")
        elif k == "yes":
            l = input("Are you a Megalosaurus? (yes/no)\n")
            if l == "yes":
                print ("Decision: Eat it.")
            elif l == "no":
                print ("Decision: Don't eat it.")