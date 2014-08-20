message = "no message yet"
selection = ""
while selection.upper() != 'X':
    print("Welcome to UCT BBS")
    print("MENU")
    print("(E)nter a message")
    print("(V)iew message")
    print("(L)ist files")
    print("(D)isplay file")
    print("e(X)it")
    selection = input("Enter your selection:\n")
    if selection.upper() =='E':
        message = input("Enter the message:\n")
    elif selection.upper() =='V':
        print("The message is: " + message)
    elif selection.upper() =='L':
        print("List of files: 42.txt, 1015.txt")
    elif selection.upper() =='D':
        file = input("Enter the filename:\n")
        if file == "42.txt":
            print("The meaning of life is blah blah blah ...")
        elif file == "1015.txt":
            print("Computer Science class notes ... simplified")
            print("Do all work")
            print("Pass course")
            print("Be happy")
        else:
            print("File not found")
print("Goodbye!")