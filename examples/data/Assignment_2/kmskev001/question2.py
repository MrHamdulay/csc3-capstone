# question 2
# program to determine wether to eat a cupcake that's fallen 
# kevin kumasamba

print("Welcome to the 30 Second Rule Expert")
print("-"*36)
print("Answer the following questions by selecting from among the options.")

def D(): # to make things go quicker
    print("Decision: Don't eat it.")
def E():
    print("Decision: Eat it.")
def Y():
    print("Decision: Your call.")
def cat():
    ans=input("Did the cat lick it? (yes/no)\n")
    if ans=="no":
        E()
    if ans=="yes":
        ans=input("Is your cat healthy? (yes/no)\n")
        if ans=="yes":
            E()
        if ans=="no":
            Y()

ans=input("Did anyone see you? (yes/no)\n")
if ans=="yes": # the answers that you make the varaible equal to have to be strings
    ans=input("Was it a boss/lover/parent? (yes/no)\n")
    if ans=="no":
            E()
    if ans=="yes":
        ans=input("Was it expensive? (yes/no)\n")
        if ans=="yes":
            ans=input("Can you cut off the part that touched the floor? (yes/no)\n")
            if ans=="yes":
                E()
            if ans=="no":
                Y()
        elif ans=="no":
            ans=input("Is it chocolate? (yes/no)\n")
            if ans=="yes":
                E()
            if ans=="no":
                D()
elif ans=="no":
    ans=input("Was it sticky? (yes/no)\n")
    if ans=="yes":
        ans=input("Is it a raw steak? (yes/no)\n")
        if ans=="yes":
            ans=input("Are you a puma? (yes/no)\n")
            if ans=="yes":
                E()
            if ans=="no":
                D()
        elif ans=="no":
            ans=input("Did the cat lick it? (yes/no)\n")
            if ans=="no":
                E()
            if ans=="yes":
                ans=input("Is your cat healthy? (yes/no)\n")
                if ans=="yes":
                    E()
                if ans=="no":
                    Y()
    elif ans=="no":
        ans=input("Is it an Emausaurus? (yes/no)\n")
        if ans=="no":
            cat()
        if ans=="yes":
            ans=input("Are you a Megalosaurus? (yes/no)\n")
            if ans=="no":
                D()
            if ans=="yes":
                E()
                
                
                
                
        
        
        