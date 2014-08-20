""" UCT Bulletin Board System """
__author__ = 'Stephen Temple - TMPSTE002'
__date__ = '2014/04/13'

message = 'no message yet'
selection = ''
while selection != 'x':  # continue loop until selection is 'x'
    print("Welcome to UCT BBS")
    print("MENU")
    print("(E)nter a message")
    print("(V)iew message")
    print("(L)ist files")
    print("(D)isplay file")
    print("e(X)it")
    selection = input("Enter your selection:\n").lower()

    # run code for selection x
    if selection == 'e':
        message = input("Enter the message:\n")
    elif selection == 'v':
        print('The message is: ' + message)
    elif selection == 'l':
        print("List of files: 42.txt, 1015.txt")
    elif selection == 'd':
        filename = input("Enter the filename:\n")
        if filename == '42.txt':
            print("The meaning of life is blah blah blah ...")
        elif filename == '1015.txt':
            print("Computer Science class notes ... simplified")
            print("Do all work")
            print("Pass course")
            print("Be happy")
        else:
            print("File not found")
    elif selection == 'x':
        print("Goodbye!")