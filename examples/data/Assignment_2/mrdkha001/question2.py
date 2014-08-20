# Question 2
# Name: Khanyisile Morudu
# Student Number: mrdkha001
# Date: 07/03/2014

def Cupcake_Check():
    print("\nWelcome to the 30 Second Rule Expert")
    print("------------------------------------")
    print("Answer the following questions by selecting from among the options.")
    Q1  = input("Did anyone see you? (yes/no) \n")
    if Q1 == "yes":
        Q2 = input("Was it a boss/lover/parent? (yes/no)\n")
        if Q2 == "yes":
            Q3 = input("Was it expensive? (yes/no)\n")
            if Q3 == "yes":
                Q4 = input("Can you cut off the part that touched the floor? (yes/no)\n")
                if Q4 == "yes":
                    print("Decision: Eat it.")
                else:
                    print("Decision: Your call.")
            else: 
                Q4 = input("Is it chocolate? (yes/no)\n")
                if Q4 == "yes":
                    print("Decision: Eat it.")
                else:
                    print("Decision: Don't eat it.")
        else: 
            print("Decision: Eat it.")
    else:
        Q2 = input("Was it sticky? (yes/no)\n")
        if Q2 == "yes":
            Q3 = input("Is it a raw steak? (yes/no)\n")
            if Q3 == "yes":
                Q4 = input("Are you a puma? (yes/no)\n")
                if Q4 == "yes":
                    print("Decision: Eat it.")
                else:
                    print("Decision: Don't eat it.")                
            else:
                Q4 = input("Did the cat lick it? (yes/no)\n")
                if Q4 == "yes":
                    Q5 = input("Is your cat healthy? (yes/no)\n")
                    if Q5 == "yes":
                        print("Decision: Eat it.")
                    else:
                        print("Decision: Your call.")
                else:
                    print("Eat it.")
        else:
            Q3 = input("Is it an Emausaurus? (yes/no)\n")
            if Q3 == "yes":
                Q4 = input("Are you a Megalosaurus? (yes/no)\n")
                if Q4 == "yes":
                    print("Decision: Eat it.")
                else:
                    print("Decision: Don't eat it.")      
            else:
                Q4 = input("Did the cat lick it? (yes/no)\n")
                if Q4 == "yes":
                    Q5 = input("Is your cat healthy? (yes/no)\n")
                    if Q5 == "yes":
                        print("Decision: Eat it.")  
                    else:
                        print("Decision: Your call.")
                else:
                    print("Decision: Eat it.")
Cupcake_Check()