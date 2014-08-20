print("Welcome to the 30 Second Rule Expert")
print("-"*36) #prints a welcome message
print("Answer the following questions by selecting from among the options.")

eat_it="Decision: Eat it."
your_call="Decision: Your call."
eat_it="Decision: Eat it."
do_not="Decision: Don't eat it."
q1=input("Did anyone see you? (yes/no)\n") #asks the user to answer yes or no
#q1=q1.lower,q1.upper()
if q1=="yes":
    q2=input("Was it a boss/lover/parent? (yes/no)\n")
    if q2=="yes":
        q3=input("Was it expensive? (yes/no)\n")
        if q3=="yes":
            q4=input("Can you cut off the part that touched the floor? (yes/no)\n")
            if q4=="yes":
                print(eat_it)
            elif q4=="no":
                print(your_call)
        elif q3=="no":
            q5=input("Is it chocolate? (yes/no)\n")
            if q5=="yes":
                print(eat_it)
            elif q5=="no":
                print(do_not)
    elif "no":
        print(eat_it)
        
elif q1=="no":
    q6=input("Was it sticky? (yes/no)\n")
    if q6=="yes":
        q7=input("Is it a raw steak? (yes/no)\n")
        if q7=="yes":
            q8=input("Are you a puma? (yes/no)\n")
            if q8=="yes":
                print(eat_it)
            elif q8=="no":
                print(do_not)
        elif q7=="no":
            q8=input("Did the cat lick it? (yes/no)\n")
            if q8=="yes":
                q9=input("Is your cat healthy? (yes/no)\n")
                if q9=="yes":
                    print(eat_it)
                elif q9=="no":
                    print(your_call)
            elif q8=="no":
                print(eat_it)
    if q6=="no":
        q21=input("Is it an Emausaurus? (yes/no)\n")
        if q21=="yes":
            q22=input("Are you a Megalosaurus? (yes/no)\n")
            if q22=="yes":
                print(eat_it)
            elif q22=="no":
                print(do_not)
        elif q21=="no":
            q23=input("Did the cat lick it? (yes/no)\n")
            if q23=="yes":
                q24=input("Is your cat healthy? (yes/no)\n")
                if q24=="yes":
                    print(eat_it)
                elif q24=="no":
                    print(your_call)
            elif q23=="no":
                print(eat_it)