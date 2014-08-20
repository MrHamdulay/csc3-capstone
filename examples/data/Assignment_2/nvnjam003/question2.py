print ("Welcome to the 30 Second Rule Expert")
print ("------------------------------------")
print ("Answer the following questions by selecting from among the options.")
answer = input("Did anyone see you? (yes/no)\n")
if (answer == "yes"):
    answer = input("Was it a boss/lover/parent? (yes/no)\n")
    if (answer == "yes"):
        answer = input("Was it expensive? (yes/no)\n")
        if (answer == "yes"):
            answer = input("Can you cut off the part that touched the floor? (yes/no)\n")
            if (answer == "yes"):
                eat = 1
            else:
                eat = 0
        else:
            answer = input("Is it chocolate? (yes/no)\n")
            if (answer == "yes"):
                eat = 1
            else:
                eat = -1
    else:
        eat = 1
else:
    answer = input("Was it sticky? (yes/no)\n")
    if (answer == "yes"):
        answer = input("Is it a raw steak? (yes/no)\n")
        if (answer == "yes"):
            answer = input("Are you a puma? (yes/no)\n")
            if (answer == "yes"):
                eat = 1
            else:
                eat = -1
        else:
            answer = input("Did the cat lick it? (yes/no)\n")
            if (answer == "yes"):
                answer = input("Is your cat healthy? (yes/no)\n")
                if (answer == "yes"):
                    eat = 1
                else:
                    eat = 0
            else:
                eat = 1
    else:
        answer = input("Is it an Emausaurus? (yes/no)\n")
        if (answer == "yes"):
            answer = input("Are you a Megalosaurus? (yes/no)\n")
            if (answer == "yes"):
                eat = 1
            else:
                eat = -1
        else:
            answer = input("Did the cat lick it? (yes/no)\n")
            if (answer == "yes"):
                    answer = input("Is your cat healthy? (yes/no)\n")
                    if (answer == "yes"):
                        eat = 1
                    else:
                        eat = 0
            else:
                eat = 1            
if (eat == 1):
    print ("Decision: Eat it.")
elif (eat == 0):
    print ("Decision: Your call.")
else:
    print ("Decision: Don't eat it.")