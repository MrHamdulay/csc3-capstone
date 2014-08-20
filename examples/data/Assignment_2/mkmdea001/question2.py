print("Welcome to the 30 Second Rule Expert")
print("------------------------------------")
print("Answer the following questions by selecting from among the options.")
yes= 1
no = 0
e = ('Decision: Eat it.')
d = ("Decision: Don't eat it.")
m = ("Decision: Your call.")
x = eval(input('Did anyone see you? (yes/no)\n'))
if x==yes:
    y = eval(input('Was it a boss/lover/parent? (yes/no)\n'))
    if y==yes:
        a = eval(input('Was it expensive? (yes/no)\n'))   
        if a==yes:
            b = eval(input('Can you cut off the part that touched the floor? (yes/no)\n'))
            if b==yes: 
                print(e)
            else: print(m)
        else: 
            c = eval(input('Is it chocolate? (yes/no)\n'))
            if c==yes:
                print(e)
            else: print(d)  
    else:
        print(e)
  
       
else:
    n = eval(input('Was it sticky? (yes/no)\n'))
    if n==yes:
        v = eval(input('Is it a raw steak? (yes/no)\n'))
        if v==yes: 
            j = eval(input('Are you a puma? (yes/no)\n'))
            if j==no:
                print(d)
            else:
                print(e)
        else: 
            s = eval(input('Did the cat lick it? (yes/no)\n'))
            if s==yes:
                f = eval(input('Is your cat healthy? (yes/no)\n'))
                if f==yes: print(e)
                else: print(m)
            else: print(e)
    else: 
        z = eval(input('Is it an Emausaurus? (yes/no)\n')) 
        if z==no:
            s = eval(input('Did the cat lick it? (yes/no)\n'))
            if s==yes:
                f = eval(input('Is your cat healthy? (yes/no)\n'))
                if f==yes: print(e)
                else: print(m)
            else: print(e)  
        else:
            h = eval(input('Are you a Megalosaurus? (yes/no)\n'))
            if h==yes:
                print(e)
            else: 
                print(d)