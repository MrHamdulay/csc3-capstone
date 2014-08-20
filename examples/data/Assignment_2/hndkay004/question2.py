a="Decision: Eat it."
b="Decision: Your call."
c="Decision: Don't eat it."

print("Welcome to the 30 Second Rule Expert")
print("------------------------------------")
print("Answer the following questions by selecting from among the options.")
see=input("Did anyone see you? (yes/no)"'\n')
if see=='yes':
    blt=input("Was it a boss/lover/parent? (yes/no)"'\n')
    if blt=='yes':
        ex=input("Was it expensive? (yes/no)"'\n')
        if ex=='no':
            choc=input("Is it chocolate? (yes/no)"'\n')
            if choc=='yes':
                print(a)
            else:
                print(c)
        if ex=='yes':
            cut=input("Can you cut off the part that touched the floor? (yes/no)"'\n')
            if cut=='yes':
                print(a)
            else: print(b)
    else:
        print(a)
elif see=='no':
    sticky=input("Was it sticky? (yes/no)"'\n')
    if sticky=='yes':
        raw=input("Is it a raw steak? (yes/no)"'\n')
        if raw=='yes':
            puma=input("Are you a puma? (yes/no)"'\n')
            if puma=='no':
                print(c)
            else: 
                print(a)
        if raw=='no':
            cat=input("Did the cat lick it? (yes/no)"'\n')
            if cat=='yes':
                healthy=input("Is your cat healthy? (yes/no)"'\n')
                if healthy=='no':
                    print(b)
                else: print(a)
            else: print(a)
    if sticky=='no':
        emausaurus=input("Is it an Emausaurus? (yes/no)"'\n')
        if emausaurus=='no':
            cat=input("Did the cat lick it? (yes/no)"'\n')
            if cat=='yes':
                healthy=input("Is your cat healthy? (yes/no)"'\n')
                if healthy=='no':
                    print(b)
                else: print(a)
            else: print(a)
        else:
            megalosaurus=input("Are you a Megalosaurus? (yes/no)"'\n')
            if megalosaurus=='yes':
                print(a)
            else:
                print(c)