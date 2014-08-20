# Define End Decisions
def eat():
    print ("Decision: Eat it.")
    
def dont():
    print ("Decision: Don't eat it.")
    
def call():
    print ("Decision: Your call.")
    
# See
def see():
    ans = input("Did anyone see you? (yes/no)\n")
    if ans == 'yes':
        who()
    elif ans == 'no':
        sticky()

# Who
def who():
    ans = input("Was it a boss/lover/parent? (yes/no)\n")
    if ans == 'yes':
        expensive()
    elif ans == 'no':
        eat()

# Sticky
def sticky():
    ans = input("Was it sticky? (yes/no)\n")
    if ans == 'yes':
        steak()
    elif ans == 'no':
        dino()
        
# Expensive
def expensive():
    ans = input("Was it expensive? (yes/no)\n")
    if ans == 'yes':
        cut()
    elif ans == 'no':
        chocolate()

# Steak
def steak():
    ans = input("Is it a raw steak? (yes/no)\n")
    if ans == 'yes':
        puma()
    elif ans == 'no':
        lick()
        
# Dino
def dino():
    ans = input("Is it an Emausaurus? (yes/no)\n")
    if ans == 'yes':
        you()
    elif ans == 'no':
        lick()
        
# Cut
def cut():
    ans = input("Can you cut off the part that touched the floor? (yes/no)\n")
    if ans == 'yes':
        eat()
    elif ans == 'no':
        call()
        
# Chocolate
def chocolate():
    ans = input("Is it chocolate? (yes/no)\n")
    if ans == 'yes':
        eat()
    elif ans == 'no':
        dont()
        
# Puma
def puma():
    ans = input("Are you a puma? (yes/no)\n")
    if ans == 'yes':
        eat()
    elif ans == 'no':
        dont()
        
# Lick
def lick():
    ans = input("Did the cat lick it? (yes/no)\n")
    if ans == 'yes':
        healthy()
    elif ans == 'no':
        eat()
        
# You
def you():
    ans = input("Are you a Megalosaurus? (yes/no)\n")
    if ans == 'yes':
        eat()
    elif ans == 'no':
        dont()
        
# Healthy
def healthy():
    ans = input("Is your cat healthy? (yes/no)\n")
    if ans == 'yes':
        eat()
    elif ans == 'no':
        call()

# Main Program        
print ("Welcome to the 30 Second Rule Expert")
print ("------------------------------------")
print ("Answer the following questions by selecting from among the options.")
see()