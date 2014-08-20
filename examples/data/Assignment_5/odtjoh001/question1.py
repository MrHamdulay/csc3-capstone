message = "no message yet"
option = ""
while (option != "x") and (option != "X"):  
    option = input("Welcome to UCT BBS\nMENU\n(E)nter a message\n(V)iew message\n(L)ist files\n(D)isplay file\ne(X)it\nEnter your selection:\n")
    if option == "e" or option == "E":
        message = input("Enter the message:\n")
    elif option == "v" or option == "V":
        print("The message is:",message)
    elif option == "l" or option == "L":
        print("List of files: 42.txt, 1015.txt")
    elif option == "d" or option == "D":
        sel = input("Enter the filename:\n")
        if sel == "42.txt":
            print("The meaning of life is blah blah blah ...")
        elif sel == "1015.txt":
            print("Computer Science class notes ... simplified\nDo all work\nPass course\nBe happy")
        else:
            print("File not found")
    
    elif option == "x" or option == "X":
        print("Goodbye!")
    
        
