def Q1():
    ans = input("Did anyone see you? (yes/no)\n")
    if ans == "yes":
        Q2()
    else:
        Q3()
def Q2():
    ans = input("Was it a boss/lover/parent? (yes/no)\n")
    if ans == "yes":
        Q4()
    else:
        eat()
def Q3():
    ans = input("Was it sticky? (yes/no)\n")
    if ans == "yes":
        Q5()
    else:
        Q6()
def Q4():
    ans = input("Was it expensive? (yes/no)\n")
    if ans == "yes":
        Q7()
    else:
        Q8()
def Q5():
    ans = input("Is it a raw steak? (yes/no)\n")
    if ans == "yes":
        Q9()
    else:
        Q10()
def Q6():
    ans = input("Is it an Emausaurus? (yes/no)\n")
    if ans == "yes":
        Q11()
    else:
        Q10()
def Q7():
    ans = input("Can you cut off the part that touched the floor? (yes/no)\n")
    if ans == "yes":
        eat()
    else:
        yourCall()
def Q8():
    ans = input("Is it chocolate? (yes/no)\n")
    if ans == "yes":
        eat()
    else:
        dontEat()
def Q9():
    ans = input("Are you a puma? (yes/no)\n")
    if ans == "yes":
        eat()
    else:
        dontEat()
def Q10():
    ans = input("Did the cat lick it? (yes/no)\n")
    if ans == "yes":
        Q12()
    else:
        eat()
def Q11():
    ans = input("Are you a Megalosaurus? (yes/no)\n")
    if ans == "yes":
        eat()
    else:
        dontEat()
def Q12():
    ans = input("Is your cat healthy? (yes/no)\n")
    if ans == "yes":
        eat()
    else:
        yourCall()
def eat():
    print("Decision: Eat it.")
def yourCall():
    print("Decision: Your call.")
def dontEat():
    print("Decision: Don't eat it.")
            
        
print("Welcome to the 30 Second Rule Expert\n------------------------------------\nAnswer the following questions by selecting from among the options.")
Q1()