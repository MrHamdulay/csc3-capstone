print("Welcome to the 30 Second Rule Expert")
print("------------------------------------")
print("Answer the following questions by selecting from among the options.")
def see():
    a=input("Did anyone see you? (yes/no)\n").lower()
    if a == "yes":
        lover()
    else:
        sticky()           
def eat():
    g=input("Decision: Eat it.").lower()
def sticky():
    f=input("Was it sticky? (yes/no)\n").lower()
    if f=="yes":
        raw()
    else:
        ema()
    
def lover():
    b=input("Was it a boss/lover/parent? (yes/no)\n").lower()
    if b == "no":
        eat()
    else:
        exp()
def exp():
    c=input("Was it expensive? (yes/no)\n").lower()
    if c== "yes":
        floor()
    else:
        choc()
def choc():
    d=input("Is it chocolate? (yes/no)\n").lower()
    if d== "yes":
        eat()
    elif d=="no":
        print("Decision: Don't eat it.")
def floor():
    e=input("Can you cut off the part that touched the floor? (yes/no)\n").lower() 
    if e=="yes":
        eat()
    elif e== "no":
        call()
def eat():
    print("Decision: Eat it.")
def call():
    i=input("Decision: Your call.") 
def ema():
    j=input("Is it an Emausaurus? (yes/no)\n").lower()
    if j=="yes":
        mega()
    elif j=="no":
        cat()
def raw():
    k=input("Is it a raw steak? (yes/no)\n").lower()
    if k=="yes":
        puma()
    elif k=="no":
        cat()
def cat():
    l=input("Did the cat lick it? (yes/no)\n").lower()
    if l=="yes":
        healthy()
    elif l=="no":
        eat()
def puma():
    m=input("Are you a puma? (yes/no)\n").lower()
    if m=="no":
        print("Decision: Don't eat it.")
    elif m=="yes":
        eat()
def mega():
    n=input("Are you a Megalosaurus? (yes/no)\n").lower()
    if n=="yes":
        eat()
    elif n=="no":
        print("Decision: Don't eat it.")
def healthy():
    o=input("Is your cat healthy? (yes/no)\n").lower()
    if o=="yes":
        eat()
    elif o=="no":
        call()

see()        
            
        
        
        
        
        
        
