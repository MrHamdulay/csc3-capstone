print("Welcome to the 30 Second Rule Expert")
print("------------------------------------")
print("Answer the following questions by selecting from among the options.")
q1 = input("Did anyone see you? (yes/no)\n")
if q1 == "yes":
    Aq2y = input("Was it a boss/lover/parent? (yes/no)\n")
    if Aq2y == "yes":
        Aq3y = input("Was it expensive? (yes/no)\n")
        if Aq3y == "yes":
            Aq4y = input("Can you cut off the part that touched the floor? (yes/no)\n")
            if Aq4y == "yes":
                print("Decision: Eat it.")
            elif Aq4y == "no":
                print("Decision: Your call.")
            else:
                print("Invalid Input")
        elif Aq3y == "no":
            Aq4n = input("Is it chocolate? (yes/no)\n")
            if Aq4n == "yes":
                print("Decision: Eat it.")
            elif Aq4n == "no":
                print("Decision: Don't eat it.")
            else:
                print("Invalid Input")
        else:
            print("Invalid Input")            
    elif Aq2y == "no":
        print("Decision: Eat it.") 
    else:
        print("Invalid Input")
elif q1 == "no":
    Bq2n = input("Was it sticky? (yes/no)\n")
    if Bq2n == "yes":
        Bq3y = input("Is it a raw steak? (yes/no)\n")
        if Bq3y == "yes":
            Bq4y = input("Are you a puma? (yes/no)\n")
            if Bq4y == "yes":
                print("Decision: Eat it.")
            elif Bq4y == "no":
                print("Decision: Don't eat it.")
            else:
                print("Invalid Input")
        elif Bq3y == "no":
            Bq7n = input("Did the cat lick it? (yes/no)\n")
            if Bq7n == "yes":
                Bq8n = input("Is your cat healthy? (yes/no)\n")
                if Bq8n == "yes":
                    print("Decision: Eat it.")
                elif Bq8n == "no":
                    print("Decision: Don't eat it.")
            elif Bq7n == "no":
                print("Decision: Eat it.")
        else:
            print("Invalid Input")
    elif Bq2n == "no":
        Bq3n = input("Is it an Emausaurus? (yes/no)\n")
        if Bq3n == "yes":
            Bq4n = input("Are you a Megalosaurus? (yes/no)\n")
            if Bq4n == "yes":
                print("Decision: Eat it.")
            elif Bq4n == "no":
                print("Decision: Don't eat it.")
        elif Bq3n == "no":
            Bq5n = input("Did the cat lick it? (yes/no)\n")
            if Bq5n == "yes":
                Bq6n = input("Is your cat healthy? (yes/no)\n")
                if Bq6n == "yes":
                    print("Decision: Eat it.")
                elif Bq6n == "no":
                    print("Decision: Your call.")
                else:
                    print("Inalid Input")
            elif Bq5n == "no":
                print("Decision: Eat it.")
            else:
                print("Invalid Input")
        else:
            print("Invalid Input")
    else:
        print("Invalid Input")
            
else:
    print("Invalid Input")
    