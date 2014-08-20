"""
UCT BBS
Aaron Weinstein
16 April 2014
"""
message = ""
selection = ""
while selection.upper() != "X":
    print ("Welcome to UCT BBS")
    print ("MENU")
    print ("(E)nter a message")
    print ("(V)iew message")
    print ("(L)ist files")
    print ("(D)isplay file")
    print ("e(X)it")
    selection = input ("Enter your selection:\n")
    if selection.upper() == "E":
        message = input("Enter the message:\n")
    if selection.upper() == "V":
        if message == "":
            print ("The message is: no message yet", sep="")
        else:
            print ("The message is:",message)
    if selection.upper() == "X":
        print ("Goodbye!")
    if selection.upper() == "L":
        print ("List of files: 42.txt, 1015.txt")
    if selection.upper() == "D":
        filename = input ("Enter the filename:\n")
        if filename == "1015.txt":
            print ("Computer Science class notes ... simplified")
            print("Do all work")
            print("Pass course")
            print ("Be happy")
        elif filename == "42.txt":
            print ("The meaning of life is blah blah blah ...")
        else:
            print ("File not found")