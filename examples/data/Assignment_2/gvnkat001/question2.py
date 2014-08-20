print("Welcome to the 30 Second Rule Expert")
print("------------------------------------")
print("Answer the following questions by selecting from among the options.")
yes=1
no=0
x=eval(input("Did anyone see you? (yes/no)\n"))
if x==yes :
    k=eval(input("Was it a boss/lover/parent? (yes/no)\n"))
    if k==yes :
        z=eval(input("Was it expensive? (yes/no)\n"))
        if z==yes :
            p=eval(input("Can you cut off the part that touched the floor? (yes/no)\n"))
            if p==yes :
                print("Decision: Eat it.")
            elif p==no :
                print("Decision: Your call.")
        elif z==no :
            q=eval(input("Is it chocolate? (yes/no)\n"))
            if q==yes :
                print("Decision: Eat it.")
            elif q==no :
                print("Decision: Don't eat it.")
    elif k==no :
        print("Decision: Eat it.")
elif x==no :
    y=eval(input("Was it sticky? (yes/no)\n"))
    if y==yes :
        b=eval(input("Is it a raw steak? (yes/no)\n"))
        if b==yes :
            i=eval(input("Are you a puma? (yes/no)\n"))
            if i==yes :
                print("Decision: Eat it.")
            elif i==no :
                print("Decision: Don't eat it.") 
        elif b==no :
            r=eval(input("Did the cat lick it? (yes/no)\n"))
            if r==no :
                print("Decision: Eat it.")
            elif r==yes :
                u=eval(input("Is your cat healthy? (yes/no)\n"))
                if u==yes :
                    print("Decision: Eat it.")
                elif u==no :
                    print("Decision: Your call.")
                       
    elif y==no :
        t=eval(input("Is it an Emausaurus? (yes/no)\n"))
        if t==yes :
            w=eval(input("Are you a Megalosaurus? (yes/no)\n"))
            if w==yes :
                print("Decision: Eat it.")
            elif w==no :
                print("Decision: Don't eat it.")
        elif t==no :
            m=eval(input("Did the cat lick it? (yes/no)\n"))
            if m==yes :
                j=eval(input("Is your cat healthy? (yes/no)\n"))
                if j==yes :
                    print("Decision: Eat it.")
                elif j==no :
                    print("Decision: Your call.")
            elif m==no :
                print("Decision: Eat it.")
    