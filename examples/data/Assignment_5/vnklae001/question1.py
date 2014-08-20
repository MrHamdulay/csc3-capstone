# Question 1 - Assignment 5
# Bullitin board system (BBS)
# Written by: Laene van Niekerk

choice = "run"  # Initiates the while loop
message = ""

while choice:
    print("Welcome to UCT BBS")
    print("MENU")
    print("(E)nter a message")
    print("(V)iew message")
    print("(L)ist files")
    print("(D)isplay file")
    print("e(X)it")
    choice = input("Enter your selection:\n")
    if choice == "E" or choice == "e":
        message = input("Enter the message:\n")
    elif choice == "V" or choice == "v":
        if message != "":
            print("The message is:", message)
        elif message == "":
            print("The message is: no message yet")
    elif choice == "X" or choice == "x":
        print("Goodbye!")
        break
    elif choice == "L" or choice == "l":
        print("List of files: 42.txt, 1015.txt")
    elif choice == "D" or choice == "d":
        filename = input("Enter the filename:\n")
        if filename == "42.txt":
            print("The meaning of life is blah blah blah ...")
        elif filename == "1015.txt":
            print("Computer Science class notes ... simplified", "Do all work", "Pass course", "Be happy", sep="\n")
        else:
            print("File not found")