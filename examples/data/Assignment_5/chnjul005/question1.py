i = 0
m="no message yet"
while i != -1 :
    print("Welcome to UCT BBS")
    print("MENU")
    print("(E)nter a message")
    print("(V)iew message")
    print("(L)ist files")
    print("(D)isplay file")
    print("e(X)it")
    c = input("Enter your selection:\n")
    if c == "E" or c == "e":
        m = input("Enter the message:\n")
    if c == "V" or c == "v":
        print("The message is:",m)
    if c == "L" or c == "l":
        print("List of files: 42.txt, 1015.txt")
    if c == "D" or c == "d":
        fn = input("Enter the filename:\n")
        if fn == "42.txt":
            print("The meaning of life is blah blah blah ...")
        elif fn == "1015.txt":
            print("Computer Science class notes ... simplified\nDo all work\nPass course\nBe happy") 
        else :
            print("File not found")
    if c == "X" or c == "x":
        i = -1  
        print("Goodbye!")
    
    
    