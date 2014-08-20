#You droppped it on the floor
#Ruchaan Schmidt


def food():
    
    print ("Welcome to the 30 Second Rule Expert")
    print ("------------------------------------")
    print ("Answer the following questions by selecting from among the options.")
    
    y='yes'
    n='no'
    
    boss=('Was it a boss/lover/parent? (yes/no)'+'\n')
    expensive=('Was it expensive? (yes/no)'+'\n')
    cut=('Can you cut off the part that touched the floor? (yes/no)'+'\n')
    choc=('Is it chocolate? (yes/no)'+'\n')    
    sticky=('Was it sticky? (yes/no)'+'\n')
    raw=('Is it a raw steak? (yes/no)'+'\n')
    puma=('Are you a puma? (yes/no)'+'\n')
    cat=('Did the cat lick it? (yes/no)'+'\n')
    health=('Is your cat healthy? (yes/no)'+'\n')
    emausaurus=('Is it an Emausaurus? (yes/no)'+'\n')
    megalosaurus=('Are you a Megalosaurus? (yes/no)'+'\n')
    ei=('Decision: Eat it.')
    de=("Decision: Don't eat it.")
    yc=("Decision: Your call.")
    
    see=input('Did anyone see you? (yes/no)'+'\n')
    if see==y:
        boss=input(boss)
        if boss==y:
            exp=input(expensive)
            if exp==y:
                cut=input(cut)
                if cut==y:
                    print(ei)
                if cut==n:
                    print(yc)
            if exp==n:
                choc=input(choc)
                if choc==y:
                    print(ei)
                if choc==n:
                    print(de)
        if boss==n:
            print(ei)
    if see==n:
        sticky=input(sticky)
        if sticky==y:
            raw=input(raw)
            if raw==y:
                puma=input(puma)
                if puma==y:
                    print(ei)
                if puma==n:
                    print(de)
            if raw==n:
                cat=input(cat)
                if cat==y:
                    health=input(health)
                    if health==y:
                        print(ei)
                    if health==n:
                        print(yc)
                if cat==n:
                    print(ei)
        if sticky==n:
            ema=input(emausaurus)
            if ema==y:
                meg=input(megalosaurus)
                if meg==y:
                    print(ei)
                if meg==n:
                    print(de)
            if ema==n:
                cat=input(cat)
                if cat==y:
                    health=input(health)
                    if health==y:
                        print(ei)
                    if health==n:
                        print(yc)
                if cat==n:
                    print(ei)
food()