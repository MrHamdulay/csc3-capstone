#Cristina Russo
#14 March 2014
#Decision Tree: Can you still eat it?


print("Welcome to the 30 Second Rule Expert")
print("------------------------------------")
print("Answer the following questions by selecting from among the options.")

x = "Decision: Eat it."
y = "Decision: Don't eat it."
z = "Decision: Your call."

a = input("Did anyone see you? (yes/no)\n") #Top of the decision tree
if a == "no":
    b = input("Was it sticky? (yes/no)\n")   #Programming to the left first
    if b == "no":
        c = input("Is it an Emausaurus? (yes/no)\n")  #programming far left
        if c == "yes":
            d = input("Are you a Megalosaurus? (yes/no)\n")
            if d == "no":
                print(y)  #End of branch on left
            if d == "yes":
                print(x)  #End of branch to the right
        if c == "no":
            e = input("Did the cat lick it? (yes/no)\n") #No Answer to Emausaurus
            if e == "no":
                print(x) #end of branch
            if e == "yes":
                f = input("Is your cat healthy? (yes/no)\n") 
                if f == "yes":
                    print(x)
                if f == "no":
                    print(z)
    if b == "yes":
        g = input("Is it a raw steak? (yes/no)\n")
        if g == "no":
            e = input("Did the cat lick it? (yes/no)\n")
            if e == "no":
                print(x)
            if e == "yes":
                f = input("Is your cat healthy? (yes/no)\n")
                if f == "yes":
                    print(x)
                if f == "no":
                    print(z)
        if g == "yes":
            h = input("Are you a puma? (yes/no)\n")
            if h == "yes":
                print(x)
            if h == "no":
                print(y)

if a == "yes":  # First question if answer is yes
    k = input("Was it a boss/lover/parent? (yes/no)\n")
    if k == "no": 
        print(x) # end of branch
    if k == "yes":
        l = input("Was it expensive? (yes/no)\n")
        if l == "no":
            m = input("Is it chocolate? (yes/no)\n")
            if m == "no":
                print(y) #end of branch
            if m == "yes":
                print(x)  #end if branch
        if l == "yes":
            m = input("Can you cut off the part that touched the floor? (yes/no)\n")
            if m == "yes":
                print(x)
            if m == "no":
                print(z)
        
