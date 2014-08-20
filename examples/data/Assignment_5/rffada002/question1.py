def BBS():
    
    while True:
        print ("Welcome to UCT BBS\nMENU\n(E)nter a message\n(V)iew message\n(L)ist files\n(D)isplay file\ne(X)it")

        sel = input("Enter your selection:\n")
    
         
        if sel == "X" or sel == "x":
            print ("Goodbye!")
            break
        if sel == "E" or sel == "e":
            message = input("Enter the message:\n")
        if sel == "V" or sel == "v":
            try:
                message
            except NameError:
                print ("The message is: no message yet")
            else:
                print ("The message is:",message)
        if sel == "L" or sel == "l":
            print ("List of files: 42.txt, 1015.txt")
        if sel == "D" or sel == "d":
            req_file = input("Enter the filename:\n")
            if req_file == "42.txt":
                print ("The meaning of life is blah blah blah ...")
            elif req_file == "1015.txt":
                print ("Computer Science class notes ... simplified\nDo all work\nPass course\nBe happy")
            else:
                print ("File not found")
        
        
BBS()