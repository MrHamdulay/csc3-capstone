def BBS():
    message="no message yet" 
    while True :
        print("Welcome to UCT BBS\nMENU")
        print("(E)nter a message")
        print("(V)iew message")
        print("(L)ist files")
        print("(D)isplay file")
        print("e(X)it")
        selection=input("Enter your selection:\n")
        selection=selection.upper()
        if selection=="V":
            print("The message is:",message)
        elif selection=="E":
            message=input("Enter the message:\n")
            if selection=="v":
                print("The message is:",message)    
        elif selection=="X":
            print("Goodbye!")
            break
        elif selection=="L":
            print("List of files: 42.txt, 1015.txt")
        elif selection=="D":
            filename=input("Enter the filename:\n")
            if filename=="42.txt":
                print("The meaning of life is blah blah blah ...")
            elif filename=="1015.txt":
                print("Computer Science class notes ... simplified")
                print("Do all work")
                print("Pass course")
                print("Be happy")
            elif filename=="1016.txt":
                print("File not found")
BBS()