def filing():
    
    
    selection = ""
    message = ""
    while str.upper(selection) != "X":
        print("Welcome to UCT BBS\n")
        print("MENU")
    
        print("(E)nter a message\n")
        print("(V)iew message\n")
        print("(L)ist files\n")
        print("(D)isplay file\n")
        print("e(X)it")
    
        selection = input("Enter your selection:\n")
        selection = str.upper # will change all to upper case
        
        if (selection) == "E":
            message = input("Enter the message:\n")
        elif (selection) == "E":
            message == ""
        if (selection) == "V":
            if message != "":
                print("The message is:", message)
            else:   
                print("The message is: no message yet")      
        elif (selection) == "L":
            print("List of files: 42.txt, 1015.txt")        
        elif (selection) == "D":
            filename = input("Enter the filename:\n")
            if filename == "42.txt":
                print("The meaning of life is blah blah blah ... ")
            elif filename == "1015.txt":
                print("Computer Science class notes ... simplified\n")
                print("Do all work\n")
                print("Pass course\n")
                print("Be happy")
            else:
                print("File not found")    
    print("Goodbye!")
filing()