# question 2
# justin valsecchi
# 14 march 2014

def displayName ():
    print("Welcome to the 30 Second Rule Expert")
    print('-'*36)
    
def main ():
    displayName ()
    print("Answer the following questions by selecting from among the options.")
    choice = input("Did anyone see you? (yes/no)\n")
    if choice == 'yes':
        choice = input("Was it a boss/lover/parent? (yes/no)\n")
        if choice == 'yes':
            choice = input("Was it expensive? (yes/no)\n")
            if choice == 'yes':
                choice = input("Can you cut off the part that touched the floor? (yes/no)\n")
                if choice == 'yes':
                    print("Decision: Eat it.")
                else:
                    print("Decision: Your call.")
            else:
                choice = input("Is it chocolate? (yes/no)\n")
                if choice == 'yes':
                    print("Decision: Eat it.")
                else:
                    print("Decision: Don't eat it.")
        else:
            print("Decision: Eat it.")
    else:
        choice = input("Was it sticky? (yes/no)\n")
        if choice == 'yes':
            choice = input("Is it a raw steak? (yes/no)\n")
            if choice == 'yes':
                choice = input("Are you a puma? (yes/no)\n")
                if choice == 'yes':
                    print("Decision: Eat it.")
                else:
                    print("Decision: Don't eat it.")
            else:
                choice = input("Did the cat lick it? (yes/no)\n")
                if choice == 'yes':
                    choice = input("Is your cat healthy? (yes/no)\n")
                    if choice == 'yes':
                        print("Decision: Eat it.")
                    else:
                        print("Decision: Your call.")
                else:
                    print("Decision: Eat it.")
        else:
            choice = ("Is it an Emausaurus? (yes/no)\n")
            if choice == 'yes':
                choice = input("Are you a Megalosaurus? (yes/no)\n")
                if choice == 'yes':
                    print("Decision: Eat it.")
                else:
                    print("Decision: Don't eat it.")
            else:
                choice = input("Did the cat lick it? (yes/no)\n")
                if choice == 'yes':
                    choice = input("Is your cat healthy? (yes/no)\n")
                    if choice == 'yes':
                        print("Decision: Eat it.")
                    else:
                        print("Decision: Your call.")
                else:
                    print("Decision: Eat it.")                
                
main ()


