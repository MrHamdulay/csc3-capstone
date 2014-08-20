print("Welcome to UCT BBS\nMENU\n(E)nter a message\n(V)iew message\n(L)ist files\n(D)isplay file\ne(X)it")

mess = "no message yet"
selec = input("Enter your selection:\n")
selec = selec.upper()
while (selec!="X"):
    if (selec == "E"):
        mess = input("Enter the message:\n")
    elif(selec == "V"):
        print("The message is:", mess)
    elif(selec == "D"):
        file = input("Enter the filename:\n")
        if(file == "42.txt"):
            print("The meaning of life is blah blah blah ...")
        elif(file == "1015.txt"):
            print("Computer Science class notes ... simplified\nDo all work\nPass course\nBe happy")
        else:
            print("File not found")
    elif(selec == "L"):
        print("List of files: 42.txt, 1015.txt")
    else:
        print("no message yet")
    
    print("Welcome to UCT BBS\nMENU\n(E)nter a message\n(V)iew message\n(L)ist files\n(D)isplay file\ne(X)it")        
    selec = input("Enter your selection:\n")
    selec = selec.upper()
else:
    print("Goodbye!")