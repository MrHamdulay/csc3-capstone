#Assignment 5 Question 1
#WRTJOS001 Joshua Wort
#13 April 2014

message="no message yet"
while True:
    print("Welcome to UCT BBS")
    print("MENU")
    print("(E)nter a message")
    print("(V)iew message")
    print("(L)ist files")
    print("(D)isplay file")
    print("e(X)it")
    select=input("Enter your selection:\n")
    select=select.upper()
    if select=="E":
        message=input("Enter the message:\n")
    elif select=="V":
        print("The message is:",message,sep=" ")
    elif select=="L":
        print("List of files: 42.txt, 1015.txt")
    elif select=="D":
        filename=input("Enter the filename:\n")
        if filename=="42.txt":
            print("The meaning of life is blah blah blah ...")
        elif filename=="1015.txt":
            print("Computer Science class notes ... simplified")
            print("Do all work")
            print("Pass course")
            print("Be happy")
        else:
            print("File not found")
    elif select=="X":
        print("Goodbye!")
        break
    