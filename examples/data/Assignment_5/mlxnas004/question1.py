def UCTBBS():
    message = ""
    selection = ""
    while selection != "X": #or selection != "x":
        print("Welcome to UCT BBS\nMENU\n(E)nter a message\n(V)iew message\n(L)ist files\n(D)isplay file\ne(X)it")
        x = input("Enter your selection:\n")
    
        if x == "e" or x == "E":
            message = input("Enter the message:\n")
        elif x == "v" or x == "V":
            if message=="":
                print("The message is: no message yet")
            else:
                print("The message is:",message)
        elif x== "l" or x=="L":
            print("List of files: 42.txt, 1015.txt")
            
        elif x== "d" or x == "D":
            choice = input("Enter the filename:\n")
            if choice == "42.txt":
                print("The meaning of life is blah blah blah ...")
            elif choice == "1015.txt":
                print("Computer Science class notes ... simplified\nDo all work\nPass course\nBe happy")
            else:
                print("File not found")
        elif x=="X" or x=="x":
            selection=x.upper()
            print("Goodbye!")
UCTBBS()
