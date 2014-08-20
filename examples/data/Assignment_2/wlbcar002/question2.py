print("Welcome to the 30 Second Rule Expert\n", "-"*36+"\nAnswer the following questions by selecting from among the options.",sep="")
op1 = input("Did anyone see you? (yes/no)\n")

def catFunc():
    cat = input("Did the cat lick it? (yes/no)\n")
    if cat == "yes":
        cat1 = input("Is your cat healthy? (yes/no)\n")
        if cat1 == "yes":
                print("Decision: Eat it.")
        else:
                print("Decision: Your call.")    
    else:
        print("Decision: Eat it.")
        
    
if op1 == "yes":
    op11 = input("Was it a boss/lover/parent? (yes/no)\n")
    if op11 == "yes":
            op111 = input("Was it expensive? (yes/no)\n")
            if op111 == "yes":
                op1111 = input("Can you cut off the part that touched the floor? (yes/no)\n")
                if op1111 == "yes":
                    print("Decision: Eat it.")
                else:
                    print("Decision: Your call.")
            else:
                op1112 = input("Is it chocolate? (yes/no)\n")
                if op1112 == "yes":
                    print("Decision: Eat it.")         
                else:
                    print("Decision: Don't eat it.")
    else:
            print("Decision: Eat it.")
else:
    op2 = input("Was it sticky? (yes/no)\n")
    if op2 == "yes":
        op21 = input("Is it a raw steak? (yes/no)\n")
        if op21 == "yes":
            op211 = input("Are you a puma? (yes/no)\n")
            if op211 == "yes":
                print("Decision: Eat it.")
            else:
                print("Decision: Don't eat it.")
        else:
            catFunc()
    else:
        op22 = input("Is it an Emausaurus? (yes/no)\n")
        if op22 == "yes":
            op221 = input("Are you a Megalosaurus? (yes/no)\n")
            if op221 == "yes":
                print("Decision: Eat it.")
            else:
                print("Decision: Don't eat it.")
        else:    
            catFunc()