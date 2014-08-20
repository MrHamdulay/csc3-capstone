# The 30 second Rule Expert
# Done by Kelly Isaacs
# 10-03-2014

# Display Name
print("Welcome to the 30 Second Rule Expert")
print("------------------------------------")
print("Answer the following questions by selecting from among the options.")

def q1():
    answer1=input("Did anyone see you? (yes/no)\n")
    if answer1 =="yes":
        q2()
    elif answer1=="no":
        q6()
        
def q2():
    answer2=input("Was it a boss/lover/parent? (yes/no)\n")
    if answer2=="yes":
        q3()
    elif answer2=="no":
        conc2()
    
def q3():
    answer3=input("Was it expensive? (yes/no)\n")
    if answer3=="yes":
        q4()
    elif answer3=="no":
        q5()
    
def q4():
    answer4=input("Can you cut off the part that touched the floor? (yes/no)\n")
    if answer4=="yes":
        conc2()
    elif answer4=="no":
        conc3()
    
def q5():
    answer5=input("Is it chocolate? (yes/no)\n")
    if answer5=="yes":
        conc2()
    elif answer5=="no":
        conc1()
    
def q6():
    answer6=input("Was it sticky? (yes/no)\n")
    if answer6=="yes":
        q8()
    elif answer6=="no":
        q7()
    
def q7():
    answer7=input("Is it an Emausaurus? (yes/no)\n")
    if answer7=="yes":
        q9()
    elif answer7=="no":
        q10()
    
def q8():
    answer8=input("Is it a raw steak? (yes/no)\n")
    if answer8=="yes":
        q11()
    elif answer8=="no":
        q10()
    
def q9():
    answer9=input("Are you a Megalosaurus? (yes/no)\n")
    if answer9=="yes":
        conc2()
    elif answer9=="no":
        conc1()
    
def q10():
    answer10=input("Did the cat lick it? (yes/no)\n")
    if answer10=="yes":
        q12()
    elif answer10=="no":
        conc2()
    
def q11():
    answer11=input("Are you a puma? (yes/no)\n")
    if answer11=="yes":
        conc2()
    elif answer11=="no":
        conc1()
    
def q12():
    answer12=input("Is your cat healthy? (yes/no)\n")
    if answer12=="yes":
        conc2()
    elif answer12=="no":
        conc3()
    
def conc1():
    print("Decision: Don't eat it.")
    
def conc2():
    print("Decision: Eat it.")
    
def conc3():
    print("Decision: Your call.")
    
q1()