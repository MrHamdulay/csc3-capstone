print("Welcome to the 30 Second Rule Expert")
print("------------------------------------")
print("Answer the following questions by selecting from among the options.")

def q_see():
    x=input("Did anyone see you? (yes/no)\n")
    if x == "yes":
        q_boss()
    else:
        q_sticky()

def q_sticky():
    x=input("Was it sticky? (yes/no)\n")
    if x == "yes":
        q_steak()
    else:
        q_emausaurus()
        
def q_boss():
    x=input("Was it a boss/lover/parent? (yes/no)\n")
    if x == "yes":
        q_expensive()
    else:
        print("Decision: Eat it.")
        

def q_emausaurus():
    x=input("Is it an Emausaurus? (yes/no)\n")
    if x == "yes":
        q_megalosaurus()
    else:
        q_cat_lick()
        

def q_steak():
    x=input("Is it a raw steak? (yes/no)\n")
    if x == "yes":
        q_puma()
    else:
        q_cat_lick()
        

def q_cat_lick():
    x=input("Did the cat lick it? (yes/no)\n")
    if x == "yes":
        q_cat_healthy()
    else:
        print("Decision: Eat it.")
        

def q_cat_healthy():
    x=input("Is your cat healthy? (yes/no)\n")
    if x == "yes":
        print("Decision: Eat it.")
    else:
        print("Decision: Your call.")
        

def q_megalosaurus():
    x=input("Are you a Megalosaurus? (yes/no)\n")
    if x == "yes":
        print("Decision: Eat it.")
    else:
        print("Decision: Don't eat it.")
        

def q_puma():
    x=input("Are you a puma? (yes/no)\n")
    if x == "yes":
        print("Decision: Eat it.")
    else:
        print("Decision: Don't eat it.")
        

def q_expensive():
    x=input("Was it expensive? (yes/no)\n")
    if x == "yes":
        q_cut()
    else:
        q_chocolate()
        

def q_cut():
    x=input("Can you cut off the part that touched the floor? (yes/no)\n")
    if x == "yes":
        print("Decision: Eat it.")
    else:
        print("Decision: Your call.")
        

def q_chocolate():
    x=input("Is it chocolate? (yes/no)\n")
    if x == "yes":
        print("Decision: Eat it.")
    else:
        print("Decision: Don't eat it.")

q_see()
