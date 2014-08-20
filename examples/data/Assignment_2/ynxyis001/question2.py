print("Welcome to the 30 Second Rule Expert")
print("------------------------------------")
print("Answer the following questions by selecting from among the options.")

def YES():
    q1=input("Was it a boss/lover/parent? (yes/no)\n")
    if q1=="no":
        print("Decision: Eat it.")
    else:
        q2=input("Was it expensive? (yes/no)\n")
        if q2=="yes":
            q3=input("Can you cut off the part that touched the floor? (yes/no)\n")
            if q3=="yes":
                print("Decision: Eat it.")
            else:
                print("Decision: Your call.")
        
        else:
            q4=input("Is it chocolate? (yes/no)\n")
            if q4=="yes":
                print("Decision: Eat it.")
            else: 
                print("Decision: Don't eat it.")
                
def cat():
    cat=input("Did the cat lick it? (yes/no)\n")
    if cat=="no":
        print("Decision: Eat it.")
    else:
        healthy=input("Is your cat healthy? (yes/no)\n")
        if healthy=="no":
            print("Decision: Your call.")
        else: 
            print("Decision: Eat it.")
            
def NO():
    r1=input("Was it sticky? (yes/no)\n")
    if r1=="yes":
        r2=input("Is it a raw steak? (yes/no)\n")
        if r2=="no":
            cat()
        else:
            r3=input("Are you a puma? (yes/no)\n")
            if r3=="yes":
                print("Decision: Eat it.")
            else:
                print("Decision: Don't eat it.")
    else:
        r4=input("Is it an Emausaurus? (yes/no)\n")
        if r4=="no":
            cat()
        else: 
            r5=input("Are you a Megalosaurus? (yes/no)\n")
            if r5=="no":
                print("Decision: Don't eat it.")
            else: 
                print("Decision: Eat it.")
                
Q1=input("Did anyone see you? (yes/no)\n")
if Q1=="yes":
    YES()
else:
    NO()
        
            