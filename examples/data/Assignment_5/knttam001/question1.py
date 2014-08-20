while True:
    print("Welcome to UCT BBS")
    print("MENU")
    print("(E)nter a message")
    print("(V)iew message")
    print("(L)ist files")
    print("(D)isplay file")
    print("e(X)it")
    selec = input("Enter your selection:\n")
    message = ""
    if selec=="E" or selec == "e":
        message = input("Enter the message:\n")
        print("Welcome to UCT BBS")
        print("MENU")
        print("(E)nter a message")
        print("(V)iew message")
        print("(L)ist files")
        print("(D)isplay file")
        print("e(X)it")
        selec = input("Enter your selection:\n")
        if selec=="V" or selec =="v":
                print("The message is:",message)        
    elif selec=="V" or selec == "v":
        if message=="":
            print("The message is: no message yet")
        elif message!="":
            print("The message is:",message)
    elif selec == "L" or selec == "l":
        print("List of files: 42.txt, 1015.txt")
    elif selec == "D" or selec == "d":
        filename = input("Enter the filename:\n")
        if filename=="42.txt":
            print("The meaning of life is blah blah blah ...")
        elif filename=="1015.txt":
            print("Computer Science class notes ... simplified")
            print("Do all work")
            print("Pass course")
            print("Be happy")
        else: print("File not found")
    elif selec=="x" or selec=="X":
        print("Goodbye!")
        break