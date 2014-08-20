# "30 second rule" program to check if user should eat food dropped on the floor or not
# Mick Perring
# 8 March 2014

y = "yes" # defines "yes" as y
n = "no"  # defines "no" as n

print ("Welcome to the 30 Second Rule Expert")  # program intro and instruction
print ("------------------------------------")
print ("Answer the following questions by selecting from among the options.")

# questions requiring "yes" or "no" answers input from the user
# responses lead to further yes/no questions, ultimately providing a decision on whether to eat
# the food or not, based on users responses
x1 = input("Did anyone see you? (yes/no)""\n")  
if x1 == y:
    x2 = input("Was it a boss/lover/parent? (yes/no)""\n")
    if x2 == y:
        x3 = input("Was it expensive? (yes/no)""\n")
        if x3 == y:
            x4 = input("Can you cut off the part that touched the floor? (yes/no)""\n")
            if x4 == y:
                print ("Decision: Eat it.")
            elif x4 == n:
                print ("Decision: Your call.")
        elif x3 == n:
            x5 = input("Is it chocolate? (yes/no)""\n")
            if x5 == y:
                print ("Decision: Eat it.")
            elif x5 == n:
                print ("Decision: Don't eat it.")
    elif x2 == n:
        print ("Decision: Eat it.")
        
elif x1 == n:
    x6 = input("Was it sticky? (yes/no)""\n")
    if x6 == y:
        x7 = input("Is it a raw steak? (yes/no)""\n")
        if x7 == y:
            x8 = input("Are you a puma? (yes/no)""\n")
            if x8 == y:
                print ("Decision: Eat it.")
            elif x8 == n:
                print ("Decision: Don't eat it.")
        elif x7 == n:
            x9 = input("Did the cat lick it? (yes/no)""\n")
            if x9 == y:
                x10 = input("Is your cat healthy? (yes/no)""\n")  
                if x10 == y:
                    print ("Decision: Eat it.")
                elif x10 == n:
                    print ("Decision: Your call.")
            elif x9 == n:
                print ("Decision: Eat it.")
    elif x6 == n:
        x11 = input("Is it an Emausaurus? (yes/no)""\n")
        if x11 == y:
            x12 = input("Are you a Megalosaurus? (yes/no)""\n")
            if x12 == y:
                print ("Decision: Eat it.")
            elif x12 == n:
                print ("Decision: Don't eat it.")
        elif x11 == n:
            x13 = input("Did the cat lick it? (yes/no)""\n")
            if x13 == y:
                x14 = input("Is your cat healthy? (yes/no)""\n")  
                if x14 == y:
                    print ("Decision: Eat it.")
                elif x14 == n:
                    print ("Decision: Your call.")
            elif x13 == n:
                print ("Decision: Eat it.")            
            
