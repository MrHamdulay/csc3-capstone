print("Welcome to the 30 Second Rule Expert")
print("------------------------------------")
print("Answer the following questions by selecting from among the options.")
print("Did anyone see you? (yes/no)")
a = input()
if a==str('yes'):
    print("Was it a boss/lover/parent? (yes/no)")
    a = input()
    if a==str('yes'):
        print("Was it expensive? (yes/no)")
        a = input()
        if a==str('yes'):
            print("Can you cut off the part that touched the floor? (yes/no)")
            a = input()
            if a==str('yes'):
                print("Decision: Eat it.")
            elif a==str('no'):
                print("Decision: Your call.")
        elif a==str('no'):
            print("Is it chocolate? (yes/no)")
            a = input()
            if a==str('yes'):
                print("Decision: Eat it.")
            elif a==str('no'):
                print("Decision: Don't eat it.")
    elif a==str('no'):
        print("Decision: Eat it.")    
elif a==str('no'):
    print("Was it sticky? (yes/no)")
    a = input()
    if a==str('yes'):
        print("Is it a raw steak? (yes/no)")
        a = input()
        if a==str('yes'):
            print("Are you a puma? (yes/no)")
            a = input()
            if a==str('yes'):
                print("Decision: Eat it.")
            elif a==str('no'):
                print("Decision: Don't eat it.")
        elif a==str('no'):
            print("Did the cat lick it? (yes/no)")
            a = input()
            if a==str('yes'):
                print("Is your cat healthy? (yes/no)")
                a = input()
                if a==str('yes'):
                    print("Decision: Eat it.")
                elif a==str('no'):
                    print("Decision: Your call.")
            elif a==str('no'):
                print("Decision: Eat it.")
    elif a==str('no'):
        print("Is it an Emausaurus? (yes/no)")
        a = input()
        if a==str('yes'):
            print("Are you a Megalosaurus? (yes/no)")
            a = input()
            if a==str('yes'):
                print("Decision: Eat it.")
            elif a==str('no'):
                print("Decision: Don't eat it.")
        elif a==str('no'):
            print("Did the cat lick it? (yes/no)")
            a = input()
            if a==str('yes'):
                print("Is your cat healthy? (yes/no)")
                a = input()
                if a==str('yes'):
                    print("Decision: Eat it.")
                elif a==str('no'):
                    print("Decision: Your call.")
            elif a==str('no'):
                print("Decision: Eat it.")