e = ("Decision: Eat it.")
yy = ("Decision: Your call.")
d = ("Decision: Don't eat it.")
print("Welcome to the 30 Second Rule Expert")
print("------------------------------------")
print("Answer the following questions by selecting from among the options.")
a = input("Did anyone see you? (yes/no) \n")
y= ("yes")
if a==y:
    a = input("Was it a boss/lover/parent? (yes/no) \n")
    if a== y:
        a = input("Was it expensive? (yes/no) \n")
        if a==y:
            a = input("Can you cut off the part that touched the floor? (yes/no) \n")
           
            if a== y:
                print(e)
            else:
                print(yy)
        else:
            a = input("Is it chocolate? (yes/no) \n")
            if a==y:
                print(e)
            else:
                print(d)
    else:
        print(e)
else:
    a = input("Was it sticky? (yes/no) \n")
    if a==y:
        a = input("Is it a raw steak? (yes/no) \n")
        if a==y:
            a =input("Are you a puma? (yes/no) \n")
            if a==y:
                print(e)
            else:
                print(d)
        else:
            a = input("Did the cat lick it? (yes/no) \n")
            if a==y:
                a=input("Is your cat healthy? (yes/no) \n")
                if a==y:
                    print(e)
                else:
                    print(d)
            else:
                print(e)
    else:
        a = input("Is it an Emausaurus? (yes/no) \n")
        if a ==y:
            a=input("Are you a Megalosaurus? (yes/no) \n")
            if a==y:
                print(e)
            else:
                print(d)
        else:
            a = input("Did the cat lick it? (yes/no) \n")
            if a==y:
                a=input("Is your cat healthy? (yes/no) \n")
                if a==y:
                    print(e)
                else:
                    print(yy)
            else:
                print(e)
    