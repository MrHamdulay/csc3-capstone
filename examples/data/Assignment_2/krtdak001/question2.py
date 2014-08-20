#KRTDAK001

a = input("Did anyone see you? (yes/no)\n")
if a == "yes":
    c = input("Was it a boss/lover/parent? (yes/no)\n")
    if c == "yes":
        g = input("Was it expensive? (yes/no)\n")
        if g == "yes":
            k = input("Can you cut off the part that touched the floor? (yes/no)\n")
            if k == "yes":
                print("Decision: Eat it.")
if a == "yes" and c == "no":
    print("Decision: Eat it.")
if a == "yes" and c == "yes" and g == "yes" and k == "yes":
    print("Decision: Eat it.")
if a == "yes"and c == "yes" and g == "no":
    l = input("Is it chocolate? (yes/no)\n")
    if l == "yes":
        print("Decision: Eat it.")
if a == "yes" and c == "yes" and g == "no" and l == "no":
    print("Decision: Don't eat it.")
if a == "yes" and c == "yes" and g == "yes" and k == "no":
    print("Decisiion: Your call.")
if a == "no":
    b = input("Was it sticky? (yes/no)\n")
    if b == "yes":
        e = input("Is it a raw steak? (yes/no)\n")
        if e == "yes":
            h = input("Are you a puma? (yes/no)\n")
            if h == "no":
                print("Decision: Don't eat it.")
if a == "no" and b == "yes" and e == "no":
    i = input("Did the cat lick it? (yes/no)\n")
    if i == "no":
        print("Decision: Eat it")
if a == "no" and b == "no":
    f = input("Is it an Emausaurus? (yes/no)\n")
    if f == "no" and i == "yes":
        m = input("Is you cat healthy? (yes/no)\n")
        if m == "yes":
            print("Decision: Eat it.")
if a == "no" and b == "no" and f == "no" and i == "yes" and m == "no":
    print("Decision: Your call.")
if a == "no" and b == "no" and f == "yes":
    j = input("Are you a Megalosourus? (yes/no)\n")
    if j == "yes":
        print("Decision: Eat it.")
if a == "no" and b == "no" and f == "yes" and j == "no":
    print("Decision: Don't eat it.")