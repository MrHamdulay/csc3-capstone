import os
#assignment6.1
bExit = False
message = "no message yet"
while bExit == False:
    print("Welcome to UCT BBS")
    print("MENU")
    print("(E)nter a message\n(V)iew message\n(L)ist files\n(D)isplay file\ne(X)it")
    s = input("Enter your selection:\n")
    s = s.upper()
    if s=="E":
        message = input("Enter the message:\n")
    elif s =="V":
        print("The message is: " + message)
    elif s =="L":
        print("List of files: 42.txt, 1015.txt")
    elif s=="D":
        fn = input("Enter the filename:\n")
        if fn != "42.txt" and fn != "1015.txt":
            print("File not found")
        else:
            file = open(fn, "r")
            data = file.read()
            print(data)
            file.close()
    elif s=="X":
        print("Goodbye!")
        bExit = True
    else:
        print("no message yet")
    
    
