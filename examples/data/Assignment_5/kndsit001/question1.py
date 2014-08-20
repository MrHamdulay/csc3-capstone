"""Program to simulate a simple BBS
16 April 2014
Sithasibanzi Kondleka"""

message = ""
while True:
    print("Welcome to UCT BBS")
    print("MENU")
    print("(E)nter a message")
    print("(V)iew message")
    print("(L)ist files")
    print("(D)isplay file")
    print("e(X)it")
    selection = input("Enter your selection:\n").upper()
    if selection == "E":
        message = input("Enter the message:\n")
    elif selection == "V":
        if message == "":
            print("The message is: no message yet")
        else:
            print("The message is:",message)
    elif selection == "L":
        print("List of files: 42.txt, 1015.txt")
    elif selection == "D":
        filename = input("Enter the filename:\n")
        if filename == "42.txt":
            print("The meaning of life is blah blah blah ...")
        elif filename == "1015.txt":
            print("Computer Science class notes ... simplified")
            print("Do all work")
            print("Pass course")
            print("Be happy")
        else:
            print("File not found")
    elif selection == "X":
        break
    else:
        print("no message yet")
print("Goodbye!")