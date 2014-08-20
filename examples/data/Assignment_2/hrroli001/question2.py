# Assignment 1 - Question 2
# Oliver Harrison - HRROLI001
# 08 Match 2013

def cupcake():
    print("Welcome to the 30 Second Rule Expert")
    print(36*"-")
    print("Answer the following questions by selecting from among the options.")
    q1=input("Did anyone see you? (yes/no) \n")
    if q1=="yes":
        q2=input("Was it a boss/lover/parent? (yes/no) \n")
        if q2=="no":
            print("Decision: Eat it.")
        else:
            q3=input("Was it expensive? (yes/no) \n")
            if q3=="yes":
                q4=input("Can you cut off the part that touched the floor? (yes/no) \n")
                if q4=="no":
                    print("Decision: Your call.")
                else:
                        print("Decision: Eat it.")
            else:
                q5=input("Is it chocolate? (yes/no) \n")
                if q5=="yes":
                    print("Decision: Eat it.")
                else:
                    print("Decision: Don't eat it.")
    else:
        q6=input("Was it sticky? (yes/no) \n")
        if q6=="yes":
            q7=input("Is it a raw steak? (yes/no) \n")
            if q7=="yes":
                q8=input("Are you a puma? (yes/no) \n")
                if q8=="yes":
                    print("Decision: Eat it.")
                else:
                    print("Decision: Don't eat it.")
            else: 
                q9=input("Did the cat lick it? (yes/no) \n")
                if q9=="no":
                    print("Decision: Eat it.")
                else:
                    q10=input("Is your cat healthy? (yes/no) \n")
                    if q10=="yes":
                        print("Decision: Eat it.")
                    else:
                        print("Your call.")
        else:
            q11=input("Is it an Emausaurus? (yes/no) \n")
            if q11=="no":
                q9=input("Did the cat lick it? (yes/no) \n")
                if q9=="no":
                    print("Decision: Eat it.")
                else:                
                    q10=input("Is your cat healthy? (yes/no) \n")
                    if q10=="yes":
                        print("Decision: Eat it.")
                    else:
                        print("Decision: Your call.")                
            else:
                q12=input("Are you a Megalosaurus? (yes/no) \n")
                if q12=="no":
                    print("Decision: Don't eat it.")
                else:
                    print("Decision: Eat it.")
                    
cupcake()
                
                