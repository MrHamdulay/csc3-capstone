print("Welcome to the 30 Second Rule Expert")
print("------------------------------------")
print("Answer the following questions by selecting from among the options.")
a = input("Did anyone see you? (yes/no)\n")
if a == 'yes':
    b = input("Was it a boss/lover/parent? (yes/no)\n")
    if b == 'yes':
        c = input("Was it expensive? (yes/no)\n")
        if c == 'yes':
            d = input("Can you cut off the part that touched the floor? (yes/no)\n")
            if d == 'yes':
                print("Decision: Eat it.")
            elif d == 'no':
                print("Decision: Your call.")
        elif c == 'no':
            h = input("Is it chocolate? (yes/no)\n")
            if h == 'yes':
                print("Decision: Eat it.")
            elif h == 'no':
                print("Decision: Don't eat it.")
    elif b == 'no':
        print("Decision: Eat it.") 
if a == 'no':
    e = input("Was it sticky? (yes/no)\n")
    if e == 'yes':
        f = input("Is it a raw steak? (yes/no)\n")
        if f == 'yes':
            g = input("Are you a puma? (yes/no)\n")
            if g == 'yes':
                print("Decision: Eat it.")
            elif g == 'no':
                print("Decision: Don't eat it.")
        elif f == 'no':
            k = input("Did the cat lick it? (yes/no)\n")
            if k == 'yes':
                l = input("Is your cat healthy? (yes/no)\n")
                if l == 'yes':
                    print("Decision: Eat it.")
                elif l == 'no':
                    print("Decision: Your call.")
            elif k == 'no':
                print("Decision: Eat it.")    
    if e == 'no':
        i = input("Is it an Emausaurus? (yes/no)\n")
        if i == 'yes':
            j = input("Are you a Megalosaurus? (yes/no)\n")
            if j == 'yes':
                print("Decision: Eat it.")
            elif j == 'no':
                print("Decision: Don't eat it.")
        elif i == 'no':
            k = input("Did the cat lick it? (yes/no)\n")
            if k == 'yes':
                l = input("Is your cat healthy? (yes/no)\n")
                if l == 'yes':
                    print("Decision: Eat it.")
                elif l == 'no':
                    print("Decision: Your call.")
            elif k == 'no':
                print("Decision: Eat it.")
                
#Author: Lenard Carroll
#Student Number: CRRLEN001
            