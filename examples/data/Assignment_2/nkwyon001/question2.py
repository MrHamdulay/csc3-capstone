print("Welcome to the 30 Second Rule Expert")
print("------------------------------------")
print("Answer the following questions by selecting from among the options.")
a=input("Did anyone see you? (yes/no)\n")
if a=='no':
    aa=input("Was it sticky? (yes/no)\n")
    if aa=='no':
        aaa=input("Is it an Emausaurus? (yes/no)\n")
        if aaa=='no':
            aaaa=input("Did the cat lick it? (yes/no)\n")
            if aaaa=='no':
                print("Decision: Eat it.")
            if aaaa=='yes':
                d=input("Is your cat healthy? (yes/no)\n")
                if d=='yes':
                    print("Decision: Eat it.")
                if d=='no':
                    print("Decision: Your call.")
        if aaa=='yes':
            c=input("Are you a Megalosaurus? (yes/no)\n")
            if c=='no':
                print("Decision: Don't eat it.")
            if c=='yes':
                print("Decision: Eat it.")
    if aa=='yes':
        b=input("Is it a raw steak? (yes/no)\n")
        if b=='no':
            bb=input("Did the cat lick it? (yes/no)\n")
            if bb=='no':
                print("Decision: Eat it.")
            if bb=='yes':
                bbb=input("Is your cat healthy? (yes/no)\n")
                if bbb=='no':
                    print("Decision: Your call.")
                if bbb=='yes':
                    print("Decision: Eat it.")
        if b=='yes':
            e=input("Are you a puma? (yes/no)\n")
            if e=='no':
                print("Decision: Don't eat it.")
            if e=='yes':
                print("Decision: Eat it.")
if a=='yes':
    y=input("Was it a boss/lover/parent? (yes/no)\n")
    if y=='no':
        print("Decision: Eat it.")
    if y=='yes':
        z=input("Was it expensive? (yes/no)\n")
        if z=='no':
            s=input("Is it chocolate? (yes/no)\n")
            if s=='no':
                print("Decision: Don't eat it.")
            if s=='yes':
                print("Decision: Eat it.")
        if z=='yes':
            ss=input("Can you cut off the part that touched the floor? (yes/no)\n")
            if ss=='no':
                print("Decision: Your call.")
            if ss=='yes':
                print("Decision: Eat it.")
    

