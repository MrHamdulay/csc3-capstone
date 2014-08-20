# Assignment 2 - Question 2
#07 March 2014
#Jayan Smart
#Funtion Library:
def a(): #see
    x = input("Did anyone see you? (yes/no)\n")
    if x == 'yes':
        i()
    elif x == 'no':
        b()
    else:
        a()
def b(): #sticky
    x = input("Was it sticky? (yes/no)\n")
    if x== 'yes':
            g()
    elif x == 'no':
            c()
    else:
            b()
def c(): #emousaurus
    x = input("Is it an Emausaurus? (yes/no)\n")
    if x == 'yes':
        d()
    elif x == 'no':
        e()
    else:
        c()  
def d(): #megalosaurus
    x = input("Are you a Megalosaurus? (yes/no)\n")
    if x == 'yes':
        eat()
    elif x == 'no':
        dont_eat()
    else:
        d()
def e(): #cat lick
    x = input("Did the cat lick it? (yes/no)\n")
    if x == 'yes':
        f()
    elif x == 'no':
        eat()
    else:
        e()
def f(): #cat health
    x = input("Is your cat healthy? (yes/no)\n")
    if x == 'yes':
        eat()
    elif x == 'no':
        call()
    else:
        f()
def g(): #steak
    x = input("Is it a raw steak? (yes/no)\n")
    if x == 'yes':
        h()
    elif x == 'no':
        e()
    else:
        g()
def h(): #puma
    x = input("Are you a puma? (yes/no)\n")
    if x == 'yes':
        eat()
    elif x == 'no':
        dont_eat()
    else:
        h()
def i(): #boss/lover/parent
    x = input("Was it a boss/lover/parent? (yes/no)\n")
    if x == 'yes':
        j()
    elif x == 'no':
        eat()
    else:
        i()
def j(): #price
    x = input("Was it expensive? (yes/no)\n")
    if x == 'yes':
        l()
    elif x == 'no':
        k()
    else:
        j()
def k(): #chocolate
    x = input("Is it chocolate? (yes/no)\n")
    if x == 'yes':
        eat()
    elif x == 'no':
        dont_eat()
    else:
        k()
def l(): #cut
    x = input("Can you cut off the part that touched the floor? (yes/no)\n")
    if x == 'yes':
        eat()
    elif x == 'no':
        call()
    else:   
        l()
def eat():
    print("Decision: Eat it.")
def dont_eat():
    print("Decision: Don't eat it.")
def call():
    print("Decision: Your call.")
x = 2
print("""
Welcome to the 30 Second Rule Expert
------------------------------------
Answer the following questions by selecting from among the options.""")
a()


    
