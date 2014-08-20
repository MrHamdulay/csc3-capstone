a="Decision: Eat it."
b="Decision: Your call."
c="Decision: Don't eat it."
x="Welcome to the 30 Second Rule Expert"
y="------------------------------------"
z="Answer the following questions by selecting from among the options."
print(x,y,z,sep="\n")
def kitty():
    l=input("Did the cat lick it? (yes/no)\n")
    if l=='yes':
        m=input("Is your cat healthy? (yes/no)\n")
        if m=='yes':
            print(a)
        else:
            print(b)
    else:
        print(a)    
d=input("Did anyone see you? (yes/no)\n")
if d=='yes':
    e=input("Was it a boss/lover/parent? (yes/no)\n")
    if e=='yes':
        f=input("Was it expensive? (yes/no)\n")
        if f=='yes':
            g=input("Can you cut off the part that touched the floor? (yes/no)\n")
            if g=='yes':
                print(a)
            else:
                print(b)
        else:
            h=input("Is it chocolate? (yes/no)\n")
            if h=='yes':
                print(a)
            else:
                print(c)
    else:
        print(a)
else:
    i=input("Was it sticky? (yes/no)\n")
    if i=='yes':
        j=input("Is it a raw steak? (yes/no)\n")
        if j=='yes':
            k=input("Are you a puma? (yes/no)\n")
            if k=='yes':
                print(a)
            else:
                print(c)
        else:
            kitty()
    else:
        n=input("Is it an Emausaurus? (yes/no)\n")
        if n=='yes':
            o=input("Are you a Megalosaurus? (yes/no)\n")
            if o=='yes':
                print(a)
            else:
                print(c)
        else:
            kitty()