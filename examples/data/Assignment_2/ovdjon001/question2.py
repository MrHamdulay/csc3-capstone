def main():
    print("Welcome to the 30 Second Rule Expert")
    print("------------------------------------")
    thirtySecondRule()
    
def thirtySecondRule():
    print("Answer the following questions by selecting from among the options.")
    response = input("Did anyone see you? (yes/no)")
    print()
    if response == "yes":
        response = input("Was it a boss/lover/parent? (yes/no)")
        print()
        if response == "yes":
            response = input("Was it expensive? (yes/no)")
            print()
            if response == "yes":
                response = input("Can you cut off the part that touched the floor? (yes/no)")
                print()
                if response == "yes":
                    print("Decision: Eat it.")
                else:
                    print("Decision: Your call.")
            else:
                response = input("Is it chocolate? (yes/no)")
                print()
                if response == "yes":
                    print("Decision: Eat it.")
                else:
                    print("Decision: Don't eat it.")
                    
        else:
            print("Decision: Eat it.")
    else:
        response = input("Was it sticky? (yes/no)")
        print()
        if response == "yes":
            response = input("Is it a raw steak? (yes/no)")
            print()
            if response == "yes":
                response = input("Are you a puma? (yes/no)")
                print()
                if response == "yes":
                    print("Decision: Eat it.")
                else:
                    print("Decision: Don't eat it.")   
            else:
                response = input("Did the cat lick it? (yes/no)")
                print()
                if response == "yes":
                    response = input("Is your cat healthy? (yes/no)")
                    print()
                    if response == "yes":
                        print("Decision: Eat it.")
                    else:
                        print("Decision: Your call.")
                else:
                    print("Decision: Eat it.")
        else:
            response = input("Is it an Emausaurus? (yes/no)")
            print()
            if response == "yes":
                response = input("Are you a Megalosaurus? (yes/no)")
                print()
                if response == "yes":
                    print("Decision: Eat it.")
                else:
                    print("Decision: Don't eat it.")   
            else:
                response = input("Did the cat lick it? (yes/no)")
                print()
                if response == "yes":
                    response = input("Is your cat healthy? (yes/no)")
                    print()
                    if response == "yes":
                        print("Decision: Eat it.")
                    else:
                        print("Decision: Your call.")
                else:
                    print("Decision: Eat it.")
                    
             
main()