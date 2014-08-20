#storing and retrieving simple string
#wayne de jager
#14 april 2014

message="no message yet"

#menu will display untill called to end
while True:
    print("Welcome to UCT BBS")
    print("MENU")
    print("(E)nter a message")
    print("(V)iew message")
    print("(L)ist files")
    print("(D)isplay file")
    print("e(X)it")
    a=input("Enter your selection:\n")
    if a=="e":
        message=input("Enter the message:\n")
    elif a=="v":
        print("The message is:",message)
    elif a=="l":
        print("List of files: 42.txt, 1015.txt")
    elif a=="d":
        file=input("Enter the filename:\n")
        if file=="42.txt":
            print("The meaning of life is blah blah blah ...")
        elif file=="1015.txt":
            print("Computer Science class notes ... simplified")
            print("Do all work")
            print("Pass course")
            print("Be happy")
        else:
            print("File not found")
    else:
        print("Goodbye!")
        break