A="Decision: Eat it."
B="Decision: Don't eat it."
C="Decision: Your call."

print("Welcome to the 30 Second Rule Expert")
print("------------------------------------")
print("Answer the following questions by selecting from among the options.")
see=input("Did anyone see you? (yes/no)\n")
if see=="yes":
    who=input("Was it a boss/lover/parent? (yes/no)\n")
    if who=="no":
        print(A)
    if who=="yes":
        expensive=input("Was it expensive? (yes/no)\n")
        if expensive=="no":
            chocolate=input("Is it chocolate? (yes/no)\n")
            if chocolate=="no":
                print(B)
            if chocolate=="yes":
                print(A)
        if expensive=="yes":
            cut_off=input("Can you cut off the part that touched the floor? (yes/no)\n")
            if cut_off=="no":
                print(C)
            if cut_off=="yes":
                print(A)
if see=="no":
    sticky=input("Was it sticky? (yes/no)\n")
    if sticky=="no":
        emausaurus=input("Is it an Emausaurus? (yes/no)\n")
        if emausaurus=="no":
            cat_lick=input("Did the cat lick it? (yes/no)\n")
            if cat_lick=="no":
                print(A)
            if cat_lick=="yes":
                cat_healthy=input("Is your cat healthy? (yes/no)\n")
                if cat_healthy=="no":
                    print(C)
                if cat_healthy=="yes":
                    print(A)
        if emausaurus=="yes":
            megalosaurus=input("Are you a Megalosaurus? (yes/no)\n")
            if megalosaurus=="no":
                print(B)
            if megalosaurus=="yes":
                print(A)
    if sticky=="yes":
        steak=input("Is it a raw steak? (yes/no)\n")
        if steak=="no":
            cat_lick=input("Did the cat lick it? (yes/no)\n")
            if cat_lick=="no":
                print(A)
            if cat_lick=="yes":
                cat_healthy=input("Is your cat healthy? (yes/no)\n")
                if cat_healthy=="no":
                    print(C)
                if cat_healthy=="yes":
                    print(A)    
        if steak=="yes":
            puma=input("Are you a puma? (yes/no)\n")
            if puma=="no":
                print(B)
            if puma=="yes":
                print(A)
            
    
    