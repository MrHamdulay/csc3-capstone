#Assignment 2: Question 2
#Asil Motala
#MTLASI002
print("Welcome to the 30 Second Rule Expert")
print("------------------------------------")
print("Answer the following questions by selecting from among the options.")
Q1=input("Did anyone see you? (yes/no)\n")
Q2=0
Q3=0
if Q1=="no":
    Q2=input("Was it sticky? (yes/no)\n")
else:
    Q3=input("Was it a boss/lover/parent? (yes/no)\n")

if Q3=="yes":
    Q4=input("Was it expensive? (yes/no)\n")
    if Q4=="yes":
        Q5=input("Can you cut off the part that touched the floor? (yes/no)\n")
        if Q5=="yes":
            print("Decision: Eat it.")
        else:
            print("Decision: Your call.")        
    else:
        Q6=input("Is it chocolate? (yes/no)\n")
        if Q6=="yes":
            print("Decision: Eat it.")
        else:
            print("Decision: Don't eat it.")        
elif Q3=="no":
    print("Decision: Eat it.")
else:
    print("",end="")


if Q2=="yes":
    Q7=input("Is it a raw steak? (yes/no)\n")
    if Q7=="yes":
        Q9=input("Are you a puma? (yes/no)\n")
        if Q9=="yes":
            print("Decision: Eat it.")
        else:
            print("Decision: Don't eat it.")        
    else:
        Q10=input("Did the cat lick it? (yes/no)\n")
        if Q10=="yes":
            Q12=input("Is your cat healthy? (yes/no)\n")
            if Q12=="yes":
                print("Decision: Eat it.")
            else:
                print("Decision: Your call.")            
        else:
            print("Decision: Eat it.")        
elif Q2=="no":
    Q8=input("Is it an Emausaurus? (yes/no)\n")
    if Q8=="yes":
        Q11=input("Are you a Megalosaurus? (yes/no)\n")
        if Q11=="yes":
            print("Decision: Eat it.")
        else:
            print("Decision: Don't eat it.")        
    else:
        Q10=input("Did the cat lick it? (yes/no)\n")
        if Q10=="yes":
            Q12=input("Is your cat healthy? (yes/no)\n")
            if Q12=="yes":
                print("Decision: Eat it.")
            else:
                print("Decision: Your call.")            
        else:
            print("Decision: Eat it.")
else:
    print("",end="")