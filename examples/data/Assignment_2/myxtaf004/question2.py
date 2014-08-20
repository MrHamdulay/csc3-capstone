print("Welcome to the 30 Second Rule Expert", "------------------------------------", "Answer the following questions by selecting from among the options.", sep="\n")
def eat():
    print("Decision: Eat it.")
def dont():
    print("Decision: Don't eat it.")
def your():
    print("Decision: Your call.")
a=input("Did anyone see you? (yes/no)\n")
if(a=="yes"):
    a=input("Was it a boss/lover/parent? (yes/no)\n")
    if(a=="yes"):
        a=input("Was it expensive? (yes/no)\n")
        if(a=="yes"):
            a=input("Can you cut off the part that touched the floor? (yes/no)\n")
            if(a=="yes"):
                eat()
            else: your()
        else: 
            a=input("Is it chocolate? (yes/no)\n")
            if(a=="yes"):
                eat()
            else: dont()            
            
    else: eat()
else: 
    a=input("Was it sticky? (yes/no)\n")
    if(a=="yes"):
        a=input("Is it a raw steak? (yes/no)\n")
        if(a=="yes"):
            a=input("Are you a puma? (yes/no)\n")
            if(a=="yes"):eat()
            else:dont()
        else:
            a=input("Did the cat lick it? (yes/no)\n")
            if(a=="yes"):
                a=input("Is your cat healthy? (yes/no)\n")
                if(a=="yes"):
                    eat()
                else: your()
            else:eat()            
    else:
        a=input("Is it an Emausaurus? (yes/no)\n")
        if(a=="yes"):
            a=input("Are you a Megalosaurus? (yes/no)\n")
            if(a=="yes"):eat()
            else:dont()
        else:
            a=input("Did the cat lick it? (yes/no)\n")
            if(a=="yes"):
                a=input("Is your cat healthy? (yes/no)\n")
                if(a=="yes"):
                    eat()
                else: your()
            else:eat()