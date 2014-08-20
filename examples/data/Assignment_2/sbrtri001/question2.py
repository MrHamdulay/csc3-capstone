# Tristan Subroyen
# Assignment 2 Question 2

print("Welcome to the 30 Second Rule Expert")
print("------------------------------------")
print("Answer the following questions by selecting from among the options.")
q = input("Did anyone see you? (yes/no)\n")
eat = "Decision: Eat it."
no = "Decision: Don't eat it."
yc = "Decision: Your call."
if (q == "yes") or (q == "Yes"):
    q_y = input("Was it a boss/lover/parent? (yes/no)\n")
    if (q_y == "yes") or (q_y == "Yes"):
        q_y_y = input("Was it expensive? (yes/no)\n")
        if (q_y_y == "yes") or (q_y_y == "Yes"):
            q_y_y_y = input("Can you cut off the part that touched the floor? (yes/no)\n")
            if (q_y_y_y == "yes") or (q_y_y_y == "Yes"):
                print(eat)
            elif (q_y_y_y == "no") or (q_y_y_y == "No"):
                print(yc)
        elif (q_y_y == "no") or (q_y_y == "No"):
            q_y_y_n = input("Is it chocolate? (yes/no)\n")
            if (q_y_y_n == "yes") or (q_y_y_n == "Yes"):
                print(eat)
            elif (q_y_y_n == "no") or (q_y_y_n == "No"):
                print(no)
    elif (q_y == "no") or (q_y == "No"):
        print(eat)
        
elif (q == "no") or (q == "No"):
    q_n = input("Was it sticky? (yes/no)\n")
    if (q_n == "no") or (q_n == "No"):
        q_n_n = input("Is it an Emausaurus? (yes/no)\n")
        if (q_n_n == "no") or (q_n_n == "No"):
            q_n_n_n = input("Did the cat lick it? (yes/no)\n")
            if (q_n_n_n == "no") or (q_n_n_n == "No"):
                print(eat)
            elif (q_n_n_n == "yes") or (q_n_n_n == "Yes"):
                q_n_n_n_y = input("Is your cat healthy? (yes/no)\n")
                if (q_n_n_n_y == "no") or (q_n_n_n_y == "No"):
                    print(yc)
                elif (q_n_n_n_y == "yes") or (q_n_n_n_y == "Yes"):
                    print(eat)
        elif (q_n_n == "yes") or (q_n_n == "Yes"):
            q_n_n_y = input("Are you a Megalosaurus? (yes/no)\n")
            if (q_n_n_y == "no") or (q_n_n_y == "No"):
                print(no)
            elif (q_n_n_y == "yes") or (q_n_n_y == "Yes"):
                print(eat)
    elif (q_n == "yes") or (q_n == "Yes"):
        q_n_y = input("Is it a raw steak? (yes/no)\n")
        if (q_n_y == "no") or (q_n_y == "No"):
            q_n_y_n = input("Did the cat lick it? (yes/no)\n")
            if (q_n_y_n == "no") or (q_n_y_n == "No"):
                print(eat)
            elif (q_n_y_n == "yes") or (q_n_y_n == "Yes"):
                q_n_y_n_y = input("Is your cat healthy? (yes/no)\n")
                if (q_n_y_n_y == "no") or (q_n_y_n_y == "No"):
                    print(yc)
                elif (q_n_y_n_y == "yes") or (q_n_y_n_y == "Yes"):
                    print(eat)
        elif (q_n_y == "yes") or (q_n_y == "Yes"):
            q_n_y_y = input("Are you a puma? (yes/no)\n")
            if (q_n_y_y == "no") or (q_n_y_y == "No"):
                print(no)
            elif (q_n_y_y == "yes") or (q_n_y_y == "Yes"):
                print(eat)
                
        
        
    
        
        
                
                
