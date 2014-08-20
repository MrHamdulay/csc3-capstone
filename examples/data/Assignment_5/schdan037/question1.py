"""Daniel Schwartz
question 1
april 2014"""

cont = True
message = "no message yet"

#loop that repeats until quit command is given
while cont:
    print("Welcome to UCT BBS")
    print("MENU")
    print("(E)nter a message")
    print("(V)iew message")
    print("(L)ist files")
    print("(D)isplay file")
    print("e(X)it")
    choice = input("Enter your selection:\n")
    choice = choice.upper()                     # makes sure that all choices can be evaluated for no matter the lettercase
    if choice[0] == "E":        # enter message
        message = input("Enter the message:\n")
    elif choice[0] == "V":      # view message
        print("The message is: " + message)
    elif choice [0] == "L":     # list files
        print("List of files: 42.txt, 1015.txt")    # these files are static so no need to account for any others
    elif choice[0] == "D":      # display file
        file = input("Enter the filename: \n")
        if file == "42.txt":
            print("The meaning of life is blah blah blah ...")
        elif file == "1015.txt":
            print("Computer Science class notes ... simplified\nDo all work\nPass course\nBe happy")
        else:
            print("File not found")
    elif choice[0] == "X":      # quit command
        print("Goodbye!")
        cont = False            # ends loop