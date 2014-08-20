msg = "no message yet"
while True:
    print("Welcome to UCT BBS\nMENU\n(E)nter a message\n(V)iew message\n(L)ist files\n(D)isplay file\ne(X)it")
    i = input("Enter your selection:\n")
    if "X" == i.upper():
        print("Goodbye!")
        break
    elif "E" == i.upper():
        msg = input("Enter the message:\n")
    elif "V" == i.upper():
        print("The message is:",msg)
    elif "L" == i.upper():
        print("List of files: 42.txt, 1015.txt")
    elif "D" == i.upper():
        file = input("Enter the filename:\n")
        if file == "42.txt":
            print("The meaning of life is blah blah blah ...")
        elif file == "1015.txt":
            print("Computer Science class notes ... simplified\nDo all work\nPass course\nBe happy")
        else:
            print("File not found")

