# question2.py
# a program to determine whether or not to eat the food you dropped on the floor
# author: bxtnaa002

print("Welcome to the 30 Second Rule Expert")
print("------------------------------------")
print("Answer the following questions by selecting from among the options.")
response = input("Did anyone see you? (yes/no)\n")
response == 'yes' or response == 'no'
if response == 'yes':
    response = input("Was it a boss/lover/parent? (yes/no)\n")
    if response == 'yes':
        response = input("Was it expensive? (yes/no)\n")
        if response == 'yes':
            response = input("Can you cut off the part that touched the floor? (yes/no)\n")
            if response == 'yes':
                print("Decision: Eat it.")
            elif response == 'no':
                print("Decision: Your call.")
        elif response == 'no':
            response = input("Is it chocolate? (yes/no)\n")
            if response == 'yes':
                print("Decision: Eat it.")
            elif response == 'no':
                print("Decision: Don't eat it.")
    elif response == 'no':
        print("Decision: Eat it.")
elif response == 'no':
    response = input("Was it sticky? (yes/no)\n")
    if response == 'yes':
        response = input("Is it a raw steak? (yes/no)\n")
        if response == 'yes':
            response = input("Are you a puma? (yes/no)\n")
            if response == 'yes':
                print("Decision: Eat it.")
            elif response == 'no':
                print("Decision: Don't eat it.")
        elif response == 'no':
            response = input("Did the cat lick it? (yes/no)\n")
            if response == 'yes':
                response = input("Is your cat healthy? (yes/no)\n")
                if response == 'yes':
                    print("Decision: Eat it.")
                elif response == 'no':
                    print("Decision: Your call.")
            elif response == 'no':
                print("Decision: Eat it.")
    elif response == 'no':
        response = input("Is it an Emausaurus? (yes/no)\n")
        if response == 'yes':
            response = input("Are you a Megalosaurus? (yes/no)\n")
            if response == 'yes':
                print("Decision: Eat it.")
            elif response == 'no':
                print("Decision: Don't eat it.")
        elif response == 'no':
            response = input("Did the cat lick it? (yes/no)\n")
            if response == 'yes':
                response = input("Is your cat healthy? (yes/no)\n")
                if response == 'yes':
                    print("Decision: Eat it.")
                elif response == 'no':
                    print("Decision: Your call.")
            elif response == 'no':
                print("Decision: Eat it.")
                
                