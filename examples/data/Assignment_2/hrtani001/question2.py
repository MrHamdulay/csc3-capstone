y = "yes"

def eat():
    print("Decision: Eat it.")
    
def leave():
    print("Decision: Don't eat it.")
    
def call():
    print("Decision: Your call.")

print("Welcome to the 30 Second Rule Expert\n\
------------------------------------\n\
Answer the following questions by selecting from among the options.")
ans = input("Did anyone see you? (yes/no)\n")
if ans == y:
    ans = input("Was it a boss/lover/parent? (yes/no)\n")
    if ans == y:
        ans = input("Was it expensive? (yes/no)\n")
        if ans == y:
            ans = input("Can you cut off the part that touched the floor? (yes/no)\n")
            if ans == y:
                eat()
            else:
                call()
        else:
            ans = input("Is it chocolate? (yes/no)\n")
            if ans == y:
                eat()
            else:
                leave()                
    else:
        eat()
else:
    ans = input("Was it sticky? (yes/no)\n")  
    if ans == y:
        ans = input("Is it a raw steak? (yes/no)\n")
        if ans == y:
            ans = input("Are you a puma? (yes/no)\n")
            if ans == y:
                eat()
            else:
                leave()
        else:
            ans = input("Did the cat lick it? (yes/no)\n")
            if ans == y:
                ans = input("Is your cat healthy? (yes/no)\n")
                if ans == y:
                    eat()
                else:
                    call()
            else:
                eat()
    else:
        ans = input("Is it an Emausaurus? (yes/no)\n")
        if ans == y:
            ans = input("Are you a Megalosaurus? (yes/no)\n")
            if ans == y:
                eat()
            else:
                leave()
        else:
            ans = input("Did the cat lick it? (yes/no)\n")
            if ans == y:
                ans = input("Is your cat healthy? (yes/no)\n")
                if ans == y:
                    eat()
                else:
                    call()
            else:
                eat()