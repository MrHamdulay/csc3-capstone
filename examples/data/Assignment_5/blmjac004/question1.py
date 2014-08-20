message="no message yet"
while True:
    print("Welcome to UCT BBS\nMENU")
    print("(E)nter a message\n(V)iew message\n(L)ist files\n(D)isplay file\ne(X)it")
    selection=input("Enter your selection:\n")
    
    if selection== "E" or selection=="e":
        message=input("Enter the message:\n") 
    elif selection=="V" or selection=="v":
        print("The message is:", message)
    elif selection=="L" or selection=="l":
        print("List of files: 42.txt, 1015.txt")
    elif selection=="D" or selection=="d":
        filename=input("Enter the filename:\n")
        if filename== "1015.txt":
            print("Computer Science class notes ... simplified\nDo all work\nPass course\nBe happy")
        elif filename== "42.txt":
            print("The meaning of life is blah blah blah ...")
        else:
            print("File not found")
    elif selection=="X" or selection=="x":
        print("Goodbye!")
        break 