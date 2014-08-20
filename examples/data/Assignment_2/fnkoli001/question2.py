print("Welcome to the 30 Second Rule Expert\n------------------------------------"
      "\nAnswer the following questions by selecting from among the options.")

def eat_it():
    print("Decision: Eat it.")


def dont_eat_it():
    print("Decision: Don't eat it.")


def your_call():
    print("Decision: Your call.")


def cat_eat():
    if input("Did the cat lick it? (yes/no)\n") == "yes":
        if input("Is your cat healthy? (yes/no)\n") == "yes":
            eat_it()
        else:
            your_call()
    else:
        eat_it()

if input("Did anyone see you? (yes/no)\n") == "yes":
    if input("Was it a boss/lover/parent? (yes/no)\n") == "yes":
        if input("Was it expensive? (yes/no)\n") == "yes":
            if input("Can you cut off the part that touched the floor? (yes/no)\n") == "yes":
                eat_it()
            else:
                your_call()
        else:
            if input("Is it chocolate? (yes/no)\n") == "yes":
                eat_it()
            else:
                dont_eat_it()
    else:
        eat_it()
else:
    if input("Was it sticky? (yes/no)\n") == "yes":
        if input("Is it a raw steak? (yes/no)\n") == "yes":
            if input("Are you a puma? (yes/no)\n") == "yes":
                eat_it()
            else:
                dont_eat_it()
        else:
            cat_eat()
    else:
        if input("Is it an Emausaurus? (yes/no)\n") == "yes":
            if input("Are you a Megalosaurus? (yes/no)\n") == "yes":
                eat_it()
            else:
                dont_eat_it()
        else:
            cat_eat()