print("Welcome to the 30 Second Rule Expert")
print("-"*36)
print("Answer the following questions by selecting from among the options.")
#s="(yes/no)"
a=input("Did anyone see you? (yes/no)\n")
eat="Decision: Eat it."
don="Decision: Don't eat it."
you="Decision: Your call."
if a=="yes":
    b=input("Was it a boss/lover/parent? (yes/no)\n")
    if b=="yes":
        c=input("Was it expensive? (yes/no)\n")
        if c=="no":
            d=input("Is it chocolate? (yes/no)\n")
            if d=="yes":
                print(eat)#("Decision: Eat it.")
            elif d=="no":
                print(don)#("Decision: Don't eat it.")
        elif c=="yes":
            e=input("Can you cut off the part that touched the floor? (yes/no)\n")
            if e=="yes":
                print(eat)#("EAT IT")
            else:
                print(you)#("YOUR CALL")
    else:
        print(eat)#("EAT IT")
elif a=="no":
    f=input("Was it sticky? (yes/no)\n")
    if f=="yes":
        g=input("Is it a raw steak? (yes/no)\n")
        if g=="yes":
            h=input("Are you a puma? (yes/no)\n")
            if h=="no":
                print(don)#("DON'T EAT IT")
            elif h=="yes":
                print(eat)#("EAT IT")
        elif g=="no":
            i=input("Did the cat lick it? (yes/no)\n")
            if i=="no":
                print(eat)#("EAT IT")
            elif i=="yes":
                j=input("Is your cat healthy? (yes/no)\n")
                if j=="yes":
                    print(eat)#("EAT IT")
                else:print(you)#("YOUR CALL")
    elif f=="no":
        k=input("Is it an Emausaurus? (yes/no)\n")
        if k=="yes":
            l=input("Are you a Megalosaurus? (yes/no)\n")
            if l=="yes":
                print(eat)#("EAT IT")
            elif l=="no":
                print(don)#("DON'T EAT IT")
        else:
            m=input("Did the cat lick it? (yes/no)\n")
            if m=="yes":
                n=input("Is your cat healthy? (yes/no)\n")
                if n=="yes":
                    print(eat)#("EAT IT")
                else:
                    print(you)#("YOUR CALL")
            elif m=="no":
                print(eat)#("EAT IT")
                
                
                
            
    
        
