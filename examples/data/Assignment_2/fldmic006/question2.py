yours = "Decision: Your call."
eat = "Decision: Eat it."

print("Welcome to the 30 Second Rule Expert\n"""
      "------------------------------------\n"""
      "Answer the following questions by selecting from among the options.")
in1 = input("Did anyone see you? (yes/no)\n")

#someone saw you eat
if(in1 == "yes"):
    in2 = input("Was it a boss/lover/parent? (yes/no)\n")
    if (in2 == "yes"):
        in3 = input("Was it expensive? (yes/no)\n")
        if (in3 == "yes"):
            in4 = input("Can you cut off the part that touched the floor? (yes/no)\n")
            if (in4 == "yes"):
                    print(eat)
            else:
                    print(yours)
        else:
            in4 = input("Is it chocolate? (yes/no)\n")
            if (in4 == "yes"):
                print(eat)
            else:
                print("Decision: Don't eat it.\n")
    else:
        print(eat)

#no1 saw
else:
    in2 = input("Was it sticky? (yes/no)\n")
    if (in2 == "yes"):
        in3 = input("Is it a raw steak? (yes/no)\n")
        if (in3 == "yes"):
            in4 = input("Are you a puma? (yes/no)\n")
            if (in4 == "yes"):
                print(eat)
            else:
                print("Decision: Don't eat it.")
        else:
            in4 = input("Did the cat lick it? (yes/no)\n")
            if (in4 == "yes"):
                in5 = input("Is your cat healthy? (yes/no)\n")
                if (in5 == "yes"):
                    print(eat)
                else:
                    print(yours)
            else:
                print(eat)
    else:
        in3 = input("Is it an Emausaurus? (yes/no)\n")
        if (in3 == "yes"):
            in4 = input("Are you a Megalosaurus? (yes/no)\n")
            if (in4 == "yes"):
                print(eat)
            else:
                print("Decision: Don't eat it.")
        else:
            in4 = input("Did the cat lick it? (yes/no)\n")
            if (in4 == "yes"):
                in5 = input("Is your cat healthy? (yes/no)\n")
                if (in5 == "yes"):
                    print(eat)
                else:
                    print(yours)
            else:
                print(eat)
            