# question2.py
#   a program to determine whether or not you should eat the food

def main():
    print("Welcome to the 30 Second Rule Expert")
    print("------------------------------------") 
    print("Answer the following questions by selecting from among the options.") 
    q1 = input("Did anyone see you? (yes/no)\n") 
    if q1 == "yes":
        q2a = input("Was it a boss/lover/parent? (yes/no)\n")
        if q2a == "yes":
            q3 = input("Was it expensive? (yes/no)\n") 
            if q3 == "yes":
                q4a = input("Can you cut off the part that touched the floor? (yes/no)\n")
                if q4a == "yes":
                    print("Decision: Eat it.")
                else:
                    print("Decision: Your call.")
            else:
                q4b = input("Is it chocolate? (yes/no)\n")
                if q4b == "yes":
                    print("Decision: Eat it.")
                else:
                    print("Decision: Don't eat it.")
        else:
            print("Decision: Eat it.")
    else:
        q2b = input("Was it sticky? (yes/no)\n") 
        if q2b == "yes":
            q5a = input("Is it a raw steak? (yes/no)\n") 
            if q5a == "yes":
                q6a = input("Are you a puma? (yes/no)\n")
                if q6a == "yes":
                    print("Decision: Eat it.")
                else:
                    print("Decision: Don't eat it.") 
            else:
                q6b = input("Did the cat lick it? (yes/no)\n")
                if q6b == "yes":
                    q7 = input("Is your cat healthy? (yes/no)\n")
                    if q7 == "yes":
                        print("Decision: Eat it.") 
                    else:
                        print("Decision: Your call") 
                else:
                    print("Decision: Eat it.") 
        else:
            q5b = input("Is it an Emausaurus? (yes/no)\n")
            if q5b == "yes":
                q8a = input("Are you a Megalosaurus? (yes/no)\n")
                if q8a == "yes":
                    print("Decision: Eat it.")
                else:
                    print("Decision: Don't eat it.")
            else:
                q8b = input("Did the cat lick it? (yes/no)\n")
                if q8b == "yes":
                    q9 = input("Is your cat healthy? (yes/no)\n")
                    if q9 == "yes":
                        print("Decision: Eat it.")
                    else:
                        print("Decision: Your call.")
                else:
                    print("Decision: Eat it.")
                    
main()

                