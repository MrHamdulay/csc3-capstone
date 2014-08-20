print("Welcome to the 30 Second Rule Expert")
print("------------------------------------")
print("Answer the following questions by selecting from among the options.")
yes= 1
no = 0
v = ('Decision: Eat it.')
w = ("Decision: Don't eat it.")
n = ("Decision: Your call.")
c = eval(input('Did anyone see you? (yes/no)\n'))
if c==yes:
    b = eval(input('Was it a boss/lover/parent? (yes/no)\n'))
    if b==yes:
        z = eval(input('Was it expensive? (yes/no)\n'))   
        if z==yes:
            y = eval(input('Can you cut off the part that touched the floor? (yes/no)\n'))
            if y==yes: 
                print(v)
            else: print(n)
        else: 
            x = eval(input('Is it chocolate? (yes/no)\n'))
            if x==yes:
                print(v)
            else:print(w)  
    else:
        print(v)
  
       
else:
    m = eval(input('Was it sticky? (yes/no)\n'))
    if m==yes:
        e = eval(input('Is it a raw steak? (yes/no)\n'))
        if e==yes: 
            q = eval(input('Are you a puma? (yes/no)\n'))
            if q==no:
                print(w)
            else:
                print(v)
        else: 
            h = eval(input('Did the cat lick it? (yes/no)\n'))
            if h==yes:
                u = eval(input('Is your cat healthy? (yes/no)\n'))
                if u==yes: print(v)
                else: print(n)
            else: print(v)
    else: 
        a = eval(input('Is it an Emausaurus? (yes/no)\n')) 
        if a==no:
            h = eval(input('Did the cat lick it? (yes/no)\n'))
            if h==yes:
                u = eval(input('Is your cat healthy? (yes/no)\n'))
                if u==yes: print(v)
                else: print(n)
            else: print(v)  
        else:
            p = eval(input('Are you a Megalosaurus? (yes/no)\n'))
            if p==yes:
                print(v)
            else: 
                print(w)