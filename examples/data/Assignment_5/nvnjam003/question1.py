message = "no message yet"
userChoice = 1
while (userChoice not in ['x', 'X']):
    print ("Welcome to UCT BBS\nMENU")
    print ("(E)nter a message\n(V)iew message")
    print ("(L)ist files\n(D)isplay file")
    print ("e(X)it")
    userChoice = input("Enter your selection:\n")
    if (userChoice in ['E', 'e']):
        message = input("Enter the message:\n")
    elif (userChoice in ['V', 'v']):
        print ("The message is: " + message)
    elif (userChoice in ['L', 'l']):
        print ("List of files: 42.txt, 1015.txt")
    elif (userChoice in ['D', 'd']):
        userFile = input("Enter the filename:\n")
        if (userFile == "42.txt"):
            print ("The meaning of life is blah blah blah ...")
        elif (userFile == "1015.txt"):
            print ("Computer Science class notes ... simplified\nDo all work\nPass course\nBe happy")
        else:
            print ("File not found")
    elif (userChoice in ['X', 'x']):
        print ("Goodbye!")