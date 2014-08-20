while True:
    print("Welcome to UCT BBS\nMENU\n(E)nter a message\n(V)iew message\n(L)ist files\n(D)isplay file\ne(X)it")
    selection = input("Enter your selection:\n")
    files = ["42.txt","1015.txt"]
    if selection in ["E","e"]:
        message = input("Enter the message:\n")
    if selection in ["V","v"]:
        try:
            print("The message is:",message)
        except NameError:
            print("The message is: no message yet")
    if selection in ["L","l"]:
        print("List of files:", ', '.join(files))
    if selection in ["D","d"]:
        file = input("Enter the filename:\n")
        if file in files:
            if file == "42.txt":
                print("The meaning of life is blah blah blah ...")
            elif file == "1015.txt":
                print("Computer Science class notes ... simplified\nDo all work\nPass course\nBe happy")
        else:
            print("File not found")
    if selection in ["X","x"]:
        print("Goodbye!")
        break
        