#You dropped your food on the floor
#Palesa Magudulela
#14/03/2014

print("Welcome to the 30 Second Rule Expert")
print("-"*36)
print("Answer the following questions by selecting from among the options.")
n=input("Did anyone see you? (yes/no) \n")
if n=="yes":
    n=input("Was it a boss/lover/parent? (yes/no) \n")
    if n=='yes':
        n=input("Was it expensive? (yes/no) \n")
        if n=='yes':
            n=input("Can you cut off the part that touched the floor? (yes/no) \n")
            if n=="yes":
                print("Decision: Eat it.")
            if n=="no":
                print("Decision: Your call.")
        elif n=='no':
            n=input("Is it chocolate? (yes/no) \n")
            if n=="yes":
                print("Decision: Eat it.")
            if n=="no":
                print("Decision: Don't eat it.")
    elif n=="no":
        print("Decision: Eat it.")
elif n=='no':
    n=input("Was it sticky? (yes/no) \n")
    if n=='yes':
        n=input("Is it a raw steak? (yes/no) \n")
        if n=="yes":
            n=input("Are you a puma? (yes/no) \n")
            if n=="yes":
                print("Decision: Eat it.")
            if n=="no":
                print("Decision: Don't eat it.")
        elif n=="no":
            n=input("Did the cat lick it? (yes/no) \n")
            if n=='yes':
                n=input("Is your cat healthy? (yes/no) \n")
                if n=="yes":
                    print("Decision: Eat it.")
                if n=="no":
                    print("Decision: Your call.")
            elif n=="no":
                print("Decision: Eat it.")
    elif n=='no':
        n=input("Is it an Emausaurus? (yes/no) \n")
        if n=="yes":
            n=input("Are you a Megalosaurus? (yes/no) \n")
            if n=="yes":
                print("Decision: Eat it.")
            if n=="no":
                print("Decision: Don't eat it.")
        elif n=='no':
            n=input("Did the cat lick it? (yes/no) \n")
            if n=='yes':
                n=input("Is your cat healthy? (yes/no) \n")
                if n=='yes':
                    print("Decision: Eat it.")
                if n=='no':
                    print('Decision: Your call.')
            elif n=='no':
                print("Decision: Eat it.")
                
        