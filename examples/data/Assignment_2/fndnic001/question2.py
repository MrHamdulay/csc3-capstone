#You dropped your cupcake on the floor, should you eat it
#by Nic Findlay

print("Welcome to the 30 Second Rule Expert")
print("------------------------------------")
print("Answer the following questions by selecting from among the options.")
y="yes"
n="no"
x=input("Did anyone see you? (yes/no)\n")
if x==y:
    q=input("Was it a boss/lover/parent? (yes/no)\n")
    if q==y:
        z=input("Was it expensive? (yes/no)\n")
        if z==y:
            w=input("Can you cut off the part that touched the floor? (yes/no)\n")
            if w==y:
                print("Decision: Eat it.")
            else: 
                print("Decision: Your call.")
        else:
            e=input("Is it chocolate? (yes/no)\n")
            if e==y: 
                print("Decision: Eat it.")
            else: 
                print("Decision: Don't eat it.")
    else:
        print("Decision: Eat it.")
else: 
    r=input("Was it sticky? (yes/no)\n")
    if r==y: 
        t=input("Is it a raw steak? (yes/no)\n")
        if t==y:
            u=input("Are you a puma? (yes/no)\n")
            if u==y:
                print("Decision: Eat it.")
            else:
                print("Decision: Don't eat it.")
        else:
            i=input("Did the cat lick it? (yes/no)\n")
            if i==y:
                o=input("Is your cat healthy? (yes/no)\n")
                if o==y: 
                    print("Decision: Eat it.")
                else: print("Decision: Your call.")
            else: print("Decision: Eat it.")
            
    else:
        p=input("Is it an Emausaurus? (yes/no)\n")
        if p==y:
            a=input("Are you a Megalosaurus? (yes/no)\n")
            if a==y: print("Decision: Eat it.")
            else: print("Decision: Don't eat it.")
        else: 
            s=input("Did the cat lick it? (yes/no)\n")
            if s==y: 
                d=input("Is your cat healthy? (yes/no)\n")
                if d==y: print("Decision: Eat it.")
                else: print("Decision: Your call.")
            else: print("Decision: Eat it.")
        

